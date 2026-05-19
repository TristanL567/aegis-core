---
id: AEGIS-SKILL-003
title: Add the canonical operating discipline document and reference it from roles.
epic: epic-skill-architecture
status: ready
risk: medium
allowed_areas:
  - skills/discipline/
  - AGENT_PROMPT.md
  - skills/roles/master/SKILL.md
  - skills/roles/*/SKILL.md
must_not_touch:
  - contracts/
  - tools/
  - execution/
  - prompt_templates/
requirements:
  - Create skills/discipline/operating-discipline.md.
  - Consolidate the always-on anti-AI-slope rules from AGENT_PROMPT.md, contracts/, and the roadmap into the discipline document.
  - Reference the discipline document from AGENT_PROMPT.md.
  - Reference the discipline document from every role prompt body with reference-extraction edits only.
  - Strip duplicated discipline text from role bodies only when it is replaced by the canonical reference and behavior is preserved.
non_goals:
  - Do not change structural contract fields.
  - Do not add procedural skills.
  - Do not alter role handoff behavior.
  - Do not edit validation tooling.
acceptance_criteria:
  - skills/discipline/operating-discipline.md exists and contains the canonical anti-AI-slope rules.
  - Every role prompt references skills/discipline/operating-discipline.md.
  - No discipline rule is maintained as a duplicated full policy block in multiple role prompt bodies.
  - py -3.10 .\tools\validate_skill_library.py passes.
verification_commands:
  - Test-Path .\skills\discipline\operating-discipline.md
  - rg -n "skills/discipline/operating-discipline.md" .\AGENT_PROMPT.md .\skills\roles
  - rg -n "speculative|unrelated refactor|small diff|surgical|completion report" .\skills\discipline\operating-discipline.md
  - py -3.10 .\tools\validate_skill_library.py
completion_report_required: true
depends_on:
  - AEGIS-SKILL-002
---

# Body

## Goal

Create one canonical operating discipline document and make all roles reference it instead of carrying duplicated anti-AI-slope guidance.

## Context

The operating discipline layer is behavioral guidance, not a structural contract. This ticket gives it a single home under `skills/discipline/` after the folder split from AEGIS-SKILL-002.

## Procedure

1. Read `docs/skill-architecture.md` and `to-do/project-skill-architecture.md`.
2. Create `skills/discipline/operating-discipline.md`.
3. Consolidate ticket scope, small diff, no speculation, no unrelated refactor, verification, and completion-report behavior.
4. Add references to the discipline document from `AGENT_PROMPT.md` and all role prompt bodies.
5. Remove duplicated discipline blocks only when they are replaced by the canonical reference.
6. Run the verification commands.

## Out of Scope

- Changing role handoff topology.
- Creating procedures.
- Updating the ticket contract unless a future ticket names that envelope change.
- Provider-specific edits.

## Verification

The validator must confirm the discipline document exists, every role references it, role behavior is preserved, and the existing skill validator still passes.
