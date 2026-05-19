---
id: AEGIS-SKILL-007
title: Add ticket-scope-validation as the first meta-control procedure and scope firewall tool.
epic: epic-skill-architecture
status: ready
risk: medium
allowed_areas:
  - skills/procedures/ticket-scope-validation/
  - tools/validate_ticket_scope.py
  - skills/roles/code-validator/SKILL.md
must_not_touch:
  - contracts/
  - execution/
  - skills/discipline/
  - skills/procedures/clean-commit/
  - prompt_templates/
requirements:
  - Create skills/procedures/ticket-scope-validation/SKILL.md following the procedural template.
  - Add tools/validate_ticket_scope.py to check staged or changed files against a ticket envelope's allowed_areas and must_not_touch.
  - Define a small, documented CLI for validate_ticket_scope.py.
  - Update code-validator to invoke ticket-scope-validation instead of restating the scope check inline.
  - Provide accept and reject verification examples for the scope firewall.
non_goals:
  - Do not implement a full ticket ledger.
  - Do not alter clean-commit procedure content.
  - Do not add provider-specific behavior.
  - Do not change unrelated validator review criteria.
acceptance_criteria:
  - skills/procedures/ticket-scope-validation/SKILL.md exists and passes procedural validation.
  - tools/validate_ticket_scope.py accepts a valid ticket envelope and matching changed-file list.
  - tools/validate_ticket_scope.py rejects files outside allowed_areas and files under must_not_touch.
  - code-validator references the ticket-scope-validation procedure instead of duplicating its full scope logic.
  - py -3.10 .\tools\validate_skill_library.py passes.
verification_commands:
  - Test-Path .\skills\procedures\ticket-scope-validation\SKILL.md
  - Test-Path .\tools\validate_ticket_scope.py
  - py -3.10 .\tools\validate_skill_library.py
  - py -3.10 .\tools\validate_ticket_scope.py --ticket .\to-do\tickets\AEGIS-SKILL-007-ticket-scope-validation.md --changed-file tools/validate_ticket_scope.py
  - py -3.10 .\tools\validate_ticket_scope.py --ticket .\to-do\tickets\AEGIS-SKILL-007-ticket-scope-validation.md --changed-file prompt_templates/custom_instructions.md
completion_report_required: true
depends_on:
  - AEGIS-SKILL-005
  - AEGIS-SKILL-004
---

# Body

## Goal

Add a meta-control procedure and deterministic scope firewall so ticket boundaries can be checked by execution rather than only by model judgment.

## Context

The epic requires verification loops wherever output can be checked. Scope validation is a high-value loop because every ticket declares `allowed_areas` and `must_not_touch`.

## Procedure

1. Read `docs/procedural-skill-template.md` and `skills/procedures/clean-commit/SKILL.md`.
2. Create `skills/procedures/ticket-scope-validation/SKILL.md`.
3. Implement `tools/validate_ticket_scope.py` with a documented CLI that can check a ticket envelope against supplied changed files and, if feasible, staged files.
4. Add accept and reject checks to the completion report evidence.
5. Update `skills/roles/code-validator/SKILL.md` so it invokes the procedure and tool instead of restating scope rules inline.
6. Run the verification commands.

## Out of Scope

- Creating a ticket ledger.
- Changing the clean-commit procedure.
- Rewriting validator architecture.
- Touching provider-specific files.

## Verification

The validator must see a valid meta-control procedure, a runnable scope firewall script, one passing scope example, one failing scope example, and an updated code-validator prompt that composes with the procedure.

## Failure Modes This Ticket Addresses

- Workers modifying files outside `allowed_areas`.
- Workers touching `must_not_touch` paths.
- Validators relying only on prose review for scope checks.
- Completion reports claiming ticket scope compliance without executable evidence.
