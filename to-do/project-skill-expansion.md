# Project: Skill Library Migration and Expansion

## Scope

This project covers two planning epics:

- `to-do/epic-worker-migration.md`
- `to-do/epic-library-expansion.md`

The project plans role migration, reference creation, and procedural skill expansion. It does not write skill or reference content during planning.

## Doctrine

Every ticket must link to:

- `docs/skill-architecture.md`
- `docs/procedural-skill-template.md`

Tickets must link doctrine rather than restating it.

## Reference Contract

- References hold Axis-2 knowledge only.
- Every reference declares its scope.
- Every reference names at least one consuming skill.
- References without consuming skills are forbidden.
- Language, model-family, methodology, and domain candidates become references only.
- Proposed reference home is `skills/references/`, pending operator confirmation about `aegis-core`, MDCS, or both.

## Composition Contract

- Every procedural skill declares non-coverage.
- Every procedural skill names adjacent skills or references that handle nearby concerns.
- Adjacent workflow phases may compose.
- Competing skills for the same decision are forbidden.
- Broad workers remain until procedural coverage exists and validators can enforce it.

## Verification Expectation

- Every skill states how output is verified.
- Manual verification is acceptable when no deterministic check exists.
- Deterministic checks must be preferred when available.
- Reference tickets must verify that each reference names its consuming skills.
- Skill tickets must verify procedural frontmatter through `py -3.10 .\tools\validate_skill_library.py`.

## Working Agreement

- Planning artifacts only until the operator confirms missing evidence.
- One ticket at a time.
- No speculative skills.
- No reference without a consumer.
- No role deletion in these epics.
- Epic B skill tickets are blocked until the operator confirms real encountered failure modes.

## Definition of Ready

- Ticket has one goal.
- Ticket names doctrine links.
- `allowed_areas` and `must_not_touch` are explicit.
- Skill tickets cite a named failure mode.
- Reference tickets name consuming skills.
- Verification commands are listed.

## Definition of Done

- Ticket-owned files only.
- Validation commands pass or skipped risk is reported.
- Completion report includes `human_readability`.
- Validator approves or human override is recorded.
- Role behavior is preserved unless the ticket explicitly owns a role-reference update.

## Open Questions

1. Which create-now skill failure modes have actually been encountered recently?
2. Which recurring real task is missing from each area?
3. Should shared references, especially Oracle SQL, live in `aegis-core`, MDCS, or both?
4. Should language references begin as one shared folder or one folder per language?
