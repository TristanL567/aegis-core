---
id: AEGIS-EXPAND-005
title: Create the cloud operations reference.
epic: epic-library-expansion
status: needs_clarification
risk: low
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/references/cloud-operations/
must_not_touch:
  - skills/procedures/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create a reference after reference home is confirmed.
  - Name consuming skills `deployment-failure-triage` and `cloud-iam-change-review`.
non_goals:
  - Do not create cloud skills.
  - Do not create provider-specific runtime docs.
acceptance_criteria:
  - Reference names scope and consumers.
  - Provider knowledge is reference material only.
verification_commands:
  - rg -n "scope|consuming skill|deployment-failure-triage|cloud-iam-change-review" .\skills\references\cloud-operations
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on: []
---

# Body

## Goal

Create cloud operations reference knowledge for deployment and IAM procedures.

## Context

Cloud provider knowledge is not a skill; deployment triage and IAM review are situations.

## Procedure

1. Confirm reference location.
2. Create scope and consumer declaration.
3. Run verification.

## Out of Scope

- Provider-specific runtime changes.
- Skill creation.

## Verification

Reference must name consuming skills.
