---
id: AEGIS-EXPAND-006
title: Create the language idioms reference.
epic: epic-library-expansion
status: needs_clarification
risk: low
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/references/language-idioms/
must_not_touch:
  - skills/procedures/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create a reference after operator confirms whether language references should be shared or split by language.
  - Name consuming skills `new-api-endpoint` and `frontend-component-implementation`.
non_goals:
  - Do not create Python, TypeScript, SQL, or language skills.
acceptance_criteria:
  - Reference names scope and consumers.
  - The document states languages are references only.
verification_commands:
  - rg -n "scope|consuming skill|new-api-endpoint|frontend-component-implementation|languages are references" .\skills\references\language-idioms
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on: []
---

# Body

## Goal

Create language idiom knowledge as reference material, not procedural skills.

## Context

The two-axis rule rejects language-shaped skills on sight.

## Procedure

1. Confirm shared versus per-language reference layout.
2. Create scope and consumers.
3. Run verification.

## Out of Scope

- Language-specific skills.
- Tooling changes.

## Verification

Reference must name consuming skills.
