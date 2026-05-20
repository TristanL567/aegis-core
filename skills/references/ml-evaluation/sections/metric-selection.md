relevant-when: Open this drawer when model quality must be interpreted through task, baseline, metric, or objective-fit evidence.

# Metric Selection

- Metrics should match the task and decision surface. Classification,
  regression, ranking, forecasting, anomaly detection, and survival settings
  require different evidence.
- Compare model performance to simple baselines, prior models, business-as-usual
  rules, or chance levels before treating an absolute metric as meaningful.
- Report the metric direction, scale, averaging method, and target population.
  Macro, micro, weighted, top-k, and per-class metrics answer different
  questions.
- Prefer metrics aligned with the actual error cost. Accuracy can hide minority
  class failure, RMSE can overweight outliers, and aggregate loss can mask
  poor decision performance at the chosen operating point.
