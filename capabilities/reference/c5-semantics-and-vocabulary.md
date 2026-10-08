---
title: C5 Semantics and Vocabulary
version: 0.2.0
status: draft
date: 2026-10-08
---

# C5. Semantics and Vocabulary

## Capability summary

| Capability ID | Function | Purpose | Primary owner | Primary standard | Key outputs | Key evidence |
|---|---|---|---|---|---|---|
| C5 | DEFINE | Make material concepts interpretable consistently. | Semantic steward | ODPV | Controlled terms and mappings | Approved vocabulary version |

## Purpose

C5 governs the concepts whose interpretation changes a decision, rule, calculation or integration. It separates a stable concept identity from labels and aliases.

## Why it matters

Ambiguous terms such as “active customer” allow two correct-looking but incompatible uses of the same product, especially across domains and AI-assisted work.

## When it applies

Apply it when a term is shared across products, appears in a material commitment or policy, or could be interpreted differently by consumers or agents.

## Inputs

Candidate terms, existing definitions, subject experts, external mappings, product fields and known ambiguity are inputs.

## Practices

Reuse a definition where possible; assign identifiers; retain preferred labels, aliases, definitions and relationships; map external terms cautiously; version changes and check contract and graph references.

## Roles and accountability

A semantic steward is accountable for definition quality. Product owners apply terms, domain experts validate meaning and governance participants resolve material conflicts.

## Outputs

Produce a versioned vocabulary, term decisions, mappings, deprecated terms and usage references.

## ODPS family mapping

ODPV is primary. ODPS and ODPC reference the meaning they need; ODPG shows where concepts and products are connected. Semantics are not an unstructured note in every product contract.

## Evidence

Keep vocabulary validation, stewardship approval, mapping rationale, usage scans and change records.

## Measures

Measure material terms with an owner, active contracts referencing approved terms, unresolved ambiguity and time to resolve a semantic conflict.

## Example

Customer 360 uses the approved definition of “customer” and documents that “service interaction” includes a recorded assisted contact, not an abandoned call event.

## Questions to ask

- Which term would create material risk if interpreted differently?
- Is the identifier distinct from the label?
- Does an existing approved definition apply?
- Who can approve a changed meaning?
- Where is the term used across products and policies?

## Common failure modes

Teams standardise labels only, assume two identical labels mean the same thing, or map terms as equivalent without recording limitations.

## Minimum implementation

Define and assign a steward to the small set of terms that control the pilot's decisions and metrics.

## Advanced implementation

Provide versioned, machine-readable vocabulary with mapping governance and automated reference checks.

## AI-Agent-First extension

Agents should resolve a concept identifier and definition before joining or acting on product data; ambiguity is a stopping condition, not a prompt to guess.

## Assessment levels 1-5

Level 1 has local labels. Level 2 maintains managed definitions. Level 3 applies them across active products. Level 4 detects drift and unresolved mappings. Level 5 uses semantic context in discovery, validation and governed agent workflows.
