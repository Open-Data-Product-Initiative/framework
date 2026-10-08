---
title: C12 Observability and Service Assurance
version: 0.2.0
status: draft
date: 2026-10-08
---

# C12. Observability and Service Assurance

## Capability summary

| Capability ID | Function | Purpose | Primary owner | Primary standard | Key outputs | Key evidence |
|---|---|---|---|---|---|---|
| C12 | ASSURE | Compare declared commitments with observed service. | Service owner | Runtime evidence; ODPS declares commitments | Observation and remediation decision | Timestamped measurement and incident record |

## Purpose

C12 measures service, quality and availability against the declared product commitments and makes the resulting evidence usable for remediation and product decisions.

## Why it matters

A declared target is not proof of operation. Without versioned observations, teams cannot explain which promise failed, who was affected or whether a release caused the issue.

## When it applies

Apply it wherever a product has measurable quality, freshness, availability, latency, reliability or support commitments.

## Inputs

Declared commitment, metric definition, threshold, measurement method, product and contract version, observation period, dependency context and escalation rule are inputs.

## Practices

Collect observations, identify the evaluated version and period, compare results to declared thresholds, detect missing measurements, open remediation, notify affected consumers and retain the method and evidence.

## Roles and accountability

The service owner is accountable for measurement and response. Product owners decide product implications; operations performs remediation; consumers receive material notices; governance reviews persistent failure.

## Outputs

Produce observations, status, incident or exception, consumer-impact assessment, remediation action and trend review.

## ODPS family mapping

ODPS declares product commitments where supported. Observations belong in runtime and evidence systems; ODPG can identify dependencies and affected consumers; ODPR can coordinate remediation.

## Evidence

Keep raw or retained measurements, method and rule versions, evaluated product version, alert, incident, remediation and closure decision.

## Measures

Measure commitment attainment, missing observations, time to detect and resolve, repeated breach rate and affected-consumer duration.

## Example

Customer 360 is observed at 94.7% completeness, 43-minute freshness and 99.93% availability. Freshness and availability pass; completeness fails the 98% commitment. Retention analysts may be affected and the quality workflow must open a remediation record.

## Questions to ask

- What has the product promised and which version applies?
- Which promises are measurable and how are they measured?
- Which commitments are currently missed?
- Which consumers are affected?
- What remediation and exception decision was triggered?

## Common failure modes

Teams report a green dashboard without the method, silently treat missing data as pass, or compare observations to an obsolete contract version.

## Minimum implementation

Measure one declared commitment, retain its result and route a failed result to an accountable owner.

## Advanced implementation

Continuously reconcile declared and observed state, expose consumer impact and use trends in lifecycle and investment reviews.

## AI-Agent-First extension

Agents may read recent, versioned assurance evidence but must not use stale or failed products for a governed action without an approved exception.

## Assessment levels 1-5

Level 1 has ad hoc monitoring. Level 2 defines commitments and measures. Level 3 retains observations and response evidence. Level 4 measures trends and consumer impact. Level 5 feeds assurance evidence into automated gates and accountable decisions.
