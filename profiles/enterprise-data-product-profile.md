---
title: Enterprise Data Product Profile
version: 0.1.0
status: draft
date: 2026-10-06
purpose: Provide the baseline implementation profile for organisations managing enterprise data products through conventional enterprise systems and human-led operating models.
---

# Enterprise Data Product Profile

## 1. Scope

The Enterprise Data Product Profile provides the baseline implementation profile for organisations managing enterprise data products through conventional enterprise systems and human-led operating models.

It applies the [Data Product Operating Framework Core](../framework-core.md) without redefining its functions, capabilities, terminology, assessment model or conformance model.

Typical environments include:

- data catalogs
- data platforms
- APIs
- analytics systems
- governance systems
- human approval processes
- product managers
- domain owners
- engineers
- business consumers

The profile provides a realistic adoption path for organisations that do not yet operate AI agents extensively. Automation and AI may be used, but neither is required for profile adoption.

## 2. Intended users

This profile is intended for:

- data product managers
- domain and data owners
- portfolio and investment decision-makers
- data governance teams
- platform and catalog teams
- data and software engineers
- risk, compliance and assurance teams
- business consumers

## 3. Assumptions

The profile assumes that:

- accountability remains primarily human-led
- approvals may be manual or workflow-supported
- catalogs and platforms may be federated or heterogeneous
- product information may be distributed across several enterprise systems
- machine-readable artifacts can be adopted incrementally
- existing governance and delivery systems remain operational authorities
- the ODPS standards family supplies portable contracts and context where applicable

The profile does not require replacement of existing platforms. It requires clear authority, portable definitions, traceability and evidence across them.

## 4. Core capability requirements

All fourteen Core capabilities apply.

### C1. Strategy and Objectives

Objectives should be explicit, measurable where practical and owned by accountable roles.

### C2. Demand and Use Case Management

Use cases should be registered, owned and linked to relevant objectives and data products.

### C3. Portfolio, Investment and Accountability

Products should have accountable owners, explicit investment decisions and governed lifecycle decisions.

### C4. Product Definition and Contract

Active products should have authoritative ODPS definitions with stable identities, responsible providers, versions, interfaces and lifecycle states.

### C5. Semantics and Vocabulary

Shared vocabulary is recommended for important cross-domain concepts. Material terms should have consistent definitions across product contracts, catalogs and governance records.

### C6. Product Commitments and Usage Conditions

Relevant quality, service-level, access, usage, policy, privacy, security, licensing and commercial conditions should be explicit.

### C7. Relationships, Dependencies and Context

Critical product relationships and dependencies should be represented, including relationships to objectives, use cases, owners, upstream products, downstream consumers and applicable policies.

### C8. Catalog, Publication and Discovery

Products should be discoverable through an approved catalog or equivalent governed discovery service.

### C9. Provisioning, Integration and Consumption

Access and provisioning should follow defined identity, entitlement, approval and revocation controls.

### C10. Lifecycle, Version and Change Management

Versions, lifecycle states, material changes, deprecation and retirement should be managed and communicated to affected consumers.

### C11. Workflow, Automation and Agent Operations

Critical repeatable workflows should be documented, reviewable and increasingly automated where rules are clear. Human approval should remain where judgement, investment authority or risk acceptance is required.

### C12. Observability and Service Assurance

Important service and quality commitments should be measured, compared with declared commitments and retained as evidence.

### C13. Governance, Risk, Compliance and Control Assurance

Applicable policies and controls should be linked to products, operated by accountable roles and supported by evidence.

### C14. Adoption, Outcomes and Value Realisation

Products should be evaluated for discovery, access, adoption, supported use-case outcomes and organisational value rather than usage alone.

## 5. Mandatory evidence

At minimum, an in-scope operational product should have evidence of:

- an approved objective or registered demand
- one or more registered use cases
- an accountable product owner
- an explicit product decision and lifecycle state
- an authoritative, versioned ODPS product contract
- publication in an approved catalog or equivalent
- defined access and usage conditions
- recorded critical relationships and dependencies
- an access, provisioning or entitlement decision
- a governed release or change decision
- measured quality or service performance where commitments apply
- control execution where policies or obligations apply
- adoption or meaningful consumption
- an outcome or value review

Evidence may remain in existing enterprise systems when it is identifiable, retained and traceable to the product.

## 6. Recommended automation

Organisations should progressively automate:

- schema and contract validation
- catalog publication
- broken-reference and dependency checks
- access request routing
- entitlement verification
- release and change notifications
- quality measurement
- service-level evaluation
- control evidence collection
- lifecycle review reminders
- evidence packaging for assessment

Automation should not replace accountable decisions merely to increase throughput.

## 7. ODPS-family expectations

The profile applies the common authority model:

- **ODPS** represents the individual data product contract.
- **ODPC** represents portfolio and discovery objects.
- **ODPV** represents shared vocabulary and semantics.
- **ODPG** represents relationships and context.
- **ODPR** represents reusable workflow contracts.
- **Operational systems** execute work and provide runtime observations.
- **The evidence layer** preserves what proves what happened.

ODPS definitions are expected for active governed products. The other ODPS-family standards should be adopted where shared portfolio objects, vocabulary, relationship graphs or portable workflows create practical value.

The framework and this profile do not redefine ODPS-family standards.

## 8. Minimum implementation baseline

An organisation meets the minimum implementation baseline when it can demonstrate one complete governed traceability chain containing:

1. an owned objective
2. a registered use case
3. an approved product decision
4. an accountable data product owner
5. a valid, versioned ODPS product contract
6. an approved catalog entry or equivalent discovery record
7. a controlled access path
8. a managed lifecycle state
9. one measured quality or service commitment
10. applicable control evidence
11. an adoption measure
12. an outcome or value review

The chain should be established for a small number of products before it is scaled across the portfolio.

## 9. Assessment expectations

Assessment uses the common [Assessment Standard](../assessment-standard.md), the same C1-C14 capability model and the same four dimensions:

- Accountability
- Practice
- Evidence
- Outcome

Profile requirements add context-specific expectations to those capabilities. They do not create a separate maturity model or allow artifact conformance to substitute for operating evidence.

Assessment should verify that human-led decisions are explicit, machine-readable artifacts are increasing, and operational evidence can be traced back to the relevant product, use case and objective.
