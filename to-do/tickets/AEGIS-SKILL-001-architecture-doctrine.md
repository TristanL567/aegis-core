---
id: AEGIS-SKILL-001
title: Add the architecture doctrine document for the three-layer skill model.
epic: epic-skill-architecture
status: ready
risk: low
allowed_areas:
  - docs/
  - to-do/
must_not_touch:
  - skills/
  - contracts/
  - tools/
requirements:
  - Create docs/skill-architecture.md as the canonical doctrine for this epic.
  - Name and define the three layers: orchestration roles, operating discipline, and procedural skills.
  - Include the existence gate, composition rule, verification rule, attention rule, proliferation constraint, and enforcement rule.
  - Reference to-do/epic-skill-architecture.md as the source planning artifact.
non_goals:
  - Do not move, rename, or edit any existing skill or role prompt.
  - Do not create procedural skills.
  - Do not change validator behavior.
  - Do not edit contracts.
acceptance_criteria:
  - docs/skill-architecture.md exists.
  - Every layer is named and given a purpose, repository location, coverage boundary, and relationship to the other layers.
  - Every doctrinal constraint is named and given one-sentence rationale.
  - The document states that broad domain skillsets are not procedural skills.
verification_commands:
  - Test-Path .\docs\skill-architecture.md
  - rg -n "orchestration roles|operating discipline|procedural skills|existence gate|composition rule|verification rule|attention rule|proliferation constraint|enforcement rule" .\docs\skill-architecture.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on: []
---

# Body

## Goal

Create the doctrine document that defines the three-layer AEGIS skill architecture and prevents future drift back into broad role-shaped skillsets.

## Context

This ticket implements the first success condition from `to-do/epic-skill-architecture.md`: the repository must explicitly distinguish roles, operating discipline, and procedural skills before any migration work begins.

## Procedure

1. Read `to-do/epic-skill-architecture.md`.
2. Create `docs/skill-architecture.md`.
3. Define the three layers and their repository locations after migration.
4. Add the six doctrinal constraints with one-sentence rationales.
5. State that role prompts are not procedural skills and that domain taxonomies are not valid skill cuts.
6. Run the verification commands.

## Out of Scope

- Moving files.
- Editing existing role prompts.
- Adding procedural skill files.
- Changing validation tooling.

## Verification

The validator must see the new doctrine file, confirm the required layer and constraint names are present, and confirm the existing skill library validator still passes.
