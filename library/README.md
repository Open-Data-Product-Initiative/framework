# Framework Evidence Library

The evidence library is a governed set of external sources used to research, review and improve the Data Product Operating Framework. It supports traceable editorial decisions without turning every external statement into a framework requirement.

## Authority boundary

The library is non-normative. A catalog entry records that a source may be relevant; it does not mean that the framework adopts the source, that the source is universally applicable or that the Open Data Product Initiative redistributes its content.

The framework Markdown remains the normative, human-maintained source. External standards retain their own authority and licensing terms. An LLM response is never a source.

## Contents

- `catalog.json` — canonical source metadata and framework relevance
- `source-policy.md` — authority, selection, rights and citation rules
- `collections/` — curated source sets for recurring research questions
- `cache/` — ignored local downloads and retrieval receipts
- `extracted/` — ignored text derived from locally retrieved material
- `index/` — ignored deterministic search index

JSON is used for catalog and collection metadata so validation works with the Python standard library and does not introduce a YAML parser into the publication pipeline.

## Source authority tiers

| Tier | Source class | Permitted role |
|---|---|---|
| 1 | Adopted standard, official regulation or authoritative specification | May support requirements when scope and applicability are explicit |
| 2 | Official guidance from a public or standards institution | May support practices and interpretation |
| 3 | Peer-reviewed research | May support concepts, evidence and limitations |
| 4 | Recognised professional framework | May support implementation guidance and crosswalks |
| 5 | Vendor material or implementation example | May illustrate practice but must not establish a universal Core requirement |

Tier is not a quality score. It describes the source's authority for framework work.

## Local workflow

Validate metadata:

```sh
npm run library:validate
```

Retrieve sources whose catalog policy permits local analysis:

```sh
npm run library:ingest
```

Build a deterministic local index from catalog summaries and any retrieved text:

```sh
npm run library:index
```

Retrieval is optional. The index remains usable from catalog summaries alone. See the [enrichment workflow](../enrichment/README.md) for proposal generation and review.

## Adding a source

1. Prefer the source owner's canonical page or persistent identifier.
2. Record authority tier, publisher, publication state, version or date, rights and retrieval policy.
3. Explain what the source can and cannot support.
4. Map it only to relevant collections and Core capabilities.
5. Add its identifier to each corresponding collection file.
6. Run library and repository validation.

Do not commit retrieved full text unless its redistribution terms are explicit and the project has intentionally approved that inclusion.
