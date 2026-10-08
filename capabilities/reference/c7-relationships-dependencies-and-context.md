---
title: C7 Relationships Dependencies and Context
version: 0.2.0
status: draft
date: 2026-10-08
---

# C7. Relationships, Dependencies and Context

## Capability summary

| Capability ID | Function | Purpose | Primary owner | Primary standard | Key outputs | Key evidence |
|---|---|---|---|---|---|---|
| C7 | DEFINE | Connect product context into a traversable graph. | Product owner | ODPG | Valid relationship graph | Graph validation and review |

## Purpose

C7 records the material relationships that let a person or system traverse from objective to use case, product, policy, workflow, consumer and outcome.

## Why it matters

An isolated catalog record cannot answer what breaks when an upstream product, policy or definition changes. Free-text dependency notes are neither testable nor reliably traversable.

## When it applies

Apply it when a relationship supports discovery, impact analysis, accountability, assurance, workflow or value traceability.

## Inputs

Stable object references, approved relationship types, sources of assertion, confidence, owner and review criteria are inputs.

## Practices

Record both ends and direction of a relationship; distinguish confirmed from inferred edges; validate references; review critical paths; retain provenance and resolve conflicts rather than overwriting them.

## Roles and accountability

Product owners confirm product edges. Domain owners confirm objectives and use cases. Stewards maintain relationship conventions; governance roles review critical dependencies.

## Outputs

Produce an ODPG graph, relationship provenance, dependency analysis and a review or remediation record for broken critical edges.

## ODPS family mapping

ODPG is primary. ODPC supplies objective, use-case and product-reference objects; ODPS remains the detailed product contract; ODPV supplies shared relationship terminology where adopted.

## Evidence

Evidence is a validated graph, reference-resolution report, source of assertion, review record and impact analysis.

## Measures

Track unresolved critical references, confirmed relationships, graph review coverage and time to identify affected consumers after a change.

## Example

The Customer 360 graph links the churn use case to its objective, Customer 360, Orders, Loyalty and the service-interaction gap. It also connects the extension workflow and retention outcome.

## Questions to ask

- What decision requires this edge?
- Are both endpoint identifiers resolvable?
- Is the relationship direction meaningful?
- Is it confirmed or inferred, and by whom?
- Can the graph answer an impact question?

## Common failure modes

Teams graph every possible link, treat inference as fact, or record relationships without source, owner or review responsibility.

## Minimum implementation

Create a small validated graph that links the pilot objective, use case, product and dependency.

## Advanced implementation

Use graph traversal for impact analysis, discovery and control coverage while preserving confidence and provenance.

## AI-Agent-First extension

Agents use only resolvable, permitted graph context and must expose the traversed path as evidence for a recommendation.

## Assessment levels 1-5

Level 1 has isolated notes. Level 2 defines key relationship types. Level 3 maintains valid critical paths. Level 4 measures integrity and impact response. Level 5 uses graph context in automated checks and governed workflows.
