#!/usr/bin/env python3
"""Retrieve permitted evidence sources into ignored local working directories."""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import ssl
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from library_support import ROOT, extract_html, load_collections, sources_by_id


CACHE = ROOT / "library" / "cache"
EXTRACTED = ROOT / "library" / "extracted"
USER_AGENT = "DataProductOperatingFrameworkResearch/0.1 (+https://opendataproducts.org/framework/)"


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_ids", nargs="*", help="Stable source IDs; default is all locally retrievable sources")
    parser.add_argument("--collection", help="Restrict retrieval to one collection ID")
    parser.add_argument("--refresh", action="store_true", help="Retrieve even when a local cache file exists")
    parser.add_argument("--timeout", type=int, default=30)
    return parser.parse_args()


def extension(content_type: str, url: str) -> str:
    if "pdf" in content_type.lower() or url.lower().endswith(".pdf"):
        return ".pdf"
    guessed = mimetypes.guess_extension(content_type.split(";", 1)[0].strip())
    return ".html" if "html" in content_type.lower() else (guessed or ".bin")


def extract_pdf(path: Path) -> str | None:
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        return None
    reader = PdfReader(str(path))
    return "\n\n".join((page.extract_text() or "").strip() for page in reader.pages).strip()


def tls_context() -> ssl.SSLContext:
    """Use the platform trust store, with certifi as an optional local fallback."""
    try:
        import certifi  # type: ignore
    except ImportError:
        return ssl.create_default_context()
    return ssl.create_default_context(cafile=certifi.where())


def main() -> int:
    args = arguments()
    sources = sources_by_id()
    selected = set(args.source_ids)
    if args.collection:
        collections = load_collections()
        if args.collection not in collections:
            print(f"Unknown collection: {args.collection}", file=sys.stderr)
            return 2
        selected.update(collections[args.collection]["source_ids"])
    unknown = sorted(selected - set(sources))
    if unknown:
        print(f"Unknown source IDs: {', '.join(unknown)}", file=sys.stderr)
        return 2

    records = [
        source for source in sources.values()
        if (not selected or source["id"] in selected)
        and source["access"] == "local-analysis"
        and source.get("retrieval_url")
    ]
    CACHE.mkdir(parents=True, exist_ok=True)
    EXTRACTED.mkdir(parents=True, exist_ok=True)
    failures = 0
    for source in records:
        receipt_path = CACHE / f"{source['id']}.receipt.json"
        if receipt_path.exists() and not args.refresh:
            print(f"skip {source['id']}: cached receipt exists")
            continue
        request = urllib.request.Request(source["retrieval_url"], headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=args.timeout, context=tls_context()) as response:
                data = response.read()
                content_type = response.headers.get("Content-Type", "application/octet-stream")
                final_url = response.geturl()
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            failures += 1
            print(f"error {source['id']}: {exc}", file=sys.stderr)
            continue

        suffix = extension(content_type, final_url)
        cache_path = CACHE / f"{source['id']}{suffix}"
        cache_path.write_bytes(data)
        extracted: str | None = None
        if suffix in {".html", ".htm"}:
            extracted = extract_html(data.decode("utf-8", errors="replace"))
        elif suffix == ".pdf":
            extracted = extract_pdf(cache_path)
        if extracted:
            (EXTRACTED / f"{source['id']}.txt").write_text(extracted + "\n", encoding="utf-8")
        receipt = {
            "source_id": source["id"],
            "requested_url": source["retrieval_url"],
            "final_url": final_url,
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "content_type": content_type,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "cache_file": cache_path.name,
            "text_extracted": bool(extracted),
        }
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        note = "" if extracted else " (no extractor available)"
        print(f"retrieved {source['id']}: {len(data)} bytes{note}")

    if failures:
        print(f"Retrieval completed with {failures} failure(s).", file=sys.stderr)
        return 1
    print(f"Retrieval completed for {len(records)} permitted source(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
