# Procedural Skill Authoring Template

Procedural skills define narrow, situationally triggered procedures for observed model failure modes. They live under `skills/procedures/<procedure-name>/SKILL.md` and must include YAML frontmatter with every required field below.

Do not create a procedural skill for a broad domain, a role, always-on discipline, speculative future work, or a situation without an observed failure mode.

## Required Frontmatter

```yaml
---
trigger:
  - The concrete situation or observed signal that activates this procedure.
non_trigger:
  - Similar situations that must not activate this procedure.
failure_modes_addressed:
  - The named model failure mode this procedure is designed to prevent.
attention_signals:
  - Specific details the model must notice before choosing steps.
procedure:
  - The ordered steps to execute once the trigger applies.
scope_boundary:
  - What this procedure covers.
  - What this procedure explicitly does not cover.
composition_points:
  - Adjacent roles, discipline, or procedures this skill composes with.
reference_pointers:
  - ref: Reference directory name under skills/references/.
    section: Addressable section drawer id inside that reference.
    open_when: The condition under which the agent should open that drawer.
verification:
  - The closed loop used to check the result where checking is possible.
output_contract:
  - The fields, artifacts, or report shape the procedure must produce.
---
```

## Field Contract

`trigger` names the concrete conditions that activate the procedure. It should be specific enough that a role can decide whether to invoke the skill without guessing.

`non_trigger` names nearby situations where the procedure must not be used. This prevents broad procedural skills from absorbing adjacent concerns.

`failure_modes_addressed` names the observed failure modes the skill exists to counter. A procedure without a named failure mode should not be added.

`attention_signals` lists the evidence the model must notice before acting. These are the expert signals that usually appear before the procedural steps become obvious.

`procedure` gives the bounded steps to perform after the trigger applies. Keep the steps narrow and situation-specific.

`scope_boundary` states both the included scope and explicit exclusions. It must keep the procedure from becoming a role, domain skillset, or operating discipline.

`composition_points` identifies adjacent skills, roles, or discipline constraints that should handle related work. Use this to compose orthogonally instead of bundling concerns.

`reference_pointers` is required and names the reference drawers this procedure may open. Each entry must include `ref`, `section`, and `open_when`: `ref` is the reference directory name, `section` is the section drawer id, and `open_when` is the concrete condition under which the agent should open that drawer. Use `reference_pointers: []` when the procedure genuinely consumes no reference.

`verification` defines how the output is checked. Where direct verification is possible, include a closed loop that can fail and cause revision.

`output_contract` defines the expected final artifact, fields, or reporting shape for the procedure. It should make completion auditable by a downstream role or human reviewer.

## Closet Size Budget

The closet size budget for a procedural `SKILL.md` is at most 200 lines total.

The `procedure` field is a skeleton: it should carry the ordered control flow,
decision points, and terminal checks needed to execute the situation without
embedding detailed domain knowledge.

Detailed domain knowledge belongs in reference drawers rather than inline.
Use `reference_pointers` to point from the compact procedure closet to the
specific reference sections that should be opened only when their `open_when`
conditions apply.
