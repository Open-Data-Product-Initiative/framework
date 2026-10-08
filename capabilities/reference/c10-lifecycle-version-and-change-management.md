---
title: C10 Lifecycle Version and Change Management
version: 0.2.0
status: draft
date: 2026-10-08
---

# C10. Lifecycle, Version and Change Management

## Capability summary

| Capability ID | Function | Purpose | Primary owner | Primary standard | Key outputs | Key evidence |
|---|---|---|---|---|---|---|
| C10 | OPERATE | Change products without hiding consumer impact. | Product owner | ODPS; ODPG for impact | Version, change decision and notice | Approval and deployment reconciliation |

## Purpose

C10 manages the product lifecycle and makes consumer-relevant change visible. It distinguishes an implementation change from a change to meaning, interface, commitment or usage condition.

## Why it matters

Unclassified change breaks consumers quietly, invalidates assurance evidence and makes it impossible to know which contract governed a past use.

## When it applies

Apply it to releases, deprecations, breaking changes, dependency changes, exception expiry and retirement.

## Inputs

Current and proposed contract versions, impact analysis, downstream relationships, tests, approvals, consumer list and migration plan are inputs.

## Practices

Classify the change, update the authoritative artifact, assess graph impact, obtain required approval, communicate to affected consumers, reconcile deployed versus declared version and retain rollback or retirement evidence.

## Roles and accountability

The product owner approves within delegated authority. Engineers implement, consumers validate material changes, and governance participants approve risk, privacy or policy implications.

## Outputs

Outputs are a change record, new product version, impact analysis, approval, release notice, deprecation plan and deployment reconciliation.

## ODPS family mapping

ODPS carries product version and lifecycle declaration. ODPG identifies affected context. ODPR can express a reusable release workflow. Operational deployment evidence remains external to the contract.

## Evidence

Retain semantic version decision, diff, validation results, approvals, consumer notification, deployment record and actual runtime version check.

## Measures

Measure unreconciled deployed versions, breaking changes with notice, migration completion, failed changes and deprecated versions still consumed.

## Example

Customer 360 declares 2.4, while runtime evidence shows 2.3. The mismatch, missing approval for the latest deployment and affected retention consumers become an assurance and change-control issue.

## Questions to ask

- What changed for a consumer?
- Which version is declared and which is deployed?
- Who is affected through dependencies?
- Was the required approval recorded?
- Is there a supported migration or rollback path?

## Common failure modes

Teams version code but not the contract, use a release date as a version, or retire an interface without checking active consumers.

## Minimum implementation

Use a versioned contract, a change classification, approval and consumer notice for one material change.

## Advanced implementation

Automate impact detection and reconciliation while keeping policy decisions and risk acceptance accountable.

## AI-Agent-First extension

An agent must check product and workflow versions before execution and stop if the declared and deployed states are incompatible.

## Assessment levels 1-5

Level 1 changes are informal. Level 2 has lifecycle and version rules. Level 3 retains controlled change evidence. Level 4 measures drift and change outcomes. Level 5 uses validated context to coordinate safe automated change paths.
