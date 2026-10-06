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

### Operating intent

Observability connects a measurement to the exact product, version, commitment and evaluation period to which it applies. A dashboard value without this context may be useful operational telemetry, but it is weak assurance evidence. The measurement method, sampling window, exclusions and status logic should be explicit enough for another reviewer to reproduce or challenge the result.

Service assurance should combine technical observations with consumer impact. A short availability failure may be immaterial for one use case and decisive for another; a quality average may hide a critical segment. Evaluation should therefore preserve the declared threshold while allowing impact, severity and approved exceptions to be assessed separately.

The measurement system also requires assurance. Missing telemetry, changed metric definitions, delayed observations and unmonitored interfaces should be visible rather than interpreted as successful performance.

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

### Assurance questions

- Is every result tied to the product, contract version, metric and evaluation period in force?
- Can a reviewer reproduce the status from the recorded observations and method?
- Are missing, delayed or invalid measurements distinguished from passing results?
- Does incident and impact evidence reach the owner who can change the product or commitment?

## C13. Governance, Risk, Compliance and Control Assurance

### Purpose

Determine whether applicable governance obligations have been translated into controls and whether those controls operate effectively.

### Operating intent

Control assurance begins with applicability. The organisation should be able to explain why an obligation, policy and control applies to a product and which authority accepted that interpretation. Copying a standard control catalog into every product obscures accountability and makes evidence review unmanageable.

A control definition should identify its objective, owner, trigger or frequency, scope, method, expected result, evidence and response to failure. Control execution then produces an observation about a particular product and version. Design approval, execution evidence and effectiveness assessment are different stages and should not be collapsed into one “compliant” status.

Exceptions are governed decisions with scope, rationale, compensating measures, accountable acceptance and expiry. Findings should connect to remediation and retest evidence. Independent assurance may sample evidence or repeat tests, but independence and sampling limits must be disclosed.

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

### Assurance questions

- Can each material control be traced to an applicable requirement and accountable interpretation?
- Does the evidence show that the control executed, not merely that it was designed or configured?
- Are exceptions time-bound, scoped, accepted and reviewed before expiry?
- Can findings be followed through remediation, retest and closure?

## C14. Adoption, Outcomes and Value Realisation

### Purpose

Determine whether consumers use the data product and whether that consumption contributes to the outcome that originally justified investment.

### Operating intent

Adoption is meaningful use by an intended consumer, not an account count or isolated access event. The organisation should define what meaningful use means for each use case and separate initial trial, recurring consumption, production dependency and reuse by an additional use case.

Outcome measurement compares the present state with a baseline, target or credible counterfactual. It should record the period, population, calculation, assumptions and other changes that may explain the result. Attribution must be proportionate to the decision: a small operational improvement may use contribution evidence, while a major investment claim may need stronger causal analysis.

Value combines the outcome with its significance, cost and attribution. Financial value may be appropriate, but risk reduction, compliance, public value, decision quality and service improvement should not be forced into artificial revenue estimates. A mandatory product can have value even when stopping it is not a realistic option; the portfolio decision may instead concern cost, quality or risk.

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

### Assurance questions

- Is meaningful adoption defined for the relevant consumer and use case?
- Can usage be connected to a change in a decision, process, obligation or service outcome?
- Are baseline, target, period, assumptions, cost and attribution method visible?
- Would the investment decision change if the reported value were lower or more uncertain?

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

A combined executive view may summarize the four perspectives, but it should preserve drill-down to the underlying measures, evidence, exceptions and decision owners. A healthy service can still be unused, a compliant product can still lack value, and a valuable product can still require urgent control remediation.

## Evidence basis and external references

The framework requirements above remain Open Data Product Initiative decisions. These sources support the assurance model:

- **`w3c-dqv`** — [W3C Data Quality Vocabulary](https://www.w3.org/TR/vocab-dqv/) separates quality dimensions, metrics, measurements, annotations and policy context. It informs machine-readable quality evidence without making RDF mandatory.
- **`w3c-prov-o`** — [W3C PROV-O](https://www.w3.org/TR/prov-o/) supports attribution of evidence to entities, activities and agents. Provenance improves reviewability but does not by itself prove that a claim is true.
- **`w3c-shacl`** — [W3C SHACL](https://www.w3.org/TR/shacl/) distinguishes constraints from validation reports and individual validation results. This supports the framework's declared-versus-observed separation.
- **`nist-csf-2.0`**, **`nist-privacy-framework-1.0`** and **`nist-sp-800-53r5`** — [NIST Cybersecurity Framework 2.0](https://doi.org/10.6028/NIST.CSWP.29), [NIST Privacy Framework 1.0](https://www.nist.gov/privacy-framework/privacy-framework) and [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) provide risk, control and assessment patterns. They inform applicable control design and evidence; they do not establish universal legal obligations for every product.
- **`oecd-ai-principles-2024`** — [OECD AI Principles](https://oecd.ai/en/ai-principles) emphasise beneficial outcomes, accountability, robustness and lifecycle risk management for AI. They are relevant when AI participates in the product environment, while C14 continues to measure organisational outcomes rather than AI activity counts.
