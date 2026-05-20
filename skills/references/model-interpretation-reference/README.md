# Model Interpretation Reference

## Scope

Reference scope: Axis-2 knowledge for interpreting model outputs, including
uncertainty, feature effects, causal caution, evidence boundaries, and domain
interpretation limits used by future interpretation procedures.

It is not a procedural skill and is not independently executable.

## Consuming Skills

- `model-output-interpretation`

## Sections

| id | topic | open when |
| --- | --- | --- |
| uncertainty-evidence | Uncertainty and model output as evidence. | Open when an interpretation needs uncertainty, intervals, calibration evidence, or evidence-strength boundaries. |
| causal-caution-feature-effects | Causal caution and feature effect explanations. | Open when an interpretation discusses coefficients, importance, SHAP, partial dependence, or causal-sounding claims. |
| population-and-limitations | Population, time period, sampling frame, feature construction, and model limitations. | Open when interpretation depends on transferability, data limits, extrapolation, leakage risk, or unstable attribution. |
| domain-boundaries-and-conflicts | Domain judgment boundaries and conflicting evidence. | Open when an interpretation makes domain, policy, operational, or narrative claims from model evidence. |

## Out Of Scope

- Activation rules, workflow steps, output contracts, or procedure behavior.
- Role prompt content or model-interpreter-worker routing.
- Model training, tuning, calibration repair, leakage investigation, or
  validation tooling.
