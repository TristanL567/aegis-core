---
id: AEGIS-SKILL-008
title: Add new-api-endpoint as the first situational procedural skill.
epic: epic-skill-architecture
status: ready
risk: low
allowed_areas:
  - skills/procedures/new-api-endpoint/
must_not_touch:
  - skills/roles/
  - skills/discipline/
  - skills/procedures/clean-commit/
  - skills/procedures/ticket-scope-validation/
  - tools/
  - contracts/
  - execution/
requirements:
  - Create skills/procedures/new-api-endpoint/SKILL.md following docs/procedural-skill-template.md.
  - Encode the recognized situation of adding an API surface.
  - Declare scope_boundary excluding database schema changes and auth boundary changes.
  - Declare composition_points for future database-migration and auth-boundary-change procedures.
  - Name failure modes observed in real AI coding work, including hidden auth changes, missing request validation, unverified response shapes, and route implementation without tests.
  - Include verification guidance through relevant test execution and endpoint contract checks.
non_goals:
  - Do not create database-migration or auth-boundary-change procedures.
  - Do not edit backend-worker.
  - Do not add API implementation code.
  - Do not update validation tooling.
acceptance_criteria:
  - skills/procedures/new-api-endpoint/SKILL.md exists and passes procedural validation.
  - The skill explicitly excludes database schema and auth boundary work.
  - The skill names adjacent procedures for excluded concerns.
  - Failure modes are concrete and tied to observed AI coding errors.
  - Verification includes test execution and request/response contract checks.
verification_commands:
  - Test-Path .\skills\procedures\new-api-endpoint\SKILL.md
  - rg -n "database-migration|auth-boundary-change|request validation|response|test" .\skills\procedures\new-api-endpoint\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-SKILL-005
  - AEGIS-SKILL-007
---

# Body

## Goal

Add `new-api-endpoint` as the first situational procedural skill, proving that procedure skills can be narrow, triggerable, and composable.

## Context

After clean-commit and ticket-scope-validation establish reference shapes, this ticket adds a real implementation-situation procedure. It must avoid becoming a broad backend skill.

## Procedure

1. Read `docs/procedural-skill-template.md`.
2. Read the existing `backend-worker` role only to avoid duplicating broad role guidance.
3. Create `skills/procedures/new-api-endpoint/SKILL.md`.
4. Fill every procedural field with API-surface-specific content.
5. Explicitly exclude database migration and auth boundary concerns.
6. Add verification guidance for tests and API contract checks.
7. Run the verification commands.

## Out of Scope

- Database schema changes.
- Auth policy or permission boundary changes.
- Backend role migration.
- Real API implementation work.

## Verification

The validator must see a valid procedural skill, explicit scope boundaries, named adjacent procedures, concrete failure modes, and passing skill library validation.

## Failure Modes This Ticket Addresses

- API changes that silently include database schema work.
- API changes that silently alter auth or permission boundaries.
- Missing input validation at the request boundary.
- Endpoint implementations without test or contract verification.
- Response shapes that are not documented or checked.
