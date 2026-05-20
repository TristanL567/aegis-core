---
id: AEGIS-EXPAND-002
title: Create the quantitative backtesting reference.
epic: epic-library-expansion
status: needs_clarification
risk: low
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/references/quant-backtesting/
must_not_touch:
  - skills/procedures/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create a reference after reference home is confirmed.
  - Name consuming skills `backtest-validation` and `risk-metric-reconciliation`.
non_goals:
  - Do not create quant procedures.
  - Do not create stochastic-volatility or option-pricing skills.
acceptance_criteria:
  - Reference names scope and consumers.
  - Model families are treated as reference knowledge only.
verification_commands:
  - rg -n "scope|consuming skill|backtest-validation|risk-metric-reconciliation" .\skills\references\quant-backtesting
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on: []
---

# Body

## Goal

Create shared quantitative backtesting knowledge for quant workflow procedures.

## Context

Backtesting is a situation when validating a backtest; quantitative finance knowledge is a reference.

## Procedure

1. Confirm reference location.
2. Create scope and consumer declaration.
3. Run verification.

## Out of Scope

- Skill creation.
- Strategy implementation.

## Verification

Reference must be consumed by named skills.
