# Role Index

One row per role folder under `skills/roles/`.

| role | type | handoffs | selected when |
| --- | --- | --- | --- |
| backend-worker | worker | master, validator | Backend services, APIs, middleware, server-side logic, integrations, or backend tests need scoped implementation. |
| chart-worker | worker | master, validator | A chart, plot, visualization script, or visual reporting artifact needs scoped generation or triage. |
| code-validator | validator | master | Worker output needs independent security, correctness, maintainability, scope, or verification review. |
| ds-validator | validator | master | Data science or machine learning work needs leakage, reproducibility, performance, or pipeline-quality review. |
| master | master | worker, validator, human | A bounded task or ticket needs coordination, routing, approval handling, or remediation-loop control. |
| master-planner | master | master, validator, human | Epic-level dispatch, checkpoint handling, ledger decisions, or merge-gate coordination is needed. |
| master-validator | validator | master | Epic-level evidence, ticket validator verdicts, ledger state, or AEGIS Conformance Gate review is needed. |
| model-interpreter-worker | worker | master, validator | Existing model output, feature effects, diagnostics, predictions, or attribution results need evidence-bound interpretation. |
| skill-library-worker | worker | master, validator | Skill-library metadata, manifests, routing sections, or validator-support files need bounded maintenance under explicit path authorization. |
| ticket-planner-worker | worker | master, validator | A larger goal, PRD, plan, or ambiguous request needs conversion into strict, independently reviewable tickets. |
