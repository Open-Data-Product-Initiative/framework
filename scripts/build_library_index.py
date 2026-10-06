#!/usr/bin/env python3
"""Build a deterministic local search index for governed evidence sources."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from library_support import INDEX_PATH, ROOT, catalog_text, chunk_text, load_catalog, tokenize


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=INDEX_PATH)
    parser.add_argument("--max-words", type=int, default=240)
    return parser.parse_args()


def build_index(output: Path, max_words: int = 240) -> dict:
    catalog = load_catalog()
    extracted_dir = ROOT / "library" / "extracted"
    entries = []
    for source in sorted(catalog["sources"], key=lambda item: item["id"]):
        parts = [("catalog", catalog_text(source))]
        extracted_path = extracted_dir / f"{source['id']}.txt"
        if extracted_path.is_file():
            parts.append(("retrieved", extracted_path.read_text(encoding="utf-8")))
        chunk_number = 0
        for origin, value in parts:
            for text in chunk_text(value, max_words=max_words):
                entries.append({
                    "source_id": source["id"],
                    "title": source["title"],
                    "authority_tier": source["authority_tier"],
                    "origin": origin,
                    "chunk": chunk_number,
                    "text": text,
                    "tokens": tokenize(text),
                })
                chunk_number += 1
    result = {
        "schema_version": "1.0.0",
        "catalog_schema_version": catalog["schema_version"],
        "entries": entries,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def main() -> int:
    args = arguments()
    result = build_index(args.output, args.max_words)
    try:
        display = args.output.resolve().relative_to(ROOT)
    except ValueError:
        display = args.output
    print(f"Built {display} with {len(result['entries'])} evidence chunks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
