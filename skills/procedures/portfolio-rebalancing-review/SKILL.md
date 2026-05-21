---
trigger:
  - "A task asks to review, accept, reject, or qualify a portfolio rebalance suggestion, allocation update, target-weight correction, or drift-based trade plan."
  - "A rebalance looks mathematically reasonable from target weights or allocation drift before mandate, turnover, tax, liquidity, cash, and implementation constraints have been checked."
  - "A review must decide whether a proposed rebalance is actionable, constrained, or blocked."
non_trigger:
  - "The task is broad portfolio construction, strategic asset allocation design, optimization, manager selection, or investment advice."
  - "The task is trade execution guidance, order placement, broker routing, tax advice, or regulated advice."
  - "The task is investment thesis evidence review, risk metric reconciliation, full backtest validation, model work, backend, frontend, deployment, SQL, or chart artifact generation."
  - "The task is only explaining portfolio risk numbers without a rebalance suggestion; use risk-metric-reconciliation for that concern."
failure_modes_addressed:
  - "Rebalance suggestions ignore constraints, turnover, tax, mandate, or liquidity limits."
  - "A target-weight or drift-based rebalance is accepted before checking mandate limits, turnover, taxes, liquidity, cash needs, trading frictions, risk exposure, concentration, or implementation constraints."
attention_signals:
  - "Target weights, drift, tolerance bands, overweight or underweight positions, rebalance trades, cash flows, or allocation changes."
  - "Missing mandate, policy range, risk tolerance, benchmark, account constraints, tax lot, liquidity, transaction cost, or cash reserve evidence."
  - "Claims that a rebalance is optimal, actionable, or required based only on allocation math."
  - "Turnover, taxable accounts, illiquid positions, large trades, concentrated exposures, withdrawals, contributions, or reserve needs."
  - "Reference pointer conditions for mandate, allocation drift, trading frictions, risk exposure, and cash-flow implementation."
procedure:
  - "Classify the work as portfolio rebalance review rather than portfolio construction, trade execution, investment advice, or risk metric reconciliation."
  - "Inventory the proposed rebalance, current and target weights, drift, policy ranges, mandate, account constraints, costs, taxes, liquidity, risk exposures, and cash needs."
  - "Open the matching investment-management drawers from reference_pointers when mandate, drift, cost, tax, liquidity, risk, or cash-flow context needs reference knowledge."
  - "Check whether the rebalance is supported after constraints, turnover, tax impact, liquidity, cash needs, implementation limits, and risk exposure tradeoffs are considered."
  - "Separate actionable rebalance elements from blocked, constrained, or evidence-insufficient elements."
  - "Report review status, tradeoffs, required confirmations, and excluded concerns."
scope_boundary:
  - "Covers review of a proposed rebalance for mandate fit, allocation drift, thresholds, turnover, taxes, liquidity, transaction costs, cash-flow needs, risk exposure, concentration, and implementation constraints."
  - "Covers qualifying whether a rebalance suggestion is actionable, constrained, blocked, or needs more evidence."
  - "Does not cover broad portfolio construction, strategic allocation design, optimization, trade execution guidance, tax advice, regulated investment advice, or order placement."
  - "Does not cover investment thesis evidence review, full backtest validation, risk metric reconciliation beyond rebalance context, model procedures, backend, frontend, deployment, SQL, or charting work."
composition_points:
  - "reference_pointers bind this procedure to investment-management drawers for mandate, allocation drift, transaction costs and taxes, risk exposure, and cash-flow implementation."
  - "Risk-metric-reconciliation owns comparing risk numbers when the issue is metric comparability rather than rebalance actionability."
  - "Future investment-thesis-evidence-check owns evidence for security-level thesis claims discovered during rebalance review."
  - "Backtest-validation owns leakage, timing, cost, and evidence checks for strategy backtests, not portfolio rebalance actionability."
  - "Chart-artifact-generation owns auditable chart artifacts when rebalance review requires producing a visualization."
reference_pointers:
  - ref: investment-management
    section: portfolio-policy-and-mandate
    open_when: "Open when portfolio objective, benchmark, risk tolerance, constraints, account purpose, or mandate boundaries affect the rebalance."
  - ref: investment-management
    section: allocation-drift-and-thresholds
    open_when: "Open when current versus target weights, policy ranges, tolerance bands, drift, or rebalance urgency need review."
  - ref: investment-management
    section: transaction-costs-taxes-liquidity
    open_when: "Open when turnover, tax lots, realized gains or losses, spreads, transaction costs, liquidity, or implementation frictions affect actionability."
  - ref: investment-management
    section: risk-exposure-and-concentration
    open_when: "Open when factor, sector, issuer, currency, duration, leverage, liquidity, or concentration exposure changes affect the rebalance tradeoff."
  - ref: investment-management
    section: cash-flow-and-implementation
    open_when: "Open when contributions, withdrawals, cash buffers, settlement, sequencing, or practical implementation constraints affect the rebalance."
verification:
  - "Verify constraints are reviewed or explicitly missing, including mandate, policy ranges, risk tolerance, account limits, benchmark, and permitted instruments."
  - "Verify tradeoffs are reviewed or explicitly missing, including turnover, taxes, transaction costs, liquidity, cash needs, implementation limits, and risk exposure changes."
  - "Verify the rebalance decision is not based only on target-weight math or drift when constraints and implementation evidence are unresolved."
  - "Verify blocked or constrained rebalance elements are named, and required user or owner confirmations are listed before actionability is claimed."
  - "Verify excluded concerns such as portfolio construction, trade execution guidance, investment advice, thesis review, and risk metric reconciliation are not handled inside this procedure."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "rebalance_reviewed: current allocation, target allocation, drift, proposed trades, and source artifact reviewed."
  - "constraint_review: mandate, policy range, risk tolerance, account, benchmark, and permitted-instrument constraints found or missing."
  - "tradeoff_review: turnover, tax, transaction cost, liquidity, cash-flow, implementation, and risk-exposure tradeoffs found or missing."
  - "actionability_decision: actionable, actionable_with_limits, blocked, or not_applicable with concise rationale."
  - "required_confirmations: user, owner, tax, liquidity, mandate, or implementation confirmations needed before treating the rebalance as actionable."
  - "excluded_concerns: portfolio construction, trade execution, investment advice, investment thesis review, risk metric reconciliation, charting, or other work left to owning procedures or roles."
---

# Portfolio Rebalancing Review

Use this procedure when a proposed portfolio rebalance must be reviewed before it is treated as actionable. It exists to prevent the confirmed failure mode where rebalance suggestions ignore constraints, turnover, tax, mandate, or liquidity limits.

Open only the needed `investment-management` drawers through `reference_pointers`. Keep detailed investment-management knowledge in the drawers and keep this procedure focused on constraints and tradeoffs: mandate, drift, costs, taxes, liquidity, cash needs, implementation limits, and risk exposure.
