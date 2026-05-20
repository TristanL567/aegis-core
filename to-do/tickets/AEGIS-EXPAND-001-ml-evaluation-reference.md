---
id: AEGIS-EXPAND-001
title: Create the ML evaluation reference.
epic: epic-library-expansion
status: needs_clarification
risk: low
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/references/ml-evaluation/
must_not_touch:
  - skills/procedures/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create a reference only after reference home is confirmed.
  - Name consuming skills `training-run-diagnostics` and `model-calibration-review`.
non_goals:
  - Do not create ML skills.
  - Do not add model-family skills.
acceptance_criteria:
  - Reference names scope and consuming skills.
  - Reference contains no trigger logic.
verification_commands:
  - rg -n "scope|consuming skill|training-run-diagnostics|model-calibration-review" .\skills\references\ml-evaluation
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on: []
---

# Body

## Goal

Create shared ML evaluation knowledge for ML procedural skills.

## Context

ML evaluation knowledge is Axis-2 reference material, not a skill.

## Procedure

1. Confirm reference location.
2. Create reference scope and consumers.
3. Run verification.

## Out of Scope

- Skill creation.
- Validator changes.

## Verification

Reference must name at least one consuming skill.
