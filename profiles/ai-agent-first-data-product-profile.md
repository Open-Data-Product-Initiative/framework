---
title: AI-Agent-First Data Product Profile
version: 0.1.0
status: draft
date: 2026-10-06
purpose: Define the stronger requirements for data product environments where AI agents directly discover, interpret, access, combine or act on data products.
---

# AI-Agent-First Data Product Profile

## 1. Scope

The AI-Agent-First Data Product Profile defines stronger requirements for data product environments where AI agents directly:

- discover data products
- interpret product context
- select products
- access products
- combine products
- invoke tools
- execute workflows
- reason over relationships
- evaluate evidence
- take actions based on data products

The AI-Agent-First Profile extends the [Data Product Operating Framework Core](../framework-core.md). It does not create a separate framework.

It strengthens selected Core capabilities. It does not rename them, fork Core terminology, create a separate maturity model or redefine ODPS-family standards.

## 2. Intended users

This profile is intended for organisations operating or preparing to operate:

- AI agents that consume or act on data products
- agent-oriented discovery services
- agent-assisted product operations
- automated evidence evaluation
- tool-using workflows
- governed decision-support or action-taking systems

It is also relevant to product, platform, governance, security, risk, compliance and assurance teams responsible for those environments.

## 3. Assumptions

The profile assumes that:

- the Core is already adopted as the common operating model
- enterprise ownership and lifecycle controls remain in force
- agents have identifiable operating contexts and bounded authority
- authoritative artifacts can be resolved programmatically
- agent actions can be observed and retained as evidence
- human accountability remains explicit
- higher autonomy requires stronger context, controls and assurance

Agent-first does not mean agent-only. Human review, escalation and decision rights remain part of the operating model where material judgement or authority is required.

### Proportional strengthening

The strength of implementation should reflect at least:

- autonomy — whether the agent recommends, prepares, decides or acts
- materiality — the consequence for people, services, finances, rights or obligations
- reversibility — whether an action can be safely undone
- reach — the number and variety of products, consumers and systems affected
- uncertainty — the reliability of context, semantics, models and observations
- exposure — the sensitivity of data and power of available tools

Higher consequence, autonomy or irreversibility requires stronger identity, authorization, validation, monitoring, approval, suspension and evidence. Low-risk assistance may use lighter controls, but it should still remain traceable to an approved use case and accountable owner.

## 4. Strengthened Core capability requirements

All fourteen Core capabilities apply. The profile adds the following context-specific expectations.

### C1. Strategy and Objectives

Agent participation should be linked to an explicit objective, approved use case and expected outcome. Autonomy should not be introduced without a justified operating need.

### C2. Demand and Use Case Management

Agent-supported use cases should identify the consumer, intended decision or action, acceptable outcome, evidence needs and material failure conditions.

### C3. Portfolio, Investment and Accountability

Agent-enabled products and workflows should have accountable owners, explicit investment decisions and lifecycle decisions covering continuation, suspension and retirement.

### C4. Product Definition and Contract

Require:

- an authoritative machine-readable ODPS contract
- stable identifiers
- explicit versions
- machine-resolvable interfaces
- clear consumer context
- agent-usable product descriptions

The contract should allow an agent to determine what the product is, what it provides, how it can be accessed and which version is applicable without relying only on free-text pages.

### C5. Semantics and Vocabulary

Require:

- machine-readable semantic definitions
- controlled vocabulary for material concepts
- stable identifiers
- explicit aliases
- multilingual labels where relevant
- mappings to external vocabularies where useful
- semantic consistency across artifacts

Ambiguous or conflicting meanings should be treated as operating risks, not only documentation defects.

### C6. Product Commitments and Usage Conditions

Require machine-readable:

- quality expectations
- service-level expectations
- access conditions
- usage restrictions
- security conditions
- privacy conditions
- licensing where relevant
- commercial terms where relevant

Executable or automatically testable rules are preferred where practical. Machine-readable conditions do not remove the need for accountable policy ownership or exception decisions.

### C7. Relationships, Dependencies and Context

Require graph-traversable relationships for relevant:

- objectives
- use cases
- products
- dependencies
- KPIs
- policies
- controls
- APIs
- agents
- workflows

Relationship provenance and confidence should be retained where relevant. Agents should be able to distinguish authoritative, inferred and unverified relationships.

### C8. Catalog, Publication and Discovery

Require agent-oriented discovery through structured metadata and machine interfaces.

AI agents should be able to identify suitable products, resolve authoritative references and evaluate basic fitness for use without depending only on free-text catalog pages.

Discovery results should respect visibility, policy and entitlement boundaries.

### C9. Provisioning, Integration and Consumption

Require machine-readable access and integration instructions.

Where required, agents should have identifiable identities and explicit authorization. Agent access follows the same product contract, policy boundaries, entitlement controls and revocation processes as other consumers.

Credentials should not be inferred from the identity of the human or system that initiated the workflow unless explicitly authorised.

### C10. Lifecycle, Version and Change Management

Require agents to identify:

- the current version
- supported versions
- deprecated versions
- breaking changes
- migration expectations

Agent consumers should not silently continue using invalid assumptions after product changes. Cached context and workflow dependencies should be invalidated or reviewed when material contracts change.

### C11. Workflow, Automation and Agent Operations

This is the strongest capability in this profile.

Agent-assisted workflows should define where appropriate:

- workflow intent
- authoritative input artifacts
- grounding boundaries
- available tools
- permissions
- allowed actions
- iteration limits
- stopping conditions
- expected outputs
- validation gates
- human approval gates
- escalation conditions
- workflow version
- provenance requirements

