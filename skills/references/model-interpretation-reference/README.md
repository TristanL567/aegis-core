# Model Interpretation Reference

## Scope

Reference scope: Axis-2 knowledge for interpreting model outputs, including
uncertainty, feature effects, causal caution, evidence boundaries, and domain
interpretation limits used by future interpretation procedures.

It is not a procedural skill and is not independently executable. The
consuming skill is `model-output-interpretation`.

## Interpretation Knowledge

- Treat model output as evidence with uncertainty, not as a direct statement of
  ground truth. Preserve confidence intervals, credible intervals, prediction
  intervals, calibration evidence, or other uncertainty estimates when present.
- Distinguish fitted associations from causal claims. Do not imply causality
  from predictive importance, correlations, coefficients, SHAP values, partial
  dependence, or counterfactual-style displays unless the study design supports
  that claim.
- Explain feature effects in the scale and context of the model output. Name
  whether effects are marginal, conditional, local, global, linearized,
  transformed, standardized, or otherwise dependent on modeling assumptions.
- Keep interpretation tied to the population, time period, sampling frame,
  label definition, and feature construction used by the model. Note when a
  conclusion may not transfer to adjacent domains or future data.
- Surface model limitations that materially affect interpretation, including
  missingness, leakage risk, proxy variables, class imbalance, extrapolation,
  weak calibration, sparse segments, or unstable feature attribution.
- Separate statistical explanation from domain judgment. Domain conclusions
  should be marked as interpretation bounded by the available evidence, not as
  policy, clinical, legal, financial, or operational advice by default.
- Preserve disagreement between metrics, diagnostics, and narrative claims.
  When evidence conflicts, report the conflict rather than smoothing it into a
  single confident explanation.

## Out Of Scope

- Activation rules, workflow steps, output contracts, or procedure behavior.
- Role prompt content or model-interpreter-worker routing.
- Model training, tuning, calibration repair, leakage investigation, or
  validation tooling.
