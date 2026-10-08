---
title: C2 Demand and Use Case Management
version: 0.2.0
status: draft
date: 2026-10-08
---

# C2. Demand and Use Case Management

## Capability summary

| Capability ID | Function | Purpose | Primary owner | Primary standard | Key outputs | Key evidence |
|---|---|---|---|---|---|---|
| C2 | DIRECT | Turn a consumer problem into qualified, reusable demand. | Use-case owner | ODPC | Use case and information need | Registered demand and reuse search |

## Purpose

C2 describes why information is needed before deciding what product to build. A use case identifies the consumer, decision or process, expected outcome and information need without prematurely prescribing a new data product.

## Why it matters

If demand is captured as a product request, duplicate products become likely and teams cannot tell whether a need was met after the implementation changes.

## When it applies

Apply it to new requests, material product changes, regulatory obligations, recurring service problems and agent scenarios that need governed information.

## Inputs

An objective or trigger, consumer, current problem, decision or process, expected outcome, information need and existing-product search are required.

## Practices

Capture the use case in the consumer's language; state the decision, required information and success measure; search existing products before approving a candidate; document the gap and prioritisation rationale.

## Roles and accountability

The use-case owner is accountable for the problem statement and outcome. Consumers validate usefulness, product owners assess reuse, and portfolio governance approves priority.

## Outputs

Outputs are a qualified use case, information needs, an existing-product assessment, gap statement, priority and links to objective and product decision.

## ODPS family mapping

ODPC can represent the UseCase. ODPG expresses its relationship to objectives and products. ODPS represents a later product contract, not the use-case demand.

## Evidence

Keep the registered use case, search results, consumer confirmation, prioritisation record and subsequent adoption/outcome evidence.

## Measures

Track demand evaluated against existing products, time to product decision, reuse across use cases and use cases with an outcome measure.

## Example

Retention analysts need to identify customers likely to leave in 30 days. They require recent purchases, service interactions, loyalty status and customer profile; the search finds Customer 360, Orders and Loyalty but exposes an insufficient service-interaction capability.

## Questions to ask

- Who needs this information and for what decision?
- What outcome should improve?
- Which information is actually required?
- Did we search existing products first?
- Could an existing product be extended?
- How will the use case be judged successful?

## Common failure modes

Common failures are treating a dashboard as the use case, accepting solution-first requests, or recording no reason why reuse was rejected.

## Minimum implementation

Use one shared use-case record with consumer, decision, outcome, information need and existing-product search.

## Advanced implementation

Cluster related demand, measure reuse and maintain a graph of recurring needs, dependencies and outcomes.

## AI-Agent-First extension

An agent may propose a candidate product from an approved information need, but must show the discovery evidence and stop for a human product decision.

## Assessment levels 1-5

Level 1 captures requests ad hoc. Level 2 uses a common use-case record. Level 3 consistently searches existing products and retains rationale. Level 4 measures reuse and demand quality. Level 5 uses evidence to consolidate demand and improve portfolio decisions.
