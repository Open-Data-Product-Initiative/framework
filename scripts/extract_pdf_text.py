#!/usr/bin/env python3
"""Extract text from a PDF for publication validation."""

from pathlib import Path
import sys

from pypdf import PdfReader


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: extract_pdf_text.py <pdf-file> <text-file>")

    source = Path(sys.argv[1]).resolve()
    destination = Path(sys.argv[2]).resolve()
    text = "\n\f\n".join(page.extract_text() or "" for page in PdfReader(source).pages)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
