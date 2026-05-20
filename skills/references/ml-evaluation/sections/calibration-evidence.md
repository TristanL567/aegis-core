relevant-when: Open this drawer when predicted probabilities or confidence scores need calibration review.

# Calibration Evidence

- Calibration concerns whether predicted probabilities match observed
  frequencies, not whether the ranking is good. A model can rank well and still
  be poorly calibrated.
- Use reliability curves, calibration tables, Brier score, expected calibration
  error, or observed-versus-predicted rates where available.
- Calibration should be assessed on held-out data that matches the deployment
  population. Calibration can drift across time, segments, prevalence regimes,
  and label definitions.
- Recalibration claims should distinguish evidence of miscalibration from the
  corrective method; this drawer only covers evaluation knowledge, not repair
  instructions.
