import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import MarkdownIt from "markdown-it";

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(scriptDirectory, "..");
const publicationDirectory = path.join(root, "publication");
const distDirectory = path.join(root, "dist");

const manifest = JSON.parse(await fs.readFile(path.join(publicationDirectory, "manifest.json"), "utf8"));
const template = await fs.readFile(path.join(publicationDirectory, "template.html"), "utf8");
const chapterIdBySource = new Map(
  manifest.chapters.map((chapter) => [path.posix.normalize(chapter.source), chapter.id])
);

const escapeHtml = (value) => String(value)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;")
  .replaceAll("'", "&#39;");

const stripMarkup = (value) => value.replace(/<[^>]*>/g, "").replace(/&amp;/g, "&").trim();
const stripFrontMatter = (source) => source.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, "");
const stripFirstHeading = (source) => source.replace(/^\s*#\s+.*(?:\r?\n)+/, "");

function slugify(value) {
  return value
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "") || "section";
}

function resolvePublicationLink(href, chapter) {
  if (!href || href.startsWith("#") || /^[a-z][a-z0-9+.-]*:/i.test(href)) return href;

  const [rawPath, rawFragment = ""] = href.split("#", 2);
  if (!rawPath.toLowerCase().endsWith(".md")) return href;

  const resolvedSource = path.posix.normalize(
    path.posix.join(path.posix.dirname(chapter.source), decodeURIComponent(rawPath))
  );
  const targetChapterId = chapterIdBySource.get(resolvedSource);
  if (!targetChapterId) {
    throw new Error(
      `Markdown link from ${chapter.source} targets ${href}, but ${resolvedSource} is not a published chapter`
    );
  }

  return rawFragment
    ? `#${targetChapterId}-${slugify(decodeURIComponent(rawFragment))}`
    : `#${targetChapterId}`;
}

function renderMarkdown(source, chapter) {
  const md = new MarkdownIt({ html: false, linkify: true, typographer: true });
  const seen = new Map();
  const headings = [];
  const defaultHeadingOpen = md.renderer.rules.heading_open
    ?? ((tokens, index, options, env, self) => self.renderToken(tokens, index, options));

  md.core.ruler.after("block", "publication-heading-metadata", (state) => {
    for (let index = 0; index < state.tokens.length; index += 1) {
      const token = state.tokens[index];
      if (token.type !== "heading_open") continue;

      const originalLevel = Number(token.tag.slice(1));
      const displayLevel = Math.min(6, originalLevel + 1);
      const inline = state.tokens[index + 1];
      const text = inline?.content ?? "Section";
      const base = `${chapter.id}-${slugify(text)}`;
      const occurrence = (seen.get(base) ?? 0) + 1;
      seen.set(base, occurrence);
      const id = occurrence === 1 ? base : `${base}-${occurrence}`;

      token.tag = `h${displayLevel}`;
      token.attrSet("id", id);
      token.meta = { id };
      const closing = state.tokens.find((candidate, closingIndex) => closingIndex > index && candidate.type === "heading_close");
      if (closing) closing.tag = `h${displayLevel}`;

      if (originalLevel === 2) headings.push({ id, title: text });
    }
  });

  md.renderer.rules.heading_open = (tokens, index, options, env, self) => defaultHeadingOpen(tokens, index, options, env, self);
  const defaultLinkOpen = md.renderer.rules.link_open
    ?? ((tokens, index, options, env, self) => self.renderToken(tokens, index, options));
  md.renderer.rules.link_open = (tokens, index, options, env, self) => {
    const href = tokens[index].attrGet("href");
    tokens[index].attrSet("href", resolvePublicationLink(href, chapter));
    return defaultLinkOpen(tokens, index, options, env, self);
  };
  md.renderer.rules.heading_close = (tokens, index, options, env, self) => {
    const opening = [...tokens.slice(0, index)].reverse().find((token) => token.type === "heading_open");
    const id = opening?.meta?.id;
    const anchor = id
      ? `<a class="heading-anchor" href="#${escapeHtml(id)}" aria-label="Link to this section">#</a>`
      : "";
    return `${anchor}${self.renderToken(tokens, index, options)}`;
  };

  let html = md.render(stripFirstHeading(stripFrontMatter(source)));
  html = html.replaceAll("<table>", '<div class="table-wrap" tabindex="0" role="region" aria-label="Scrollable table"><table>');
  html = html.replaceAll("</table>", "</table></div>");
  return { html, headings };
}

const chapters = [];
for (const chapter of manifest.chapters) {
  const source = await fs.readFile(path.join(root, chapter.source), "utf8");
  const rendered = renderMarkdown(source, chapter);
  chapters.push({ ...chapter, ...rendered });
}

