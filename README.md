---
title: Data Product Operating Framework
version: 0.2.0
status: draft
date: 2026-10-06
---

# Data Product Operating Framework

The Data Product Operating Framework defines how organisations direct, define, operate and assure data products from business demand to measurable value.

Its Core is a universal, vendor-neutral and technology-neutral operating model. Implementation profiles adapt the Core for different organisational stages and operating models.

The framework does not require organisations to operate AI agents. It provides one common operating model that supports organisations from traditional enterprise data product management through AI-agent-first operations.

It sits above the ODPS standards family and explains how the specifications work together as part of an organisational operating model. The framework itself is not another ODPS-family specification.

![Data Product Operating Framework Core overview](assets/framework-overview-v0.1.png)

## Project scope

This repository is the source project for the Data Product Operating Framework. The repository slug is `framework`; the framework's published name remains **Data Product Operating Framework**.

The framework is:

- an implementation-neutral operating model
- a connection between organisational decision-making and data product execution
- a structure for evidence, assessment and measurable value
- guidance for using the ODPS standards family together

The framework is not:

- a replacement for an ODPS-family specification
- a data platform or catalog implementation
- evidence that a specific organisation or product conforms

## Core structure

The conceptual architecture is:

`Data Product Operating Framework Core → Enterprise Data Product Profile → AI-Agent-First Data Product Profile`

This is one framework, not three. The profiles extend Core requirements without renaming capabilities, forking terminology or creating separate maturity models.

The universal Core contains four functions and fourteen capabilities:

1. **DIRECT** — Why should we do this, and who decides?
2. **DEFINE** — What exactly are we committing to provide?
3. **OPERATE** — How do we make it available, use it and change it?
4. **ASSURE** — Does it work, comply and create value?

The core rule is:

> Intent and directives flow toward execution. Evidence and value flow toward decision-making.

The Core also defines common principles, terminology, traceability, evidence, assessment and conformance models. It supports human users, traditional applications, analytics systems, data platforms, automation, AI systems and AI agents without requiring any one consumer or implementation technology.

## Profile progression

The implementation progression is:

`Enterprise Data Products → Machine-Readable Data Products → Agent-Ready Data Products → Agent-First Operations`

### Enterprise Data Products

Governed products exist with ownership, contracts, catalogs and lifecycle management.

### Machine-Readable Data Products

Core product definitions, semantics, relationships and policies are increasingly structured and machine-readable.

### Agent-Ready Data Products

Products contain enough explicit context, semantics, access information and governance information for safe machine interpretation.

### Agent-First Operations

AI agents actively participate in discovery, product operations, workflows, assurance and decision support within explicit governance boundaries.

## Repository structure

- [`framework-core.md`](framework-core.md) — universal framework definition
- [`capabilities/`](capabilities/) — detailed capability references
- [`assessment-standard.md`](assessment-standard.md) — common capability assessment model
- [`implementation-playbook.md`](implementation-playbook.md) — implementation guidance
- [`glossary.md`](glossary.md) — common terminology
- [`profiles/`](profiles/) — Core implementation profiles
- [`crosswalks/`](crosswalks/) — mappings to other frameworks and standards
- [`library/`](library/) — governed external evidence catalog and thematic source collections
- [`enrichment/`](enrichment/) — proposal and review workflow for evidence-grounded content enrichment
- `assets/` — framework diagrams and other publication assets
- `publication/` — shared HTML and PDF templates, styles and publication manifest
- `scripts/build_publication.mjs` — deterministic Markdown-to-HTML publication build
- `scripts/render_pdf.mjs` — PDF rendering from the generated print publication
- `VERSIONING.md` — versioning and release approach
- `GOVERNANCE.md` — project authority and change process
- `CONTRIBUTING.md` — contribution requirements
- `CHANGELOG.md` — notable framework changes
- `scripts/validate_repository.py` — repository integrity checks
- `scripts/validate_library.py` — evidence catalog and collection integrity checks

## Start here

- [Framework Core](framework-core.md)
- [DIRECT Capability Reference](capabilities/direct.md)
- [DEFINE Capability Reference](capabilities/define.md)
- [OPERATE Capability Reference](capabilities/operate.md)
- [ASSURE Capability Reference](capabilities/assure.md)
- [Assessment Standard](assessment-standard.md)
- [Implementation Playbook](implementation-playbook.md)
- [Enterprise Data Product Profile](profiles/enterprise-data-product-profile.md)
- [AI-Agent-First Data Product Profile](profiles/ai-agent-first-data-product-profile.md)
- [Glossary](glossary.md)

## ODPS standards family

The framework uses the ODPS standards family as its machine-readable foundation:

- **ODPS** — data product contracts
- **ODPC** — portfolio and discovery
- **ODPV** — shared vocabulary
- **ODPG** — relationships and context
- **ODPR** — workflow contracts

Operational systems execute work and provide runtime observations. The evidence layer preserves what proves what happened.

ODPS is machine-readable by design. Human-readable documentation and interfaces should increasingly be generated from the same underlying product artifacts used by software and AI agents.

The framework defines how these standards and runtime responsibilities work together in an operating model. It does not redefine the standards.

## Publication model

Markdown is the normative, human-maintained source of truth for this framework repository.

The responsive standalone HTML publication and the PDF are generated from the same ordered Markdown sources in `publication/manifest.json`. The HTML uses a dark, collapsible chapter navigation and a light reading area; below desktop width, navigation becomes an accessible hamburger-controlled drawer.

Generated publication files should not be manually edited and are not independent normative sources.

## Evidence library and assisted enrichment

The framework can draw on a governed library of external standards, regulation, research and professional guidance. The library records source authority, currency, rights, intended uses and relevant framework capabilities. It is evidence for editorial decisions; it is not automatically part of the framework and does not transfer external requirements into the Core.

LLM-assisted enrichment is proposal-only. The tooling retrieves material from the local evidence index, requires source identifiers for claims and writes a review artifact outside the normative Markdown. A maintainer must assess relevance, source authority, licensing, architectural fit and wording before manually accepting any change.

The workflow is:

```text
Catalog sources -> retrieve permitted local copies -> build index
    -> prepare or run an enrichment proposal -> validate citations
    -> human review -> deliberate Markdown change
```

See the [evidence library](library/README.md), [source policy](library/source-policy.md) and [enrichment workflow](enrichment/README.md). A model or provider is not required to build and inspect a proposal prompt, and no provider is made authoritative by the tooling.

Install dependencies and run the complete publication pipeline:

```sh
npm ci
npm run publication
```

The pipeline writes:

- `dist/index.html` — standalone responsive framework publication
- `dist/downloads/data-product-operating-framework-v0.2.0.pdf` — PDF served by the website
- `output/pdf/data-product-operating-framework-v0.2.0.pdf` — canonical local PDF artifact

For HTML-only validation during editing:

```sh
npm test
```

GitHub Actions builds, validates and deploys `dist/` to GitHub Pages after changes reach `main`. Under the Open Data Product Initiative custom domain, the intended project URL is `https://opendataproducts.org/framework/`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution workflow and [GOVERNANCE.md](GOVERNANCE.md) for project decision-making.

## License

Except where otherwise noted, the framework documentation and publication assets are licensed under the [Creative Commons Attribution 4.0 International License](LICENSE).

When sharing or adapting the material, credit the **Data Product Operating Framework contributors**, link to the source repository and license, and indicate whether changes were made. Third-party material remains subject to its original terms and should be identified separately.

## Status

This repository currently contains the draft Core v0.2, fourteen capability definitions and two draft implementation profiles. Draft material is open for review but must not be represented as a released or adopted framework version.
