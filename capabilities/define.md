---
title: DEFINE Capability Reference
version: 0.2.0
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

### Operating intent

The product contract is the stable point of agreement between provider and consumer. It should be independently identifiable, versioned and sufficiently complete for a consumer to determine what the product offers, who is accountable for it, how it can be accessed and which commitments and conditions apply. A catalog page or platform configuration may present parts of that information, but neither should silently become the only authoritative definition.

The contract should describe the product rather than the internal project that created it. Implementation details belong where they affect consumption, commitments or change impact; temporary delivery tasks do not. When information is maintained in another authoritative artifact, the contract should use a stable reference and define what happens if that reference cannot be resolved.

Human-readable pages should be generated from or demonstrably aligned with the same machine-readable definition. Parallel hand-maintained descriptions create ambiguity precisely when a consumer needs certainty about a version, interface or commitment.

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

### Assurance questions

- Can a consumer distinguish the product identity from the catalog record, dataset and delivery interface?
- Is there one authoritative version of the contract and a defined approval authority?
- Can the contract be validated without depending on a particular catalog vendor?
- Do human and machine presentations resolve to the same meaning and version?

## C5. Semantics and Vocabulary

### Purpose

Ensure that people and systems, including AI agents where used, interpret product concepts consistently.

### Operating intent

Semantic management should focus first on concepts whose ambiguity changes a decision, rule, calculation or integration. Not every label needs central governance. Material terms—such as customer, active account, service region or reportable incident—need stable identity, a clear definition, accountable stewardship and an explicit relationship to local or external terms.

Labels and aliases support discovery, but they are not substitutes for concept identity. A renamed label should not silently create a new concept, and two identical labels should not be assumed to have identical meaning. Where multilingual labels are provided, the underlying identifier and definition should preserve equivalence or disclose the difference.

Semantic consistency must be checked across contracts, catalogs, graphs, policies and workflow inputs. A vocabulary is useful only when implementations actually reference it and changes are governed.

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

### Assurance questions

- Which concepts would create material risk if interpreted differently by two consumers?
- Are labels, aliases, definitions and identifiers managed separately?
- Can a reviewer trace where a concept is used across product and governance artifacts?
- Are mappings to external vocabularies qualified rather than treated as automatic equivalence?

## C6. Product Commitments and Usage Conditions

### Purpose

Define what consumers should expect from the product and the conditions under which it is provided and used.

### Operating intent

A commitment should identify the subject, metric or rule, threshold, evaluation period, measurement method, scope and consequence of failure. “High quality” and “available when needed” are aspirations, not testable commitments. A product may also disclose non-binding objectives, but consumers must be able to distinguish them from approved obligations.

Usage conditions should be understandable before access is granted. They may include permitted purposes, prohibited uses, attribution, retention, privacy, security, geographic, licensing or commercial conditions. Machine-readable expression improves consistency and automated evaluation, but expression alone does not create legal validity or operational enforcement.

The provider should manage conflicts between conditions, record approved exceptions and identify which rule prevails. A declared rule, an enforcement configuration and evidence that the rule operated are three separate objects.

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

### Assurance questions

- Can each material commitment be evaluated using a defined observation and period?
- Can consumers distinguish binding conditions, service objectives and descriptive guidance?
- Are policy conflicts, exceptions and precedence decisions recorded?
- Does the product state what happens when a commitment is missed or a condition changes?

## C7. Relationships, Dependencies and Context

### Purpose

Connect the individual data product to the wider network of objectives, use cases, KPIs, policies, systems, products, APIs, workflows, consumers and organisational responsibilities.

### Operating intent

Relationships turn isolated records into operational context. Each material relationship should identify both endpoints, use a defined relationship type and retain enough provenance to explain who asserted it, from which evidence, when and with what confidence. A free-text note that “product A depends on product B” is difficult to validate, traverse or use for impact analysis.

Not every possible edge belongs in the shared graph. Include relationships that support a decision, control, discovery path, dependency analysis, workflow or value chain. Derived relationships should be distinguishable from confirmed relationships, and conflicting assertions should remain reviewable rather than being silently overwritten.

Graph quality includes more than valid syntax. References must resolve, relationship direction must be meaningful, lifecycle states must be compatible and critical paths must have accountable owners. These checks allow a change in an objective, policy, interface or upstream product to be traced to affected consumers and outcomes.

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

### Assurance questions

- Can critical product dependencies be traversed in both directions?
- Does each material relationship have type, provenance, status and review responsibility?
- Are inferred or low-confidence relationships visibly different from confirmed assertions?
- Can the graph answer an impact question, not merely display connected nodes?

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

Exit is a controlled transition, not a claim that the definition is permanently complete. Any unresolved assumption, exception or planned semantic decision should be recorded with an owner and due date. Material changes after the transition return through the relevant DEFINE and lifecycle controls.

## Evidence basis and external references

The framework requirements above remain Open Data Product Initiative decisions. These sources support the implementation reasoning:

- **`w3c-dcat-3`** — [W3C Data Catalog Vocabulary 3](https://www.w3.org/TR/vocab-dcat-3/) provides interoperable patterns for datasets, services, distributions, catalog records, identifiers and relationships. It informs catalog interoperability but is not a substitute for an ODPS product contract.
- **`wilkinson-fair-principles-2016`** — [FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18) emphasise persistent identifiers, rich metadata, provenance and machine actionability. The framework applies those ideas selectively; a FAIR digital object is not automatically a governed data product.
- **`w3c-skos`** — [W3C SKOS](https://www.w3.org/TR/skos-reference/) distinguishes concepts, labels, semantic relationships and mappings. It supports the vocabulary guidance without requiring every implementation to use RDF.
- **`w3c-odrl-2.2`** — [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/) separates permissions, prohibitions, duties and constraints. It informs machine-readable usage conditions but does not prove that a policy was enforced.
- **`w3c-prov-o`** — [W3C PROV-O](https://www.w3.org/TR/prov-o/) represents entities, activities, agents and provenance relationships. It informs relationship and evidence provenance without redefining ODPG.
- **`w3c-shacl`** — [W3C SHACL](https://www.w3.org/TR/shacl/) demonstrates how machine-readable constraints can produce validation results. It is an implementation option, not a mandatory validation technology for the Core.
