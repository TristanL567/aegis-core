---
id: AEGIS-EXPAND-011
title: Create risk-metric-reconciliation after failure evidence is confirmed.
epic: epic-library-expansion
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/procedures/risk-metric-reconciliation/
must_not_touch:
  - skills/references/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Do not execute until operator confirms this failure mode happened.
  - Cite failure mode: risk numbers are compared without matching definitions, frequency, or units.
  - Consult `quant-backtesting` and `investment-management`.
non_goals:
  - Do not create full backtest validation.
  - Do not create portfolio construction.
acceptance_criteria:
  - Procedural frontmatter validates.
  - Verification includes metric definition and frequency checks.
verification_commands:
  - Test-Path .\skills\procedures\risk-metric-reconciliation\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-EXPAND-002
  - AEGIS-EXPAND-003
---

# Body

## Goal

Create a procedure for reconciling financial risk metrics.

## Context

This skill is disjoint from validating an entire backtest.

## Procedure

1. Confirm failure evidence.
2. Define metric reconciliation procedure.
3. Define verification loop.

## Out of Scope

- Backtest validation.
- Portfolio rebalancing.

## Verification

Validator confirms the metric checks are explicit.

## Failure Modes This Ticket Addresses

Comparing or trusting risk metrics with mismatched definitions, frequencies, units, or data windows.
