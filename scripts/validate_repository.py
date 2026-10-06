#!/usr/bin/env python3
"""Validate the structure and internal integrity of the framework repository."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]

FRAMEWORK_SOURCES = (
    Path("README.md"),
    Path("VERSIONING.md"),
    Path("assessment-standard.md"),
    Path("framework-core.md"),
    Path("glossary.md"),
    Path("implementation-playbook.md"),
    Path("capabilities/assure.md"),
    Path("capabilities/define.md"),
    Path("capabilities/direct.md"),
    Path("capabilities/operate.md"),
    Path("crosswalks/README.md"),
    Path("profiles/README.md"),
)

REQUIRED_PATHS = FRAMEWORK_SOURCES + (
    Path("CHANGELOG.md"),
    Path("CODE_OF_CONDUCT.md"),
    Path("CONTRIBUTING.md"),
    Path("GOVERNANCE.md"),
    Path("LICENSE"),
    Path("SECURITY.md"),
    Path("assets/framework-overview-v0.1.png"),
    Path(".github/PULL_REQUEST_TEMPLATE.md"),
    Path(".github/ISSUE_TEMPLATE/config.yml"),
    Path(".github/ISSUE_TEMPLATE/documentation.yml"),
    Path(".github/ISSUE_TEMPLATE/framework-change.yml"),
    Path(".github/workflows/pages.yml"),
    Path(".github/workflows/validate.yml"),
    Path("package.json"),
    Path("package-lock.json"),
    Path("requirements-publication.txt"),
    Path("publication/manifest.json"),
    Path("publication/template.html"),
    Path("publication/assets/framework.css"),
    Path("publication/assets/framework.js"),
    Path("publication/assets/fonts/OFL.txt"),
    Path("publication/assets/fonts/Poppins-Regular.ttf"),
    Path("publication/assets/fonts/Poppins-SemiBold.ttf"),
    Path("publication/assets/fonts/poppins-400.woff2"),
    Path("publication/assets/fonts/poppins-500.woff2"),
    Path("publication/assets/fonts/poppins-600.woff2"),
    Path("publication/assets/fonts/poppins-700.woff2"),
    Path("publication/assets/fonts/poppins-800.woff2"),
    Path("scripts/build_publication.mjs"),
    Path("scripts/extract_pdf_text.py"),
    Path("scripts/finalize_pdf.py"),
    Path("scripts/render_pdf.mjs"),
    Path("scripts/test_publication.mjs"),
    Path("scripts/validate_pdf.mjs"),
)

ALLOWED_STATUSES = {"draft", "candidate", "stable", "deprecated"}
FRONT_MATTER_PATTERN = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
HEADING_PATTERN = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$", re.MULTILINE)
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\((?P<target>[^)]+)\)")
CAPABILITY_PATTERN = re.compile(r"^## C(?P<number>\d{1,2})\.\s+", re.MULTILINE)


def read_text(relative_path: Path, errors: list[str]) -> str:
    path = ROOT / relative_path
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"{relative_path}: file is not valid UTF-8")
    except OSError as exc:
        errors.append(f"{relative_path}: cannot read file: {exc}")
    return ""


def parse_front_matter(relative_path: Path, text: str, errors: list[str]) -> dict[str, str]:
    match = FRONT_MATTER_PATTERN.match(text)
    if not match:
        errors.append(f"{relative_path}: missing YAML-style front matter")
        return {}

    metadata: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"{relative_path}: unsupported front-matter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"\'')

    for key in ("title", "version", "status", "date"):
        if not metadata.get(key):
            errors.append(f"{relative_path}: missing front-matter field {key!r}")

    status = metadata.get("status")
    if status and status not in ALLOWED_STATUSES:
        errors.append(
            f"{relative_path}: status {status!r} is not one of {sorted(ALLOWED_STATUSES)}"
        )

    version = metadata.get("version", "")
    if version and not re.fullmatch(
        r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)", version
    ):
        errors.append(f"{relative_path}: version {version!r} is not semantic x.y.z")

    date = metadata.get("date", "")
    if date and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        errors.append(f"{relative_path}: date {date!r} is not YYYY-MM-DD")

    return metadata


def validate_headings(relative_path: Path, text: str, errors: list[str]) -> None:
    headings = list(HEADING_PATTERN.finditer(text))
    if not headings:
        errors.append(f"{relative_path}: no Markdown heading found")
        return

    levels = [len(match.group("marks")) for match in headings]
    if levels[0] != 1:
        errors.append(f"{relative_path}: first heading must be level 1")
    if levels.count(1) != 1:
        errors.append(f"{relative_path}: expected exactly one level-1 heading")

    previous = levels[0]
    for match, level in zip(headings[1:], levels[1:]):
        if level > previous + 1:
            errors.append(
                f"{relative_path}:{text.count(chr(10), 0, match.start()) + 1}: "
                f"heading level jumps from {previous} to {level}"
            )
        previous = level


def validate_local_links(relative_path: Path, text: str, errors: list[str]) -> None:
    for match in LINK_PATTERN.finditer(text):
        raw_target = match.group("target").strip()
        target = raw_target.split(maxsplit=1)[0].strip("<>")
        parsed = urlparse(target)
        if parsed.scheme or target.startswith(("#", "mailto:")):
            continue
        file_part = unquote(target.split("#", 1)[0])
        if not file_part:
            continue
        resolved = (ROOT / relative_path.parent / file_part).resolve()
        if ROOT not in resolved.parents and resolved != ROOT:
            errors.append(f"{relative_path}: local link escapes repository: {raw_target!r}")
        elif not resolved.exists():
            errors.append(f"{relative_path}: local link does not exist: {raw_target!r}")


def validate_text_quality(relative_path: Path, text: str, errors: list[str]) -> None:
    if "\r" in text:
        errors.append(f"{relative_path}: contains non-LF line endings")
    if not text.endswith("\n"):
        errors.append(f"{relative_path}: missing final newline")
    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.endswith((" ", "\t")):
            errors.append(f"{relative_path}:{line_number}: trailing whitespace")


def main() -> int:
    errors: list[str] = []

    for relative_path in REQUIRED_PATHS:
        if not (ROOT / relative_path).is_file():
            errors.append(f"missing required file: {relative_path}")

    versions: dict[Path, str] = {}
    statuses: dict[Path, str] = {}
    for relative_path in FRAMEWORK_SOURCES:
        text = read_text(relative_path, errors)
        if not text:
            continue
        metadata = parse_front_matter(relative_path, text, errors)
        versions[relative_path] = metadata.get("version", "")
        statuses[relative_path] = metadata.get("status", "")
        validate_headings(relative_path, text, errors)
        validate_local_links(relative_path, text, errors)
        validate_text_quality(relative_path, text, errors)

    for relative_path in REQUIRED_PATHS:
        if relative_path.suffix in {".css", ".html", ".js", ".json", ".md", ".mjs", ".py", ".txt", ".yml"} and relative_path not in FRAMEWORK_SOURCES:
            text = read_text(relative_path, errors)
            if text:
                validate_text_quality(relative_path, text, errors)
                if relative_path.suffix == ".md":
                    validate_headings(relative_path, text, errors)
                    validate_local_links(relative_path, text, errors)

    declared_versions = {value for value in versions.values() if value}
    if len(declared_versions) > 1:
        details = ", ".join(f"{path}={version}" for path, version in versions.items())
        errors.append(f"framework source versions are inconsistent: {details}")

    capability_numbers: list[int] = []
    for relative_path in (
        Path("capabilities/direct.md"),
        Path("capabilities/define.md"),
        Path("capabilities/operate.md"),
        Path("capabilities/assure.md"),
    ):
        text = read_text(relative_path, errors)
        capability_numbers.extend(
            int(match.group("number")) for match in CAPABILITY_PATTERN.finditer(text)
        )

    counts = Counter(capability_numbers)
    expected = set(range(1, 15))
    actual = set(counts)
    if actual != expected:
        errors.append(
            "capability identifiers must be exactly C1-C14; "
            f"missing={sorted(expected - actual)}, unexpected={sorted(actual - expected)}"
        )
    duplicates = sorted(number for number, count in counts.items() if count != 1)
    if duplicates:
        errors.append(f"capability identifiers must occur once in capability files: {duplicates}")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    version = next(iter(declared_versions), "unknown")
    status_values = sorted({value for value in statuses.values() if value})
    print(
        "Repository validation passed: "
        f"{len(FRAMEWORK_SOURCES)} framework sources, "
        f"14 capabilities, version {version}, statuses {', '.join(status_values)}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
