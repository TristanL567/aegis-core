---
trigger:
  - "A task asks to diagnose a training run, model performance issue, failed experiment, surprising metric movement, or degraded model result before changing modeling code."
  - "A proposed fix would expand feature engineering, alter model logic, tune parameters, or change training code before data, split, metric, config, and run evidence have been inspected."
  - "A review must check whether training-run changes are supported by run evidence rather than premature modeling expansion."
non_trigger:
  - "The task is only to interpret already-finalized model output for narrative explanation; use model-output-interpretation for that concern."
  - "The task is calibration reliability, threshold choice, or probability quality review; use future model-calibration-review for that concern."
  - "The task is hyperparameter tuning, model-family selection, architecture design, or feature ideation after diagnostics are already complete."
  - "The task is backend endpoint, frontend component, chart artifact, SQL dialect, deployment, or investment workflow work."
failure_modes_addressed:
  - "Model code is changed before data, metrics, config, and run evidence are diagnosed."
  - "The agent expands feature categories for time dynamics, cross-sectional rankings, interactions, or effects before checking split logic, metric behavior, run configuration, or the user's intended modeling direction."
attention_signals:
  - "Requests to add features, change model code, tune parameters, or expand the feature space while the cause of a training issue is still unclear."
  - "Evidence gaps around train, validation, test, time, group, leakage, metric definition, baseline comparison, configuration, seed, data extract, or run artifact identity."
  - "Metric movement that may come from split changes, data leakage, segment shifts, label changes, run configuration drift, or incomparable evaluation windows."
  - "Feature engineering growth that makes the run harder to inspect or exceeds the user's confirmed modeling intent."
  - "Reference pointer conditions for metric choice, run health, data split integrity, and segment evaluation."
procedure:
  - "Classify the work as training-run diagnostics and pause model-code or feature-space expansion until evidence has been inventoried."
  - "Inventory run artifacts: data version, split logic, config, seed, code version, metric definitions, baselines, logs, and generated outputs."
  - "Open the matching ml-evaluation drawers from reference_pointers when metric, run-health, split, or segment evidence needs reference knowledge."
  - "Compare the observed issue against data split behavior, metric comparability, configuration drift, run health signals, and segment-level evidence."
  - "Ask for or record user confirmation before recommending additional feature categories, model logic changes, or broader modeling direction."
  - "Produce a diagnosis-first report that separates supported fixes from unresolved evidence gaps and excluded modeling changes."
scope_boundary:
  - "Covers pre-change diagnosis of training-run issues through data split, metric, configuration, run artifact, baseline, and segment evidence."
  - "Covers preventing premature feature expansion when the run issue may come from split logic, metric setup, configuration drift, or unclear user modeling intent."
  - "Does not cover hyperparameter-tuning, model-family guidance, architecture selection, broad feature ideation, or implementing model-code changes after diagnosis."
  - "Does not cover calibration repair, threshold optimization, model output interpretation, chart artifact generation, backend, frontend, deployment, or investment procedures."
composition_points:
  - "reference_pointers bind this procedure to ml-evaluation drawers for metric selection, run health signals, data split integrity, and segment evaluation."
  - "Future model-calibration-review owns calibration reliability, probability quality, and threshold concerns discovered during diagnostics."
  - "Model-output-interpretation owns narrative explanation of finalized model output once diagnostic evidence is established."
  - "Chart-artifact-generation owns auditable chart artifacts when training diagnostics require producing a visualization artifact."
  - "Worker roles remain fallback routers for broader or ambiguous ML implementation work not covered by this procedure."
reference_pointers:
  - ref: ml-evaluation
    section: metric-selection
    open_when: "Open when diagnosing whether metric definition, baseline choice, averaging, objective fit, or comparability explains the training issue."
  - ref: ml-evaluation
    section: run-health-signals
    open_when: "Open when logs, curves, instability, overfit, underfit, checkpoint behavior, or run history need diagnostic interpretation."
  - ref: ml-evaluation
    section: data-split-integrity
    open_when: "Open when train, validation, test, time, group, leakage, preprocessing, or split boundaries may explain the result."
  - ref: ml-evaluation
    section: segment-evaluation
    open_when: "Open when aggregate metrics may hide class, subgroup, sparse-slice, or segment-level failures."
verification:
  - "Verify that the diagnostic report inventories data version, split logic, metric definitions, config, seed or run identity, baseline, and available logs or run outputs before recommending model-code changes."
  - "Verify that each proposed fix is mapped to observed evidence, and unresolved evidence gaps are labeled rather than patched over with feature expansion."
  - "Verify that premature feature categories, model logic changes, hyperparameter tuning, or model-family changes are deferred unless the user confirms that modeling direction after diagnostics."
  - "Verify that the report explicitly checks whether split logic, metric comparability, config drift, run health, or segment behavior could explain the issue."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "diagnostic_scope: training run, data version, split, config, metric, baseline, and run artifacts reviewed."
  - "evidence_inventory: available and missing data, split, metric, config, seed, logs, curves, and output evidence."
  - "diagnosis: supported explanation candidates and evidence gaps before any model-code or feature-space change."
  - "recommended_next_actions: evidence-backed fixes, checks, or user confirmations needed before modeling expansion."
  - "premature_change_guard: feature, model, tuning, or architecture changes deferred because diagnosis is incomplete or user intent is unconfirmed."
  - "excluded_concerns: calibration, model interpretation, hyperparameter tuning, model-family guidance, charting, backend, frontend, or deployment work left to owning procedures or roles."
---

# Training Run Diagnostics

Use this procedure when a training run or model performance problem must be diagnosed before changing model code or expanding feature engineering. It exists to prevent the confirmed failure mode where model code is changed before data, metrics, config, and run evidence are diagnosed.

Open only the needed `ml-evaluation` drawers through `reference_pointers`. Keep detailed ML evaluation knowledge in the drawers and keep the procedure focused on the diagnostic loop: inventory evidence, inspect split and metric comparability, check run health and segments, then recommend only evidence-backed next actions.
