---
id: AEGIS-MIGRATE-010
title: Update validator roles to compose with procedures without taxonomy expansion.
epic: epic-worker-migration
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/roles/code-validator/SKILL.md
  - skills/roles/ds-validator/SKILL.md
must_not_touch:
  - skills/procedures/
  - skills/references/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Keep validators as blocking review gates.
  - Reference existing procedures where relevant.
  - Do not add a new validator taxonomy.
non_goals:
  - Do not create `data-leakage-review` or `ml-reproducibility-review`.
  - Do not alter validator handoffs.
acceptance_criteria:
  - Code-validator and ds-validator remain validator roles.
  - Procedure references are compositional, not replacement behavior.
  - Validation passes.
verification_commands:
  - rg -n "ticket-scope-validation|clean-commit|new-api-endpoint|procedure" .\skills\roles\code-validator\SKILL.md .\skills\roles\ds-validator\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-MIGRATE-009
---

# Body

## Goal

Make validators explicitly compose with procedures while preserving validator authority.

## Context

Validators are not procedures. They consume procedure evidence and remain blocking gates.

## Procedure

1. Update validator reference text only.
2. Preserve review-only posture.
3. Run validation.

## Out of Scope

- New validators.
- New procedures.
- Tool changes.

## Verification

Validator confirms validator handoffs remain unchanged.
