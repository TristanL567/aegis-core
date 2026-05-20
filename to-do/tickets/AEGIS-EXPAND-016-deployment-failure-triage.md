---
id: AEGIS-EXPAND-016
title: Create deployment-failure-triage after failure evidence is confirmed.
epic: epic-library-expansion
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/procedures/deployment-failure-triage/
must_not_touch:
  - skills/references/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Do not execute until operator confirms this failure mode happened.
  - Cite failure mode: AI changes deployment config before reading logs, rollout state, and recent deltas.
  - Consult `cloud-operations`.
non_goals:
  - Do not create IAM review.
  - Do not add provider-specific runtime files.
acceptance_criteria:
  - Procedural frontmatter validates.
  - Verification includes logs, rollout status, recent-change review, and manual confirmation.
verification_commands:
  - Test-Path .\skills\procedures\deployment-failure-triage\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-EXPAND-005
---

# Body

## Goal

Create a procedure for deployment failure triage.

## Context

Provider knowledge belongs in references; triage is the operator situation.

## Procedure

1. Confirm failure evidence.
2. Write procedure fields.
3. Define verification loop.

## Out of Scope

- IAM policy changes.
- Provider-specific runtime docs.

## Verification

Validator confirms logs, rollout state, and recent deltas are checked before config changes.

## Failure Modes This Ticket Addresses

Changing deployment configuration before inspecting logs, rollout state, health checks, and recent deltas.
