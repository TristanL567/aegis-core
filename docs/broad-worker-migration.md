# Broad Worker Migration Map

## Purpose and Boundary

This document maps the current broad worker, validator, and master roles against the three-layer AEGIS skill architecture. It is a planning artifact only. It does not deprecate, rename, move, remove, or edit any role prompt, validator, tool, procedure, contract, execution document, or operating discipline file.

Role migration and procedural skill creation are separate activities:

- Role migration decides whether a role remains a router, fallback, validator, or future deprecation candidate.
- Procedural skill creation writes narrow, situational procedures only after observed failure modes justify them.

Existing broad workers must remain available until procedural coverage exists and is validated. Candidate future procedures named here are planning labels, not created skills.

## Disposition Categories

- `retain as thin router`: Keep the role as the orchestration-facing assignment surface, but route narrow repeated work through existing or future procedures when they apply.
- `retain as fallback`: Keep the role for work that is too broad, ambiguous, novel, or under-covered by procedures.
- `deprecate in favor of procedures`: Long-term target only after procedures cover the role's recurring work and the master can route directly without losing safety or clarity.
- `keep as validator`: Keep the role as a blocking review gate. Procedures may strengthen its checks, but do not replace the review role.

## Current Role Inventory

| Role | Current function | Disposition | Rationale | Procedure coverage |
| --- | --- | --- | --- | --- |
| `backend-worker` | Implements backend services, APIs, middleware, server-side logic, external integrations, and backend tests. | retain as thin router | Backend work is still broad and implementation-owned, but narrow endpoint work now has a procedural shape. The role should invoke applicable procedures rather than carry all backend guidance in the role prompt. | Existing: `new-api-endpoint`, `ticket-scope-validation`, `clean-commit`. Candidate future: `database-migration`, `auth-boundary-change`, `external-api-integration`, `background-job-change`, `middleware-change`, `service-layer-refactor`. |
| `chart-worker` | Produces charting scripts and visualization artifacts under explicit styling and data-quality constraints. | retain as fallback | Chart work spans data preparation, visual encoding, styling, artifact generation, and manual readability. No current procedure covers chart-specific failure modes, so the worker remains necessary until narrower chart procedures exist. | Existing: `ticket-scope-validation`, `clean-commit` when ticket scope or commit readiness applies. Candidate future: `chart-artifact-generation`, `visual-style-conformance`, `chart-data-quality-check`, `plot-export-verification`. |
| `model-interpreter-worker` | Interprets statistical or model results and translates analytical output into domain-relevant narratives. | retain as fallback | Interpretation depends on evidence, domain framing, uncertainty, and contradiction handling. No current procedure covers model-interpretation failure modes, so the role should remain until repeated interpretation workflows justify narrow procedures. | Existing: `ticket-scope-validation`, `clean-commit` when file scope or commit readiness applies. Candidate future: `model-output-interpretation`, `feature-effect-explanation`, `theory-conflict-analysis`, `uncertainty-narrative-review`. |
| `ticket-planner-worker` | Converts large goals, PRDs, strategy notes, or plans into strict ticket backlogs. | retain as thin router | Ticket planning is a role-level planning function, not implementation. It can eventually route repeated checks to ticket procedures, but the planning worker remains useful for decomposing ambiguous work and returning backlog artifacts to master review. | Existing: `ticket-scope-validation` can later validate changed ticket artifacts when applicable; `clean-commit` can review commit readiness if the planning artifact is committed. Candidate future: `ticket-backlog-decomposition`, `ticket-contract-authoring`, `dependency-ordering`, `allowed-area-design`, `planning-ambiguity-review`. |
| `ds-validator` | Reviews data science and machine learning work for leakage, performance, reproducibility, and pipeline quality. | keep as validator | This is a domain-specific blocking review gate. Procedures can provide deterministic or repeatable checks, but validator judgment is still required for leakage, reproducibility, and pipeline quality. | Existing: `ticket-scope-validation` for changed-file scope; `clean-commit` for commit evidence when relevant. Candidate future: `data-leakage-review`, `ml-reproducibility-review`, `split-hygiene-check`, `feature-pipeline-review`, `model-performance-validation`. |
| `code-validator` | Reviews worker output for security, correctness, maintainability, ticket acceptance, scope compliance, and verification evidence. | keep as validator | This role is the general blocking quality gate. It already composes with `ticket-scope-validation` and should remain responsible for findings and verdicts while procedures supply narrower checks. | Existing: `ticket-scope-validation`, `clean-commit`, `new-api-endpoint` for endpoint-specific review context. Candidate future: `security-review`, `test-coverage-review`, `acceptance-criteria-validation`, `regression-risk-review`, `human-readability-review`. |
| `master` | Coordinates the swarm, owns human communication, routes work, enforces ticket mode, and manages validator remediation loops. | retain as thin router | Master is orchestration, not a broad procedural skill. It should remain the routing and approval surface while delegating narrow repeated work to roles and procedures. | Existing: `ticket-scope-validation`, `clean-commit`, `new-api-endpoint` as procedures it may require workers or validators to invoke. Candidate future: `ticket-dispatch-readiness`, `validator-remediation-routing`, `human-approval-checkpoint`, `cross-ticket-dependency-gate`. |

