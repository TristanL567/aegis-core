# Epic: Library Expansion

## Intent

This epic expands the procedural library across ML, quantitative finance, investment management, frontend, and cloud computing while enforcing the two-axis rule. Situations become skills; knowledge becomes references. Language, model-family, methodology, and domain candidates are references only.

## Candidate Classification

Legend:

- `create-now`: candidate passes the shape tests, but execution is blocked until the operator confirms the named failure mode was encountered in real work.
- `reference-only`: knowledge source, not a skill.
- `deferred`: plausible situation but lacks observed failure-mode evidence or is not the highest priority.
- `reject`: broad domain, taxonomy, or ambiguous overlap.

### ML

| Candidate | Classification | Rationale | Test result |
| --- | --- | --- | --- |
| `training-run-diagnostics` | create-now pending evidence | Situation: diagnosing a failed or suspicious training run; failure mode is changing model code before checking data, metrics, and run config. | Verb pass; same-situation pass; trigger boundary against calibration and hyperparameter tuning needed; boundary pass. |
| `model-calibration-review` | create-now pending evidence | Situation: checking whether predicted probabilities or scores match observed outcomes; failure mode is treating accuracy as calibration. | Verb pass; same-situation pass; trigger disjoint from model interpretation; boundary pass. |
| Neural networks | reference-only | Model family knowledge, not an operator situation. | Reclassified to reference by two-axis rule. |
| Bayesian inference | reference-only | Methodology knowledge, not a situation. | Reclassified to reference by two-axis rule. |
| Hyperparameter tuning | deferred | Situation-shaped, but no confirmed recent failure mode yet. | Needs operator evidence. |

### Quantitative Finance

| Candidate | Classification | Rationale | Test result |
| --- | --- | --- | --- |
| `backtest-validation` | create-now pending evidence | Situation: validating a strategy backtest; failure mode is accepting results with leakage, bad costs, or broken timing assumptions. | Verb pass; same-situation pass; trigger disjoint from risk metric reconciliation; boundary pass. |
| `risk-metric-reconciliation` | create-now pending evidence | Situation: reconciling VaR, volatility, drawdown, exposure, or beta numbers; failure mode is trusting mismatched definitions or frequencies. | Verb pass; same-situation pass; trigger disjoint from backtesting; boundary pass. |
| Stochastic volatility | reference-only | Model-family or methodology knowledge. | Reclassified to reference. |
| Option pricing models | reference-only | Domain/model knowledge. | Reclassified to reference. |
| Signal generation | deferred | Too broad until a concrete repeated task is named. | Needs narrower situation. |

### Investment Management

| Candidate | Classification | Rationale | Test result |
| --- | --- | --- | --- |
| `portfolio-rebalancing-review` | create-now pending evidence | Situation: reviewing proposed portfolio rebalance; failure mode is ignoring constraints, turnover, tax, or mandate limits. | Verb pass; same-situation pass; trigger disjoint from thesis review; boundary pass. |
| `investment-thesis-evidence-check` | create-now pending evidence | Situation: checking whether a written investment thesis is supported by cited evidence and risks; failure mode is unsupported narrative overreach. | Verb pass; same-situation pass; trigger disjoint from rebalancing; boundary pass. |
| Asset allocation theory | reference-only | Knowledge used by portfolio decisions. | Reclassified to reference. |
| Factor investing | reference-only | Methodology/domain knowledge. | Reclassified to reference. |
| Portfolio construction | deferred | Broad domain unless narrowed to rebalancing, constraints, or risk budgeting. | Needs narrower trigger. |

### Frontend

| Candidate | Classification | Rationale | Test result |
| --- | --- | --- | --- |
| `frontend-component-implementation` | create-now pending evidence | Situation: adding one UI component or screen unit; failure mode is building broad page architecture or inconsistent controls. | Verb pass; same-situation pass; trigger disjoint from accessibility audit; boundary pass. |
| `accessibility-audit` | create-now pending evidence | Situation: auditing an existing UI for accessibility; failure mode is visual-only review without keyboard, semantics, contrast, or screen-reader checks. | Verb pass; same-situation pass; trigger disjoint from component implementation; boundary pass. |
| React | reference-only | Library knowledge, not a situation. | Reclassified to reference. |
| TypeScript | reference-only | Language knowledge, not a situation. | Reclassified to reference. |
| Design-system update | deferred | Valid situation but may overlap with component implementation until real failure examples define boundary. | Needs evidence. |

### Cloud Computing

| Candidate | Classification | Rationale | Test result |
| --- | --- | --- | --- |
| `deployment-failure-triage` | create-now pending evidence | Situation: diagnosing a failed deployment; failure mode is changing config before reading logs, rollout state, and recent deltas. | Verb pass; same-situation pass; trigger disjoint from IAM change review; boundary pass. |
| `cloud-iam-change-review` | create-now pending evidence | Situation: reviewing cloud identity, permission, or access-policy changes; failure mode is over-broad permissions or missing trust boundary checks. | Verb pass; same-situation pass; trigger disjoint from deployment triage; boundary pass. |
| AWS, GCP, Azure | reference-only | Provider knowledge. | Reclassified to references. |
| Terraform | reference-only | Tool/language knowledge. | Reclassified to reference. |
| Cost optimization | deferred | Valid area, but needs a concrete recurring task and observed failure. | Needs evidence. |

### Languages and Shared Knowledge

| Candidate | Classification | Rationale | Test result |
| --- | --- | --- | --- |
| Python idioms | reference-only | Language knowledge consumed by coding situations. | Reclassified to reference. |
| TypeScript strictness | reference-only | Language knowledge consumed by frontend/API situations. | Reclassified to reference. |
| Oracle SQL | reference-only pending location | Shared DB/query knowledge; operator must decide whether it lives in `aegis-core`, MDCS, or both. | Reclassified to reference; location unresolved. |

## Create-Now Candidates Requiring Operator Evidence

- `training-run-diagnostics`
- `model-calibration-review`
- `backtest-validation`
- `risk-metric-reconciliation`
- `portfolio-rebalancing-review`
- `investment-thesis-evidence-check`
- `frontend-component-implementation`
- `accessibility-audit`
- `deployment-failure-triage`
- `cloud-iam-change-review`

## Deferred Candidates

- `hyperparameter-tuning`: defer until an actual recurring failure is named.
- `signal-generation`: too broad; needs a concrete situation.
- `portfolio-construction`: too broad unless narrowed to one repeated workflow.
- `design-system-update`: plausible but needs boundary against component implementation.
- `cost-optimization-review`: plausible but needs an observed failure mode.
- `database-migration`: already identified, but should be created only after a real DB migration failure is confirmed.
- `auth-boundary-change`: high-value, but still needs a recent confirmed failure example.

## Reference Folders Proposed

Reference home is not finalized. The proposed path is `skills/references/` pending operator confirmation.

- `skills/references/ml-evaluation/`
- `skills/references/quant-backtesting/`
- `skills/references/investment-management/`
- `skills/references/frontend-accessibility/`
- `skills/references/cloud-operations/`
- `skills/references/language-idioms/`
- `skills/references/oracle-sql/`

## Open Clarifications

1. For each create-now skill, has the named failure mode actually been encountered recently? Please provide one short example per confirmed skill.
2. For each area, what recurring real task is missing from this candidate list?
3. Should shared references such as Oracle SQL live in `aegis-core`, MDCS, or both?
4. Should language references be split by language immediately, or start as one `language-idioms` reference consumed by multiple procedures?
