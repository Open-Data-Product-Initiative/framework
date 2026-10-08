---
title: C11 Workflow Automation and Agent Operations
version: 0.2.0
status: draft
date: 2026-10-08
---

# C11. Workflow, Automation and Agent Operations

## Capability summary

| Capability ID | Function | Purpose | Primary owner | Primary standard | Key outputs | Key evidence |
|---|---|---|---|---|---|---|
| C11 | OPERATE | Execute repeatable work with explicit boundaries. | Workflow owner | ODPR | Versioned workflow contract | Execution, exception and approval record |

## Purpose

C11 defines how repeatable data-product work is initiated, executed, stopped, approved and evidenced. It applies to human-led, automated and agent-assisted operations.

## Why it matters

An automation that only records a technical success hides whose authority it used, which artifact versions it acted on and whether it should have stopped.

## When it applies

Apply it to onboarding, catalog publication, validation, release, remediation, portfolio review and any agent action with a material effect.

## Inputs

Trigger, approved workflow version, input artifact versions, permissions, tools, policies, decision points, stopping conditions and evidence retention are inputs.

## Practices

Model the workflow, validate reusable ODPR recipes where appropriate, establish accountable ownership, log the actor and input versions, route exceptions and preserve human approval points.

## Roles and accountability

The workflow owner is accountable for its purpose and controls. Performers or agents execute only within granted tools and permissions. Approvers make decisions the workflow explicitly reserves for humans.

## Outputs

Produce a workflow contract, execution record, decision and exception trail, outputs, status and remediation path.

## ODPS family mapping

ODPR is primary for portable workflow contracts. ODPS/ODPC/ODPG/ODPV artifacts may be inputs or outputs. Runtime logs are evidence and should not be misrepresented as recipe declarations.

## Evidence

Keep workflow validation, execution ID, recipe and input versions, actor identity, approval, outputs, error and exception records.

## Measures

Track successful and failed runs, exception rate, unresolved approvals, reproducibility and workflow steps executed outside policy.

## Example

The Customer 360 release recipe validates the proposed contract, checks the change record, pauses for human production approval and records the exact version that was deployed.

## Questions to ask

- What starts and ends this workflow?
- Which versions, tools and permissions does it require?
- What must stop execution?
- Which decisions require a human approver?
- Can the execution be reproduced from retained evidence?

## Common failure modes

Typical failures are embedding policy in opaque code, allowing an agent to approve its own output, or treating a completed run as proof of a business outcome.

## Minimum implementation

Document one versioned workflow with owner, inputs, outputs, a stop condition and an approval step.

## Advanced implementation

Publish portable workflows, collect structured execution evidence and continuously test permissions, exception handling and reproducibility.

## AI-Agent-First extension

AI agents require an explicit tool allowlist, permissions, grounding sources, stop conditions, human-approval gates and provenance; see the profile rather than creating a second workflow model.

## Assessment levels 1-5

Level 1 has informal handoffs. Level 2 defines repeatable workflows. Level 3 retains execution and exception evidence. Level 4 measures reliability and control performance. Level 5 uses governed automation while preserving accountable decisions.
