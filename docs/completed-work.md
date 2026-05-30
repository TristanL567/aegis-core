# AEGIS Completed Work

This document records completed epics and replaces completed per-ticket files
that have been removed from `to-do/`. Active and upcoming framework backlog
items stay in `to-do/`.

Resolution status is confirmed against git history and repository artifacts, not
against stale ticket status fields.

## Completed Epics

### Three-Layer Skill Architecture

Original planning file: `to-do/epic-skill-architecture.md` (removed).

Established the three-layer architecture: orchestration roles, always-on
operating discipline, and narrow procedural skills. It also added the initial
authoring doctrine, completion-report expectations, and validator enforcement.

Delivered:
- `skills/roles/`
- `skills/discipline/operating-discipline.md`
- `skills/procedures/clean-commit/`
- `skills/procedures/ticket-scope-validation/`
- `skills/procedures/new-api-endpoint/`
- `docs/skill-architecture.md`
- `docs/procedural-skill-template.md`
- `docs/broad-worker-migration.md`
- `tools/validate_skill_library.py`
- `tools/validate_ticket_scope.py`

Tickets completed: `AEGIS-SKILL-001` through `AEGIS-SKILL-009`.

### Broad Worker Migration

Original planning file: `to-do/epic-worker-migration.md` (removed).

Extracted reusable knowledge from broad workers into references, created narrow
procedures for chart and model interpretation work, and reframed broad workers
as routers or fallbacks without deleting the role prompts.

Delivered:
- `skills/references/charting-artifact-reference/`
- `skills/references/model-interpretation-reference/`
- `skills/references/backend-api-patterns-reference/`
- `skills/procedures/chart-artifact-generation/`
- `skills/procedures/model-output-interpretation/`
- router/fallback updates for chart, model interpretation, backend, and ticket
  planning roles
- validator composition updates

Tickets completed: `AEGIS-MIGRATE-001` through `AEGIS-MIGRATE-010`.

### Progressive Disclosure

Original planning file: `to-do/epic-progressive-disclosure.md` (removed).

Added the closet/drawer loading discipline so procedural skills remain compact
and point to addressable reference drawers through `reference_pointers`.

Delivered:
- required `reference_pointers` procedural frontmatter
- `docs/reference-authoring-template.md`
- indexed drawer migrations for the initial references
- closet migrations for the initial procedures
- validator enforcement for closet budgets, pointer integrity, and indexed
  references

Tickets completed: `AEGIS-PD-001` through `AEGIS-PD-004`.

### Library Expansion

Original planning file: `to-do/epic-library-expansion.md` (removed).

Expanded the library with ML, quantitative finance, investment management,
frontend, cloud, language, and SQL reference knowledge, then added evidence-gated
procedural skills for confirmed failure modes.

Delivered references:
- `skills/references/ml-evaluation/`
- `skills/references/quant-backtesting/`
- `skills/references/investment-management/`
- `skills/references/frontend-accessibility/`
- `skills/references/cloud-operations/`
- `skills/references/language-idioms/`
- `skills/references/sql-dialects/`

Delivered procedures:
- `skills/procedures/training-run-diagnostics/`
- `skills/procedures/model-calibration-review/`
- `skills/procedures/backtest-validation/`
- `skills/procedures/risk-metric-reconciliation/`
- `skills/procedures/portfolio-rebalancing-review/`
- `skills/procedures/investment-thesis-evidence-check/`
- `skills/procedures/frontend-component-implementation/`
- `skills/procedures/accessibility-audit/`
- `skills/procedures/deployment-failure-triage/`
- `skills/procedures/cloud-iam-change-review/`

Tickets completed: `AEGIS-EXPAND-001` through `AEGIS-EXPAND-017`.

### Conformance Anchor

Original planning file: `to-do/epic-conformance-anchor.md` (removed).

Created the root consumer anchor that makes `reference AEGIS-CORE` a binding
instruction for external agents, then wired it into consumer entry paths.

Delivered:
- `AEGIS.md`
- canonical invocation text
- `execution/prompts/use-aegis-core.md`
- Conformance Gate guidance referenced from validator and apply-to-project paths
- consumer entry pointers from `README.md`, `AGENT_PROMPT.md`, and
  `docs/library-consumption.md`

Tickets completed: `AEGIS-ANCHOR-001` through `AEGIS-ANCHOR-003`.

### AI Coding Design Discipline

Original planning location: `to-do/agentic-coding-framework-roadmap.md`.

Added procedures and ticket context fields that reduce software entropy before
implementation by making design intent, domain language, tests, and module
boundaries explicit.

Delivered:
- `skills/procedures/design-clarification-interview/`
- `skills/procedures/ubiquitous-language-map/`
- `skills/procedures/test-first-change/`
- `skills/procedures/module-boundary-review/`
- ticket business and architecture context fields in
  `contracts/ticket-contract.md`

Tickets completed: `AEGIS-DESIGN-001` through `AEGIS-DESIGN-006`.

### Understand Anything Cross-Reference

Original planning location: operator-directed external tool integration.

Documented Lum1104/Understand-Anything as an optional external codebase mapping
tool, added a runbook, created a narrow codebase-map procedure, composed it with
existing design procedures, and defined the generated graph artifact policy.

Delivered:
- `docs/cross-references/`
- `execution/runbooks/understand-anything.md`
- `skills/procedures/codebase-map-generation/`
- optional map-evidence composition in design procedures and code-validator
- `.gitignore` policy for local graph scratch artifacts

Tickets completed: `AEGIS-UA-001` through `AEGIS-UA-005`.

## Active Planning

Active and upcoming work is kept in `to-do/`.

Currently active:
- `to-do/agentic-coding-framework-roadmap.md` for future framework backlog and
  prioritization.

No completed epic ticket files should remain in `to-do/`.
