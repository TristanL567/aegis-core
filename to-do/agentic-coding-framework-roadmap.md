# AEGIS Agentic Coding Framework Roadmap

This document is the active framework backlog for future AEGIS work. Completed
epics and their tickets are recorded in `docs/completed-work.md`.

## Current Direction

AEGIS should stay ticket-driven:

- one ticket at a time;
- explicit `allowed_areas` and `must_not_touch`;
- small diffs;
- validator gate before completion;
- clean commit with ticket ID, goal, acceptance criteria, and validation
  evidence.

The framework should help a human keep overview. Do not optimize for autonomous
volume before scope, audit trail, and review workflow are solid.

## Completed Epic Record

Completed epics are no longer active planning files in `to-do/`.

- Three-Layer Skill Architecture: `AEGIS-SKILL-001` through
  `AEGIS-SKILL-009`.
- Broad Worker Migration: `AEGIS-MIGRATE-001` through `AEGIS-MIGRATE-010`.
- Progressive Disclosure: `AEGIS-PD-001` through `AEGIS-PD-004`.
- Library Expansion: `AEGIS-EXPAND-001` through `AEGIS-EXPAND-017`.
- Conformance Anchor: `AEGIS-ANCHOR-001` through `AEGIS-ANCHOR-003`.

## Active Backlog

### TODO-001: Revise Worker Skill Architecture

Goal: collapse the current worker set to the most important durable roles, then
expand technical depth through reusable references or skillsets rather than many
shallow worker prompts.

Produce a future ticket backlog that preserves:

- `master -> worker -> validator -> master`;
- ticket-based execution;
- provider-agnostic skills;
- migration safety for existing roles.

### TODO-002: Define Project Access Model

Goal: document how other projects access and apply AEGIS without copying stale
prompts everywhere.

Evaluate local path, submodule, versioned snapshot, and future package-style
access. A first version should keep canonical AEGIS files in `aegis-core` and
let target projects declare their local project conventions separately.

### TODO-003: Enforce Human-Readable Code and Limited Scope

Goal: make every implementation ticket produce concise, reviewable code and a
small audit trail.

Future work should consider:

- branch-aware implementation tickets;
- exact allowed areas;
- validator checks for unrelated refactors and unnecessary abstractions;
- human-readable diff summaries;
- explicit justification for added abstraction or code volume.

### TODO-004: Add Target-Project Run Logs

Goal: preserve per-ticket audit trails in target projects without bloating
AEGIS-CORE.

Potential records:

- ticket envelope;
- worker result;
- validator result;
- completion report;
- commit SHA.

### TODO-005: Add Definition of Ready and Definition of Done

Goal: make ticket readiness and completion checks explicit before more
automation is added.

Ready means the goal, dependencies, allowed areas, protected paths, validation
commands, and manual verification needs are known. Done means the worker output
is validated, scope is clean, and the completion report is present.

## Deferred Ideas

- project manifest such as `.aegis/project.yaml` in target projects;
- ticket ledger format;
- scope firewall tooling;
- ADR or decision log support for architecture-impacting tickets;
- specialized validator matrix;
- project onboarding report;
- prompt evaluation tests;
- risk labels.

These remain backlog candidates until converted into explicit tickets.
