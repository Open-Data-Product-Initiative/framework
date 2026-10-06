---
title: Versioning Policy
version: 0.1.0
status: draft
date: 2026-10-06
---

# Versioning Policy

## 1. Version model

Use semantic-style framework versions:

`MAJOR.MINOR.PATCH`

Example:

`0.1.0`

## 2. Major version

Increment MAJOR when:

- functions change materially
- capabilities are added, removed or redefined incompatibly
- assessment semantics change materially
- conformance claims change materially

## 3. Minor version

Increment MINOR when:

- new guidance is added
- capability definitions are expanded
- profiles are added
- crosswalks are added
- new examples are added
- backward-compatible evidence requirements are added

## 4. Patch version

Increment PATCH when:

- wording is corrected
- broken links are fixed
- formatting changes
- clarifications do not alter framework meaning

## 5. Status values

Recommended values:

- draft
- review
- release-candidate
- stable
- deprecated

## 6. Source-of-truth rule

Markdown files are the normative human-maintained source.

HTML and PDF files are generated outputs.

Generated files should include the exact source version used to build them.
