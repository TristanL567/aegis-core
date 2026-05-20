relevant-when: Open this drawer when model evaluation depends on a thresholded decision or deployment operating point.

# Threshold And Decision Risk

- Thresholded decisions should identify the operating point, metric tradeoff,
  and cost or risk rationale. A model score alone does not define an action.
- Precision, recall, specificity, sensitivity, false positive rate, false
  negative rate, and lift can move in opposite directions as thresholds change.
- Thresholds selected on validation data should be checked against independent
  test or holdout evidence when available.
- Decision thresholds can interact with calibration, prevalence shifts, segment
  performance, and operational capacity constraints.
