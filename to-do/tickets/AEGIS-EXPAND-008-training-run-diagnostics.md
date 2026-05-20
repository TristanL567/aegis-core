---
id: AEGIS-EXPAND-008
title: Create training-run-diagnostics after failure evidence is confirmed.
epic: epic-library-expansion
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/procedures/training-run-diagnostics/
must_not_touch:
  - skills/references/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Do not execute until operator confirms this failure mode happened.
  - Cite failure mode: model code is changed before data, metrics, config, and run evidence are diagnosed.
  - Consult `ml-evaluation`.
non_goals:
  - Do not create hyperparameter-tuning.
  - Do not create model-family guidance.
acceptance_criteria:
  - Procedural frontmatter validates.
  - Failure mode and verification loop are explicit.
verification_commands:
  - Test-Path .\skills\procedures\training-run-diagnostics\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-EXPAND-001
---

# Body

## Goal

Create a procedure for diagnosing suspicious ML training runs before changing model code.

## Context

This is blocked until the operator confirms a recent real failure.

## Procedure

1. Record the confirmed failure example.
2. Write the procedure from the template.
3. Add verification expectations.

## Out of Scope

- Hyperparameter tuning.
- Model-family references.

## Verification

Validator confirms procedural validation and evidence-gate compliance.

## Failure Modes This Ticket Addresses

Changing model code before diagnosing data, metric, configuration, or run-state evidence.
