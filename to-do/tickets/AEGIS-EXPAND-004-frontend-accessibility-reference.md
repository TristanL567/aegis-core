---
id: AEGIS-EXPAND-004
title: Create the frontend accessibility reference.
epic: epic-library-expansion
status: needs_clarification
risk: low
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/references/frontend-accessibility/
must_not_touch:
  - skills/procedures/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create a reference after reference home is confirmed.
  - Name consuming skills `frontend-component-implementation` and `accessibility-audit`.
non_goals:
  - Do not create frontend skills.
  - Do not create React or CSS skills.
acceptance_criteria:
  - Reference names scope and consumers.
  - Framework knowledge remains reference material.
verification_commands:
  - rg -n "scope|consuming skill|frontend-component-implementation|accessibility-audit" .\skills\references\frontend-accessibility
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on: []
---

# Body

## Goal

Create shared frontend accessibility knowledge for UI implementation and review procedures.

## Context

Frontend framework knowledge is Axis-2 reference material.

## Procedure

1. Confirm reference location.
2. Create reference scope and consumers.
3. Run verification.

## Out of Scope

- Skill creation.
- Design-system migration.

## Verification

Reference must name its consumers.
