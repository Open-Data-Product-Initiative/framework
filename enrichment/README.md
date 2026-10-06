# Evidence-Grounded Enrichment Workflow

The enrichment workflow helps maintainers develop richer framework text from the governed evidence library. It creates reviewable proposals; it never edits framework source files.

## Control model

```text
External sources -> governed catalog -> local deterministic index
    -> retrieved evidence -> LLM or human synthesis -> proposal
    -> automated checks -> maintainer review -> deliberate source edit
```

The source catalog, retrieved passages and reviewer judgement have distinct roles. An LLM is a drafting mechanism, not an authority.

## Prepare the index

```sh
npm run library:validate
npm run library:ingest
npm run library:index
```

Ingestion is optional. Without it, catalog summaries provide a smaller but still traceable index.

## Build a proposal prompt without calling a model

```sh
npm run enrich:propose -- \
  --target framework-core.md \
  --heading "F7. Treat evidence as a first-class object" \
  --question "Clarify how evidence provenance should be recorded" \
  --collection governance-and-assurance \
  --dry-run
```

The command writes a JSON proposal under `enrichment/proposals/`. The proposal contains the target excerpt, retrieved evidence, source identifiers, prompt, model metadata and review state. Generated proposal files are ignored by default.

## Optional model invocation

The tool can call an operator-selected endpoint that implements the OpenAI-compatible chat completions request shape:

```sh
ENRICHMENT_API_KEY="..." npm run enrich:propose -- \
  --target capabilities/assure.md \
  --heading "C12. Observability and Service Assurance" \
  --question "Add a concise evidence provenance practice" \
  --endpoint "https://provider.example/v1/chat/completions" \
  --model "provider-model-name"
```

No endpoint or model is selected by the repository. The API key is read from `ENRICHMENT_API_KEY` and must not be committed. Operators must evaluate provider confidentiality, retention and licensing terms before sending content.

## Expected model response

The prompt asks for JSON with:

- `summary` — explanation of the proposed improvement
- `draft_markdown` — replacement or additional Markdown, without modifying files
- `claims` — individual claims with one or more catalog source identifiers
- `limitations` — uncertainty, conflicts and applicability boundaries
- `architecture_impact` — expected effect on Core, profiles, capabilities and ODPS-family boundaries

The wrapper preserves the raw response. It does not trust model-supplied URLs or add unknown sources to the catalog.

## Validate and review

```sh
npm run enrich:validate -- enrichment/proposals/<proposal>.json
```

Automated validation checks structure, target existence, known source identifiers, citation coverage and prohibited approval states. It cannot establish whether a source truly supports a claim.

Use the [review checklist](reviews/README.md) before manually editing normative Markdown. Any accepted text should be rewritten as needed to fit framework terminology, avoid unnecessary quotation and preserve the Core/profile authority boundary.
