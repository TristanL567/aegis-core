# Epic: Three-Layer Skill Architecture

## Intent

This epic commits AEGIS to a three-layer architecture: orchestration roles, operating discipline, and procedural skills. Roles define the swarm topology, operating discipline defines the always-on anti-AI-slope behavior, and procedural skills define narrow situational procedures with sharp triggers and verification loops. The highest-leverage first move is not creating many skills, but creating the gate that prevents bad, broad, or speculative skills from being created.

## Layer Definitions

### Layer 1: Orchestration Roles

- Name: Orchestration roles.
- Purpose: Define the swarm topology and handoff rules between `master`, `worker`, `validator`, and `human`.
- Repository location after migration: `skills/roles/`.
- Covers: master coordination, worker execution boundaries, validator gating, handoff permissions, and role output envelopes.
- Does not cover: procedure-specific implementation guidance, behavioral discipline text that should apply everywhere, or deterministic verification tooling.
- Relationship to other layers: roles invoke procedural skills while operating under the discipline layer. Roles run the work, but they are not the procedural knowledge itself.

### Layer 2: Operating Discipline

- Name: Operating discipline.
- Purpose: Hold the always-on anti-AI-slope rules that govern how every role and procedure works.
- Repository location after migration: `skills/discipline/operating-discipline.md`.
- Covers: one-ticket-only execution, small diffs, declared scope, no speculative changes, no unrelated refactors, surgical edits, concrete verification, named completion artifacts, and human-readable reporting.
- Does not cover: structural handoff envelopes, role topology, provider-specific behavior, or situation-specific procedures.
- Relationship to other layers: discipline applies to every role and every procedural skill simultaneously. It is behavioral guidance, not a structural contract.

### Layer 3: Procedural Skills

- Name: Procedural skills.
- Purpose: Define narrow, situationally triggered procedures that address named model failure modes.
- Repository location after migration: `skills/procedures/`.
- Covers: recognized work situations with trigger and non-trigger boundaries, failure modes, attention signals, procedure, scope boundary, composition points, verification loops, and output contract.
- Does not cover: broad domains such as backend, frontend, or data science, role handoff topology, or universal behavioral discipline.
- Relationship to other layers: procedural skills are invoked by roles and constrained by the operating discipline. They compose orthogonally with other procedures instead of bundling adjacent concerns.

## Doctrinal Constraints

- Existence gate: no procedural skill is written unless a named failure mode has been observed in real work, because speculative skills dilute attention and create false precision.
- Composition rule: every procedural skill declares what it does not cover and which adjacent skills handle those concerns, because overlapping skills become broad mini-frameworks and weaken triggering.
- Verification rule: every procedural skill includes a closed verification loop wherever output can be checked, because generation-only procedures leave correctness to model confidence.
- Attention rule: every procedural skill encodes what to notice, not only what to do, because the model often fails by missing expert signals before it chooses steps.
- Proliferation constraint: the library grows from observed evidence one skill at a time, because upfront taxonomies create broad domain skills that are hard to trigger and maintain.
- Enforcement rule: authoring requirements are enforced by `tools/validate_skill_library.py` in the same ticket that introduces them, because authoring rules without tooling erode over time.

## Migration Posture

This epic is a migration pipeline, not a refactor. Existing role prompts remain functional throughout the work. New layer infrastructure is added alongside the current library before any broad role prompt is reassessed. Broad workers such as `backend-worker`, `chart-worker`, and `model-interpreter-worker` are preserved during migration. Their deprecation, conversion to thin fallback, or conversion to router shape is decided only after procedural coverage exists.

## Success Criteria for the Epic

The epic is complete when:

- The three layers are physically separated in the repository.
- The operating discipline is consolidated, canonical, and referenced from every role.
- The authoring contract for procedural skills exists and is enforced by the validator.
- At least one procedural skill and one meta-control skill exist as reference shapes.
- Completion reports carry observable evidence of discipline compliance.
- The library is positioned to grow incrementally from observed failure modes.

## Non-Goals

- No mass renaming of existing roles.
- No deletion of existing broad workers in this epic.
- No speculative procedural skills beyond the two reference shapes.
- No new validator taxonomy expansion.
- No provider-specific changes.
