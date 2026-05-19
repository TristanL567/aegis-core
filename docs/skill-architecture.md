# AEGIS Skill Architecture

This document is the canonical doctrine for the AEGIS three-layer skill architecture. It implements the planning direction from `to-do/epic-skill-architecture.md` and governs future skill-library migration work.

The architecture separates orchestration roles, operating discipline, and procedural skills so that swarm topology, always-on behavior, and narrow situational procedures do not collapse into broad role-shaped skillsets. Broad domain skillsets such as backend, frontend, data science, charting, or model interpretation are not procedural skills.

## Layer 1: Orchestration Roles

**Purpose:** Orchestration roles define the swarm topology and the handoff rules between `master`, `worker`, `validator`, and `human`.

**Repository location:** After migration, orchestration roles live in `skills/roles/`.

**Coverage boundary:** Orchestration roles cover master coordination, worker execution boundaries, validator gating, handoff permissions, and role output envelopes. They do not cover procedure-specific implementation guidance, always-on behavioral discipline, or deterministic validation tooling.

**Relationship to other layers:** Roles run the work, invoke procedural skills when their triggers apply, and remain constrained by the operating discipline throughout execution.

## Layer 2: Operating Discipline

**Purpose:** Operating discipline defines the always-on anti-AI-slope behavior that governs every role and every procedure.

**Repository location:** After migration, operating discipline lives in `skills/discipline/operating-discipline.md`.

**Coverage boundary:** Operating discipline covers one-ticket-only execution, declared scope, small diffs, no speculative changes, no unrelated refactors, surgical edits, concrete verification, named completion artifacts, and human-readable reporting. It does not cover role topology, handoff envelopes, provider-specific behavior, or situation-specific procedures.

**Relationship to other layers:** Operating discipline applies simultaneously to orchestration roles and procedural skills; it is behavioral doctrine, not a role contract or a procedure.

## Layer 3: Procedural Skills

**Purpose:** Procedural skills define narrow, situationally triggered procedures for observed model failure modes.

**Repository location:** After migration, procedural skills live in `skills/procedures/`.

**Coverage boundary:** Procedural skills cover named work situations with trigger boundaries, non-trigger boundaries, failure modes, attention signals, procedure steps, scope boundaries, composition points, verification loops, and output contracts. They do not cover broad domains, role handoff topology, universal behavioral discipline, or validator taxonomy.

**Relationship to other layers:** Procedural skills are invoked by orchestration roles and constrained by operating discipline; they compose orthogonally with adjacent procedures instead of bundling multiple concerns into broad skillsets.

## Doctrinal Constraints

- **existence gate:** No procedural skill is written unless a named failure mode has been observed in real work, because speculative skills dilute attention and create false precision.
- **composition rule:** Every procedural skill declares what it does not cover and which adjacent skills handle those concerns, because overlapping skills become broad mini-frameworks and weaken triggering.
- **verification rule:** Every procedural skill includes a closed verification loop wherever output can be checked, because generation-only procedures leave correctness to model confidence.
- **attention rule:** Every procedural skill encodes what to notice, not only what to do, because the model often fails by missing expert signals before it chooses steps.
- **proliferation constraint:** The library grows from observed evidence one skill at a time, because upfront taxonomies create broad domain skills that are hard to trigger and maintain.
- **enforcement rule:** Authoring requirements are enforced by `tools/validate_skill_library.py` in the same ticket that introduces them, because authoring rules without tooling erode over time.

## Migration Boundary

This doctrine document does not start or prepare AEGIS-SKILL-002. It does not move files, edit role prompts, add procedural skill files, change validation tooling, or edit contracts.