const chevron = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg>';
const menuIcon = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
const closeIcon = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 6 12 12M18 6 6 18"/></svg>';

function renderNavigation() {
  const groups = chapters.map((chapter) => {
    const sublistId = `nav-${chapter.id}-sections`;
    const sublist = chapter.headings.length
      ? `<ul class="nav-sublist" id="${sublistId}">${chapter.headings.map((heading) =>
          `<li><a class="nav-link" href="#${heading.id}" data-nav-target="${heading.id}">${escapeHtml(heading.title)}</a></li>`
        ).join("")}</ul>`
      : "";
    const toggle = chapter.headings.length
      ? `<button class="nav-group-toggle" type="button" aria-expanded="false" aria-controls="${sublistId}" aria-label="Toggle ${escapeHtml(chapter.navLabel)} sections">${chevron}</button>`
      : "";
    return `<li class="nav-group" style="--nav-accent:var(--${escapeHtml(chapter.tone)})">
      <div class="nav-row">
        <a class="nav-link" href="#${chapter.id}" data-nav-target="${chapter.id}">${escapeHtml(chapter.navLabel)}</a>
        ${toggle}
      </div>
      ${sublist}
    </li>`;
  }).join("");

  return `<nav class="framework-nav" aria-label="Framework chapters">
    <ul>
      <li class="nav-overview"><a class="nav-link" href="#overview" data-nav-target="overview">Overview</a></li>
      ${groups}
    </ul>
  </nav>`;
}

const sidebar = `<aside class="sidebar" id="site-navigation" aria-label="Framework navigation">
  <div class="sidebar-head">
    <div class="sidebar-brand">
      <a class="sidebar-home" href="${escapeHtml(manifest.homepageUrl)}">Open Data Product Initiative</a>
      <a class="sidebar-title" href="#overview" data-nav-target="overview" aria-label="Back to the beginning">${escapeHtml(manifest.shortTitle)}</a>
      <div class="sidebar-meta"><span class="status-chip">${escapeHtml(manifest.status)}</span><span class="version-chip">v${escapeHtml(manifest.version)}</span></div>
    </div>
    <button class="sidebar-close" id="nav-close" type="button" aria-label="Close navigation">${closeIcon}</button>
  </div>
  ${renderNavigation()}
  <div class="sidebar-footer">Licensed under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.</div>
</aside>`;

const mobileHeader = `<header class="mobile-header">
  <button class="mobile-nav-toggle" id="nav-toggle" type="button" aria-label="Open navigation" aria-controls="site-navigation" aria-expanded="false">${menuIcon}</button>
  <a class="mobile-title" href="#overview" aria-label="Back to the beginning">${escapeHtml(manifest.shortTitle)}</a>
  <span class="mobile-version">v${escapeHtml(manifest.version)}</span>
</header>`;

const hero = `<header class="web-hero" id="overview" data-scroll-section>
  <div class="hero-inner">
    <div class="hero-copy">
      <p class="eyebrow">Open Data Product Initiative · Framework publication</p>
      <h1>${escapeHtml(manifest.title)}</h1>
      <p class="hero-summary">${escapeHtml(manifest.description)}</p>
      <div class="hero-meta">
        <span><strong>Version</strong> ${escapeHtml(manifest.version)}</span>
        <span><strong>Status</strong> ${escapeHtml(manifest.status)}</span>
        <span><strong>Published</strong> ${escapeHtml(manifest.date)}</span>
        <span><strong>License</strong> ${escapeHtml(manifest.license)}</span>
      </div>
      <div class="hero-actions">
        <a class="button button--primary" href="downloads/${escapeHtml(manifest.pdfFilename)}">Download PDF</a>
        <a class="button button--secondary" href="${escapeHtml(manifest.repositoryUrl)}">View source on GitHub</a>
      </div>
    </div>
    <figure class="overview-figure">
      <img src="assets/framework-overview-v0.1.png" alt="The Core connects DIRECT, DEFINE, OPERATE and ASSURE through fourteen capabilities and a continuous feedback loop.">
      <figcaption>The Data Product Operating Framework Core at a glance.</figcaption>
    </figure>
  </div>
</header>`;

const printCover = `<section class="print-cover" aria-label="Publication cover">
  <div>
    <p class="eyebrow">Open Data Product Initiative · Framework publication</p>
    <h1>${escapeHtml(manifest.title)}</h1>
    <p class="print-cover-summary">${escapeHtml(manifest.description)}</p>
    <figure class="print-cover-figure"><img src="assets/framework-overview-v0.1.png" alt="Framework overview diagram"></figure>
  </div>
  <div class="print-cover-meta">
    <div><strong>Version</strong>${escapeHtml(manifest.version)} · ${escapeHtml(manifest.status)}</div>
    <div><strong>Published</strong>${escapeHtml(manifest.date)}</div>
    <div><strong>License</strong>${escapeHtml(manifest.license)}</div>
  </div>
</section>`;

