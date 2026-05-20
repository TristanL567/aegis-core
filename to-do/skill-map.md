# Skill Map

This map places existing, create-now, and deferred procedural skills on the workflow axis. It is the overlap-detection artifact and operator index for the migration and expansion epics.

## Existing Procedures

| Workflow phase | Skill | Status | Consulted references |
| --- | --- | --- | --- |
| Commit and audit | `clean-commit` | existing | Operating discipline, ticket contract |
| Scope validation | `ticket-scope-validation` | existing | Ticket contract |
| Backend implementation | `new-api-endpoint` | existing | Future `backend-api-patterns`, future language references |

## Proposed Create-Now Skills Pending Operator Evidence

| Workflow phase | Skill | Area | Consulted references | Overlap boundary |
| --- | --- | --- | --- | --- |
| Artifact creation | `chart-artifact-generation` | worker migration | `charting-artifact-reference` | Excludes visual style audit and chart data-quality investigation. |
| Analysis interpretation | `model-output-interpretation` | worker migration | `model-interpretation-reference`, ML evaluation reference when relevant | Excludes model training, calibration, and leakage validation. |
| ML diagnostics | `training-run-diagnostics` | ML | `ml-evaluation` | Excludes hyperparameter tuning and model calibration. |
| ML review | `model-calibration-review` | ML | `ml-evaluation` | Excludes general model interpretation and training diagnostics. |
| Quant validation | `backtest-validation` | quantitative finance | `quant-backtesting`, `oracle-sql` if data query scope is involved | Excludes signal generation and portfolio allocation. |
| Quant reconciliation | `risk-metric-reconciliation` | quantitative finance | `quant-backtesting`, `investment-management` | Excludes full backtest validation. |
| Portfolio review | `portfolio-rebalancing-review` | investment management | `investment-management` | Excludes investment thesis writing and order execution. |
| Thesis review | `investment-thesis-evidence-check` | investment management | `investment-management` | Excludes portfolio construction and trade implementation. |
| Frontend implementation | `frontend-component-implementation` | frontend | `frontend-accessibility`, `language-idioms` | Excludes accessibility audit and design-system migration. |
| Frontend review | `accessibility-audit` | frontend | `frontend-accessibility` | Excludes component implementation and visual redesign. |
| Cloud operations | `deployment-failure-triage` | cloud computing | `cloud-operations` | Excludes IAM policy changes and cost optimization. |
| Cloud security | `cloud-iam-change-review` | cloud computing | `cloud-operations` | Excludes deployment incident triage. |

## Deferred Skills

| Workflow phase | Skill | Reason deferred | Evidence needed |
| --- | --- | --- | --- |
| ML tuning | `hyperparameter-tuning` | Plausible situation but no confirmed recent failure mode. | Example where tuning proceeded without diagnostics or validation. |
| Backend data | `database-migration` | High value but not confirmed in this planning run. | Recent migration where AI mishandled schema, lock, rollback, or backfill risk. |
| Backend security | `auth-boundary-change` | High value but not confirmed in this planning run. | Recent auth, tenant, or permission boundary failure. |
| Quant research | `signal-generation` | Too broad. | A narrower recurring action, such as validating a signal definition. |
| Investment construction | `portfolio-construction` | Too broad. | Narrow repeated workflow and failure mode. |
| Frontend system | `design-system-update` | Boundary against component implementation unclear. | Example where AI changed design tokens or shared components incorrectly. |
| Cloud finance | `cost-optimization-review` | No confirmed repeated task. | Example where AI missed cost, resource, or utilization evidence. |

## Reference Index

| Reference | Status | Consuming skills |
| --- | --- | --- |
| `charting-artifact-reference` | proposed | `chart-artifact-generation` |
| `model-interpretation-reference` | proposed | `model-output-interpretation` |
| `backend-api-patterns-reference` | proposed | `new-api-endpoint` |
| `ml-evaluation` | proposed | `training-run-diagnostics`, `model-calibration-review`, future `data-leakage-review` |
| `quant-backtesting` | proposed | `backtest-validation`, `risk-metric-reconciliation` |
| `investment-management` | proposed | `portfolio-rebalancing-review`, `investment-thesis-evidence-check` |
| `frontend-accessibility` | proposed | `frontend-component-implementation`, `accessibility-audit` |
| `cloud-operations` | proposed | `deployment-failure-triage`, `cloud-iam-change-review` |
| `language-idioms` | proposed | `frontend-component-implementation`, `new-api-endpoint`, cloud/tooling procedures when code is involved |
| `oracle-sql` | proposed pending location | `backtest-validation`, future `database-migration`, future data-query procedures |

## Overlap Findings

- Healthy composition: endpoint work can compose with language references, ticket-scope validation, and clean-commit.
- Healthy composition: backtest validation can consult Oracle SQL knowledge when the backtest depends on database queries.
- Forbidden overlap risk: `frontend-component-implementation` and `design-system-update` need clearer boundaries before design-system work becomes a skill.
- Forbidden overlap risk: `training-run-diagnostics`, `hyperparameter-tuning`, and `model-calibration-review` must stay phase-disjoint.
- Reference overlap is acceptable when multiple skills consume the same knowledge source.
