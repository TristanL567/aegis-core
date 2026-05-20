---
id: AEGIS-MIGRATE-002
title: Create chart-artifact-generation as the proving procedural skill.
epic: epic-worker-migration
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/procedures/chart-artifact-generation/
must_not_touch:
  - skills/roles/
  - skills/references/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create a procedure only after the operator confirms the chart artifact failure mode was encountered.
  - Cite failure mode: AI creates chart output without reproducible artifact, data-quality note, or visual verification.
  - Declare non-coverage for visual-style conformance and chart data-quality investigation.
  - Consult `charting-artifact-reference`.
non_goals:
  - Do not edit chart-worker.
  - Do not create chart data-quality or style procedures.
acceptance_criteria:
  - Procedural frontmatter validates.
  - Trigger and non-trigger are chart artifact situations, not chart domain taxonomy.
  - Verification includes artifact existence and nonblank/manual visual review.
verification_commands:
  - Test-Path .\skills\procedures\chart-artifact-generation\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-MIGRATE-001
---

# Body

## Goal

Create the first worker-migration procedure from the thinnest broad worker.

## Context

This skill must pass the verb test, same-situation test, trigger-disjointness test, and boundary-declaration test.

## Procedure

1. Confirm the failure mode is real.
2. Write the procedure using the procedural template.
3. Declare adjacent non-coverage.
4. Run validation.

## Out of Scope

- Role edits.
- Reference edits.

## Verification

The validator must see procedural validation and a clear reference to `charting-artifact-reference`.

## Failure Modes This Ticket Addresses

AI-generated chart artifacts that are not reproducible, not visually verified, or not tied to declared data and output paths.
