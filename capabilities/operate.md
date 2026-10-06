---
title: OPERATE Capability Reference
version: 0.1.0
status: draft
date: 2026-10-06
capabilities: [C8, C9, C10, C11]
---

# OPERATE

## Purpose

OPERATE turns defined data products into available, consumable and managed services.

## Operating principle

Declaration and execution are separate responsibilities.

`DECLARE → EXECUTE → EVIDENCE`

The ODPS standards family declares portable contracts.

Operational platforms execute them.

Runtime systems produce evidence.

## C8. Catalog, Publication and Discovery

### Purpose

Make governed data products and surrounding business context discoverable by people, applications and AI agents.

### Practices

1. Register the product.
2. Maintain authoritative references.
3. Publish portfolio context.
4. Apply visibility controls.
5. Support business-context search.
6. Support machine discovery.
7. Federate where required.
8. Validate catalog integrity.
9. Manage catalog lifecycle.

### Primary standard

ODPC.

### Evidence

- valid ODPC catalog
- resolvable ProductReference
- publication record
- catalog validation result
- search index record
- visibility configuration
- broken-reference report

## C9. Provisioning, Integration and Consumption

### Purpose

Turn a defined product interface into controlled consumer access.

### Practices

1. Resolve the access contract.
2. Identify the consumer.
3. Evaluate entitlement.
4. Provision access.
5. Provide implementation context.
6. Validate connectivity.
7. Associate consumption with the product.
8. Manage consumer changes.
9. Revoke access.
10. Support agent consumption.

### Primary standard

ODPS.

### Supporting standard

ODPR for implementation handoff and onboarding workflows.

### Evidence

- access request
- approval where required
- provisioning record
- entitlement record
- connectivity test
- product version consumed
- subscription record
- revocation record
- consumption event

## C10. Lifecycle, Version and Change Management

### Purpose

Control the evolution of a data product from initial development through production, change, deprecation and retirement.

### Practices

1. Maintain lifecycle state.
2. Version the product.
3. Classify changes.
4. Analyse impact.
5. Validate the change.
6. Apply change gates.
7. Release the change.
8. Communicate change.
9. Deprecate safely.
10. Retire products.

### Lifecycle baseline

- announcement
- draft
- development
- testing
- acceptance
- production
- sunset
- retired

### Evidence

- previous product version
- new product version
- version difference
- change classification
- impact analysis
- validation results
- gate results
- approval
- publication result
- consumer notification
- rollback or remediation record where required

## C11. Workflow, Automation and Agent Operations

### Purpose

Make repeatable data product work explicit, portable, bounded and reviewable.

### Practices

1. Identify repeatable work.
2. Declare workflow intent.
3. Declare inputs.
4. Declare ordered activities.
5. Declare outputs.
6. Define gates.
7. Define human review.
8. Bound agent work.
9. Separate contract from runtime.
10. Record execution evidence.
11. Manage workflow versions.
12. Reuse proven workflows.

### Primary standard

ODPR.

### Operational patterns

- delivery flows
- product handoff flows
- agent discovery flows
- trigger-based flows

### Evidence

- ODPR recipe
- recipe version
- input manifest
- execution record
- validation result
- gate result
- human review decision
- output manifest
- exception record
- run outcome

## Declared state versus observed state

OPERATE introduces a formal comparison between:

- what the product contract or workflow says should happen
- what operational systems show happened

This difference becomes evidence for ASSURE.
