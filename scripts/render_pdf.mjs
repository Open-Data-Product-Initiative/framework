import fs from "node:fs/promises";
import path from "node:path";
import { spawn } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const manifest = JSON.parse(await fs.readFile(path.join(root, "publication", "manifest.json"), "utf8"));
const printFile = path.join(root, "dist", "print.html");
const outputDirectory = path.join(root, "output", "pdf");
const downloadDirectory = path.join(root, "dist", "downloads");
const temporaryDirectory = path.join(root, "tmp", "pdfs");
const outputFile = path.join(outputDirectory, manifest.pdfFilename);
const downloadFile = path.join(downloadDirectory, manifest.pdfFilename);

function run(command, args) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, { cwd: root, stdio: "inherit" });
    child.on("error", reject);
    child.on("exit", (code) => code === 0 ? resolve() : reject(new Error(`${command} exited with code ${code}`)));
  });
}

async function renderWithChrome(chromePath, args, outputPath) {
  await fs.rm(outputPath, { force: true });
  const child = spawn(chromePath, args, { cwd: root, stdio: "inherit" });
  let exitState = null;
  child.on("exit", (code, signal) => {
    exitState = { code, signal };
  });

  let previousSize = -1;
  let stableChecks = 0;
  for (let attempt = 0; attempt < 120; attempt += 1) {
    await new Promise((resolve) => setTimeout(resolve, 500));
    let size = -1;
    try {
      size = (await fs.stat(outputPath)).size;
    } catch {
      // Chrome has not written the file yet.
    }

    if (size > 50_000 && size === previousSize) stableChecks += 1;
    else stableChecks = 0;
    previousSize = size;

    if (exitState && exitState.code !== 0 && size < 50_000) {
      throw new Error(`Chrome exited with ${exitState.code ?? exitState.signal} before creating the PDF.`);
    }
    if (exitState?.code === 0 && size > 50_000) return;
    if (stableChecks >= 4) {
      if (!exitState) child.kill("SIGTERM");
      return;
    }
  }

  if (!exitState) child.kill("SIGTERM");
  throw new Error("Chrome did not finish the PDF within 60 seconds.");
}

const candidates = [
  process.env.CHROME_PATH,
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  "/usr/bin/google-chrome",
  "/usr/bin/google-chrome-stable",
  "/usr/bin/chromium",
  "/usr/bin/chromium-browser"
].filter(Boolean);

let chromePath;
for (const candidate of candidates) {
  try {
    await fs.access(candidate);
    chromePath = candidate;
    break;
  } catch {
    // Try the next supported Chrome path.
  }
}
if (!chromePath) throw new Error("Chrome or Chromium is required to render the PDF.");

await fs.access(printFile);
await fs.mkdir(outputDirectory, { recursive: true });
await fs.mkdir(downloadDirectory, { recursive: true });
await fs.mkdir(temporaryDirectory, { recursive: true });

const profileDirectory = path.join(temporaryDirectory, "chrome-profile");
await fs.rm(profileDirectory, { recursive: true, force: true });
await fs.mkdir(profileDirectory, { recursive: true });

await renderWithChrome(chromePath, [
  "--headless=new",
  "--disable-gpu",
  "--no-sandbox",
  "--disable-background-networking",
  "--disable-breakpad",
  "--disable-component-update",
  "--disable-default-apps",
  "--disable-sync",
  "--no-first-run",
  "--allow-file-access-from-files",
  "--run-all-compositor-stages-before-draw",
  "--no-pdf-header-footer",
  `--user-data-dir=${profileDirectory}`,
  `--print-to-pdf=${outputFile}`,
  pathToFileURL(printFile).href
], outputFile);

await fs.copyFile(outputFile, path.join(temporaryDirectory, "chrome-source.pdf"));
await run("python3", [path.join(root, "scripts", "finalize_pdf.py"), outputFile]);
await fs.copyFile(outputFile, downloadFile);
console.log(`Created ${path.relative(root, outputFile)} and ${path.relative(root, downloadFile)}`);
