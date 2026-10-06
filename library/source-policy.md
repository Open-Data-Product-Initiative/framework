# External Source Policy

## Purpose

This policy governs how external material may inform the Data Product Operating Framework and its implementation profiles.

## Selection

Prefer primary sources: adopted standards, official legal texts, first-party institutional guidance and original peer-reviewed research. Secondary commentary may help discovery but should not be used when the primary source is available.

A source must have a stable identifier, accountable publisher, clear relevance and enough publication metadata to assess currency. Commercial accessibility is not evidence of authority, and public accessibility is not permission to redistribute.

## Use of authority tiers

Source tier controls the weight that may be placed on a source. Applicability still requires judgement. A Tier 1 regulation may be decisive within its jurisdiction but inappropriate as a universal global requirement. A Tier 4 professional framework may be useful implementation guidance without defining conformance to this framework.

No external source may silently:

- redefine an ODPS-family specification
- make the Core vendor-specific or jurisdiction-specific
- turn profile-specific practices into universal requirements
- replace evidence of observed outcomes with declared intentions
- change the four functions or fourteen capabilities

## Rights and retrieval

Every catalog record declares both access and redistribution policy.

- `local-analysis` permits retrieval into ignored local working directories for research.
- `metadata-only` records a reference but does not retrieve the source through repository tooling.
- `redistribution` records whether the repository may publish a copy; `not-cleared` is the default.

Downloaded and extracted material is ignored by Git. Contributors must not commit third-party full text based only on the fact that it is reachable online.

## Citation and claim rules

Evidence-grounded proposals cite catalog source identifiers, not only URLs. Each material factual or prescriptive claim must identify the source that supports it. Synthesis must be labelled as synthesis; generated text must not be presented as a quotation.

Before accepting a proposal, a reviewer must check:

1. the cited source actually supports the claim
2. the source is authoritative for the stated scope
3. the source is current enough for the claim
4. the wording does not exceed the source's meaning
5. copyright and quotation limits are respected
6. conflicts or material uncertainty are visible

## LLM use

An LLM may retrieve, compare, summarize and draft. It may not approve changes, determine conformance, invent citations or write directly into normative Markdown through this workflow. Model and provider details must be recorded with a generated proposal so reviewers can reproduce or challenge the synthesis.

Prompt content may leave the local environment when a remote endpoint is used. The operator is responsible for ensuring that the selected source material and target content may be sent to that provider.
