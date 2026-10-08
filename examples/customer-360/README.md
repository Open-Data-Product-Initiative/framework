---
title: Customer 360 Complete Chain
version: 0.2.0
status: draft
date: 2026-10-08
---

# Customer 360: one complete chain

This synthetic example follows a single decision from objective to portfolio review. It deliberately uses ODPS-family artifacts only for concerns represented by the available schemas; decisions, runtime observations, control evidence and value review remain framework-level records.

| Capability | Artifact |
|---|---|
| C1 | [Business objective](objective.md) |
| C2 | [Use case and information need](objective.md) |
| C3 | [Product decision](product-decision.md) |
| C4 | [ODPS product contract](product.odps.yaml) |
| C5 | [ODPV terminology](vocabulary.odpv.yaml) |
| C6 | [Declared commitments and conditions](declared-state.md) |
| C7 | [ODPG relationship graph](relationships.odpg.yaml) |
| C8 | [ODPC catalog reference](catalog.odpc.yaml) |
| C9 | [Access evidence](assurance-evidence.md) |
| C10 | [Version mismatch evidence](observed-state.md) |
| C11 | [ODPR workflow](workflow.odpr.yaml) |
| C12 | [Runtime observations](observed-state.md) |
| C13 | [Control evidence](assurance-evidence.md) |
| C14 | [Adoption, outcome and value review](value-review.md) |

The chain is: objective → use case → information need → existing-product search → product decision → contract → vocabulary → relationships → catalog publication → access → version/change → workflow → runtime observation → control evidence → adoption → outcome → value → portfolio review.

The [declared state](declared-state.md) and [observed state](observed-state.md) are intentionally separate. The 94.7% completeness, deployed version 2.3, unresolved entitlement and missing approval are not fields invented in ODPS or ODPR; they are operating evidence compared with the declared product state.
