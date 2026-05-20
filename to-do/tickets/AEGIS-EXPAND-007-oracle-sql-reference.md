---
id: AEGIS-EXPAND-007
title: Create or route the Oracle SQL reference.
epic: epic-library-expansion
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/references/oracle-sql/
must_not_touch:
  - skills/procedures/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Ask the operator whether Oracle SQL reference material belongs in `aegis-core`, MDCS, or both.
  - Name consuming skill `backtest-validation` and future `database-migration`.
non_goals:
  - Do not create SQL skills.
  - Do not add project-private database details.
acceptance_criteria:
  - Reference location decision is recorded.
  - Reference names consumers if stored in this repo.
verification_commands:
  - rg -n "scope|consuming skill|Oracle SQL|backtest-validation|database-migration" .\skills\references\oracle-sql
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on: []
---

# Body

## Goal

Decide and create the Oracle SQL reference location without turning SQL into a skill.

## Context

Shared references may belong in `aegis-core`, MDCS, or both. This is an explicit operator question.

## Procedure

1. Get the reference-location decision.
2. Create only the approved reference home.
3. Name consumers.
4. Run verification.

## Out of Scope

- SQL skills.
- Private schema or credential content.

## Verification

Validator confirms the reference has consumers or that the external location decision is documented.
