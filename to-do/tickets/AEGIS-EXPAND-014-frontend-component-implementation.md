---
id: AEGIS-EXPAND-014
title: Create frontend-component-implementation after failure evidence is confirmed.
epic: epic-library-expansion
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/procedures/frontend-component-implementation/
must_not_touch:
  - skills/references/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Do not execute until operator confirms this failure mode happened.
  - Cite failure mode: component work expands into broad page architecture or inconsistent UI controls.
  - Consult `frontend-accessibility` and `language-idioms`.
non_goals:
  - Do not create accessibility-audit content.
  - Do not create React or TypeScript skills.
acceptance_criteria:
  - Procedural frontmatter validates.
  - Verification includes UI behavior and layout/manual review.
verification_commands:
  - Test-Path .\skills\procedures\frontend-component-implementation\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-EXPAND-004
  - AEGIS-EXPAND-006
---

# Body

## Goal

Create a narrow frontend component implementation procedure.

## Context

This must not become a frontend domain skill or a framework skill.

## Procedure

1. Confirm failure evidence.
2. Write procedure fields.
3. Define verification.

## Out of Scope

- Accessibility audit.
- Design-system migration.

## Verification

Validator confirms disjointness from accessibility audit.

## Failure Modes This Ticket Addresses

Small component requests expanding into broad page structure, inconsistent controls, or unverified UI behavior.
