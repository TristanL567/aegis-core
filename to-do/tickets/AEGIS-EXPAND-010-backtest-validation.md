---
id: AEGIS-EXPAND-010
title: Create backtest-validation after failure evidence is confirmed.
epic: epic-library-expansion
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/procedures/backtest-validation/
must_not_touch:
  - skills/references/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Do not execute until operator confirms this failure mode happened.
  - Cite failure mode: AI accepts backtest results despite leakage, bad costs, or timing errors.
  - Consult `quant-backtesting` and optionally `oracle-sql`.
non_goals:
  - Do not create signal-generation.
  - Do not create stochastic-volatility skill.
acceptance_criteria:
  - Procedural frontmatter validates.
  - Verification checks timing, leakage, costs, and result evidence.
verification_commands:
  - Test-Path .\skills\procedures\backtest-validation\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-EXPAND-002
---

# Body

## Goal

Create a procedure for validating strategy backtests.

## Context

Backtest validation is a situation; option pricing and stochastic volatility are references.

## Procedure

1. Confirm failure evidence.
2. Write procedural fields.
3. Define manual or deterministic checks.

## Out of Scope

- Signal design.
- Portfolio allocation.

## Verification

Validator confirms timing, leakage, costs, and evidence checks are present.

## Failure Modes This Ticket Addresses

Accepting backtest results without validating leakage, transaction costs, timing, or data assumptions.
