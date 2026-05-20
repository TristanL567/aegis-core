---
id: AEGIS-EXPAND-015
title: Create accessibility-audit after failure evidence is confirmed.
epic: epic-library-expansion
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/procedures/accessibility-audit/
must_not_touch:
  - skills/references/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Do not execute until operator confirms this failure mode happened.
  - Cite failure mode: visual-only UI review misses keyboard, semantic, contrast, or screen-reader checks.
  - Consult `frontend-accessibility`.
non_goals:
  - Do not create component implementation.
  - Do not create visual redesign.
acceptance_criteria:
  - Procedural frontmatter validates.
  - Verification includes manual or tool-assisted accessibility checks.
verification_commands:
  - Test-Path .\skills\procedures\accessibility-audit\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-EXPAND-004
---

# Body

## Goal

Create a procedure for accessibility audits.

## Context

Accessibility audit is a review situation, not frontend implementation.

## Procedure

1. Confirm failure evidence.
2. Write procedure fields.
3. Define manual/tool verification.

## Out of Scope

- Component implementation.
- Visual redesign.

## Verification

Validator confirms keyboard, semantics, contrast, and screen-reader checks are covered.

## Failure Modes This Ticket Addresses

Visual-only accessibility review that misses keyboard, semantic, contrast, or assistive-technology failures.
