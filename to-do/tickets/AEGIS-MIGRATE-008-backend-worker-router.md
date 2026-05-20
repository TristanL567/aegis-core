---
id: AEGIS-MIGRATE-008
title: Update backend-worker as a router to endpoint procedures.
epic: epic-worker-migration
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/roles/backend-worker/SKILL.md
must_not_touch:
  - skills/procedures/
  - skills/references/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Reference existing `new-api-endpoint` when endpoint triggers apply.
  - Reference backend API patterns reference.
  - Preserve backend-worker as a broad implementation router, not a deprecated role.
non_goals:
  - Do not create database-migration or auth-boundary-change.
  - Do not delete backend-worker.
acceptance_criteria:
  - Backend-worker references `new-api-endpoint`.
  - Role frontmatter and handoffs are unchanged.
  - Validation passes.
verification_commands:
  - rg -n "new-api-endpoint|router|skills/procedures" .\skills\roles\backend-worker\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-MIGRATE-007
---

# Body

## Goal

Make backend-worker a router for endpoint-specific procedure use.

## Context

Backend-worker remains necessary, but endpoint work already has a narrower procedure.

## Procedure

1. Add reference text only.
2. Preserve role behavior.
3. Run validation.

## Out of Scope

- New backend procedures.
- Backend role deletion.

## Verification

Validator confirms role handoffs remain unchanged.
