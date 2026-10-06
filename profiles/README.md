---
title: Framework Profiles
version: 0.1.0
status: draft
date: 2026-10-06
---

# Framework Profiles

Profiles adapt the [Data Product Operating Framework Core](../framework-core.md) to a specific operating environment.

The profile architecture is:

`Data Product Operating Framework Core → Enterprise Data Product Profile → AI-Agent-First Data Product Profile`

This is one framework. Profiles strengthen or specialise Core requirements; they do not create separate frameworks.

## Available profiles

- [Enterprise Data Product Profile](enterprise-data-product-profile.md) — baseline implementation for conventional enterprise systems and human-led operating models
- [AI-Agent-First Data Product Profile](ai-agent-first-data-product-profile.md) — stronger requirements for environments where AI agents directly discover, interpret, access, combine or act on data products

## Profile model

A profile may:

- define its scope and intended environment
- extend Core requirements
- identify stronger practices
- identify required evidence
- identify mandatory machine-readable artifacts
- identify stronger control requirements
- define context-specific assessment expectations

A profile must not:

- duplicate the entire framework
- rename Core capabilities
- create a separate maturity model
- fork Core terminology
- redefine ODPS-family standards

All profiles use the common [Assessment Standard](../assessment-standard.md) and the same C1-C14 capability model.

## Adoption progression

`Enterprise Data Products → Machine-Readable Data Products → Agent-Ready Data Products → Agent-First Operations`

### Enterprise Data Products

Governed products exist with ownership, contracts, catalogs and lifecycle management.

### Machine-Readable Data Products

Core product definitions, semantics, relationships and policies are increasingly structured and machine-readable.

### Agent-Ready Data Products

Products contain enough explicit context, semantics, access information and governance information for safe machine interpretation.

### Agent-First Operations

AI agents actively participate in discovery, product operations, workflows, assurance and decision support within explicit governance boundaries.

The stages describe an adoption path, not separate framework versions or maturity models. An organisation may adopt stronger practices selectively while retaining the same Core.
