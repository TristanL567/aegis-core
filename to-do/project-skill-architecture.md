# Project: Skill Architecture Migration

## Scope

Implements the epic in `epic-skill-architecture.md`. Adds the three-layer architecture incrementally via sequenced tickets. Does not modify existing role behavior except by reference-extraction.

## Allowed Areas (project-wide)

- `docs/`
- `skills/` and any new subdirectories created by the migration
- `contracts/` read-only except for explicit envelope changes named in tickets
- `tools/validate_skill_library.py`
- `execution/templates/` for completion report extensions
- `to-do/` for this epic and project artifacts

## Must Not Touch (project-wide)

- `prompt_templates/`
- `sandbox/`
- `.idea/`
- `.git/`
- any existing role prompt body in `skills/` except for reference-extraction edits explicitly described in a ticket
- provider-specific runtime files

## Working Agreement

- One ticket at a time. No batched tickets.
- Each ticket produces a clean commit with ticket ID, goal, acceptance criteria, and validation evidence.
- Each ticket declares `allowed_areas`, `must_not_touch`, `requirements`, `non_goals`, `acceptance_criteria`, `verification_commands`, and `completion_report_required`.
- No ticket adds a procedural skill without a named failure mode.
- No ticket adds an authoring requirement without same-ticket validator enforcement.
- Existing role prompts remain functional throughout the project. If a reference-extraction edit changes role behavior, the change must be explicitly approved.

## Validator Policy for This Project

- The code-validator gates every ticket.
- For tickets that touch `tools/validate_skill_library.py`, validator must confirm the validator still passes on the current library.
- For tickets that introduce new layer infrastructure, validator must confirm the existing role prompts still load and behave unchanged.

## Definition of Ready (per ticket)

- Ticket goal is one sentence.
- `allowed_areas` and `must_not_touch` are explicit.
- Acceptance criteria are testable.
- Verification commands are listed.
- Completion-report fields are named.

## Definition of Done (per ticket)

- All acceptance criteria met.
- All verification commands pass.
- Completion report submitted with human-readable diff summary.
- Validator approved or human override recorded.
- Commit contains only ticket-owned files.

## Completion Report Extension Required for This Project

Every completion report on this project must include:

```yaml
human_readability:
  concise: true
  unnecessary_elements_removed: true
  abstraction_added: <bool>
  abstraction_rationale: <string or null>
  diff_summary: <one-paragraph human-readable explanation>
  layer_touched: <discipline | role | procedure | meta | infrastructure>
  layer_separation_preserved: true
```
