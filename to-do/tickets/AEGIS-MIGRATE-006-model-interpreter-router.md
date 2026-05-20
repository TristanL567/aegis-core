---
id: AEGIS-MIGRATE-006
title: Update model-interpreter-worker as a thin fallback.
epic: epic-worker-migration
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/roles/model-interpreter-worker/SKILL.md
must_not_touch:
  - skills/procedures/
  - skills/references/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Reference `model-output-interpretation` when its trigger applies.
  - Preserve role frontmatter, handoffs, and validator routing.
non_goals:
  - Do not delete or deprecate model-interpreter-worker.
  - Do not create new procedures.
acceptance_criteria:
  - Model-interpreter-worker remains functional.
  - Role body points to procedure without duplicating it.
  - Validation passes.
verification_commands:
  - rg -n "model-output-interpretation|thin fallback|skills/procedures" .\skills\roles\model-interpreter-worker\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-MIGRATE-005
---

# Body

## Goal

Make model-interpreter-worker a fallback/router for interpretation procedures.

## Context

This keeps the role layer thin while preserving the role for broad or ambiguous interpretation work.

## Procedure

1. Update only model-interpreter-worker reference text.
2. Preserve role behavior.
3. Run validation.

## Out of Scope

- New skills.
- Reference edits.
- Role deletion.

## Verification

The validator confirms role behavior and handoffs are preserved.
