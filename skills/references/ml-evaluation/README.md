# ML Evaluation Reference

## Scope

Reference scope: Axis-2 knowledge for evaluating machine learning outputs,
training behavior, calibration evidence, data split integrity, segment
performance, and decision-threshold tradeoffs.

It is not a procedural skill and is not independently executable.

## Consuming Skills

- `training-run-diagnostics`: expected `reference_pointers` sections are
  `metric-selection`, `run-health-signals`, `data-split-integrity`, and
  `segment-evaluation`.
- `model-calibration-review`: expected `reference_pointers` sections are
  `calibration-evidence`, `segment-evaluation`,
  `threshold-and-decision-risk`, and `metric-selection`.

## Sections

| id | topic | open when |
| --- | --- | --- |
| metric-selection | Evaluation metric choice, baselines, and objective alignment. | Open when model quality must be interpreted through task, baseline, metric, or objective-fit evidence. |
| run-health-signals | Training curves, validation behavior, instability, and overfit or underfit evidence. | Open when a training run needs diagnostic interpretation from logged metrics or curves. |
| calibration-evidence | Probability calibration, reliability, and calibration diagnostics. | Open when predicted probabilities or confidence scores need calibration review. |
| data-split-integrity | Split hygiene, temporal leakage, group leakage, and evaluation-set validity. | Open when evaluation credibility depends on train, validation, test, time, group, or leakage boundaries. |
| segment-evaluation | Slice performance, class imbalance, sparse segments, and fairness-adjacent evidence. | Open when aggregate metrics may hide subgroup, class, or segment failures. |
| threshold-and-decision-risk | Decision thresholds, operating points, costs, and precision-recall tradeoffs. | Open when model evaluation depends on a thresholded decision or deployment operating point. |

## Out Of Scope

- Activation rules, workflow steps, output contracts, or procedural behavior.
- Model-family guidance, model architecture selection, training recipes, or
  hyperparameter tuning instructions.
- Role prompt content, validator tooling, deployment decisions, or production
  monitoring policy.
