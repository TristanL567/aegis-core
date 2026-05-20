---
id: AEGIS-MIGRATE-005
title: Create model-output-interpretation as an evidence-bound procedure.
epic: epic-worker-migration
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/procedures/model-output-interpretation/
must_not_touch:
  - skills/roles/
  - skills/references/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create only after the operator confirms the interpretation failure mode was encountered.
  - Cite failure mode: AI fabricates or smooths unsupported causal explanations from model output.
  - Consult `model-interpretation-reference`.
  - Exclude model training, calibration, and leakage validation.
non_goals:
  - Do not edit model-interpreter-worker.
  - Do not create ML validation procedures.
acceptance_criteria:
  - Procedural frontmatter validates.
  - Failure mode and non-coverage are explicit.
  - Verification includes evidence check and manual review of unsupported claims.
verification_commands:
  - Test-Path .\skills\procedures\model-output-interpretation\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-MIGRATE-004
---

# Body

## Goal

Create a narrow procedure for interpreting model output without unsupported narrative overreach.

## Context

The current model-interpreter-worker contains procedure-shaped content that should move into a situational skill.

## Procedure

1. Confirm failure evidence.
2. Write procedure from the template.
3. Declare excluded concerns.
4. Run validation.

## Out of Scope

- Model fitting.
- Calibration.
- Data leakage review.

## Verification

Validator confirms procedural frontmatter and evidence-bound output contract.

## Failure Modes This Ticket Addresses

AI-generated interpretations that invent causal or domain explanations not supported by the model evidence.
