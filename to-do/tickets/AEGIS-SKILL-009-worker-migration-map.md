---
id: AEGIS-SKILL-009
title: Produce the broad worker migration map after reference procedures exist.
epic: epic-skill-architecture
status: ready
risk: low
allowed_areas:
  - docs/
must_not_touch:
  - skills/roles/*-worker/SKILL.md
  - skills/roles/*/SKILL.md
  - skills/procedures/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create docs/broad-worker-migration.md.
  - Map every existing broad worker and validator role to one of: retain as thin router, retain as fallback, deprecate in favor of procedures, or keep as validator.
  - Include backend-worker, chart-worker, model-interpreter-worker, ds-validator, code-validator, ticket-planner-worker, and master.
  - For each role, name candidate procedures that would cover its work or justify retention.
  - Make no changes to worker or validator prompt bodies.
non_goals:
  - Do not edit, remove, rename, or deprecate any role prompt in this ticket.
  - Do not create new procedures.
  - Do not change validator tooling.
  - Do not add a new role taxonomy.
acceptance_criteria:
  - docs/broad-worker-migration.md exists.
  - Every existing role prompt has a documented disposition and rationale.
  - The document distinguishes role migration from procedural skill creation.
  - The plan preserves existing broad workers until procedural coverage exists.
verification_commands:
  - Test-Path .\docs\broad-worker-migration.md
  - rg -n "backend-worker|chart-worker|model-interpreter-worker|ds-validator|code-validator|ticket-planner-worker|master" .\docs\broad-worker-migration.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-SKILL-008
---

# Body

## Goal

Produce a migration map for broad existing workers and validators without changing any role prompt.

## Context

The epic forbids deleting broad workers before procedural coverage exists. This ticket reassesses the current role library only after the first procedural and meta-control reference shapes are present.

## Procedure

1. Read `docs/skill-architecture.md`.
2. Inspect the role prompt directory under `skills/roles/`.
3. Create `docs/broad-worker-migration.md`.
4. For every existing role, document a disposition and rationale.
5. Name candidate future procedures where useful, but do not create them.
6. Run the verification commands.

## Out of Scope

- Editing role prompts.
- Creating procedures.
- Adding validators.
- Renaming or deleting workers.

## Verification

The validator must see the migration map, confirm every existing role is covered, and confirm no role prompt body changed.
