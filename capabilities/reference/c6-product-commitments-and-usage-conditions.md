---
title: C6 Product Commitments and Usage Conditions
version: 0.2.0
status: draft
date: 2026-10-08
---

# C6. Product Commitments and Usage Conditions

## Capability summary

| Capability ID | Function | Purpose | Primary owner | Primary standard | Key outputs | Key evidence |
|---|---|---|---|---|---|---|
| C6 | DEFINE | Declare measurable product promises and conditions. | Product owner | ODPS where supported | SLA, quality and usage conditions | Approved conditions and exceptions |

## Purpose

C6 makes clear what a consumer may expect and under which conditions it may use the product. A commitment includes the subject, metric or rule, threshold, period and measurement method.

## Why it matters

“High quality” and “available when needed” cannot be assured. An access rule without a scope, approver or enforcement path leaves consumers and providers guessing.

## When it applies

Apply it whenever a product has quality, freshness, service, access, privacy, security, licensing, retention or commercial conditions.

## Inputs

Consumer needs, risk and policy requirements, product design, measurement methods, applicable contracts and exception authority are needed.

## Practices

Define testable commitments; separate a declared rule from enforcement configuration and observed result; publish conditions before access; record precedence and exceptions.

## Roles and accountability

The product owner is accountable for product commitments. Security, privacy, legal and service owners approve conditions in their remit; consumers accept applicable terms.

## Outputs

Outputs include approved SLA and quality commitments, access and usage conditions, measurement design, policy references and exception process.

## ODPS family mapping

ODPS represents applicable product commitments and access information. ODPV can clarify terms. Runtime systems record observations; the framework evidence layer retains proof that conditions operated.

## Evidence

Retain approval, published version, rule configuration, exception decision and later measurement records.

## Measures

Measure commitments with an observation method, current exceptions, conditions shown before provisioning and repeated misses by product version.

## Example

Customer 360 declares completeness of at least 98%, freshness no more than 60 minutes, availability of 99.9%, approved-consumer access and human approval before production release.

## Questions to ask

- What has the product promised?
- Which promises are measurable and by what method?
- Which conditions apply before access?
- What happens when a commitment is missed?
- Who may approve an exception and for how long?

## Common failure modes

Teams publish aspirations as commitments, make a policy link look like enforcement, or hide exceptions in operational tickets.

## Minimum implementation

Declare one measurable quality or service commitment and one access condition, with a named measurement and exception owner.

## Advanced implementation

Evaluate commitments continuously, reconcile declared and observed state and route exceptions through governed workflow.

## AI-Agent-First extension

Agents can interpret machine-readable conditions only within their permission boundary; they must not treat a discovery result as an entitlement.

## Assessment levels 1-5

Level 1 has informal promises. Level 2 defines reusable commitment patterns. Level 3 publishes testable commitments and records exceptions. Level 4 measures performance and impact. Level 5 uses evidence to drive controls and portfolio decisions.
