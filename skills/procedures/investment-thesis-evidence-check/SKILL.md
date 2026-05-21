---
trigger:
  - "A task asks to review, accept, strengthen, summarize, or qualify an investment thesis, stock or fund note, sector view, or portfolio rationale."
  - "An investment narrative sounds persuasive before its claims are mapped to evidence, valuation support, fundamentals, counterevidence, risks, catalysts, and time horizon."
  - "A review must decide whether an investment thesis is evidence-supported, overstated, incomplete, or blocked by missing risk evidence."
non_trigger:
  - "The task is portfolio construction, allocation optimization, portfolio rebalancing, trade recommendation automation, order execution, or investment advice."
  - "The task is risk metric reconciliation, backtest validation, model calibration, model interpretation, training diagnostics, backend, frontend, deployment, SQL, or chart artifact generation."
  - "The task is only formatting or editing prose without responsibility for the evidence behind investment claims."
  - "The task is regulated advice, tax advice, legal advice, or suitability determination."
failure_modes_addressed:
  - "Investment narrative makes unsupported claims or omits risk evidence."
  - "An investment thesis is accepted or strengthened before checking source quality, valuation support, fundamentals, counterevidence, downside risk, catalysts, or time horizon."
attention_signals:
  - "Claims about upside, moat, growth, quality, valuation, margin expansion, turnaround, sector tailwind, catalyst, downside protection, or portfolio role."
  - "Missing citations, stale sources, management-only support, unsupported causal language, weak valuation bridge, or hidden assumptions."
  - "Omitted bear case, downside scenario, conflicting evidence, uncertainty, risk factors, or evidence that would break the thesis."
  - "Catalyst or timing claims without observable milestones or a horizon matched to the evidence."
  - "Reference pointer conditions for thesis evidence, valuation, risks, catalysts, and mandate context."
procedure:
  - "Classify the work as investment thesis evidence review rather than portfolio construction, trade recommendation, rebalancing, or regulated advice."
  - "Inventory the thesis claims, cited sources, valuation evidence, fundamental support, risks, counterevidence, catalysts, time horizon, and portfolio or mandate context."
  - "Open the matching investment-management drawers from reference_pointers when evidence, valuation, risk, catalyst, or mandate context needs reference knowledge."
  - "Map each substantive thesis claim to evidence, assumption, or unsupported status."
  - "Review valuation and fundamental support, contrary evidence, downside risk, catalyst observability, and time-horizon fit."
  - "Report supported claims, softened or removed claims, unresolved evidence gaps, and excluded concerns."
scope_boundary:
  - "Covers evidence review for investment theses, including claim-to-evidence mapping, source quality, valuation support, fundamentals, risk and counterevidence, catalysts, time horizon, and mandate context."
  - "Covers preventing unsupported investment narratives from being accepted, strengthened, or presented without material risk evidence."
  - "Does not cover portfolio construction, portfolio rebalancing, trade recommendation automation, order execution, investment advice, tax advice, legal advice, or suitability determination."
  - "Does not cover risk metric reconciliation, backtest validation, model procedures, backend, frontend, deployment, SQL, or charting work."
composition_points:
  - "reference_pointers bind this procedure to investment-management drawers for thesis evidence, valuation, risks, catalysts, and mandate context."
  - "Portfolio-rebalancing-review owns rebalance actionability when thesis review surfaces allocation changes."
  - "Risk-metric-reconciliation owns metric comparability when the thesis relies on risk figures."
  - "Backtest-validation owns strategy backtest evidence when a thesis relies on simulated trading results."
  - "Chart-artifact-generation owns auditable chart artifacts when thesis evidence review requires producing a visualization."
reference_pointers:
  - ref: investment-management
    section: thesis-claim-evidence
    open_when: "Open when mapping investment claims to cited evidence, source quality, assumptions, or unsupported status."
  - ref: investment-management
    section: valuation-and-fundamentals
    open_when: "Open when valuation support, fundamentals, growth, margins, balance sheet, comparables, or business quality affect the thesis."
  - ref: investment-management
    section: risk-and-counterevidence
    open_when: "Open when downside risk, bear case, uncertainty, conflicting evidence, or omitted counterevidence must be reviewed."
  - ref: investment-management
    section: catalysts-and-time-horizon
    open_when: "Open when catalyst observability, event timing, monitoring markers, or thesis horizon fit affect credibility."
  - ref: investment-management
    section: portfolio-policy-and-mandate
    open_when: "Open when portfolio objective, mandate, constraints, risk tolerance, or portfolio role affects thesis interpretation."
verification:
  - "Verify evidence-to-claim mapping: each substantive claim is linked to source evidence, explicit assumption, or unsupported status."
  - "Verify risk review: bear case, downside scenario, counterevidence, uncertainty, and material omitted risks are reviewed or explicitly missing."
  - "Verify valuation, fundamental support, catalyst observability, and time-horizon fit are reviewed before the thesis is strengthened or accepted."
  - "Verify unsupported or overstated claims are removed, softened, or flagged rather than smoothed into a confident narrative."
  - "Verify excluded concerns such as portfolio construction, trade recommendation automation, investment advice, rebalancing, and backtest validation are not handled inside this procedure."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "thesis_reviewed: investment thesis, note, rationale, sector view, or portfolio claim reviewed."
  - "evidence_map: substantive claims mapped to supporting evidence, assumptions, or unsupported status."
  - "valuation_fundamental_review: valuation and fundamental support found, missing, or insufficient."
  - "risk_counterevidence_review: risks, bear case, downside scenario, conflicting evidence, and omitted evidence found or missing."
  - "catalyst_horizon_review: catalyst observability, timing, monitoring markers, and thesis horizon fit."
  - "claim_decision: supported, supported_with_limits, blocked, or not_applicable with concise rationale."
  - "excluded_concerns: portfolio construction, trade recommendation, investment advice, rebalancing, risk reconciliation, backtest validation, charting, or other work left to owning procedures or roles."
---

# Investment Thesis Evidence Check

Use this procedure when an investment narrative must be checked before it is accepted or strengthened. It exists to prevent the confirmed failure mode where an investment narrative makes unsupported claims or omits risk evidence.

Open only the needed `investment-management` drawers through `reference_pointers`. Keep detailed investment-management knowledge in the drawers and keep this procedure focused on evidence-to-claim mapping, valuation and fundamental support, risk and counterevidence review, catalysts, and time horizon.
