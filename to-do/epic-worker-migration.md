# Epic: Broad Worker Migration

## Intent

This epic executes the migration direction from `docs/broad-worker-migration.md` without deleting existing roles. Broad role prompts remain functional while procedure-shaped content is extracted into Axis-1 procedural skills and reusable knowledge is moved into Axis-2 references. The proving move is the thinnest worker first, then content workers, then validators.

## Doctrine Inputs

- `docs/skill-architecture.md`
- `docs/procedural-skill-template.md`
- `docs/broad-worker-migration.md`

## Two-Axis Classification

- Axis 1, situations: what the operator is doing. These become procedural skills.
- Axis 2, knowledge: what the situation draws on. These become references.

Rejected skill cuts: language skills, model-family skills, methodology skills, and broad domain skills. These become references only.

## Per-Worker Disposition

| Role | Disposition | Extracted situation skills | Absorbed references | Notes |
| --- | --- | --- | --- | --- |
| `chart-worker` | Thin fallback after proving move | `chart-artifact-generation` | `charting-artifact-reference` | Thinnest worker because its output is artifact-shaped and verification can be concrete. |
| `model-interpreter-worker` | Thin fallback | `model-output-interpretation` | `model-interpretation-reference` | Keeps narrative work evidence-bound and separates statistical/domain knowledge into references. |
| `backend-worker` | Router | Existing `new-api-endpoint`; future `external-api-integration`, `database-migration`, `auth-boundary-change` | `backend-api-patterns-reference` | Do not delete backend-worker; make it route endpoint work to the existing procedure. |
| `ticket-planner-worker` | Router | Deferred: `ticket-backlog-decomposition`, `ticket-contract-authoring` | Deferred: ticket planning reference | Needs operator evidence before creating planning procedures. |
| `code-validator` | Keep as validator | Existing `ticket-scope-validation`; future `acceptance-criteria-validation` | Validator review reference deferred | Validators remain gates; procedures only strengthen checks. |
| `ds-validator` | Keep as validator | Deferred: `data-leakage-review`, `ml-reproducibility-review` | ML evaluation reference in Expansion epic | Data science validation is kept as a review role until stronger evidence supports procedure extraction. |
| `master` | Router | Deferred: `ticket-dispatch-readiness`, `human-approval-checkpoint` | None initially | Master remains the human-facing orchestration role. |

## Candidate Test Results

| Candidate | Verb test | Same-situation test | Trigger-disjointness test | Boundary-declaration test | Result |
| --- | --- | --- | --- | --- | --- |
| `chart-artifact-generation` | Pass: generate/render/export a chart artifact. | Pass: same procedure across chart scripts and visual artifact outputs. | Pass: separate from data-quality review and visual style conformance. | Pass: excludes modeling, analysis, and broad chart design. | Create in Epic A pending reference home confirmation. |
| `model-output-interpretation` | Pass: interpret and narrate model output. | Pass: same evidence-bound interpretation procedure across model result summaries. | Pass: separate from training, calibration, and validation. | Pass: excludes implementation and model fitting. | Create in Epic A pending failure-mode confirmation. |
| `new-api-endpoint` | Already created and validated. | Already passes. | Already excludes database migration and auth boundary changes. | Already declares boundaries. | Use as backend migration anchor. |
| `ticket-backlog-decomposition` | Pass as a situation, but evidence not confirmed. | Likely pass. | Needs boundary against project planning and ticket-contract authoring. | Needs operator examples. | Deferred. |
| `data-leakage-review` | Pass as validator-side situation. | Likely pass. | Needs boundary against general DS validation. | Needs operator examples. | Deferred to Library Expansion. |

## Sequence

1. Add charting reference.
2. Add `chart-artifact-generation`.
3. Update `chart-worker` as a thin fallback.
4. Add model interpretation reference.
5. Add `model-output-interpretation`.
6. Update `model-interpreter-worker` as a thin fallback.
7. Add backend API patterns reference.
8. Update `backend-worker` as a router to existing endpoint procedure.
9. Update `ticket-planner-worker` as a router while deferring planning procedures.
10. Update validators to compose with existing procedures without creating a validator taxonomy.

## Non-Goals

- No role deletion.
- No broad worker deprecation in this epic.
- No new validator taxonomy.
- No language, model-family, methodology, or domain-shaped skill.
- No reference without a named consuming skill.

## Open Clarifications

- Should shared references live in `aegis-core`, MDCS, or both?
- Has the chart artifact failure mode actually occurred recently?
- Has the model interpretation hallucination or smoothing failure actually occurred recently?
- Should ticket planning procedure extraction wait for the next real planning failure?
