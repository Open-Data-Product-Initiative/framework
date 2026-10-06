import assert from "node:assert/strict";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const dist = path.join(root, "dist");
const manifest = JSON.parse(await fs.readFile(path.join(root, "publication", "manifest.json"), "utf8"));
const index = await fs.readFile(path.join(dist, "index.html"), "utf8");
const print = await fs.readFile(path.join(dist, "print.html"), "utf8");

assert.match(index, /<html lang="en"/);
assert.match(index, /id="nav-toggle"[^>]+aria-controls="site-navigation"[^>]+aria-expanded="false"/);
assert.match(index, /id="site-navigation"/);
assert.match(index, /id="nav-backdrop"/);
assert.match(index, /<a class="sidebar-title" href="#overview" data-nav-target="overview" aria-label="Back to the beginning">/);
assert.match(index, /<a class="mobile-title" href="#overview" aria-label="Back to the beginning">/);
assert.match(index, /assets\/framework\.js/);
assert.match(index, /<div class="hero-copy">/);
assert.match(index, /<div class="hero-copy">[\s\S]+?<figure class="overview-figure">/);
assert.match(print, /class="print-cover"/);
assert.match(index, new RegExp(`downloads/${manifest.pdfFilename.replaceAll(".", "\\.")}`));
assert.match(index, /CC BY 4\.0/);
assert.match(index, /Draft publication/);
assert.doesNotMatch(index, /\n---\n/);
assert.doesNotMatch(index, /(?:href|src)="\//);
assert.doesNotMatch(index, /href="[^"]+\.md(?:#[^"]*)?"/, "Published HTML must not link to Markdown source paths");

let lastChapterPosition = -1;
for (const chapter of manifest.chapters) {
  const marker = `id="${chapter.id}"`;
  const position = index.indexOf(marker);
  assert(position > lastChapterPosition, `Chapter ${chapter.id} must exist in manifest order`);
  lastChapterPosition = position;
}

for (let capability = 1; capability <= 14; capability += 1) {
  assert.match(index, new RegExp(`C${capability}\\.`), `Capability C${capability} is missing`);
}

const ids = [...index.matchAll(/\sid="([^"]+)"/g)].map((match) => match[1]);
assert.equal(new Set(ids).size, ids.length, "HTML IDs must be unique");
const idSet = new Set(ids);
for (const match of index.matchAll(/href="#([^"]+)"/g)) {
  assert(idSet.has(match[1]), `Internal link target #${match[1]} does not exist`);
}

const requiredFiles = [
  "index.html",
  "print.html",
  ".nojekyll",
  "robots.txt",
  "sitemap.xml",
  "llms.txt",
  "assets/framework.css",
  "assets/framework.js",
  "assets/framework-overview-v0.1.png",
  "assets/fonts/poppins-400.woff2",
  "assets/fonts/poppins-800.woff2",
  "assets/fonts/OFL.txt",
  "assets/fonts/Poppins-Regular.ttf",
  "assets/fonts/Poppins-SemiBold.ttf"
];
for (const relativePath of requiredFiles) await fs.access(path.join(dist, relativePath));

console.log(`Publication checks passed: ${manifest.chapters.length} chapters, ${ids.length} unique IDs.`);
