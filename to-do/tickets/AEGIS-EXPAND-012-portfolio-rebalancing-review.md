---
id: AEGIS-EXPAND-012
title: Create portfolio-rebalancing-review after failure evidence is confirmed.
epic: epic-library-expansion
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/procedures/portfolio-rebalancing-review/
must_not_touch:
  - skills/references/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Do not execute until operator confirms this failure mode happened.
  - Cite failure mode: rebalance suggestions ignore constraints, turnover, tax, mandate, or liquidity limits.
  - Consult `investment-management`.
non_goals:
  - Do not create broad portfolio construction.
  - Do not create trade execution guidance.
acceptance_criteria:
  - Procedural frontmatter validates.
  - Verification includes constraints and tradeoff review.
verification_commands:
  - Test-Path .\skills\procedures\portfolio-rebalancing-review\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-EXPAND-003
---

# Body

## Goal

Create a procedure for reviewing proposed portfolio rebalances.

## Context

Rebalancing is a situation, while investment management theory is reference material.

## Procedure

1. Confirm failure evidence.
2. Write the procedure.
3. Add verification expectations.

## Out of Scope

- Trade execution.
- Broad portfolio construction.

## Verification

Validator confirms constraint and risk checks.

## Failure Modes This Ticket Addresses

Portfolio rebalance recommendations that ignore constraints, turnover, tax, liquidity, or mandate limits.
