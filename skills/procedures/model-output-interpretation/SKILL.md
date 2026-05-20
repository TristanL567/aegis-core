---
trigger:
  - "A task asks to interpret, explain, summarize, or narrate existing model output, diagnostics, feature effects, predictions, or attribution results."
  - "A model result needs an evidence-bound explanation that distinguishes observed model evidence from causal, domain, or operational claims."
  - "A review must check whether a written model interpretation overstates what the supplied model output supports."
non_trigger:
  - "The task is model training, model fitting, feature engineering, hyperparameter tuning, or architecture selection."
  - "The task is calibration repair, threshold tuning, probability recalibration, or metric optimization; use a future model-calibration-review procedure when that concern is present."
  - "The task is data leakage validation, train/test split review, reproducibility review, or ML validation; use future ML validation procedures for those concerns."
  - "The task is implementation of model-serving code, API wiring, frontend display, chart artifact generation, or broad report writing without interpretation ownership."
failure_modes_addressed:
  - "AI fabricates or smooths unsupported causal explanations from model output."
attention_signals:
  - "Model outputs, metrics, residuals, coefficients, feature importances, SHAP values, partial dependence, counterfactual displays, calibration evidence, prediction intervals, or confidence intervals."
  - "Narrative claims that use causal language such as caused, due to, drives, explains, impact, effect, or because without supporting design or evidence."
  - "Domain conclusions, policy recommendations, operational decisions, or risk statements that exceed the supplied model evidence."
  - "Uncertainty, segment size, sampling frame, time period, label definition, feature construction, missingness, leakage risk, extrapolation, calibration weakness, or conflicting diagnostics."
  - "Guidance from skills/references/model-interpretation-reference/README.md about uncertainty, feature effects, causal caution, evidence boundaries, and domain interpretation limits."
procedure:
  - "Confirm the task is interpretation of existing model output rather than model training, calibration, leakage validation, implementation, or broad reporting."
  - "Read the supplied model artifacts and identify the evidence available for interpretation: outputs, metrics, uncertainty estimates, feature effects, diagnostics, population, time period, and label or target definition."
  - "Consult skills/references/model-interpretation-reference/README.md for shared interpretation knowledge before drafting or reviewing claims."
  - "Separate directly supported observations from uncertainty, assumptions, caveats, domain inferences, and unsupported causal explanations."
  - "Rewrite or flag causal, domain, or operational claims that are not supported by the supplied evidence, using bounded language when only association or predictive evidence is available."
  - "Preserve conflicting evidence instead of smoothing it into a single confident narrative."
  - "Record excluded concerns discovered during interpretation, including model training, calibration, leakage validation, ML validation, implementation, chart generation, or report-writing work."
scope_boundary:
  - "Covers evidence-bound interpretation of existing model output, including uncertainty, feature effects, causal caution, unsupported-claim review, and interpretation caveats."
  - "Does not cover model training, model fitting, feature engineering, hyperparameter tuning, or model architecture selection."
  - "Does not cover calibration repair, probability recalibration, threshold tuning, or metric optimization."
  - "Does not cover data leakage validation, train/test split review, reproducibility review, ML validation procedures, implementation work, chart artifact generation, frontend embedding, or broad report writing."
composition_points:
  - "skills/references/model-interpretation-reference/README.md supplies Axis-2 knowledge for uncertainty, feature effects, causal caution, and domain interpretation boundaries."
  - "Future model-calibration-review procedure owns calibration repair, probability reliability review, and threshold or metric concerns discovered during interpretation."
  - "Future data-leakage-review and ML reproducibility procedures own leakage, split integrity, validation, and reproducibility concerns discovered during interpretation."
  - "Model-interpreter-worker may route applicable interpretation work to this procedure while remaining a fallback for broader or ambiguous model interpretation tasks."
  - "Chart-artifact-generation owns chart artifact creation when interpretation work requires producing or exporting a visualization artifact."
verification:
  - "Perform an evidence check that maps each substantive interpretation claim to supplied model output, diagnostics, uncertainty estimates, feature evidence, or explicitly stated assumptions."
  - "Manually review the final interpretation for unsupported causal claims, smoothed-over conflicts, overstated domain conclusions, and recommendations that exceed the model evidence."
  - "Confirm uncertainty, limitations, sampling frame, time period, label definition, and material caveats are preserved when present in the evidence."
  - "Confirm excluded concerns such as model training, calibration, leakage validation, and ML validation are named rather than silently handled inside this procedure."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "interpreted_artifacts: model outputs, metrics, diagnostics, attribution files, or result summaries interpreted."
  - "evidence_map: concise mapping from major interpretation claims to supporting evidence or assumptions."
  - "unsupported_claim_review: manual review result naming unsupported causal, domain, or operational claims removed, softened, or left unresolved."
  - "uncertainty_and_limits: uncertainty, caveats, sampling frame, time period, label definition, and material limitations preserved in the interpretation."
  - "excluded_concerns: model training, calibration, leakage validation, ML validation, implementation, charting, or report-writing concerns intentionally left to their owning procedure or role."
---

# Model Output Interpretation

Use this procedure when the work is to interpret existing model output without unsupported narrative overreach. Keep interpretation evidence-bound: distinguish observed model behavior from causal claims, domain judgment, and operational recommendations.

Consult `skills/references/model-interpretation-reference/README.md` for shared interpretation knowledge. This procedure does not own model training, calibration, leakage validation, ML validation, implementation work, chart artifact generation, or broad report writing.
