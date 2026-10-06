#!/usr/bin/env python3
"""Shared deterministic helpers for the framework evidence library."""

from __future__ import annotations

import html
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "library" / "catalog.json"
COLLECTIONS_PATH = ROOT / "library" / "collections"
INDEX_PATH = ROOT / "library" / "index" / "library-index.json"
TOKEN_PATTERN = re.compile(r"[A-Za-z][A-Za-z0-9_-]{1,}")


class TextExtractor(HTMLParser):
    """Extract visible text from HTML without external dependencies."""

    HIDDEN = {"script", "style", "svg", "noscript", "template"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.hidden_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in self.HIDDEN:
            self.hidden_depth += 1
        elif not self.hidden_depth and tag.lower() in {"p", "div", "section", "article", "li", "br", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in self.HIDDEN and self.hidden_depth:
            self.hidden_depth -= 1
        elif not self.hidden_depth and tag.lower() in {"p", "div", "section", "article", "li", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth:
            self.parts.append(data)

    def text(self) -> str:
        value = html.unescape(" ".join(self.parts))
        value = re.sub(r"[ \t]+", " ", value)
        value = re.sub(r"\n\s*\n+", "\n\n", value)
        return value.strip()


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def load_catalog() -> dict[str, Any]:
    return load_json(CATALOG_PATH)


def sources_by_id() -> dict[str, dict[str, Any]]:
    return {source["id"]: source for source in load_catalog()["sources"]}


def load_collections() -> dict[str, dict[str, Any]]:
    return {
        path.stem: load_json(path)
        for path in sorted(COLLECTIONS_PATH.glob("*.json"))
    }


def tokenize(value: str) -> list[str]:
    return [token.lower() for token in TOKEN_PATTERN.findall(value)]


def chunk_text(value: str, max_words: int = 240, overlap: int = 35) -> list[str]:
    words = value.split()
    if not words:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(words):
        end = min(len(words), start + max_words)
        chunks.append(" ".join(words[start:end]))
        if end == len(words):
            break
        start = max(start + 1, end - overlap)
    return chunks


def catalog_text(source: dict[str, Any]) -> str:
    values: list[str] = [source["title"], source["publisher"], source["summary"]]
    values.extend(source.get("use_for", []))
    values.extend(source.get("not_for", []))
    values.extend(f"C{number}" for number in source.get("capabilities", []))
    return "\n".join(values)


def extract_html(value: str) -> str:
    parser = TextExtractor()
    parser.feed(value)
    return parser.text()


def extract_markdown_section(path: Path, heading: str | None) -> tuple[str, str | None]:
    text = path.read_text(encoding="utf-8")
    if not heading:
        return text[:12000], None

    pattern = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
    headings = list(pattern.finditer(text))
    requested = heading.strip().lower()
    for index, match in enumerate(headings):
        title = match.group(2).strip()
        if title.lower() != requested:
            continue
        level = len(match.group(1))
        end = len(text)
        for following in headings[index + 1 :]:
            if len(following.group(1)) <= level:
                end = following.start()
                break
        return text[match.start() : end].strip(), title
    raise ValueError(f"heading not found in {path.relative_to(ROOT)}: {heading!r}")


def rank_chunks(
    entries: Iterable[dict[str, Any]], query: str, limit: int = 8, max_per_source: int = 2
) -> list[dict[str, Any]]:
    query_counts = Counter(tokenize(query))
    scored: list[tuple[float, str, int, dict[str, Any]]] = []
    for entry in entries:
        token_counts = Counter(entry.get("tokens") or tokenize(entry["text"]))
        score = 0.0
        for token, query_count in query_counts.items():
            frequency = token_counts.get(token, 0)
            if frequency:
                score += (1.0 + min(frequency, 6) / 6.0) * query_count
        if score:
            scored.append((score, entry["source_id"], entry["chunk"], entry))
    scored.sort(key=lambda item: (-item[0], item[1], item[2]))
    results = []
    source_counts: Counter[str] = Counter()
    for score, _, _, entry in scored:
        if source_counts[entry["source_id"]] >= max_per_source:
            continue
        result = {key: value for key, value in entry.items() if key != "tokens"}
        result["score"] = round(score, 4)
        results.append(result)
        source_counts[entry["source_id"]] += 1
        if len(results) == limit:
            break
    return results
