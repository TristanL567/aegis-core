---
id: AEGIS-EXPAND-009
title: Create model-calibration-review after failure evidence is confirmed.
epic: epic-library-expansion
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/procedures/model-calibration-review/
must_not_touch:
  - skills/references/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Do not execute until operator confirms this failure mode happened.
  - Cite failure mode: accuracy or rank metrics are mistaken for probability calibration.
  - Consult `ml-evaluation`.
non_goals:
  - Do not create training diagnostics.
  - Do not create model interpretation.
acceptance_criteria:
  - Procedural frontmatter validates.
  - Verification includes calibration evidence or manual calibration review.
verification_commands:
  - Test-Path .\skills\procedures\model-calibration-review\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-EXPAND-001
---

# Body

## Goal

Create a procedure for reviewing model calibration separately from general performance.

## Context

Calibration is a situation; Bayesian or model-family knowledge remains reference material.

## Procedure

1. Confirm recent failure evidence.
2. Write procedural fields.
3. Define verification loop.

## Out of Scope

- Training run diagnostics.
- Model interpretation.

## Verification

Validator confirms the calibration boundary is disjoint.

## Failure Modes This Ticket Addresses

Treating accuracy, AUC, or rank performance as evidence that probability estimates are calibrated.
