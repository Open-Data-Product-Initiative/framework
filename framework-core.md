---
title: Data Product Operating Framework Core
version: 0.1.0
status: draft
date: 2026-10-06
---

# Data Product Operating Framework Core

## 1. Purpose

The Data Product Operating Framework defines how organisations direct, define, operate and assure data products from business demand to measurable value.

It provides a common operating structure connecting:

- business objectives
- use cases and demand
- investment decisions
- data products
- machine-readable product contracts
- semantics
- governance requirements
- delivery and consumption
- lifecycle management
- operational evidence
- business outcomes
- value

The framework is vendor-neutral.

The ODPS standards family provides the machine-readable standards foundation for significant parts of the framework.

## 2. The four questions

### DIRECT

Why should we do this, and who decides?

### DEFINE

What exactly are we committing to provide?

### OPERATE

How do we make it available, use it and change it?

### ASSURE

Does it work, comply and create value?

## 3. Core rule

Intent and directives flow toward execution.

Evidence and value flow toward decision-making.

Forward traceability:

`Objective → Use Case → Investment Decision → Data Product → Product Contract → Delivery → Consumption → Outcome`

Backward traceability:

`Outcome → Evidence → Data Product → Use Case → Investment Decision → Objective`

## 4. Core principles

### P1. Start from demand

The existence of data is not sufficient justification for creating a data product.

Data product investment should originate from an identifiable objective, problem, use case, obligation or consumer need.

### P2. Separate the use case from the product

A use case explains why data is needed.

A data product defines a reusable capability provided to consumers.

One use case can require many products.

One product can support many use cases.

### P3. Define products as contracts

A managed data product should have an authoritative machine-readable definition describing what is provided, by whom, under which conditions and with which commitments.

### P4. Preserve business context

Business context should survive the transition from strategy into technical implementation.

A consumer, engineer or AI agent should be able to understand why a product exists without reconstructing its history manually.

### P5. Separate declaration from execution

Specifications describe what should exist or happen.

Platforms and runtime systems execute work.

Runtime evidence records what happened.

A runtime implementation should not silently redefine the declared product contract.

### P6. Treat evidence as a first-class object

Governance, quality, service, adoption and value claims should be supported by evidence.

Where appropriate, that evidence should be machine-readable.

### P7. Measure value beyond usage

Discovery, access and usage are important signals.

They do not by themselves prove value.

Value requires evidence that product consumption contributed to an intended outcome.

### P8. Govern the lifecycle

Products should be deliberately created, changed, versioned, reviewed, deprecated and retired.

A product should not become permanent simply because it once received funding.

### P9. Design for interoperability

The framework should work across catalogs, data platforms, cloud environments, governance tools and organisational structures.

No specific platform should become a prerequisite for conformance.

### P10. Design for people and machines

Product contracts, context, relationships, workflows and evidence should be usable by humans, software and AI agents where appropriate.

## 5. Framework structure

The framework contains:

- 4 functions
- 14 capabilities
- practices within each capability
- artifacts produced by those practices
- evidence demonstrating execution and outcomes
- measures evaluating performance
- profiles adapting the framework to specific contexts

## 6. Function 1: DIRECT

Purpose: connect organisational intent to explicit data product investment and accountability.

### C1. Strategy and Objectives

Connect data product activity to explicit organisational objectives, mandates and measurable outcomes.

### C2. Demand and Use Case Management

Capture, qualify and prioritise the problems, decisions and consumer needs creating demand for data.

### C3. Portfolio, Investment and Accountability

Decide which products deserve investment, assign accountability, manage funding and govern portfolio lifecycle decisions.

DIRECT produces:

- objectives
- use cases
- priorities
- investment decisions
- accountability
- product candidates
- success measures

## 7. Function 2: DEFINE

Purpose: turn an approved product candidate into an explicit and governed data product definition.

### C4. Product Definition and Contract

Establish the authoritative machine-readable definition of the data product.

### C5. Semantics and Vocabulary

Establish shared and machine-readable meaning for important concepts and terminology.

### C6. Product Commitments and Usage Conditions

Define measurable quality, service, access, legal, privacy, security and commercial conditions where applicable.

### C7. Relationships, Dependencies and Context

Connect products to objectives, use cases, KPIs, policies, systems, products and other relevant context.

DEFINE produces:

- product contracts
- product identities
- semantics
- quality commitments
- service commitments
- access conditions
- governance context
- relationships
- dependencies

## 8. Function 3: OPERATE

Purpose: make defined products discoverable, accessible, consumable and manageable throughout their operational lifecycle.

### C8. Catalog, Publication and Discovery

Publish and organise governed products and business context so people, applications and AI agents can find suitable products.

### C9. Provisioning, Integration and Consumption

Manage the controlled path from product discovery to usable consumer access and ongoing consumption.

### C10. Lifecycle, Version and Change Management

Control how products move through lifecycle states and how versions and changes affect consumers.

### C11. Workflow, Automation and Agent Operations

Define repeatable and reviewable operating procedures for people, software systems and AI agents.

OPERATE produces:

- catalog entries
- access
- subscriptions
- integrations
- versions
- changes
- releases
- workflow executions
- approvals
- operational records

## 9. Function 4: ASSURE

Purpose: determine whether products operate as promised, remain within required boundaries and produce sufficient value.

### C12. Observability and Service Assurance

Compare actual product quality and service performance with declared commitments.

### C13. Governance, Risk, Compliance and Control Assurance

Determine whether applicable policies and controls operate effectively and produce sufficient evidence.

### C14. Adoption, Outcomes and Value Realisation

Determine whether intended consumers use products and whether that consumption contributes to expected outcomes and value.

ASSURE produces:

