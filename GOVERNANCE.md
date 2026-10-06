# Governance

## Project purpose

The Data Product Operating Framework defines an open, vendor-neutral operating model for directing, defining, operating and assuring data products from business demand to measurable value.

## Authority boundaries

The framework defines operating-model concepts, practices, evidence expectations, assessment logic, profiles and crosswalks.

It does not redefine the schemas or normative artifact requirements owned by ODPS-family specifications. When a framework document conflicts with an adopted ODPS-family specification about that specification's artifact format, the specification is authoritative.

The framework also does not treat runtime platforms as authoritative definitions of portable product contracts. Operational systems are authoritative only for the observations they produce within their stated scope.

## Maintainer responsibilities

Maintainers are responsible for:

- protecting the project purpose and authority boundaries
- reviewing semantic and compatibility impact
- requiring evidence for conformance, maturity and value claims
- keeping Core, capabilities, assessment rules, profiles and crosswalks aligned
- preparing releases according to `VERSIONING.md`
- documenting accepted decisions and dissent where material
- applying the code of conduct

Maintainer appointment and removal follow the governance rules of the Open Data Product Initiative once the project is formally adopted.

## Decision process

1. A material proposal begins with an issue describing the problem, affected framework identifiers, evidence and compatibility impact.
2. Maintainers determine whether the change is editorial, additive, behavioural or breaking.
3. Relevant ODPS-family maintainers should review changes that depend on or characterize their specifications.
4. The proposal remains open long enough for meaningful review proportional to its impact.
5. A maintainer records the decision and rationale before merge.

Consensus is preferred. When consensus cannot be reached, designated maintainers decide within the Initiative's governance model and record the unresolved concerns.

## Normative change control

Changes to Core principles, function or capability meanings, authority boundaries, conformance, or assessment levels require:

- an issue and explicit rationale
- compatibility analysis
- review of all affected framework documents
- validation passing on the complete repository
- release classification under `VERSIONING.md`

Editorial changes must not alter normative meaning.

## External evidence and generated proposals

External material informs decisions but does not acquire framework authority merely by appearing in the evidence library. Maintainers must consider the source's authority, scope, currency, rights and compatibility with the framework's vendor-neutral Core.

LLM output is an editorial proposal, not evidence, consensus or an accepted framework change. Generated proposals must preserve source identifiers and distinguish sourced claims from synthesis. Acceptance remains subject to the normal decision process and normative change controls.

## Releases

Only a versioned release approved through project governance is an adopted framework release. Files marked `draft` are proposals and must not be represented as adopted requirements.
