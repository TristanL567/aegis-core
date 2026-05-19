---
id: AEGIS-SKILL-005
title: Add clean-commit as the first reference procedural skill.
epic: epic-skill-architecture
status: ready
risk: low
allowed_areas:
  - skills/procedures/clean-commit/
must_not_touch:
  - skills/roles/
  - skills/discipline/
  - docs/
  - contracts/
  - tools/
  - execution/
requirements:
  - Create skills/procedures/clean-commit/SKILL.md.
  - Follow docs/procedural-skill-template.md exactly.
  - Make trigger and non_trigger concrete and testable.
  - Name real failure modes around dirty worktrees, unrelated staged files, missing ticket IDs, weak commit messages, and missing validation evidence.
  - Include a verification loop using git diff --stat and the ticket envelope, with the scope-check script named as pending if validate_ticket_scope.py does not yet exist.
non_goals:
  - Do not implement validate_ticket_scope.py.
  - Do not edit clean-commit execution runbooks or prompts.
  - Do not change role prompts.
  - Do not perform a commit as part of the skill file creation.
acceptance_criteria:
  - skills/procedures/clean-commit/SKILL.md exists.
  - The procedure passes tools/validate_skill_library.py.
  - trigger and non_trigger are concrete enough for a validator to test.
  - verification names at least one mechanically-checkable git command.
  - The skill explicitly states what it does not cover and which adjacent procedures handle those concerns.
verification_commands:
  - Test-Path .\skills\procedures\clean-commit\SKILL.md
  - rg -n "trigger|non_trigger|failure_modes_addressed|attention_signals|scope_boundary|composition_points|verification|output_contract" .\skills\procedures\clean-commit\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-SKILL-004
---

# Body

## Goal

Add `clean-commit` as the first procedural skill because it is narrow, frequent, and easy to verify mechanically.

## Context

The epic recommends starting with the cheapest verifiable skill instead of the most ambitious one. `clean-commit` proves the procedural skill shape and exercises the meta-control pattern before the procedure library grows.

## Procedure

1. Read `docs/procedural-skill-template.md`.
2. Create `skills/procedures/clean-commit/SKILL.md`.
3. Fill every required procedural frontmatter field.
4. Include a compact body that checks ticket ID, staged files, commit message, validation evidence, and human-readable summary.
5. Make the missing `validate_ticket_scope.py` dependency explicit as a pending verification primitive when referenced.
6. Run the verification commands.

## Out of Scope

- Adding scope firewall tooling.
- Editing completion report templates.
- Changing any role prompt.
- Performing repository commits.

## Verification

The validator must see a valid procedural skill file, concrete trigger boundaries, named failure modes, scope and composition declarations, and a passing skill library validator run.

## Failure Modes This Ticket Addresses

- Commits that mix ticket-owned changes with unrelated dirty worktree files.
- Commit messages that omit ticket ID, goal, acceptance criteria, or validation evidence.
- Staged generated artifacts that were not listed in the ticket allowed areas.
- Completion claims made before validator approval or without evidence.
