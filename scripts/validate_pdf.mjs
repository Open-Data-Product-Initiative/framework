import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import { fileURLToPath } from "node:url";

const execute = promisify(execFile);
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const manifest = JSON.parse(await fs.readFile(path.join(root, "publication", "manifest.json"), "utf8"));
const canonical = path.join(root, "output", "pdf", manifest.pdfFilename);
const download = path.join(root, "dist", "downloads", manifest.pdfFilename);
const textPath = path.join(root, "tmp", "pdfs", "extracted.txt");

const { stdout: information } = await execute("pdfinfo", [canonical], { maxBuffer: 1024 * 1024 });
const pages = Number(information.match(/^Pages:\s+(\d+)/m)?.[1]);
assert(Number.isInteger(pages) && pages >= 10, `Expected at least 10 pages, found ${pages}`);
assert.match(information, /^Title:\s+Data Product Operating Framework$/m);
assert.match(information, /^Author:\s+Open Data Product Initiative contributors$/m);
assert.match(information, /^Encrypted:\s+no$/m);
assert.match(information, /^Page size:\s+59[45]\.\d+ x 841\.\d+ pts \(A4\)$/m);

await execute("python3", [path.join(root, "scripts", "extract_pdf_text.py"), canonical, textPath]);
const extracted = await fs.readFile(textPath, "utf8");
for (const phrase of [
  "Data Product Operating Framework",
  "DIRECT",
  "DEFINE",
  "OPERATE",
  "ASSURE",
  "Assessment Standard",
  "Implementation Playbook",
  "Glossary",
  "CC BY 4.0",
  manifest.version
]) {
  assert(extracted.includes(phrase), `PDF text is missing: ${phrase}`);
}

const digest = (content) => crypto.createHash("sha256").update(content).digest("hex");
const [canonicalBytes, downloadBytes] = await Promise.all([fs.readFile(canonical), fs.readFile(download)]);
assert.equal(digest(canonicalBytes), digest(downloadBytes), "Website PDF must match the canonical PDF");
assert(canonicalBytes.length < 20 * 1024 * 1024, "PDF must remain below 20 MB");

console.log(`PDF checks passed: ${pages} A4 pages, ${(canonicalBytes.length / 1024 / 1024).toFixed(2)} MB.`);
