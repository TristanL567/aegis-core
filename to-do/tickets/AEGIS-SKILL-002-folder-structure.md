---
id: AEGIS-SKILL-002
title: Reshape the skill folder structure into roles, discipline, and procedures.
epic: epic-skill-architecture
status: ready
risk: medium
allowed_areas:
  - skills/
  - AGENT_PROMPT.md
  - README.md
  - tools/validate_skill_library.py
must_not_touch:
  - contracts/
  - prompt_templates/
  - execution/
  - docs/
requirements:
  - Preserve the top-level skills/ directory to reduce migration risk.
  - Create skills/roles/, skills/discipline/, and skills/procedures/.
  - Move existing role prompt directories under skills/roles/ without changing role prompt bodies.
  - Update README.md and AGENT_PROMPT.md references to reflect the new structure.
  - Update tools/validate_skill_library.py so every existing role remains discoverable under skills/roles/.
  - Preserve existing role names, frontmatter, allowed handoffs, and output contracts.
non_goals:
  - Do not rename skills/ to roles/.
  - Do not edit role prompt body content except path references if strictly necessary.
  - Do not create operating discipline content.
  - Do not create procedural skills.
  - Do not edit contracts or execution docs.
acceptance_criteria:
  - skills/roles/ contains every existing role prompt directory that previously lived directly under skills/.
  - skills/discipline/ and skills/procedures/ exist.
  - py -3.10 .\tools\validate_skill_library.py passes.
  - README.md and AGENT_PROMPT.md describe the new three-subdirectory structure.
  - No role prompt behavior changed.
verification_commands:
  - Test-Path .\skills\roles
  - Test-Path .\skills\discipline
  - Test-Path .\skills\procedures
  - py -3.10 .\tools\validate_skill_library.py
  - rg -n "skills/roles|skills/discipline|skills/procedures" .\README.md .\AGENT_PROMPT.md
completion_report_required: true
depends_on:
  - AEGIS-SKILL-001
---

# Body

## Goal

Separate the current role prompt files from the future discipline and procedure layers while keeping the top-level `skills/` path stable.

## Context

The epic allows either a full `skills/` to `roles/` rename or a lower-risk subdirectory migration. This ticket chooses the lower-risk subdirectory approach so existing repo identity remains stable while the layer split becomes physical.

## Procedure

1. Read `docs/skill-architecture.md`.
2. Create `skills/roles/`, `skills/discipline/`, and `skills/procedures/`.
3. Move existing role prompt directories into `skills/roles/`.
4. Update `tools/validate_skill_library.py` to discover role skills under `skills/roles/`.
5. Update `README.md` and `AGENT_PROMPT.md` to describe the new structure.
6. Run the verification commands and inspect the diff for accidental prompt body changes.

## Out of Scope

- Renaming the top-level `skills/` directory.
- Creating procedural skill content.
- Creating operating discipline content.
- Changing role behavior.

## Verification

The validator must see that every existing role remains discoverable, the skill validator passes, and the diff shows only path movement, structure references, and validator discovery updates.
