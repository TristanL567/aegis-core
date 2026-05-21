---
trigger:
  - "A task asks to compare, reconcile, trust, summarize, or explain risk metrics across a portfolio, strategy, fund, report, backtest, or risk artifact."
  - "Volatility, drawdown, VaR, CVaR, beta, Sharpe, tracking error, exposure, or similar risk numbers are being treated as comparable before definitions, frequency, units, windows, benchmark basis, and assumptions are checked."
  - "A review must decide whether risk figures can support a conclusion about relative safety, performance, or exposure."
non_trigger:
  - "The task is validating a full backtest setup for leakage, timing, transaction costs, or query semantics; use backtest-validation for that concern."
  - "The task is portfolio construction, allocation optimization, portfolio rebalancing, or trade recommendation."
  - "The task is investment thesis evidence review, model calibration, model interpretation, training diagnostics, backend, frontend, deployment, SQL, or chart artifact generation."
  - "The task is creating new risk models, stochastic-volatility skills, option-pricing skills, or regulated investment advice."
failure_modes_addressed:
  - "Risk numbers are compared without matching definitions, frequency, or units."
  - "Volatility, drawdown, VaR, beta, Sharpe, tracking error, or exposure figures are trusted before checking metric definitions, annualization, input windows, benchmark basis, gross or net basis, currency, unit, or calculation assumptions."
attention_signals:
  - "Risk metrics from different reports, systems, strategies, funds, benchmarks, time windows, currencies, return frequencies, or gross/net bases."
  - "Annualized numbers, daily or monthly returns, log versus simple returns, excess versus total returns, benchmark-relative metrics, or unstated sample windows."
  - "Conflicting volatility, drawdown, VaR, CVaR, beta, Sharpe, tracking error, concentration, duration, leverage, or exposure values."
  - "Claims that one portfolio or strategy is safer, riskier, or better-performing based on unmatched risk figures."
  - "Reference pointer conditions for performance risk metrics, benchmark evidence, data windows, volatility or option assumptions, mandate context, and exposure concentration."
procedure:
  - "Classify the work as risk metric reconciliation rather than full backtest validation, portfolio construction, or rebalancing."
  - "Inventory each risk number, source artifact, date range, return frequency, annualization convention, unit, currency, benchmark, gross or net basis, and calculation method."
  - "Open the matching quant-backtesting and investment-management drawers from reference_pointers when metric, benchmark, data-window, exposure, or mandate context needs reference knowledge."
  - "Align or flag mismatches in metric definitions, frequency, annualization, units, sample windows, benchmark basis, input data, and assumptions."
  - "Separate comparable figures from unresolved or incomparable figures before drawing risk, safety, or performance conclusions."
  - "Report reconciliation status, remaining gaps, and excluded concerns."
scope_boundary:
  - "Covers reconciliation of reported risk metrics across artifacts by checking definitions, frequency, annualization, units, data windows, benchmark basis, gross or net basis, and calculation assumptions."
  - "Covers portfolio or strategy risk interpretation only to the extent needed to decide whether risk figures are comparable."
  - "Does not cover full backtest validation, leakage review, transaction-cost validation, signal generation, portfolio construction, portfolio rebalancing, or trading recommendations."
  - "Does not cover investment thesis review, model calibration, model interpretation, training diagnostics, SQL skill creation, stochastic-volatility skill creation, or option-pricing skill creation."
composition_points:
  - "reference_pointers bind this procedure to quant-backtesting drawers for performance risk metrics, benchmark evidence, data-window integrity, stochastic volatility context, and option-pricing context."
  - "reference_pointers bind this procedure to investment-management drawers for mandate context and risk exposure or concentration interpretation."
  - "Backtest-validation owns leakage, timing, transaction costs, execution assumptions, and SQL query semantics when the underlying backtest setup itself must be validated."
  - "Future portfolio-rebalancing-review owns allocation drift and trade decisions after risk figures are reconciled."
  - "Chart-artifact-generation owns auditable chart artifacts when reconciliation needs a visualization artifact."
reference_pointers:
  - ref: quant-backtesting
    section: performance-risk-metrics
    open_when: "Open when reconciling definitions, annualization, frequency, units, gross or net basis, volatility, drawdown, Sharpe, VaR, CVaR, beta, tracking error, or exposure metrics."
  - ref: quant-backtesting
    section: benchmark-and-statistical-evidence
    open_when: "Open when benchmark basis, excess returns, uncertainty, robustness, sample support, or statistical evidence affects comparability."
  - ref: quant-backtesting
    section: data-and-lookahead-integrity
    open_when: "Open when data windows, historical coverage, missing periods, timing, restatements, or sample boundaries affect metric reconciliation."
  - ref: quant-backtesting
    section: stochastic-volatility-context
    open_when: "Open when volatility clustering, horizon, frequency, or volatility-model assumptions affect risk metric interpretation."
  - ref: quant-backtesting
    section: option-pricing-context
    open_when: "Open when option Greeks, implied volatility, payoff shape, or option-derived risk metrics affect reconciliation."
  - ref: investment-management
    section: portfolio-policy-and-mandate
    open_when: "Open when portfolio objective, risk tolerance, benchmark, constraints, or mandate boundaries affect risk interpretation."
  - ref: investment-management
    section: risk-exposure-and-concentration
    open_when: "Open when factor, sector, issuer, currency, duration, leverage, liquidity, or concentration exposure affects risk comparison."
verification:
  - "Verify metric definitions are matched or flagged, including formula, return basis, benchmark basis, gross or net basis, and calculation method."
  - "Verify frequency and annualization are matched or flagged, including daily, monthly, period-specific, annualized, log, simple, total, or excess return conventions."
  - "Verify units, currency, data windows, sample periods, missing-period handling, and input data sources are matched or flagged."
  - "Verify conclusions compare only reconciled figures, and unresolved metric mismatches are reported rather than smoothed over."
  - "Verify excluded concerns such as full backtest validation, portfolio construction, portfolio rebalancing, and investment thesis review are named rather than handled inside this procedure."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "metrics_reviewed: risk figures, source artifacts, date ranges, units, and calculation methods inspected."
  - "definition_reconciliation: matched and mismatched metric definitions, formulas, benchmark basis, and gross or net basis."
  - "frequency_unit_reconciliation: matched and mismatched frequency, annualization, return convention, currency, and units."
  - "window_and_assumption_review: data windows, sample periods, input sources, missing-period handling, and material assumptions."
  - "comparison_decision: comparable, comparable_with_limits, blocked, or not_applicable with concise rationale."
  - "excluded_concerns: full backtest validation, portfolio construction, portfolio rebalancing, investment thesis review, charting, or other concerns left to owning procedures or roles."
---

# Risk Metric Reconciliation

Use this procedure when risk numbers must be reconciled before they are compared or trusted. It exists to prevent the confirmed failure mode where risk numbers are compared without matching definitions, frequency, or units.

Open only the needed `quant-backtesting` and `investment-management` drawers through `reference_pointers`. Keep detailed domain knowledge in the drawers and keep this procedure focused on matching metric definitions, annualization, frequency, units, windows, benchmark basis, and assumptions before drawing conclusions.
