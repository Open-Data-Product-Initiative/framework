---
title: DEFINE Capability Reference
version: 0.1.0
status: draft
date: 2026-10-06
capabilities: [C4, C5, C6, C7]
---

# DEFINE

## Purpose

DEFINE turns an approved data product candidate into an explicit, governed and machine-readable product definition.

## Separation of concerns

- ODPS defines the data product.
- ODPC defines reusable portfolio objects and catalogs.
- ODPV defines shared terminology and semantics.
- ODPG defines relationships between products, use cases, objectives, policies and other objects.
- ODPR defines repeatable work and workflow contracts around those artifacts.

## C4. Product Definition and Contract

### Purpose

Establish an authoritative machine-readable definition of the data product.

### Practices

1. Assign product identity.
2. Define the product proposition.
3. Declare provider responsibility.
4. Define product type.
5. Define data and delivery structure.
6. Define lifecycle state.
7. Version the product definition.
8. Declare product-local business context.
9. Validate the product definition.
10. Approve and publish the definition.

### Primary standard

ODPS.

### Evidence

- validated ODPS artifact
- version history
- approval record
- schema validation result
- publication record
- change history
- objective and use-case references

## C5. Semantics and Vocabulary

### Purpose

Ensure that people and systems, including AI agents where used, interpret product concepts consistently.

### Core rule

Structure tells a machine where information is.

Semantics tells it what the information means.

### Practices

1. Identify controlled concepts.
2. Reuse existing definitions.
3. Assign stable concept identifiers.
4. Maintain labels and aliases.
5. Define relationships between concepts.
6. Map external vocabularies.
7. Apply vocabulary across standards.
8. Detect semantic drift.
9. Expose vocabulary for machines.

### Primary standard

ODPV.

### Evidence

- approved vocabulary
- vocabulary version
- semantic mappings
- validation reports
- terminology decisions
- controlled-term references

## C6. Product Commitments and Usage Conditions

### Purpose

Define what consumers should expect from the product and the conditions under which it is provided and used.

### Practices

1. Define quality commitments.
2. Define service commitments.
3. Define access conditions.
4. Define usage conditions.
5. Define legal terms.
6. Define privacy and security expectations.
7. Define commercial terms.
8. Reuse standard condition patterns.
9. Make commitments testable.
10. Manage exceptions.

### Primary standard

ODPS.

### Evidence

- machine-readable ODPS commitments
- quality rules
- SLA rules
- access profile
- license reference
- contract reference
- pricing plan where relevant
- policy mapping
- exception record
- validation evidence

## C7. Relationships, Dependencies and Context

### Purpose

Connect the individual data product to the wider network of objectives, use cases, KPIs, policies, systems, products, APIs, workflows, consumers and organisational responsibilities.

### Core rule

A product definition answers:

`What is this product?`

A relationship graph answers:

`How does this product fit into everything else?`

### Practices

1. Identify relevant relationship types.
2. Connect products to demand.
3. Connect demand to objectives.
4. Connect products to outcomes.
5. Connect dependencies.
6. Connect governance context.
7. Connect technical context.
8. Connect consumer and automation context where relevant.
9. Record relationship confidence.
10. Review graph integrity.

### Primary standard

ODPG.

### Evidence

- validated graph artifact
- relationship provenance
- confirmed edges
- graph review record
- broken-reference report
- dependency review
- value-path analysis

## DEFINE exit criteria

A product moves into normal operational management when:

- an accountable portfolio decision exists
- the product has an approved identity
- an authoritative product definition exists
- required semantics are resolved
- relevant quality and service commitments exist
- access and usage conditions are defined
- required relationships exist
- the artifact package passes validation
- required approvals are recorded
