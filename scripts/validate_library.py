#!/usr/bin/env python3
"""Validate evidence catalog, collections and their authority boundaries."""

from __future__ import annotations

import re
import sys
from datetime import date
from urllib.parse import urlparse

from library_support import CATALOG_PATH, load_catalog, load_collections


SOURCE_ID = re.compile(r"[a-z0-9]+(?:[.-][a-z0-9]+)*\Z")
SOURCE_TYPES = {
    "official-standard",
    "official-guidance",
    "regulation",
    "intergovernmental-recommendation",
    "peer-reviewed-research",
    "professional-framework",
    "implementation-example",
}
ACCESS_VALUES = {"local-analysis", "metadata-only"}
REDISTRIBUTION_VALUES = {"not-cleared", "prohibited", "cc-by-4.0"}


def main() -> int:
    errors: list[str] = []
    try:
        catalog = load_catalog()
        collections = load_collections()
    except (OSError, ValueError) as exc:
        print(f"Library validation failed: {exc}")
        return 1

    if catalog.get("schema_version") != "1.0.0":
        errors.append("catalog schema_version must be 1.0.0")
    if not collections:
        errors.append("at least one source collection is required")

    source_records = catalog.get("sources")
    if not isinstance(source_records, list) or not source_records:
        errors.append("catalog sources must be a non-empty array")
        source_records = []

    ids: set[str] = set()
    required = {
        "id", "title", "publisher", "source_type", "authority_tier",
        "publication_status", "version", "url", "access", "redistribution",
        "license_note", "collections", "capabilities", "summary", "use_for", "not_for"
    }
    for index, source in enumerate(source_records):
        label = source.get("id", f"source[{index}]") if isinstance(source, dict) else f"source[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{label}: source must be an object")
            continue
        missing = sorted(required - set(source))
        if missing:
            errors.append(f"{label}: missing fields {missing}")
        source_id = source.get("id", "")
        if not SOURCE_ID.fullmatch(source_id):
            errors.append(f"{label}: invalid stable source id")
        if source_id in ids:
            errors.append(f"{label}: duplicate source id")
        ids.add(source_id)
        if source.get("source_type") not in SOURCE_TYPES:
            errors.append(f"{label}: unsupported source_type {source.get('source_type')!r}")
        if source.get("authority_tier") not in range(1, 6):
            errors.append(f"{label}: authority_tier must be 1-5")
        if source.get("access") not in ACCESS_VALUES:
            errors.append(f"{label}: unsupported access policy")
        if source.get("redistribution") not in REDISTRIBUTION_VALUES:
            errors.append(f"{label}: unsupported redistribution policy")
        if source.get("access") == "metadata-only" and source.get("retrieval_url"):
            errors.append(f"{label}: metadata-only source must not have retrieval_url")
        for url_field in ("url", "retrieval_url"):
            value = source.get(url_field)
            if value and urlparse(value).scheme != "https":
                errors.append(f"{label}: {url_field} must use https")
        published = source.get("published")
        if published:
            try:
                date.fromisoformat(published)
            except (TypeError, ValueError):
                errors.append(f"{label}: published must be YYYY-MM-DD or null")
        capabilities = source.get("capabilities", [])
        if not capabilities or any(value not in range(1, 15) for value in capabilities):
            errors.append(f"{label}: capabilities must contain only C1-C14 numbers")
        if capabilities != sorted(set(capabilities)):
            errors.append(f"{label}: capabilities must be sorted and unique")
        for field in ("collections", "use_for", "not_for"):
            if not isinstance(source.get(field), list) or not source.get(field):
                errors.append(f"{label}: {field} must be a non-empty array")
        if len(source.get("summary", "")) < 40:
            errors.append(f"{label}: summary is too short")

    collection_memberships: dict[str, set[str]] = {}
    for filename_id, collection in collections.items():
        collection_id = collection.get("id")
        if filename_id != collection_id:
            errors.append(f"collection {filename_id}: id must match filename")
        if not collection.get("title") or not collection.get("purpose"):
            errors.append(f"collection {filename_id}: title and purpose are required")
        members = collection.get("source_ids")
        if not isinstance(members, list) or not members:
            errors.append(f"collection {filename_id}: source_ids must be non-empty")
            members = []
        if members != list(dict.fromkeys(members)):
            errors.append(f"collection {filename_id}: source_ids must be unique")
        unknown = sorted(set(members) - ids)
        if unknown:
            errors.append(f"collection {filename_id}: unknown source ids {unknown}")
        collection_memberships[filename_id] = set(members)

    for source in source_records:
        if not isinstance(source, dict):
            continue
        for collection_id in source.get("collections", []):
            if collection_id not in collections:
                errors.append(f"{source.get('id')}: unknown collection {collection_id!r}")
            elif source.get("id") not in collection_memberships[collection_id]:
                errors.append(f"{source.get('id')}: missing from collection {collection_id}")
    for collection_id, members in collection_memberships.items():
        for source_id in members:
            source = next((item for item in source_records if item.get("id") == source_id), {})
            if collection_id not in source.get("collections", []):
                errors.append(f"collection {collection_id}: {source_id} lacks reciprocal membership")

    if errors:
        print("Library validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Library validation passed: {len(source_records)} sources in "
        f"{len(collections)} collections ({CATALOG_PATH.relative_to(CATALOG_PATH.parents[1])})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