const chapterHtml = chapters.map((chapter) => `<article class="chapter chapter--${escapeHtml(chapter.tone)}" id="${escapeHtml(chapter.id)}" data-scroll-section>
  <header class="chapter-heading">
    <div>
      <p class="chapter-kicker">${escapeHtml(chapter.eyebrow)}</p>
      <h2>${escapeHtml(chapter.title)}<a class="heading-anchor" href="#${escapeHtml(chapter.id)}" aria-label="Link to ${escapeHtml(chapter.title)}">#</a></h2>
    </div>
  </header>
  <div class="chapter-body">${chapter.html}</div>
</article>`).join("\n");

const content = `${printCover}<div class="document">
  <aside class="publication-notice"><strong>Draft publication.</strong> Version ${escapeHtml(manifest.version)} is available for review and contribution; it is not an adopted framework release.</aside>
  ${chapterHtml}
</div>`;

const footer = `<footer class="site-footer"><div class="site-footer-inner">
  <p>© Open Data Product Initiative contributors · ${escapeHtml(manifest.license)}</p>
  <div class="site-footer-links"><a href="${escapeHtml(manifest.homepageUrl)}">opendataproducts.org</a><a href="${escapeHtml(manifest.repositoryUrl)}">GitHub repository</a></div>
</div></footer>`;

function fillTemplate(replacements) {
  let output = template;
  for (const [key, value] of Object.entries(replacements)) output = output.replaceAll(`{{${key}}}`, value);
  const unresolved = output.match(/{{[A-Z_]+}}/g);
  if (unresolved) throw new Error(`Unresolved template values: ${unresolved.join(", ")}`);
  return output;
}

const common = {
  DESCRIPTION: escapeHtml(manifest.description),
  TITLE: escapeHtml(manifest.title),
  CANONICAL_URL: escapeHtml(manifest.siteUrl),
  PAGE_TITLE: `${escapeHtml(manifest.title)} · Open Data Product Initiative`,
  SIDEBAR: sidebar,
  MOBILE_HEADER: mobileHeader,
  BACKDROP: '<button class="nav-backdrop" id="nav-backdrop" type="button" aria-label="Close navigation" tabindex="-1"></button>',
  CONTENT: content,
  FOOTER: footer
};

const indexHtml = fillTemplate({ ...common, BODY_CLASS: "publication publication--web", HERO: hero, SCRIPT: '<script src="assets/framework.js" defer></script>' });
const printHtml = fillTemplate({ ...common, BODY_CLASS: "publication publication--print", HERO: hero, SCRIPT: "" });

await fs.rm(distDirectory, { recursive: true, force: true });
await fs.mkdir(path.join(distDirectory, "assets", "fonts"), { recursive: true });
await fs.mkdir(path.join(distDirectory, "downloads"), { recursive: true });
await fs.writeFile(path.join(distDirectory, "index.html"), indexHtml);
await fs.writeFile(path.join(distDirectory, "print.html"), printHtml);
await fs.copyFile(path.join(publicationDirectory, "assets", "framework.css"), path.join(distDirectory, "assets", "framework.css"));
await fs.copyFile(path.join(publicationDirectory, "assets", "framework.js"), path.join(distDirectory, "assets", "framework.js"));
await fs.copyFile(path.join(root, "assets", "framework-overview-v0.1.png"), path.join(distDirectory, "assets", "framework-overview-v0.1.png"));

for (const file of await fs.readdir(path.join(publicationDirectory, "assets", "fonts"))) {
  await fs.copyFile(path.join(publicationDirectory, "assets", "fonts", file), path.join(distDirectory, "assets", "fonts", file));
}

await fs.writeFile(path.join(distDirectory, ".nojekyll"), "");
await fs.writeFile(path.join(distDirectory, "robots.txt"), `User-agent: *\nAllow: /\nSitemap: ${manifest.siteUrl}sitemap.xml\n`);
await fs.writeFile(path.join(distDirectory, "sitemap.xml"), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>${escapeHtml(manifest.siteUrl)}</loc><lastmod>${escapeHtml(manifest.date)}</lastmod></url></urlset>\n`);
await fs.writeFile(path.join(distDirectory, "llms.txt"), `# ${manifest.title}\n\n> ${manifest.description}\n\nCanonical documentation: ${manifest.siteUrl}\nSource: ${manifest.repositoryUrl}\nLicense: ${manifest.license}\nVersion: ${manifest.version} (${manifest.status})\n`);

console.log(`Built ${chapters.length} chapters in ${path.relative(root, distDirectory)}/`);
