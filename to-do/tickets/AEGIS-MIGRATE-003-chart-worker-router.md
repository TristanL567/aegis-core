---
id: AEGIS-MIGRATE-003
title: Update chart-worker as a thin fallback for chart procedures.
epic: epic-worker-migration
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/roles/chart-worker/SKILL.md
must_not_touch:
  - skills/procedures/
  - skills/references/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Keep chart-worker functional.
  - Reference `chart-artifact-generation` as an invoked procedure when its trigger applies.
  - Preserve role frontmatter and handoffs.
non_goals:
  - Do not delete or deprecate chart-worker.
  - Do not add new chart procedures.
acceptance_criteria:
  - Chart-worker remains a worker role.
  - Role body is thinner and points to the procedure instead of duplicating procedure content.
  - Skill library validation passes.
verification_commands:
  - rg -n "chart-artifact-generation|thin fallback|skills/procedures" .\skills\roles\chart-worker\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-MIGRATE-002
---

# Body

## Goal

Make chart-worker route applicable work to the chart procedure while remaining available as a fallback.

## Context

This validates the broad-worker migration pattern before touching heavier content workers.

## Procedure

1. Update only chart-worker reference text.
2. Preserve frontmatter and handoffs.
3. Run validation.

## Out of Scope

- Procedure creation.
- Reference creation.
- Worker deletion.

## Verification

The validator must confirm role behavior is preserved.
