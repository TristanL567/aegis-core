---
id: AEGIS-EXPAND-017
title: Create cloud-iam-change-review after failure evidence is confirmed.
epic: epic-library-expansion
status: needs_clarification
risk: medium
doctrine:
  - docs/skill-architecture.md
  - docs/procedural-skill-template.md
allowed_areas:
  - skills/procedures/cloud-iam-change-review/
must_not_touch:
  - skills/references/
  - skills/roles/
  - skills/discipline/
  - tools/
  - contracts/
  - execution/
requirements:
  - Do not execute until operator confirms this failure mode happened.
  - Cite failure mode: AI grants over-broad permissions or misses trust-boundary impact.
  - Consult `cloud-operations`.
non_goals:
  - Do not create deployment triage.
  - Do not create cloud provider reference content.
acceptance_criteria:
  - Procedural frontmatter validates.
  - Verification includes least privilege, trust boundary, and rollback/manual review.
verification_commands:
  - Test-Path .\skills\procedures\cloud-iam-change-review\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-EXPAND-005
---

# Body

## Goal

Create a procedure for reviewing cloud IAM and access-policy changes.

## Context

IAM review is a situation; cloud provider syntax is reference material.

## Procedure

1. Confirm failure evidence.
2. Write procedure fields.
3. Define verification loop.

## Out of Scope

- Deployment failure triage.
- Cost optimization.

## Verification

Validator confirms least-privilege and trust-boundary checks are included.

## Failure Modes This Ticket Addresses

Over-broad cloud permissions, missing trust-boundary review, or unreviewed access-policy side effects.
