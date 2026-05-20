---
id: AEGIS-MIGRATE-007
title: Create backend API patterns reference for endpoint procedures.
epic: epic-worker-migration
status: needs_clarification
risk: low
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/references/backend-api-patterns-reference/
must_not_touch:
  - skills/roles/
  - skills/procedures/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create Axis-2 backend API knowledge reference after reference home is confirmed.
  - Name consuming skill `new-api-endpoint`.
non_goals:
  - Do not create backend procedures.
  - Do not edit backend-worker.
acceptance_criteria:
  - Reference declares scope and consumer.
  - Reference contains no procedure trigger.
verification_commands:
  - rg -n "scope|consuming skill|new-api-endpoint" .\skills\references\backend-api-patterns-reference
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-MIGRATE-006
---

# Body

## Goal

Create backend API knowledge as a reference consumed by endpoint work.

## Context

Backend API patterns are knowledge, while adding an endpoint is a situation.

## Procedure

1. Confirm reference home.
2. Create reference and consumer declaration.
3. Run validation.

## Out of Scope

- Backend-worker edits.
- Procedure creation.

## Verification

Reference must name `new-api-endpoint` as a consumer.
