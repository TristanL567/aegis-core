---
id: AEGIS-MIGRATE-009
title: Reframe ticket-planner-worker as a router while deferring planning procedures.
epic: epic-worker-migration
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/roles/ticket-planner-worker/SKILL.md
must_not_touch:
  - skills/procedures/
  - skills/references/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Preserve ticket-planner-worker.
  - State that future planning procedures require observed failure-mode evidence.
  - Do not create `ticket-backlog-decomposition` or `ticket-contract-authoring`.
non_goals:
  - Do not modify ticket contract.
  - Do not add planning procedures.
acceptance_criteria:
  - Ticket-planner-worker remains a worker role.
  - Future planning procedures are named as deferred, not created.
  - Validation passes.
verification_commands:
  - rg -n "deferred|ticket-backlog-decomposition|ticket-contract-authoring" .\skills\roles\ticket-planner-worker\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-MIGRATE-008
---

# Body

## Goal

Keep ticket-planner-worker as a planning role while making future procedure extraction evidence-gated.

## Context

Ticket planning is useful, but no specific planning failure mode was confirmed in this planning run.

## Procedure

1. Add a concise deferred-procedure note.
2. Preserve all role behavior.
3. Run validation.

## Out of Scope

- Planning skill creation.
- Ticket contract changes.

## Verification

Validator confirms no procedure files were created.
