---
id: AEGIS-SKILL-006
title: Extend completion reports with a human_readability evidence block.
epic: epic-skill-architecture
status: ready
risk: low
allowed_areas:
  - execution/templates/
  - contracts/ticket-contract.md
  - skills/roles/code-validator/SKILL.md
must_not_touch:
  - skills/procedures/
  - skills/discipline/
  - tools/
  - prompt_templates/
  - sandbox/
requirements:
  - Update execution/templates/completion-report.example.yaml with the required human_readability block from to-do/project-skill-architecture.md.
  - Update contracts/ticket-contract.md only if needed to make the completion report extension canonical.
  - Update the code-validator role prompt to require the human_readability block during ticket validation.
  - Preserve validator handoff behavior and review-only posture.
non_goals:
  - Do not create procedural skills.
  - Do not alter the role folder structure.
  - Do not add new validator roles.
  - Do not change provider-specific execution prompts.
acceptance_criteria:
  - execution/templates/completion-report.example.yaml includes the full human_readability block.
  - code-validator requires the block when completion_report_required is true.
  - ticket-contract documents the block if the implementation makes it canonical.
  - py -3.10 .\tools\validate_skill_library.py passes.
verification_commands:
  - rg -n "human_readability|diff_summary|layer_touched|layer_separation_preserved" .\execution\templates\completion-report.example.yaml .\skills\roles\code-validator\SKILL.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-SKILL-003
---

# Body

## Goal

Make every completion report carry observable evidence that the work stayed concise, scoped, and understandable to the human reviewer.

## Context

The operating discipline layer requires human-readable completion evidence. This ticket moves that requirement into the completion report example and validator gate.

## Procedure

1. Read `to-do/project-skill-architecture.md`.
2. Update `execution/templates/completion-report.example.yaml`.
3. Decide whether `contracts/ticket-contract.md` needs an explicit completion report extension section.
4. Update `skills/roles/code-validator/SKILL.md` to require the block.
5. Run the verification commands.

## Out of Scope

- Adding scope firewall tooling.
- Creating procedures.
- Expanding validator taxonomy.
- Changing the core role output envelope beyond the named completion report extension.

## Verification

The validator must see the `human_readability` block in the example report, confirm code-validator gates on the block, and confirm the skill library validator passes.
