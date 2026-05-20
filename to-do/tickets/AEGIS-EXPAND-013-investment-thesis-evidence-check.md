---
id: AEGIS-EXPAND-013
title: Create investment-thesis-evidence-check after failure evidence is confirmed.
epic: epic-library-expansion
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/procedures/investment-thesis-evidence-check/
must_not_touch:
  - skills/references/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Do not execute until operator confirms this failure mode happened.
  - Cite failure mode: investment narrative makes unsupported claims or omits risk evidence.
  - Consult `investment-management`.
non_goals:
  - Do not create portfolio construction.
  - Do not create trade recommendation automation.
acceptance_criteria:
  - Procedural frontmatter validates.
  - Verification includes evidence-to-claim and risk review.
verification_commands:
  - Test-Path .\skills\procedures\investment-thesis-evidence-check\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-EXPAND-003
---

# Body

## Goal

Create a procedure for checking investment thesis evidence and risk coverage.

## Context

The thesis check is a review situation, not a domain skill.

## Procedure

1. Confirm failure evidence.
2. Write procedural fields.
3. Define manual evidence verification.

## Out of Scope

- Portfolio construction.
- Trade execution.

## Verification

Validator confirms evidence and risk checks.

## Failure Modes This Ticket Addresses

Unsupported investment narratives that overstate evidence, omit contrary evidence, or hide risk.
