---
title: C4 Product Definition and Contract
version: 0.2.0
status: draft
date: 2026-10-08
---

# C4. Product Definition and Contract

## Capability summary

| Capability ID | Function | Purpose | Primary owner | Primary standard | Key outputs | Key evidence |
|---|---|---|---|---|---|---|
| C4 | DEFINE | Establish one authoritative, versioned product definition. | Product owner | ODPS | Valid product contract | Validation and approval |

## Purpose

C4 defines a reusable data product as a contract between provider and consumer. It establishes identity, proposition, responsibility, lifecycle, version and consumer-relevant interfaces in an authoritative machine-readable artifact.

## Why it matters

Without a contract, catalog descriptions, platform configuration and tribal knowledge drift apart. Consumers cannot reliably identify which product version or promise applies.

## When it applies

Apply it when a portfolio decision creates or materially changes an individual product, interface, commitment or consumer-facing meaning.

## Inputs

Approved product decision, owner, product proposition, delivery design, lifecycle state, applicable terms, semantic references and change classification are inputs.

## Practices

Assign a stable product identity, author an ODPS contract using the current schema, validate it, approve it, publish an authoritative reference and keep human-facing views aligned with it.

## Roles and accountability

The product owner is accountable for what is offered. Product engineers and stewards maintain the contract; governance and security participants approve applicable conditions; consumers review usability.

## Outputs

Outputs are a versioned ODPS contract, validation result, approval record, publication reference and change history.

## ODPS family mapping

ODPS is primary. ODPV supplies referenced meaning; ODPC carries a lightweight discovery reference; ODPG connects the product to its context. Do not duplicate the full contract in ODPC.

## Evidence

Evidence includes schema validation, approved release, version history, published reference and contract-to-runtime reconciliation where applicable.

## Measures

Measure active products with a valid current contract, validation failure rate, unresolved references and time from approved decision to published contract.

## Example

Customer 360 version 2.4 has a validated ODPS contract describing its reusable customer profile proposition and the current provider responsibility. The service-interaction extension is released through a new approved contract version.

## Questions to ask

- What is the product identity, separate from its catalog record or dataset?
- Which artifact is authoritative?
- Can a consumer see the applicable version and lifecycle state?
- Does the contract validate against the supported schema?
- Does a material change alter meaning, interface, commitment or condition?

## Common failure modes

Typical failures are treating a catalog page as the contract, copying incompatible fields from another specification, or keeping different human and machine descriptions.

## Minimum implementation

Publish one schema-valid ODPS contract with identity, proposition, owner, version and lifecycle state.

## Advanced implementation

Generate catalog and documentation views from the contract and block release when validation or required approvals fail.

## AI-Agent-First extension

An agent needs the authoritative contract, version and resolvable references before it can reason about product suitability; see the [AI-Agent-First Profile](../../profiles/ai-agent-first-data-product-profile.md).

## Assessment levels 1-5

Level 1 has inconsistent documents. Level 2 defines a contract practice. Level 3 uses validated contracts for active products. Level 4 measures completeness and synchronization. Level 5 drives validation, discovery and governed workflows from contracts.
