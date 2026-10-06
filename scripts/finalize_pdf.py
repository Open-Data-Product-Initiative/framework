#!/usr/bin/env python3
"""Compose stable A4 pages and apply publication metadata."""

from pathlib import Path
import sys

import fitz


ROOT = Path(__file__).resolve().parents[1]
FONT_DIRECTORY = ROOT / "publication" / "assets" / "fonts"
REGULAR_FONT = FONT_DIRECTORY / "Poppins-Regular.ttf"
SEMIBOLD_FONT = FONT_DIRECTORY / "Poppins-SemiBold.ttf"
RUNNING_COLOR = (0.43, 0.38, 0.46)


def add_running_matter(page: fitz.Page, page_number: int, page_count: int) -> None:
    """Add consistent running matter outside the scaled content area."""

    width = page.rect.width
    height = page.rect.height
    page.insert_font(fontname="DPOFRegular", fontfile=REGULAR_FONT)
    page.insert_font(fontname="DPOFSemibold", fontfile=SEMIBOLD_FONT)
    page.insert_text(
        (48, 27),
        "Data Product Operating Framework",
        fontname="DPOFSemibold",
        fontsize=7.5,
        color=RUNNING_COLOR,
    )
    page.insert_textbox(
        fitz.Rect(width - 180, 17, width - 48, 33),
        "v0.1.0 - Draft",
        fontname="DPOFRegular",
        fontsize=7.5,
        color=RUNNING_COLOR,
        align=fitz.TEXT_ALIGN_RIGHT,
    )
    page.insert_text(
        (48, height - 21),
        "CC BY 4.0",
        fontname="DPOFRegular",
        fontsize=7.5,
        color=RUNNING_COLOR,
    )
    page.insert_textbox(
        fitz.Rect(width - 140, height - 31, width - 48, height - 15),
        f"{page_number} / {page_count}",
        fontname="DPOFRegular",
        fontsize=7.5,
        color=RUNNING_COLOR,
        align=fitz.TEXT_ALIGN_RIGHT,
    )


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: finalize_pdf.py <pdf-file>")

    pdf_path = Path(sys.argv[1]).resolve()
    temporary_path = pdf_path.with_suffix(".composed.pdf")
    source = fitz.open(pdf_path)
    output = fitz.open()
    page_count = source.page_count

    for index, source_page in enumerate(source):
        width = source_page.rect.width
        height = source_page.rect.height
        page = output.new_page(width=width, height=height)
        if index == 0:
            target = page.rect
        else:
            horizontal_inset = width * 0.06
            vertical_inset = height * 0.06
            target = fitz.Rect(
                horizontal_inset,
                vertical_inset,
                width - horizontal_inset,
                height - vertical_inset,
            )
        page.show_pdf_page(target, source, index, keep_proportion=True, overlay=True)
        if index > 0:
            add_running_matter(page, index + 1, page_count)

    output.set_metadata(
        {
            "title": "Data Product Operating Framework",
            "author": "Open Data Product Initiative contributors",
            "subject": "An open operating model for data products",
            "keywords": "data products, operating framework, ODPS, governance",
            "creator": "Data Product Operating Framework publication pipeline",
            "producer": "PyMuPDF",
        }
    )
    output.save(temporary_path, garbage=4, deflate=True, clean=True)
    output.close()
    source.close()
    temporary_path.replace(pdf_path)


if __name__ == "__main__":
    main()
