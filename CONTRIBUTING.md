# Contributing

The Data Product Operating Framework is developed through reviewable, evidence-led changes.

## Before proposing a change

1. Search existing issues and pull requests.
2. Identify whether the proposal changes the Core, a capability, an assessment rule, implementation guidance, a profile or a crosswalk.
3. Explain the problem before prescribing a solution.
4. Identify affected framework identifiers, documents and ODPS-family standards.
5. Separate observed evidence from assumptions and preferences.
6. For evidence-based enrichment, register sources in `library/catalog.json` and cite their stable source identifiers.

Use an issue for material semantic changes before opening a pull request. Editorial corrections can proceed directly to a focused pull request.

## Change requirements

A contribution must:

- preserve the distinction between the framework and ODPS-family specifications
- preserve the distinction between declared and observed state
- preserve traceability from demand and decisions through execution to evidence and value
- avoid vendor-specific requirements in the Core
- define new terminology in `glossary.md`
- update every affected capability, profile, crosswalk and assessment rule
- include migration guidance when compatibility is affected
- avoid unsupported maturity, conformance, adoption or value claims
- distinguish an external source's statement from a framework decision
- record any LLM assistance without treating generated text as evidence

Profiles may add contextual requirements but must not silently redefine the Core. A profile must not rename Core capabilities, fork Core terminology, create a separate maturity model or redefine an ODPS-family standard.

## Validation

Run:

```sh
python3 scripts/validate_repository.py
```

The validation must pass before review. Reviewers may request additional semantic or standards-alignment evidence that cannot be automated.

For library or assisted-enrichment changes, also run:

```sh
npm run library:validate
npm run library:index
```

If a generated proposal is attached to a change, validate it with `npm run enrich:validate -- path/to/proposal.json`. A proposal never authorizes an edit by itself.

## Pull requests

Keep each pull request focused on one coherent change. Complete the pull request template and include:

- the problem and intended outcome
- affected identifiers and documents
- compatibility impact
- evidence supporting the change
- validation performed

## Contribution rights

Contributors must have the right to submit their work and must disclose third-party material and applicable restrictions. Acceptance is subject to the contribution and intellectual-property requirements established by the Open Data Product Initiative at the time of submission.

By submitting a contribution for inclusion, contributors agree that accepted material may be distributed under the repository's [Creative Commons Attribution 4.0 International License](LICENSE).
