---
id: AEGIS-EXPAND-003
title: Create the investment management reference.
epic: epic-library-expansion
status: needs_clarification
risk: low
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/references/investment-management/
must_not_touch:
  - skills/procedures/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create a reference after reference home is confirmed.
  - Name consuming skills `portfolio-rebalancing-review` and `investment-thesis-evidence-check`.
non_goals:
  - Do not create investment skills.
  - Do not create portfolio-construction as a broad skill.
acceptance_criteria:
  - Reference names scope and consumers.
  - Reference does not encode procedural triggers.
verification_commands:
  - rg -n "scope|consuming skill|portfolio-rebalancing-review|investment-thesis-evidence-check" .\skills\references\investment-management
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on: []
---

# Body

## Goal

Create shared investment-management knowledge for portfolio and thesis review procedures.

## Context

Investment management is knowledge; reviewing a rebalance or thesis is a situation.

## Procedure

1. Confirm reference location.
2. Create scope and consumer declaration.
3. Run verification.

## Out of Scope

- Skill creation.
- Trading execution guidance.

## Verification

Reference must name its consumers.
