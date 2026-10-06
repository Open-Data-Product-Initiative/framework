---
title: ASSURE Capability Reference
version: 0.1.0
status: draft
date: 2026-10-06
capabilities: [C12, C13, C14]
---

# ASSURE

## Purpose

ASSURE determines whether data products operate as defined, satisfy applicable governance requirements, are adopted by intended consumers and create enough value to justify continued investment.

## Assurance principle

Do not confuse definition with evidence.

A declared quality target is not evidence of quality.

A published SLA is not evidence of service performance.

A policy reference is not evidence that a control worked.

A use case is not evidence of adoption.

A business objective is not evidence of value.

## C12. Observability and Service Assurance

### Purpose

Determine whether the operating data product satisfies the measurable quality, service and operational commitments made in its definition.

### Practices

1. Identify measurable commitments.
2. Define measurement methods.
3. Collect observations.
4. Evaluate data quality.
5. Evaluate service performance.
6. Detect deviations.
7. Assess consumer impact.
8. Trigger response.
9. Retain evidence.
10. Review measurement quality.
11. Feed findings into product management.

### Primary standard

ODPS for declared quality and service objectives.

### Evidence

- measurement result
- monitoring timestamp
- product ID
- product version
- declared objective
- observed result
- measurement method
- evaluation status
- incident reference
- remediation record
- exception where applicable

## C13. Governance, Risk, Compliance and Control Assurance

### Purpose

Determine whether applicable governance obligations have been translated into controls and whether those controls operate effectively.

### Core chain

`Requirement → Policy → Control → Product → Execution → Evidence → Finding → Response`

### Practices

1. Identify applicable obligations.
2. Map obligations to policies.
3. Map policies to controls.
4. Map controls to products.
5. Assign control ownership.
6. Execute controls.
7. Produce control evidence.
8. Assess risk.
9. Manage exceptions.
10. Test control effectiveness.
11. Manage findings.
12. Support independent assurance.
13. Retain traceability.

### Evidence

- applicable obligation
- policy version
- control definition
- control owner
- execution timestamp
- product version
- control outcome
- supporting artifact
- risk decision
- exception approval
- finding
- remediation result
- independent review where required

## C14. Adoption, Outcomes and Value Realisation

### Purpose

Determine whether consumers use the data product and whether that consumption contributes to the outcome that originally justified investment.

### Value chain

`Product exists → Product is discoverable → Consumer receives access → Consumer uses product → Use case changes → Outcome changes → Value is realised`

### Practices

1. Define expected value before investment.
2. Establish a baseline.
3. Measure discovery and access.
4. Measure adoption.
5. Measure sustained consumption.
6. Measure reuse.
7. Connect usage to use cases.
8. Measure use-case outcomes.
9. Measure business value.
10. Measure product cost.
11. Assess value contribution.
12. Review portfolio investment.
13. Retire unsupported products.

### Measurement levels

#### Reach

Can intended consumers find and access the product?

#### Adoption

Have intended consumers started meaningful use?

#### Engagement and Reuse

Does meaningful consumption continue?

#### Use-Case Outcome

Did the supported process or decision improve?

#### Organisational Value

What is that improvement worth?

#### Portfolio Return

Was investing in this product preferable to alternative uses of resources?

### Value classes

- financial value
- operational value
- decision value
- risk value
- compliance value
- public value

### Attribution classes

- direct attribution
- contribution
- enablement
- mandatory value

### Evidence

- active consumer record
- consumption events
- use-case relationship
- baseline measure
- current outcome measure
- KPI result
- cost record
- benefit calculation
- assumptions
- attribution method
- portfolio review decision

## Four assurance views

### Service Health

Does the product perform as promised?

### Control Health

Does it operate within required governance boundaries?

### Adoption Health

Are intended consumers using it?

### Value Health

Are intended outcomes being achieved?

These should not be collapsed into one opaque score.
