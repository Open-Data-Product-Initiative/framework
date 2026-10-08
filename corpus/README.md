# Framework implementation corpus

This corpus is a compact, structured set of framework and synthetic-example records for documentation generation, assessment-question design, training and agent evaluation. It is not normative specification text and it does not replace the governed external evidence library in `library/`.

Each entry in `records.jsonl` has a stable `id`, `category`, `source_type`, `source`, `provenance`, `capabilities` and `content`. The permitted source types are `normative`, `framework`, `guidance`, `example` and `synthetic`.

The current corpus intentionally labels all new scenario content as `synthetic` or `example`. Specification assertions should point to the relevant schema or official standard and should not be inferred from this corpus.
