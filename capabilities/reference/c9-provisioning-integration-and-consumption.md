---
title: C9 Provisioning Integration and Consumption
version: 0.2.0
status: draft
date: 2026-10-08
---

# C9. Provisioning, Integration and Consumption

## Capability summary

| Capability ID | Function | Purpose | Primary owner | Primary standard | Key outputs | Key evidence |
|---|---|---|---|---|---|---|
| C9 | OPERATE | Provide controlled, usable consumption. | Access owner | ODPS; ODPR where workflow is portable | Access decision and usable connection | Entitlement and acceptance evidence |

## Purpose

C9 turns a permitted request into usable consumption with the correct interface, version, terms and support path. It preserves the difference between being discoverable, being approved and being able to use the product successfully.

## Why it matters

Credentials alone do not prove a consumer received the right product or understood the conditions. Missing consumption evidence also makes later adoption claims unreliable.

## When it applies

Apply it to consumer onboarding, access renewal, integration change, delegated agent access and revocation.

## Inputs

Consumer identity, intended use, applicable conditions, product and interface version, approval route, entitlement design and support ownership are needed.

## Practices

Evaluate a request, record a decision, provision the allowed scope, communicate version and conditions, perform a safe connectivity or acceptance check, and retain proportionate consumption evidence.

## Roles and accountability

The access owner is accountable for the entitlement decision. Product owners supply interface and condition context; security and privacy roles approve constrained cases; consumers confirm intended use.

## Outputs

Produce an access decision, entitlement, onboarding record, integration guidance, accepted connection or rejection rationale.

## ODPS family mapping

ODPS describes product access where supported. ODPR can express a portable onboarding workflow. Runtime entitlement systems and logs provide operating evidence, not new ODPS fields.

## Evidence

Keep request, approval, conditions shown, entitlement, product version, acceptance test and revocation record.

## Measures

Measure provisioning time, active entitlements linked to a purpose, failed onboarding, expired access and successful first use.

## Example

The retention analytics group receives approved read access to Customer 360 version 2.4 for churn-risk analysis. The evidence includes the approved purpose, restricted scope, connection test and terms acknowledgement.

## Questions to ask

- Who is consuming which product version for what purpose?
- Are access conditions evaluated before provisioning?
- Can the consumer use the interface successfully?
- How are denied, expired or revoked requests handled?
- What consumption evidence is proportionate and lawful?

## Common failure modes

Common failures include treating account creation as onboarding, granting broad access because a product is discoverable, and collecting invasive usage telemetry without need.

## Minimum implementation

Record the request, decision, product version, permitted purpose and a successful acceptance check for one consumer group.

## Advanced implementation

Automate only well-defined decisions, continuously reconcile entitlements and link consumption evidence to use-case outcome reviews.

## AI-Agent-First extension

An agent must present its identity, permitted purpose and required version, then stop on denial, ambiguity or a required human approval.

## Assessment levels 1-5

Level 1 provisions manually without records. Level 2 defines a controlled path. Level 3 retains request-to-use evidence. Level 4 measures entitlement quality and exceptions. Level 5 supports policy-aware automation with reviewable decisions.
