---
id: AEGIS-SKILL-004
title: Add the procedural skill authoring template and enforce it in the validator.
epic: epic-skill-architecture
status: ready
risk: medium
allowed_areas:
  - docs/
  - tools/validate_skill_library.py
  - skills/procedures/
must_not_touch:
  - contracts/
  - execution/
  - skills/roles/
  - skills/discipline/operating-discipline.md
requirements:
  - Create docs/procedural-skill-template.md.
  - Define required procedural skill frontmatter fields: trigger, non_trigger, failure_modes_addressed, attention_signals, procedure, scope_boundary, composition_points, verification, and output_contract.
  - Extend tools/validate_skill_library.py to recognize procedural skills under skills/procedures/.
  - Hard-fail validation when a procedural skill is missing a required procedural field.
  - Prove the validator rejects a deliberately malformed procedural skill during verification.
non_goals:
  - Do not create a real procedural skill beyond temporary malformed test artifacts used for validator verification.
  - Do not change role prompt validation semantics except as needed for the new directory structure.
  - Do not alter operating discipline text.
acceptance_criteria:
  - docs/procedural-skill-template.md exists and documents every required procedural field.
  - py -3.10 .\tools\validate_skill_library.py passes with an empty or valid skills/procedures/ directory.
  - A deliberately malformed procedural skill causes tools/validate_skill_library.py to fail with a clear missing-field error.
  - Temporary malformed test artifacts are removed before final completion unless the ticket explicitly creates a durable fixture.
verification_commands:
  - Test-Path .\docs\procedural-skill-template.md
  - rg -n "trigger|non_trigger|failure_modes_addressed|attention_signals|scope_boundary|composition_points|verification|output_contract" .\docs\procedural-skill-template.md .\tools\validate_skill_library.py
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-SKILL-002
---

# Body

## Goal

Define and enforce the authoring contract for procedural skills before any real procedural skill is added.

## Context

The epic states that authoring rules without enforcement erode. This ticket introduces the procedural skill template and updates the validator in the same ticket so the new contract is not merely advisory.

## Procedure

1. Read `docs/skill-architecture.md`.
2. Create `docs/procedural-skill-template.md`.
3. Extend `tools/validate_skill_library.py` to scan `skills/procedures/` separately from `skills/roles/`.
4. Require all procedural frontmatter fields listed in this ticket.
5. Verify that the validator passes on the current library.
6. Temporarily create or simulate a malformed procedural skill and confirm the validator fails clearly.
7. Remove temporary malformed artifacts before completion if they were written into the repository.

## Out of Scope

- Creating `clean-commit` or any other real procedure.
- Editing role prompt bodies.
- Expanding validator taxonomy.

## Verification

The validator must see the template, the validator enforcement code, a passing normal validation run, and evidence that a malformed procedural skill is rejected.
