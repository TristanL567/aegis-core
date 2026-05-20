---
id: AEGIS-MIGRATE-004
title: Create the model interpretation reference.
epic: epic-worker-migration
status: needs_clarification
risk: low
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/references/model-interpretation-reference/
must_not_touch:
  - skills/roles/
  - skills/procedures/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create Axis-2 reference knowledge for model interpretation only after reference home is confirmed.
  - Name consuming skill `model-output-interpretation`.
non_goals:
  - Do not create interpretation procedure.
  - Do not edit model-interpreter-worker.
acceptance_criteria:
  - Reference declares scope and consuming skill.
  - Reference does not define triggers or procedure behavior.
verification_commands:
  - rg -n "scope|consuming skill|model-output-interpretation" .\skills\references\model-interpretation-reference
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-MIGRATE-003
---

# Body

## Goal

Create the knowledge reference used by model interpretation procedures.

## Context

Knowledge about uncertainty, feature effects, and causal caution belongs in references, not skills.

## Procedure

1. Confirm reference home.
2. Add reference scope and consumer.
3. Run verification.

## Out of Scope

- Skill creation.
- Role edits.

## Verification

The validator must confirm the reference has a consumer.
