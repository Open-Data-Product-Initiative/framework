---
title: C8 Catalog Publication and Discovery
version: 0.2.0
status: draft
date: 2026-10-08
---

# C8. Catalog, Publication and Discovery

## Capability summary

| Capability ID | Function | Purpose | Primary owner | Primary standard | Key outputs | Key evidence |
|---|---|---|---|---|---|---|
| C8 | OPERATE | Make approved products findable and understandable. | Catalog owner | ODPC | Catalog reference and discovery view | Publication and synchronization evidence |

## Purpose

C8 publishes a product's proposition, status, owner, current version and authoritative contract reference so a consumer can decide whether to investigate or request access.

## Why it matters

If discovery relies on personal knowledge, existing products are missed and duplicate demand becomes the default. A catalog copy that drifts from the contract creates false confidence.

## When it applies

Apply it when an approved product or a material version becomes available, changes lifecycle state or must be made discoverable across domains.

## Inputs

An approved product contract, catalog metadata, product proposition, visibility decision, owner, lifecycle state, product-model reference and graph context are required.

## Practices

Create a lightweight catalog reference to the authoritative model, expose consumer language and material conditions, validate references, publish through the approved catalog and reconcile synchronization failures.

## Roles and accountability

The catalog owner is accountable for the discovery service; the product owner confirms the offering; stewards maintain quality; access and governance teams set visibility boundaries.

## Outputs

Produce an ODPC catalog entry, search facets, publication record, authoritative contract link and synchronization status.

## ODPS family mapping

ODPC is primary. It references, rather than repeats, the ODPS product model. ODPG provides relationship context and ODPV enables consistent search terms.

## Evidence

Evidence includes successful publication, reference validation, crawl or discovery test, synchronization log and consumer feedback.

## Measures

Measure discoverability, stale references, search-to-access conversion and time for a published contract change to appear in the catalog.

## Example

Customer 360 has an ODPC ProductReference that points to the authoritative ODPS version 2.4 contract and exposes its customer-retention value proposition, status, owner and restricted visibility.

## Questions to ask

- Can a consumer find the product using business language?
- Does the entry point to the current authoritative contract?
- Which visibility and access conditions must be visible before a request?
- How are stale or broken references detected?
- Does discovery imply availability or only suitability for request?

## Common failure modes

Typical failures are copying the entire contract into the catalog, publishing unapproved drafts, or equating search visibility with permission to access.

## Minimum implementation

Publish one ODPC reference with product identity, version, description, owner, visibility and contract link.

## Advanced implementation

Federate catalog references, validate them continuously and use outcome-based search quality measures.

## AI-Agent-First extension

Agents need machine-readable discovery results that distinguish candidate suitability from access approval and identify the authoritative product version.

## Assessment levels 1-5

Level 1 has unstructured listings. Level 2 defines catalog publication. Level 3 maintains validated current references. Level 4 measures discovery quality and drift. Level 5 supports governed machine discovery and evidence-backed selection.
