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
    Path("profiles/enterprise-data-product-profile.md"),
    Path("profiles/ai-agent-first-data-product-profile.md"),
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
    Path("library/README.md"),
    Path("library/source-policy.md"),
    Path("library/catalog.json"),
    Path("library/collections/ai-and-agent-governance.json"),
    Path("library/collections/data-product-management.json"),
    Path("library/collections/governance-and-assurance.json"),
    Path("library/collections/outcomes-and-value.json"),
    Path("library/collections/semantics-and-interoperability.json"),
    Path("enrichment/README.md"),
    Path("enrichment/briefs/README.md"),
    Path("enrichment/proposals/README.md"),
    Path("enrichment/reviews/README.md"),
    Path("scripts/library_support.py"),
    Path("scripts/validate_library.py"),
    Path("scripts/ingest_library.py"),
    Path("scripts/build_library_index.py"),
    Path("scripts/propose_enrichment.py"),
    Path("scripts/validate_enrichment.py"),
)

ALLOWED_STATUSES = {"draft", "candidate", "stable", "deprecated"}
FRONT_MATTER_PATTERN = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
HEADING_PATTERN = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$", re.MULTILINE)
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\((?P<target>[^)]+)\)")
CAPABILITY_PATTERN = re.compile(r"^## C(?P<number>\d{1,2})\.\s+", re.MULTILINE)
CAPABILITY_HEADING_PATTERN = re.compile(
    r"^#{2,4}\s+C(?P<number>\d{1,2})\.\s+(?P<name>.+?)\s*$", re.MULTILINE
)
ASSESSMENT_ROW_PATTERN = re.compile(
    r"^\|\s*C(?P<number>\d{1,2})\s+(?P<name>[^|]+?)\s*\|", re.MULTILINE
)

CANONICAL_CAPABILITIES = {
    1: "Strategy and Objectives",
    2: "Demand and Use Case Management",
    3: "Portfolio, Investment and Accountability",
    4: "Product Definition and Contract",
    5: "Semantics and Vocabulary",
    6: "Product Commitments and Usage Conditions",
    7: "Relationships, Dependencies and Context",
    8: "Catalog, Publication and Discovery",
    9: "Provisioning, Integration and Consumption",
    10: "Lifecycle, Version and Change Management",
    11: "Workflow, Automation and Agent Operations",
    12: "Observability and Service Assurance",
    13: "Governance, Risk, Compliance and Control Assurance",
    14: "Adoption, Outcomes and Value Realisation",
}


def validate_capability_names(
    relative_path: Path,
    matches: list[re.Match[str]],
    errors: list[str],
    require_all: bool = True,
) -> None:
    found: dict[int, list[str]] = {}
    for match in matches:
        number = int(match.group("number"))
        found.setdefault(number, []).append(match.group("name").strip())

    expected_numbers = set(CANONICAL_CAPABILITIES)
    actual_numbers = set(found)
    if require_all and actual_numbers != expected_numbers:
        errors.append(
            f"{relative_path}: capability headings must contain exactly C1-C14; "
            f"missing={sorted(expected_numbers - actual_numbers)}, "
            f"unexpected={sorted(actual_numbers - expected_numbers)}"
        )

    for number, names in found.items():
        if number not in CANONICAL_CAPABILITIES:
            errors.append(f"{relative_path}: unexpected capability C{number}")
            continue
        if len(names) != 1:
            errors.append(f"{relative_path}: capability C{number} must occur once")
        for name in names:
            if name != CANONICAL_CAPABILITIES[number]:
                errors.append(
                    f"{relative_path}: C{number} must be named "
                    f"{CANONICAL_CAPABILITIES[number]!r}, found {name!r}"
                )


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
    capability_heading_matches: list[re.Match[str]] = []
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
        capability_heading_matches.extend(CAPABILITY_HEADING_PATTERN.finditer(text))

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

    validate_capability_names(
        Path("capabilities/"), capability_heading_matches, errors, require_all=True
    )

    for relative_path in (
        Path("framework-core.md"),
        Path("profiles/enterprise-data-product-profile.md"),
        Path("profiles/ai-agent-first-data-product-profile.md"),
    ):
        text = read_text(relative_path, errors)
        validate_capability_names(
            relative_path,
            list(CAPABILITY_HEADING_PATTERN.finditer(text)),
            errors,
            require_all=True,
        )

    assessment_text = read_text(Path("assessment-standard.md"), errors)
    validate_capability_names(
        Path("assessment-standard.md"),
        list(ASSESSMENT_ROW_PATTERN.finditer(assessment_text)),
        errors,
        require_all=True,
    )

    core_text = read_text(Path("framework-core.md"), errors)
    readme_text = read_text(Path("README.md"), errors)
    profiles_text = read_text(Path("profiles/README.md"), errors)
    ai_profile_text = read_text(
        Path("profiles/ai-agent-first-data-product-profile.md"), errors
    )

    required_core_phrases = (
        "universal, vendor-neutral and technology-neutral operating model",
        "F4. Machine-readable by default, human-readable by presentation",
        "F15. One Core, multiple profiles",
        "The framework does not require organisations to operate AI agents.",
        "The framework is an operating model, not another ODPS-family specification.",
        "human users",
        "traditional applications",
    )
    for phrase in required_core_phrases:
        if phrase not in core_text:
            errors.append(f"framework-core.md: missing required architecture phrase {phrase!r}")

    for phrase in (
        "Enterprise Data Product Profile",
        "AI-Agent-First Data Product Profile",
        "Machine-Readable Data Products",
        "Agent-Ready Data Products",
        "Agent-First Operations",
    ):
        if phrase not in readme_text or phrase not in profiles_text:
            errors.append(f"README/profile index: missing required profile concept {phrase!r}")

    if "The AI-Agent-First Profile extends the" not in ai_profile_text:
        errors.append(
            "profiles/ai-agent-first-data-product-profile.md: must state that the "
            "AI-Agent-First Profile extends the Core"
        )
    if "It does not create a separate framework." not in ai_profile_text:
        errors.append(
            "profiles/ai-agent-first-data-product-profile.md: must reject a separate framework"
        )

    for obsolete_profile in (
        "AI-Agent-Ready Data Product Profile",
        "Public Sector Data Product Profile",
        "Open Data Product Profile",
        "Commercial Data Product Profile",
        "Regulated Data Product Profile",
    ):
        if obsolete_profile in core_text or obsolete_profile in profiles_text:
            errors.append(
                f"Core profile architecture contains obsolete candidate {obsolete_profile!r}"
            )

    for authority in ("ODPS", "ODPC", "ODPV", "ODPG", "ODPR"):
        if f"### {authority}" not in core_text:
            errors.append(f"framework-core.md: missing distinct authority section for {authority}")

    authority_responsibilities = (
        "individual data product contract",
        "portfolio and discovery objects",
        "shared vocabulary and semantics",
        "relationships and context",
        "reusable workflow contracts",
        "Responsible for runtime execution",
        "proves what happened",
    )
    for phrase in authority_responsibilities:
        if phrase not in core_text:
            errors.append(
                f"framework-core.md: authority model is missing responsibility {phrase!r}"
            )

    if "not independent normative sources" not in readme_text:
        errors.append(
            "README.md: generated HTML and PDF must be identified as non-normative outputs"
        )

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
