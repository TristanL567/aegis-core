---
id: AEGIS-MIGRATE-001
title: Create the charting artifact reference for chart procedures.
epic: epic-worker-migration
status: needs_clarification
risk: low
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/references/charting-artifact-reference/
must_not_touch:
  - skills/roles/
  - skills/procedures/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create an Axis-2 reference for chart artifact knowledge only after the operator confirms reference home.
  - Declare scope and consuming skill `chart-artifact-generation`.
  - Keep visualization knowledge out of role prompts.
non_goals:
  - Do not create a chart procedure.
  - Do not edit chart-worker.
  - Do not add model, language, or frontend references.
acceptance_criteria:
  - The reference declares scope and consuming skill.
  - The reference is not triggerable as a skill.
  - No role prompt changes occur.
verification_commands:
  - rg -n "scope|consuming skill|chart-artifact-generation" .\skills\references\charting-artifact-reference
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on: []
---

# Body

## Goal

Create the charting artifact reference that the future chart procedure will consult.

## Context

This is the thinnest-worker proving move for Epic A. It is blocked until the operator confirms whether references live in `aegis-core`, MDCS, or both.

## Procedure

1. Confirm reference home.
2. Create the reference folder.
3. Document scope and consuming skill.
4. Run verification.

## Out of Scope

- Skill creation.
- Role migration.
- Validator tooling.

## Verification

The validator must confirm that the reference names `chart-artifact-generation` as its consumer.