ODPR should be the preferred portable workflow representation. Runtime-specific orchestration may execute the workflow but should not silently redefine its declared boundaries.

### C12. Observability and Service Assurance

Require automated comparison where practical between declared state and observed state.

Examples include:

- declared quality versus measured quality
- declared service level versus runtime performance
- declared version versus deployed version
- declared access rules versus observed entitlements

The comparison result, measurement method, product version and relevant agent or workflow identity should be retained as evidence.

### C13. Governance, Risk, Compliance and Control Assurance

Extend control assurance to include:

- agent permissions
- agent identity
- tool access
- action boundaries
- human escalation
- evidence provenance
- workflow provenance
- model provenance where relevant
- policy enforcement
- kill or suspension mechanisms where material

Controls should address both prohibited actions and failure to stop, escalate or request approval when required.

### C14. Adoption, Outcomes and Value Realisation

Do not measure agent success through:

- tool calls
- prompts
- token volume
- workflow execution count alone

Measure:

- successful use cases
- consumer outcomes
- decision improvements
- operational outcomes
- financial value where appropriate
- risk reduction
- service improvements

Agent activity is execution evidence. It is not automatically evidence of value.

## 5. Mandatory evidence

In addition to applicable Core evidence, an in-scope agent-first implementation should retain:

- the authoritative product and workflow versions used
- the agent identity and relevant authorization context
- resolved product, vocabulary and relationship references
- tool and action permissions
- workflow inputs and expected outputs
- validation and approval-gate results
- execution and decision provenance
- material model provenance where relevant
- policy and control outcomes
- exceptions and escalations
- observed product and service results
- the supported use-case outcome

Evidence retention should be proportionate to the materiality, autonomy and reversibility of the agent's actions.

## 6. Recommended automation

Automate where practical:

- ODPS, ODPC, ODPV, ODPG and ODPR validation
- identifier and reference resolution
- semantic consistency checks
- policy and entitlement evaluation
- breaking-change detection
- workflow boundary validation
- declared-versus-observed comparison
- provenance capture
- control evidence packaging
- suspension of workflows that exceed defined boundaries

Automation should fail safely when authoritative context, permission or required evidence cannot be resolved.

## 7. ODPS-family expectations

The profile expects stronger use of the common authority model:

- **ODPS** is the authoritative individual data product contract.
- **ODPC** supplies machine-oriented portfolio and discovery objects.
- **ODPV** supplies shared vocabulary and semantics.
- **ODPG** supplies graph-traversable relationships and context.
- **ODPR** supplies reusable workflow contracts.
- **Operational systems** execute work and provide runtime observations.
- **The evidence layer** preserves what proves what happened.

These artifacts should use stable identifiers and resolvable references. The profile strengthens how the standards are used; it does not add a new ODPS-family specification or redefine an existing one.

## 8. Minimum implementation baseline

An organisation should demonstrate at least one bounded agent-supported use case containing:

1. an approved objective and use case
2. an accountable human owner
3. a machine-readable ODPS contract
4. structured discovery metadata
5. controlled vocabulary for material concepts
6. graph-traversable product and governance context
7. machine-readable access instructions
8. an identifiable agent and explicit authorization
9. a versioned workflow contract with stopping and approval conditions
10. recorded execution and provenance evidence
11. declared-versus-observed assurance
12. a measured use-case outcome
13. a tested suspension or escalation path where material

The baseline should be proven on bounded, reviewable workflows before autonomy is expanded.

## 9. Assessment expectations

Assessment uses the common [Assessment Standard](../assessment-standard.md), C1-C14 capability model and dimensions of Accountability, Practice, Evidence and Outcome.

The profile does not award maturity merely because an organisation uses agents or automates workflows. Assessors should verify that:

- accountability and decision rights remain explicit
- required machine-readable artifacts are authoritative and resolvable
- agent permissions and action boundaries operate in practice
- evidence and provenance are retained
- declared state is compared with observed state
- outcomes and value are measured beyond execution volume

Stronger profile requirements increase the evidence expected within a capability. They do not create a separate capability score or maturity model.

## 10. Evidence basis and applicability

Library sources **`nist-ai-rmf-1.0`**, **`nist-ai-600-1-genai-profile`** and **`oecd-ai-principles-2024`** support this profile. The [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1) supports lifecycle governance, contextual risk analysis, measurement and accountable management. Its [Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) adds generative-AI risk and action patterns relevant to some agent implementations. The [OECD AI Principles](https://oecd.ai/en/ai-principles) provide intergovernmental context for beneficial outcomes, transparency, robustness and accountability.

Sources **`w3c-prov-o`**, **`w3c-odrl-2.2`** and **`w3c-shacl`** provide implementation patterns. [W3C PROV-O](https://www.w3.org/TR/prov-o/) informs execution and evidence provenance; [W3C ODRL 2.2](https://www.w3.org/TR/odrl-model/) informs machine-readable permissions and duties; and [W3C SHACL](https://www.w3.org/TR/shacl/) provides an example of machine-testable constraints and validation results. These are implementation resources, not replacements for ODPS-family authority.

Library source **`eu-ai-act-2024-1689`**, [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), may impose legal requirements for particular AI systems, actors, uses and dates in its jurisdiction. This profile does not make those jurisdiction-specific obligations universal or provide a legal compliance determination. Organisations should map applicable duties to C6 and C13 with qualified legal and risk ownership.
