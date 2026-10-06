#!/usr/bin/env python3
"""Validate generated enrichment proposals and their catalog citations."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from library_support import ROOT, sources_by_id


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("proposals", nargs="+", type=Path)
    return parser.parse_args()


def validate(path: Path, known_sources: set[str]) -> list[str]:
    errors: list[str] = []
    try:
        proposal = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read valid JSON: {exc}"]
    if proposal.get("schema_version") != "1.0.0":
        errors.append("schema_version must be 1.0.0")
    if proposal.get("review_status") != "unreviewed":
        errors.append("generated proposal review_status must remain unreviewed")
    if proposal.get("normative_effect") != "none":
        errors.append("generated proposal normative_effect must be none")
    target = proposal.get("target", {})
    target_path = (ROOT / target.get("path", "")).resolve()
    if ROOT not in target_path.parents or target_path.suffix != ".md" or not target_path.is_file():
        errors.append("target must be an existing Markdown file inside the repository")
    evidence = proposal.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        errors.append("evidence must be a non-empty array")
        evidence = []
    evidence_ids = {item.get("source_id") for item in evidence if isinstance(item, dict)}
    unknown_evidence = sorted(value for value in evidence_ids - known_sources if value)
    if unknown_evidence:
        errors.append(f"evidence contains unknown source IDs: {unknown_evidence}")
    if None in evidence_ids:
        errors.append("every evidence item requires source_id")
    if not proposal.get("question") or not proposal.get("prompt"):
        errors.append("question and prompt are required")
    model = proposal.get("model", {})
    response = proposal.get("response")
    if model.get("invoked"):
        if not model.get("endpoint") or not model.get("name"):
            errors.append("invoked model requires endpoint and name metadata")
        if not isinstance(response, dict):
            errors.append("invoked model requires a parsed JSON response")
    elif response is not None:
        errors.append("dry-run proposal must not contain a response")
    if isinstance(response, dict):
        for field in ("summary", "draft_markdown", "claims", "limitations", "architecture_impact"):
            if field not in response:
                errors.append(f"response missing {field}")
        claims = response.get("claims", [])
        if not isinstance(claims, list) or not claims:
            errors.append("response claims must be a non-empty array")
            claims = []
        for index, claim in enumerate(claims):
            source_ids = claim.get("source_ids", []) if isinstance(claim, dict) else []
            if not claim or not claim.get("claim") or not claim.get("support"):
                errors.append(f"claim {index} requires claim and support")
            if not source_ids:
                errors.append(f"claim {index} requires at least one source_id")
            unknown = sorted(set(source_ids) - known_sources)
            if unknown:
                errors.append(f"claim {index} has unknown source IDs: {unknown}")
            unavailable = sorted(set(source_ids) - evidence_ids)
            if unavailable:
                errors.append(f"claim {index} cites sources absent from retrieved evidence: {unavailable}")
    return errors


def main() -> int:
    args = arguments()
    known_sources = set(sources_by_id())
    all_errors: list[str] = []
    for path in args.proposals:
        errors = validate(path, known_sources)
        all_errors.extend(f"{path}: {error}" for error in errors)
    if all_errors:
        print("Enrichment validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1
    print(f"Enrichment validation passed: {len(args.proposals)} proposal(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
