---
trigger:
  - "A task asks whether predicted probabilities, confidence scores, risk estimates, or probability bins are reliable for decision-making."
  - "A model has acceptable accuracy, AUC, rank, lift, or discrimination metrics, and those scores are being treated as evidence that probabilities are calibrated."
  - "A review must check whether probability-based thresholds, risk estimates, or confidence claims have calibration evidence."
non_trigger:
  - "The task is diagnosing a training run, split logic, run configuration, metric drift, or premature model-code changes; use training-run-diagnostics for that concern."
  - "The task is interpreting existing model output, feature effects, causal claims, or narrative explanations; use model-output-interpretation for that concern."
  - "The task is model training, model fitting, feature engineering, hyperparameter tuning, architecture selection, or model-family guidance."
  - "The task is implementing backend, frontend, charting, deployment, SQL, quant, or investment workflow behavior."
failure_modes_addressed:
  - "Accuracy or rank metrics are mistaken for probability calibration."
  - "Acceptable AUC, accuracy, or rank performance is treated as evidence that predicted probabilities are reliable confidence or risk estimates."
attention_signals:
  - "Claims that high accuracy, AUC, rank ordering, lift, or discrimination means predicted probabilities are trustworthy."
  - "Probability thresholds, risk scores, confidence labels, expected loss, alerting cutoffs, or downstream decisions based on predicted probability values."
  - "Missing reliability curves, calibration tables, probability bins, Brier score, calibration error, segment calibration, or threshold behavior evidence."
  - "Segment, prevalence, class imbalance, time-period, or decision-threshold differences that may make aggregate calibration misleading."
  - "Reference pointer conditions for calibration evidence, segment evaluation, threshold risk, and metric selection."
procedure:
  - "Classify the work as probability calibration review rather than training-run diagnostics, model interpretation, or model-code change."
  - "Inventory probability outputs, labels, evaluation split, general metrics, calibration evidence, threshold use, and segment evidence."
  - "Open the matching ml-evaluation drawers from reference_pointers when calibration, segment, threshold, or metric evidence needs reference knowledge."
  - "Separate discrimination evidence such as AUC or accuracy from calibration evidence such as reliability, Brier, bins, or calibration error."
  - "Review whether probability-based decisions are supported at the relevant threshold, segment, and data split."
  - "Report calibration status, evidence gaps, and decisions that should not rely on probability values until calibration is checked."
scope_boundary:
  - "Covers review of predicted probability reliability, calibration evidence, probability bins, Brier or calibration error, segment calibration, and threshold decision risk."
  - "Covers preventing accuracy, AUC, rank, lift, or discrimination metrics from being mistaken for probability calibration."
  - "Does not cover training-run diagnostics, split debugging, run configuration drift, premature feature expansion, or model-code changes."
  - "Does not cover narrative model interpretation, causal explanation, feature-effect explanation, model fitting, hyperparameter tuning, architecture selection, or calibration repair implementation."
composition_points:
  - "reference_pointers bind this procedure to ml-evaluation drawers for calibration evidence, segment evaluation, threshold and decision risk, and metric selection."
  - "Training-run-diagnostics owns run evidence, split logic, configuration, and pre-change diagnosis when the training issue itself is unclear."
  - "Model-output-interpretation owns evidence-bound narrative explanation of model outputs, feature effects, and unsupported causal claims."
  - "Future calibration-repair or threshold-tuning procedures may own implementation changes after this review identifies an evidence-backed need."
  - "Worker roles remain fallback routers for broader or ambiguous ML work not covered by this procedure."
reference_pointers:
  - ref: ml-evaluation
    section: calibration-evidence
    open_when: "Open when predicted probabilities, confidence scores, reliability curves, bins, Brier score, or calibration error need review."
  - ref: ml-evaluation
    section: segment-evaluation
    open_when: "Open when aggregate calibration or probability quality may hide subgroup, class, sparse-slice, or segment failures."
  - ref: ml-evaluation
    section: threshold-and-decision-risk
    open_when: "Open when downstream decisions depend on probability thresholds, operating points, prevalence, costs, or capacity."
  - ref: ml-evaluation
    section: metric-selection
    open_when: "Open when accuracy, AUC, rank, lift, or other general metrics need to be separated from calibration evidence."
verification:
  - "Verify that calibration evidence is present or explicitly missing, including reliability curve or table, probability bins, Brier score, calibration error, or equivalent manual calibration review."
  - "Verify that accuracy, AUC, rank, lift, or discrimination metrics are not used as substitutes for probability calibration evidence."
  - "Verify that threshold behavior and segment calibration are reviewed when probability-based decisions depend on them."
  - "Verify that excluded concerns such as training-run diagnostics, model interpretation, model-code changes, hyperparameter tuning, and calibration repair are named rather than handled inside this procedure."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "reviewed_artifacts: probability outputs, labels, metrics, calibration plots, bins, threshold artifacts, or segment summaries reviewed."
  - "calibration_evidence: reliability, bin, Brier, calibration error, or manual calibration review evidence found or missing."
  - "metric_boundary: statement separating discrimination or accuracy evidence from probability calibration evidence."
  - "threshold_and_segment_review: threshold behavior and segment calibration findings when relevant."
  - "risk_note: decisions, confidence claims, or risk estimates that should not rely on probabilities until calibration is supported."
  - "excluded_concerns: training diagnostics, model interpretation, model fitting, hyperparameter tuning, calibration repair, backend, frontend, charting, deployment, or other work left to owning procedures or roles."
---

# Model Calibration Review

Use this procedure when probability outputs must be reviewed for calibration before downstream decisions treat them as reliable confidence or risk estimates. It exists to prevent the confirmed failure mode where accuracy or rank metrics are mistaken for probability calibration.

Open only the needed `ml-evaluation` drawers through `reference_pointers`. Keep detailed calibration knowledge in the drawers and keep this procedure focused on the review loop: inventory probability evidence, separate discrimination from calibration, check thresholds and segments, then report supported calibration findings and gaps.
