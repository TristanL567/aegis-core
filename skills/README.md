# AEGIS Skill Library

This directory is the canonical local skill manifest for AEGIS roles, procedures, references, and operating discipline.

## Categories

| category | path | purpose | index |
| --- | --- | --- | --- |
| roles | `skills/roles/` | Triggerable swarm personas that own routing, execution, validation, or coordination behavior. | `skills/roles/README.md` |
| procedures | `skills/procedures/` | Bounded workflows selected by roles, or used standalone only when their metadata says `standalone: true`. | `skills/procedures/README.md` |
| references | `skills/references/` | Knowledge drawers opened by roles or procedures for domain, framework, or pattern evidence. | `skills/references/README.md` |
| discipline | `skills/discipline/` | Always-on operating discipline followed by roles and procedures. | no category index |

## Selection Model

Skill selection is role-mediated by default. A master or specialized role chooses the active worker, validator, or planner, and that role may route to procedures when its Procedure Routing section says the procedure applies. Procedures do not replace role authority, handoff rules, validator gates, ticket scope, or human approval checkpoints.

Procedures with `standalone: true` may be used directly when their trigger metadata applies. Procedures without that metadata are treated as role-composed workflows unless a local role explicitly routes to them.

References are knowledge drawers, not triggerable skills. Open them only when a role or procedure points to the needed reference knowledge; do not dispatch a reference as a role, worker, validator, or procedure.

`skills/discipline/` is always-on behavioral doctrine for bounded scope, change discipline, verification, and reporting. It is intentionally not indexed as a selectable category.
