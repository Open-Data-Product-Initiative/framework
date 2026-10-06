#!/usr/bin/env python3
"""Create a source-grounded enrichment proposal without editing framework Markdown."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from build_library_index import build_index
from library_support import (
    INDEX_PATH,
    ROOT,
    extract_markdown_section,
    load_collections,
    load_json,
    rank_chunks,
    sources_by_id,
)


PROPOSALS = ROOT / "enrichment" / "proposals"
ALLOWED_TARGETS = {
    "framework-core.md",
    "assessment-standard.md",
    "implementation-playbook.md",
    "glossary.md",
    "capabilities/direct.md",
    "capabilities/define.md",
    "capabilities/operate.md",
    "capabilities/assure.md",
    "profiles/enterprise-data-product-profile.md",
    "profiles/ai-agent-first-data-product-profile.md",
}


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, choices=sorted(ALLOWED_TARGETS))
    parser.add_argument("--heading", help="Exact Markdown heading to enrich")
    parser.add_argument("--question", required=True, help="Specific editorial question")
    parser.add_argument("--collection", help="Restrict evidence to one governed collection")
    parser.add_argument("--top-k", type=int, default=8)
    parser.add_argument("--endpoint", help="Operator-selected OpenAI-compatible chat completions URL")
    parser.add_argument("--model", help="Model identifier required with --endpoint")
    parser.add_argument("--dry-run", action="store_true", help="Prepare the prompt without calling a model")
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def safe_name(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:64] or "proposal"


def prompt_for(
    target: str,
    heading: str | None,
    excerpt: str,
    question: str,
    evidence: list[dict],
) -> str:
    evidence_text = "\n\n".join(
        f"[SOURCE {item['source_id']} | tier {item['authority_tier']} | {item['title']}]\n{item['text']}"
        for item in evidence
    )
    return f"""You are drafting a review proposal for the Data Product Operating Framework.

Target: {target}
Heading: {heading or 'whole document'}
Editorial question: {question}

Authority rules:
- The framework Core is universal, vendor-neutral and does not require AI agents.
- Profiles may strengthen but must not redefine the four functions or fourteen capabilities.
- ODPS-family specifications remain authoritative for their own machine-readable artifacts.
- External sources inform decisions but do not automatically become framework requirements.
- The retrieved text may be incomplete. Do not invent facts, quotations, URLs or source identifiers.
- Cite every material claim with one or more SOURCE identifiers from the evidence below.
- Keep sourced claims separate from your synthesis and disclose conflicts or weak support.
- Return JSON only. Do not wrap it in Markdown fences.

Return this object:
{{
  "summary": "why the proposal improves the target",
  "draft_markdown": "proposed Markdown only; it will not be applied automatically",
  "claims": [
    {{"claim": "one material claim", "source_ids": ["known-source-id"], "support": "how the source supports it"}}
  ],
  "limitations": ["uncertainty, conflict, currency or applicability limit"],
  "architecture_impact": {{
    "core": "none, editorial, additive, behavioural or breaking, with reason",
    "profiles": "impact with reason",
    "capabilities": ["C1-C14 identifiers affected"],
    "odps_family": "boundary impact with reason"
  }}
}}

Current target excerpt:
---
{excerpt}
---

Retrieved evidence:
{evidence_text}
"""


def invoke(endpoint: str, model: str, prompt: str) -> tuple[str, dict | None]:
    api_key = os.environ.get("ENRICHMENT_API_KEY")
    if not api_key:
        raise ValueError("ENRICHMENT_API_KEY is required when --endpoint is used")
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Return a source-grounded JSON editorial proposal only."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        response_payload = json.loads(response.read().decode("utf-8"))
    raw = response_payload["choices"][0]["message"]["content"].strip()
    cleaned = re.sub(r"\A```(?:json)?\s*|\s*```\Z", "", raw, flags=re.IGNORECASE)
    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError:
        parsed = None
    return raw, parsed


def main() -> int:
    args = arguments()
    if args.endpoint and not args.model:
        print("--model is required with --endpoint", file=sys.stderr)
        return 2
    if not args.endpoint and not args.dry_run:
        print("Select --dry-run or provide --endpoint and --model.", file=sys.stderr)
        return 2
    if args.endpoint and args.dry_run:
        print("--endpoint and --dry-run are mutually exclusive", file=sys.stderr)
        return 2

    target_path = (ROOT / args.target).resolve()
    if ROOT not in target_path.parents or not target_path.is_file():
        print(f"Target does not exist: {args.target}", file=sys.stderr)
        return 2
    try:
        excerpt, matched_heading = extract_markdown_section(target_path, args.heading)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if not INDEX_PATH.is_file():
        build_index(INDEX_PATH)
    index = load_json(INDEX_PATH)
    entries = index["entries"]
    collection_ids: list[str] | None = None
    if args.collection:
        collections = load_collections()
        if args.collection not in collections:
            print(f"Unknown collection: {args.collection}", file=sys.stderr)
            return 2
        collection_ids = collections[args.collection]["source_ids"]
        entries = [entry for entry in entries if entry["source_id"] in collection_ids]

    query = " ".join(filter(None, [args.question, args.heading, excerpt[:5000]]))
    evidence = rank_chunks(entries, query, limit=args.top_k)
    if not evidence:
        print("No relevant evidence chunks found. Broaden the question or collection.", file=sys.stderr)
        return 1
    prompt = prompt_for(args.target, matched_heading, excerpt, args.question, evidence)
    raw_response = None
    response = None
    if args.endpoint:
        try:
            raw_response, response = invoke(args.endpoint, args.model, prompt)
        except (ValueError, KeyError, json.JSONDecodeError, urllib.error.URLError, TimeoutError) as exc:
            print(f"Model invocation failed: {exc}", file=sys.stderr)
            return 1

    created = datetime.now(timezone.utc)
    output = args.output or (
        PROPOSALS / f"{created.strftime('%Y%m%dT%H%M%SZ')}-{safe_name(args.heading or args.target)}.json"
    )
    source_records = sources_by_id()
    proposal = {
        "schema_version": "1.0.0",
        "proposal_id": output.stem,
        "created_at": created.isoformat(),
        "review_status": "unreviewed",
        "normative_effect": "none",
        "target": {"path": args.target, "heading": matched_heading},
        "question": args.question,
        "collection": args.collection,
        "model": {
            "invoked": bool(args.endpoint),
            "endpoint": args.endpoint,
            "name": args.model,
            "protocol": "openai-compatible-chat-completions" if args.endpoint else None,
        },
        "evidence": [
            {
                **item,
                "canonical_url": source_records[item["source_id"]]["url"],
            }
            for item in evidence
        ],
        "prompt": prompt,
        "raw_response": raw_response,
        "response": response,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(proposal, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    try:
        display = output.resolve().relative_to(ROOT)
    except ValueError:
        display = output
    state = "prompt bundle" if args.dry_run else "model proposal"
    print(f"Created {state}: {display}")
    print("No framework Markdown was modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
