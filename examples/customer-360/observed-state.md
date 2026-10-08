---
title: Customer 360 Observed State
version: 0.2.0
status: draft
date: 2026-10-08
---

# Observed state: assurance scenario

This synthetic observation applies to the Customer 360 assurance review for the stated period and must not be confused with a declaration in ODPS or ODPR.

| Check | Declared state | Observed state | Status |
|---|---:|---:|---|
| Completeness | >= 98% | 94.7% | Failed |
| Freshness | <= 60 minutes | 43 minutes | Passed |
| Availability | >= 99.9% | 99.93% | Passed |
| Production version | 2.4.0 | 2.3.0 | Failed: version mismatch |
| Access entitlement | Approved consumers only | One unresolved entitlement | Failed |
| Release approval | Human approval required | No latest-deployment record | Failed |

Retention analysts using the churn-risk workflow may be affected because incomplete service interactions can reduce the reliability of the intervention list. The quality-remediation workflow should open a finding, the release workflow should stop further deployment, and the access owner should resolve the entitlement. A time-bound exception would be valid only if an authorised approver records scope, rationale and expiry.

The portfolio review receives the repeated-failure trend, consumer impact and remediation cost. It may continue the extension, delay broader adoption or change the investment decision; the failed observations do not automatically determine that decision.
