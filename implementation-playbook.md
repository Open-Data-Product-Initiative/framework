---
title: Data Product Operating Framework Implementation Playbook
version: 0.2.0
status: draft
date: 2026-10-06
---

# Implementation Playbook

Start with [one complete data product chain](getting-started.md) before scaling the framework. The playbook explains how to establish the capabilities; the [capability reference](capabilities/reference/) defines the detail for each C1-C14 capability.

## 1. Purpose

The playbook provides practical guidance for implementing the framework.

The Core defines what good data product operations require.

The playbook explains how to establish them.

Implementation should begin with a bounded portfolio or value stream, not an enterprise-wide metadata exercise. Select a scope in which accountable decision-makers, product providers and consumers can establish one complete traceability chain and use its evidence to make a real continuation or change decision.

Before starting, record the implementation sponsor, scope, intended profile, product population, current systems, material obligations, success measures and decision date. This baseline prevents tooling activity from being mistaken for operating-model adoption.

## 2. Recommended implementation sequence

### Step 1. Establish DIRECT

Start with:

- organisational objectives
- use cases and demand
- product portfolio
- accountable ownership
- investment decisions

Do not begin by creating hundreds of ODPS files for products that have no clear business demand.

Choose one objective with an accountable owner and one or more active use cases. Confirm how a use-case outcome will be observed and who can approve, defer or reject a product candidate. Establish a lightweight portfolio decision record before designing the product contract.

### Step 2. Establish DEFINE

For approved product candidates:

- create authoritative ODPS product contracts
- align vocabulary through ODPV
- define commitments and conditions
- connect products to portfolio context through ODPG

Begin with the smallest contract that lets an intended consumer understand and evaluate the product. Resolve material semantic ambiguity and usage conditions first. Record unresolved decisions explicitly instead of hiding them in prose or implementation defaults.

### Step 3. Establish OPERATE

Connect definitions to:

- catalogs
- access provisioning
- delivery platforms
- lifecycle management
- change processes
- reusable workflows

Use the contract identifiers and versions in catalog, provisioning, release and workflow records. The objective is not immediate platform replacement; it is traceability across existing systems. Where integration is manual, define the accountable handoff and evidence before automating it.

### Step 4. Establish ASSURE

Collect evidence for:

- service performance
- quality
- control execution
- adoption
- use-case outcomes
- value

Select a small set of observations tied directly to declared commitments and the original use-case outcome. Confirm that missing data and failed measurements are visible. Produce an assurance view that can support a product or portfolio decision, rather than a dashboard that only reports activity.

### Step 5. Close the loop

Use ASSURE evidence to change:

- product commitments
- operational practices
- portfolio investment
- product lifecycle decisions
- strategic priorities

Hold the first review while the implementation scope is still small. Use evidence to make at least one explicit decision: continue, change, expand, merge, constrain or retire. If the review cannot change a decision, revisit the accountability and measures before scaling.

## 3. Minimum viable implementation

An initial implementation should establish at least:

- one governed business objective
- one registered use case
- one approved product decision
- one valid ODPS product contract
- one catalog reference
- one relationship graph connecting objective, use case and product
- one operational workflow
- one service or quality observation
- one adoption measure
- one outcome measure
- one portfolio review decision

This creates one complete traceability chain before scaling.

The minimum viable implementation is complete only when the chain has been exercised. Creating the artifacts without provisioning, observation and review demonstrates definition work, not an operating framework.

## 4. Adoption waves

### Wave 1. Prove the chain

Implement one objective-to-value chain for a bounded product set. Accept manual integration where responsibilities and evidence are explicit.

### Wave 2. Establish repeatability

Standardise identifiers, templates, decision records, validation and evidence packaging. Train owners and consumers, then repeat the process across several products or domains.

### Wave 3. Connect systems

Integrate portfolio, contract, catalog, provisioning, lifecycle and observability systems. Remove duplicate entry where an authoritative artifact can drive another view.

### Wave 4. Automate assurance

Automate stable validations, comparisons and evidence collection. Preserve human authority for material investment, risk and exception decisions.

### Wave 5. Adapt by evidence

Use recurring capability assessment and product evidence to improve practices, strengthen selected profile requirements and change portfolio investment.

## 5. Source-of-truth guidance

Use machine-readable standards as portable sources of truth where appropriate.

Do not let a UI become the only source of truth.

Generated HTML, PDF and catalog views should derive from underlying artifacts.

For each material field, decide which artifact or system has authority and how other systems receive updates. Avoid “bidirectional synchronization” as a default answer; without field-level authority and conflict rules, it creates multiple competing truths.

Migration can use temporary reconciliation reports. Record the old source, new source, transformation rule, unresolved differences and cutover decision. Preserve identifiers so historical evidence remains connected after systems change.

## 6. Automation guidance

Automate where the rule is clear.

Examples:

- schema validation
- contract validation
- graph integrity checks
- catalog publication
- SLA evaluation
- quality checks
- dependency impact checks
- evidence packaging

Keep human approval where judgement, risk acceptance or investment authority requires it.

Automate only after the manual or semi-automated practice has a clear input, rule, output, exception path and owner. Automation should expose failures and uncertainty rather than converting them to default success. Record rule versions and input versions so results can be reproduced.

## 7. Select an implementation profile

Use the [Enterprise Data Product Profile](profiles/enterprise-data-product-profile.md) as the baseline for conventional enterprise systems and human-led operating models.

Use the [AI-Agent-First Data Product Profile](profiles/ai-agent-first-data-product-profile.md) when AI agents directly discover, interpret, access, combine or act on data products.

The AI-Agent-First Profile extends the Core with stronger machine-readable context, workflow, control, provenance and assurance requirements. It does not create a separate framework.

An organisation can establish the Enterprise profile first and strengthen selected capabilities as it progresses toward agent-ready and agent-first operations.

## 8. Publication guidance

Markdown should remain the human-maintained source.

Generated HTML and PDF should:

- preserve headings and anchors
- include document metadata
- include framework version
- include publication date
- link back to source files
- avoid changing semantics during rendering

Publication should also expose the framework or artifact version and stable anchors so references remain meaningful. Accessibility, responsive navigation and print quality are presentation requirements; they do not change the authority of the underlying source.

## 9. Evidence-informed implementation

The [Framework Evidence Library](https://github.com/Open-Data-Product-Initiative/framework/tree/main/library) contains supporting sources and their applicability boundaries. Use it to research an implementation decision, not to copy external requirements into the Core. Relevant starting points include **`w3c-dcat-3`**, [W3C DCAT 3](https://www.w3.org/TR/vocab-dcat-3/), for catalog interoperability; **`wilkinson-fair-principles-2016`**, the [FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18), for machine-actionable metadata; **`w3c-prov-o`**, [W3C PROV-O](https://www.w3.org/TR/prov-o/), for provenance; and the cataloged NIST risk frameworks for proportionate governance and assurance.

For a material framework change, retain the research question, source identifiers, claims, limitations and architecture impact. LLM-assisted synthesis may propose text, but maintainers must verify source support and deliberately edit the normative Markdown.

## 10. Future playbook modules

Planned modules:

- starting from business demand
- converting use cases into product candidates
- defining ODPS contracts
- building demand-to-data graphs
- catalog federation
- agent-ready discovery
- product lifecycle workflows
- machine-readable governance
- service assurance
- value measurement
- portfolio review