- quality evidence
- service evidence
- control evidence
- risk findings
- adoption evidence
- outcome evidence
- value evidence
- investment recommendations

## 10. Cross-cutting enablers

### E1. Platform and Automation

Catalogs, data platforms, workflow systems, observability systems, policy engines, identity systems, developer platforms and AI infrastructure.

### E2. Engineering and Interoperability

APIs, schemas, validation, data contracts, CI/CD, metadata exchange, MCP and integration patterns.

### E3. Competency and Culture

Product management, domain expertise, data literacy, governance competence, engineering capability, leadership, ownership behaviour and consumer orientation.

## 11. Authority model

### ODPS

Authoritative representation of an individual data product contract.

It answers:

- What is this product?
- What does the provider offer?
- What commitments and conditions apply?

### ODPC

Authoritative portable representation of portfolio and discovery objects.

It answers:

- What products, use cases, objectives, signals and related portfolio objects are being managed?

### ODPV

Authoritative shared vocabulary for the standards family.

It answers:

- What do these concepts mean?

### ODPG

Authoritative portable representation of relationships.

It answers:

- How are these objects connected?

### ODPR

Authoritative portable representation of repeatable workflow contracts.

It answers:

- How should this type of work happen?

### Operational systems

Authoritative sources for relevant runtime observations.

They answer:

- What happened?

### Evidence layer

Provides durable assurance information.

It answers:

- What proves it?

## 12. Local context and shared context

Relevant context can appear inside an individual product contract even when a canonical portfolio object exists elsewhere.

The distinction is:

- local context makes the product independently understandable
- shared context creates reusable organisational objects
- relationships preserve alignment between them

For example:

- ODPS can state which objective an individual product supports
- ODPC can represent that Business Objective as a reusable portfolio object
- ODPG connects the product and objective explicitly

This is intentional contextual redundancy, provided identifiers and relationships preserve consistency.

## 13. Declared state and observed state

### Declared state

What the product contract, policy or workflow states should happen.

### Observed state

What runtime evidence shows happened.

Example:

Declared quality:

`Completeness ≥ 98%`

Observed quality:

`Completeness = 94.7%`

Assurance result:

`Commitment not met`

The difference between declared and observed state is a first-class governance signal.

## 14. Evidence model

### Directive evidence

Objectives, priorities, policies, funding decisions, portfolio decisions and approvals.

### Definition evidence

Product contracts, vocabulary, commitments, relationships and control definitions.

### Execution evidence

Workflow executions, validations, approvals, deployments, provisioning, versions and changes.

### Operational evidence

Quality observations, service observations, consumption, incidents, control executions and exceptions.

### Outcome evidence

Adoption, use-case performance, KPI changes, cost, benefit, risk reduction, public value and other demonstrated outcomes.

## 15. Value model

The framework distinguishes six value classes:

1. Financial value
2. Operational value
3. Decision value
4. Risk value
5. Compliance value
6. Public value

The framework distinguishes four attribution levels:

1. Direct attribution
2. Contribution
3. Enablement
4. Mandatory value

## 16. Four assurance views

### Service Health

Does the product perform as promised?

### Control Health

Does it operate within required governance boundaries?

### Adoption Health

Are intended consumers using it?

### Value Health

Are intended outcomes being achieved?

These views should not be collapsed into one opaque score.

## 17. Capability assessment

Each capability is evaluated independently.

- Level 0: Absent
- Level 1: Emerging
- Level 2: Defined
- Level 3: Operational
- Level 4: Measured
- Level 5: Adaptive

Assessment considers four dimensions:

- Accountability
- Practice
- Evidence
- Outcome

## 18. Framework profiles

The Core remains context-neutral.

Initial candidate profiles:

- Enterprise Data Product Profile
- AI-Agent-Ready Data Product Profile
- Public Sector Data Product Profile
- Open Data Product Profile
- Commercial Data Product Profile
- Regulated Data Product Profile

Profiles add requirements. They do not redefine the Core.

## 19. Framework conformance

The framework distinguishes three forms of conformance:

### Artifact conformance

A machine-readable artifact complies with the applicable specification.

### Practice conformance

An organisation follows the required operating practices.

### Capability conformance

Evidence demonstrates that the capability operates and achieves the required outcomes.

Having a valid ODPS file does not mean the organisation has mature data product management.

It means one important artifact conforms to the standard.

## 20. Core traceability test

For any operational data product, the organisation should be able to answer:

- What is it?
- Who is accountable for it?
- Why does it exist?
- Which use cases depend on it?
- Which objectives do those use cases support?
- Who approved its investment?
- Which version is running?
- What does it promise?
- How is it accessed?
- Who consumes it?
- What depends on it?
- Which policies apply?
- Which controls protect it?
- Which workflows operate it?
- Did those controls execute?
- Is it meeting its quality commitments?
- Is it meeting its service commitments?
- What changed recently?
- What incidents affected it?
- Is adoption increasing or declining?
- What outcome was expected?
- What outcome occurred?
- What did the product cost?
- What value did it contribute?
- When was continued investment last reviewed?

## 21. Machine-readable framework objective

The long-term objective is that a significant portion of the core traceability test can be answered from machine-readable artifacts and evidence.

The framework therefore aims toward:

- machine-readable objectives and use cases
- machine-readable data product contracts
- machine-readable semantics
- machine-readable relationships
- machine-readable policies where suitable
- machine-readable workflows
- machine-readable runtime evidence
- machine-readable assurance results
- traceable value

## 22. Positioning statement

The Data Product Operating Framework is an open operating model for managing data products from business demand to measurable value.

It connects strategy, use cases, investment, product contracts, semantics, governance, delivery, lifecycle management and assurance through shared machine-readable context and evidence.

The ODPS standards family provides the interoperable contract layer.

The framework explains how the parts work together.
