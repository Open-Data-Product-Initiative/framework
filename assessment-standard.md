---
title: Data Product Operating Framework Assessment Standard
version: 0.2.0
status: draft
date: 2026-10-06
---

# Assessment Standard

## 1. Purpose

The assessment standard defines how organisational capabilities are evaluated.

Assessment is capability-based.

A valid machine-readable artifact does not by itself prove organisational maturity.

## 2. Assessment dimensions

Each capability is evaluated across four dimensions.

### Accountability

Are ownership and decision rights explicit?

### Practice

Is there a defined and repeatable way of performing the capability?

### Evidence

Can the organisation demonstrate that the capability operates?

### Outcome

Does evidence show that the capability achieves its purpose?

The four dimensions should be scored separately before assigning the overall capability level. Strong documentation cannot compensate for missing accountability, and extensive activity cannot compensate for missing outcome evidence. An assessor should record the limiting dimension and the improvement needed to progress.

## 3. Capability levels

### Level 0: Absent

The capability is not established.

### Level 1: Emerging

Activity occurs inconsistently and depends heavily on individuals.

### Level 2: Defined

Roles, practices and expected outputs exist.

### Level 3: Operational

Practices operate consistently and produce evidence.

### Level 4: Measured

Performance, exceptions and outcomes are measured.

### Level 5: Adaptive

Evidence systematically drives improvement, decisions and suitable automation.

## 4. Assessment evidence classes

Evidence can include:

- directive evidence
- definition evidence
- execution evidence
- operational evidence
- outcome evidence

### Evidence sufficiency

Evidence should be relevant to the capability claim, attributable to a known source, tied to the applicable period and version, and retained in a form that can be reviewed. The assessor should distinguish:

- declared evidence — definitions, policies, plans, contracts and expected practices
- execution evidence — records that the defined practice was performed
- observed evidence — measurements and events showing what occurred
- decision evidence — findings, approvals, exceptions and investment responses based on the observations

A template, policy or configured control is not execution evidence. One successful execution may demonstrate existence but not consistent operation. A dashboard may show observations while providing insufficient provenance or method to support assurance.

Sampling should reflect the frequency, variability and consequence of the capability. Assessors should record the population, period, sample method, exclusions and known limitations. Evidence supplied only for the assessment should be treated cautiously if it is not produced by normal operations.

## 5. Assessment method

For each capability:

1. Identify accountable roles.
2. Review documented practices.
3. Inspect required artifacts.
4. Inspect evidence that practices operated.
5. Evaluate whether intended outcomes are measured.
6. Score each assessment dimension.
7. Determine the capability level.
8. Record findings and improvement actions.

The assessment scope should identify the organisation, portfolio, product population, profile, period and exclusions. Interviews can establish intent and explain evidence, but statements should not substitute for operating records where those records should exist.

Assessors should test forward and backward traceability. A forward test starts from an objective or use case and follows the chain to a product, execution, evidence and outcome. A backward test starts from a value or conformance claim and verifies the evidence, consumption, product version and original decision that support it.

Where evidence conflicts, record the conflict rather than selecting the more favourable source. Where a capability differs materially between domains or product classes, report the distribution and rationale instead of relying only on an average.

## 6. Capability assessment result

Organisations should receive capability-level assessment results rather than one opaque maturity score.

Each result should include:

- capability level and scores for Accountability, Practice, Evidence and Outcome
- assessment scope and applicable profile
- evidence reviewed and sampling method
- strengths and observed outcomes
- gaps, exceptions and conflicting evidence
- improvement actions, owners and target dates
- assessor and assessment date
- confidence and material limitations

Example:

| Capability | Level |
|---|---:|
| C1 Strategy and Objectives | 4 |
| C2 Demand and Use Case Management | 3 |
| C3 Portfolio, Investment and Accountability | 2 |
| C4 Product Definition and Contract | 5 |
| C5 Semantics and Vocabulary | 2 |
| C6 Product Commitments and Usage Conditions | 4 |
| C7 Relationships, Dependencies and Context | 3 |
| C8 Catalog, Publication and Discovery | 4 |
| C9 Provisioning, Integration and Consumption | 3 |
| C10 Lifecycle, Version and Change Management | 2 |
| C11 Workflow, Automation and Agent Operations | 4 |
| C12 Observability and Service Assurance | 4 |
| C13 Governance, Risk, Compliance and Control Assurance | 3 |
| C14 Adoption, Outcomes and Value Realisation | 1 |

## 7. Conformance types

Profiles use the same capability levels and assessment dimensions as the Core.

Profile requirements add context-specific expectations for practices, artifacts, evidence and controls within the applicable Core capability. A profile must not rename capabilities, create a separate maturity model or treat automation as evidence of maturity.

### Artifact conformance

A machine-readable artifact complies with the applicable specification.

### Practice conformance

An organisation follows required operating practices.

### Capability conformance

Evidence demonstrates that the capability operates and achieves required outcomes.

Conformance and maturity answer different questions. An artifact can conform while the surrounding capability is weak. A mature capability can manage several artifact formats while one particular artifact fails validation. Reports should state the object and scope of each conclusion rather than using an unqualified “compliant” label.

## 8. Assessment integrity

Assessors should be sufficiently independent from the activity being assessed for the consequence of the conclusion. Self-assessment is useful for improvement, but it should be labelled as such. Claims used for certification, regulatory response or material investment decisions may require independent evidence review.

Automation may validate artifacts, collect observations and detect missing links. It must not silently decide ambiguous applicability, risk acceptance or outcome attribution. Automated results should preserve rule version, input version, execution time and exceptions so a person can examine how the conclusion was reached.

Calibration is required when multiple assessors or organisational units are involved. A common evidence pack and example scoring decisions should be used to test whether assessors interpret levels consistently.

## 9. Evidence basis and future work

Library sources **`nist-csf-2.0`**, **`nist-sp-800-53r5`** and **`w3c-shacl`** support this section. [NIST Cybersecurity Framework 2.0](https://doi.org/10.6028/NIST.CSWP.29) supports outcome-oriented assessment while allowing implementation to vary by context. [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) provides established control-assessment concepts, and [W3C SHACL](https://www.w3.org/TR/shacl/) demonstrates the separation between declared constraints and validation results. These sources inform the assessment logic but do not define conformance to this framework.

A later version should define:

- required assessment questions per capability
- minimum evidence per level
- scoring rules
- assessor guidance
- sampling rules
- reassessment rules
- organisational certification requirements