## Candidate Future Procedure Coverage

The following names describe possible future procedures. They are not created by this document and should not be created until observed failure modes justify them.

### Backend Worker

- `database-migration`: schema, migration, seed, persistence model, and backfill changes.
- `auth-boundary-change`: authentication, authorization, tenancy, permission, and access-policy changes.
- `external-api-integration`: outbound client contracts, retries, errors, rate limits, and integration tests.
- `background-job-change`: job scheduling, idempotency, retry behavior, and observability.
- `middleware-change`: request lifecycle, ordering, side effects, and cross-route impact.
- `service-layer-refactor`: internal service behavior changes that are not endpoint-owned.

### Chart Worker

- `chart-artifact-generation`: script-first chart generation, output paths, and reproducible artifact creation.
- `visual-style-conformance`: fonts, labels, legends, layout, and style-spec adherence.
- `chart-data-quality-check`: missing data, sampling, units, aggregation, and scale issues.
- `plot-export-verification`: export format, resolution, nonblank output, and reviewable artifact evidence.

### Model Interpreter Worker

- `model-output-interpretation`: statistical finding summary and evidence-bound interpretation.
- `feature-effect-explanation`: feature effect direction, magnitude, uncertainty, and caveats.
- `theory-conflict-analysis`: explicit handling of contradictions between domain theory and observed relationships.
- `uncertainty-narrative-review`: confidence limits, unsupported causal claims, and wording discipline.

### Ticket Planner Worker

- `ticket-backlog-decomposition`: splitting large goals into independently reviewable tickets.
- `ticket-contract-authoring`: producing complete ticket fields under `contracts/ticket-contract.md`.
- `dependency-ordering`: sequencing tickets and identifying blocked work.
- `allowed-area-design`: setting narrow write areas and protected paths.
- `planning-ambiguity-review`: surfacing unclear ownership, scope, dependencies, and verification gaps.

### Validators and Master

- `data-leakage-review`: leakage and split hygiene checks for data science work.
- `ml-reproducibility-review`: configuration, seed, environment, and rerun evidence.
- `security-review`: security-sensitive code review focus for general validation.
- `test-coverage-review`: focused assessment of missing or weak verification.
- `acceptance-criteria-validation`: systematic comparison of worker output against ticket acceptance criteria.
- `ticket-dispatch-readiness`: master-side check that a ticket is complete before worker assignment.
- `validator-remediation-routing`: master-side remediation loop after blocking validator findings.
- `human-approval-checkpoint`: master-side checkpoint before requesting or applying explicit human override.

## Migration Safeguards

- Preserve every existing role prompt until enough narrow procedures exist to cover the role's recurring work safely.
- Do not remove a worker merely because one procedure covers one slice of its domain.
- Do not move implementation guidance from a role into a procedure unless the procedure has a named trigger, non-trigger boundary, failure modes, verification loop, and output contract.
- Keep validators as review gates even when procedures provide mechanical checks.
- Keep `master` as the orchestration and human-communication role; procedures can inform routing but cannot replace approval ownership.
- Treat candidate procedure names in this document as backlog ideas only. They do not authorize new files, prompt edits, validator tooling changes, or role taxonomy changes.
- Reassess disposition only after procedural coverage exists, validators can enforce it, and operating discipline still keeps one-ticket scope intact.

## Planning-Only Statement

This document is planning only. It does not deprecate, rename, move, delete, or edit `backend-worker`, `chart-worker`, `model-interpreter-worker`, `ticket-planner-worker`, `ds-validator`, `code-validator`, `master`, or any other role. It creates no procedures and changes no validator tooling. Broad workers remain preserved until future tickets create and validate procedural coverage.
