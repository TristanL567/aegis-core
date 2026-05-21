---
trigger:
  - "A task asks to validate, review, trust, compare, or report a trading strategy, factor model, volatility strategy, option strategy, or portfolio signal backtest."
  - "Backtest results look profitable, statistically strong, or decision-ready before leakage, timing, transaction costs, data assumptions, and query semantics have been checked."
  - "A review must decide whether a backtest result is supported by reproducible evidence rather than lookahead, bad costs, timing errors, or SQL behavior."
non_trigger:
  - "The task is signal generation, strategy ideation, alpha research, model-family design, or portfolio construction before a backtest result exists."
  - "The task is risk metric reconciliation across already-produced artifacts without validating the backtest setup; use future risk-metric-reconciliation for that concern."
  - "The task is database migration, SQL skill creation, stochastic-volatility modeling, option-pricing model construction, or execution system implementation."
  - "The task is investment thesis review, portfolio rebalancing review, model calibration, model interpretation, backend, frontend, deployment, or chart artifact generation."
failure_modes_addressed:
  - "AI accepts backtest results despite leakage, bad costs, or timing errors."
  - "Backtest profitability or statistical strength is trusted before checking future information, wrong timestamps, survivorship bias, transaction costs, execution assumptions, data assumptions, or Oracle SQL and PostgreSQL query semantics."
attention_signals:
  - "Strong returns, Sharpe, drawdown, hit rate, p-values, rank performance, factor spread, or option strategy result presented as valid without validation evidence."
  - "Possible lookahead leakage, data availability timing mismatch, survivorship bias, restatements, full-sample transforms, or broken train/test or walk-forward boundaries."
  - "Missing transaction costs, slippage, spread, borrow, liquidity, market impact, rebalance timing, benchmark comparison, or robustness evidence."
  - "SQL queries, Oracle SQL, PostgreSQL, date handling, row limiting, null semantics, joins, or pagination that could alter the historical dataset."
  - "Reference pointer conditions for backtest design, data timing, costs, benchmarks, stochastic volatility, option pricing, and SQL dialect semantics."
procedure:
  - "Classify the work as validation of an existing backtest result rather than signal generation, model-family design, or database migration."
  - "Inventory the backtest claim, dataset, query source, timestamp assumptions, sample window, split or walk-forward logic, benchmark, costs, execution assumptions, and reported metrics."
  - "Open the matching quant-backtesting and sql-dialects drawers from reference_pointers when validation needs domain or dialect reference knowledge."
  - "Check leakage, information timing, survivorship, split boundaries, SQL semantics, transaction costs, execution assumptions, benchmark comparison, and statistical evidence."
  - "Separate supported backtest evidence from unresolved validation gaps and reject or qualify results that fail timing, leakage, cost, or evidence checks."
  - "Report validation status, blocking issues, residual assumptions, and excluded concerns."
scope_boundary:
  - "Covers validation of existing backtest results for timing, leakage, data assumptions, costs, execution assumptions, benchmark comparison, statistical evidence, and query semantics."
  - "Covers opening Oracle SQL or PostgreSQL drawers when dialect behavior may affect the dataset or historical evidence."
  - "Does not cover signal-generation, strategy ideation, stochastic-volatility skill creation, option-pricing skill creation, SQL skill creation, database migration implementation, or trading recommendations."
  - "Does not cover risk metric reconciliation after validation, portfolio rebalancing, investment thesis review, model calibration, model interpretation, backend, frontend, deployment, or chart artifact generation."
composition_points:
  - "reference_pointers bind this procedure to quant-backtesting drawers for design, timing, costs, benchmarks, stochastic volatility, and option-pricing context."
  - "reference_pointers bind this procedure to sql-dialects drawers for Oracle SQL, PostgreSQL, date/time/null semantics, and query portability when query behavior may affect evidence."
  - "Future risk-metric-reconciliation owns reconciliation of reported risk metrics across artifacts once the underlying backtest validation scope is clear."
  - "Future database-migration owns schema and migration implementation; this procedure only reviews SQL semantics as evidence risk for a backtest."
  - "Chart-artifact-generation owns auditable chart artifacts when backtest validation requires producing a visualization."
reference_pointers:
  - ref: quant-backtesting
    section: backtest-design
    open_when: "Open when validating the backtest objective, sample window, benchmark, comparability, or design claim."
  - ref: quant-backtesting
    section: data-and-lookahead-integrity
    open_when: "Open when data timing, lookahead leakage, survivorship, restatements, splits, or walk-forward boundaries may affect results."
  - ref: quant-backtesting
    section: transaction-costs-and-execution
    open_when: "Open when fees, spread, slippage, market impact, borrow, liquidity, rebalance timing, or execution assumptions may change returns."
  - ref: quant-backtesting
    section: benchmark-and-statistical-evidence
    open_when: "Open when benchmark comparison, multiple testing, uncertainty, robustness, or statistical support must be checked."
  - ref: quant-backtesting
    section: stochastic-volatility-context
    open_when: "Open when volatility assumptions, volatility targeting, regimes, or heteroskedasticity affect validation."
  - ref: quant-backtesting
    section: option-pricing-context
    open_when: "Open when option payoff, Greeks, implied volatility, contract selection, or option execution assumptions affect validation."
  - ref: sql-dialects
    section: oracle-sql
    open_when: "Open when Oracle SQL syntax, functions, row limiting, sequences, empty-string behavior, or optimizer context may affect the dataset."
  - ref: sql-dialects
    section: postgresql
    open_when: "Open when PostgreSQL syntax, functions, identity, JSON, arrays, extensions, or planner behavior may affect the dataset."
  - ref: sql-dialects
    section: date-time-and-null-semantics
    open_when: "Open when date, timestamp, timezone, interval, null, or empty-string behavior may affect historical timing or query correctness."
  - ref: sql-dialects
    section: query-portability
    open_when: "Open when cross-dialect query shape, row limiting, analytic functions, pagination, or migration checks may affect evidence."
verification:
  - "Verify timing and leakage: data availability, timestamps, train/test or walk-forward boundaries, survivorship, restatements, and full-sample transforms are checked or explicitly unresolved."
  - "Verify costs and execution: fees, spread, slippage, borrow, liquidity, market impact, rebalance timing, and fill assumptions are checked or explicitly unresolved."
  - "Verify result evidence: benchmark comparison, reported metrics, statistical evidence, robustness, and sample-window support are checked before accepting the result."
  - "Verify query semantics: Oracle SQL or PostgreSQL behavior, date/time/null handling, joins, row limiting, and portability concerns are checked when SQL built the dataset."
  - "Verify unsupported results are qualified or rejected rather than treated as investment-ready."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "validated_backtest: strategy, dataset, sample window, benchmark, query source, and reported metrics reviewed."
  - "timing_leakage_review: lookahead, data availability, split or walk-forward, survivorship, restatement, and timestamp findings."
  - "cost_execution_review: transaction cost, slippage, spread, borrow, liquidity, market impact, and execution assumption findings."
  - "query_semantics_review: Oracle SQL, PostgreSQL, date/time/null, join, row limiting, or portability findings when relevant."
  - "result_evidence: benchmark, statistical evidence, robustness, and residual assumptions supporting or weakening the result."
  - "validation_decision: accepted_with_limits, blocked, rejected, or not_applicable with concise rationale."
  - "excluded_concerns: signal generation, stochastic-volatility skill, option-pricing skill, SQL skill, database migration, risk reconciliation, charting, or investment workflow concerns left to owning procedures or roles."
---

# Backtest Validation

Use this procedure when an existing backtest result must be validated before it is trusted. It exists to prevent the confirmed failure mode where AI accepts backtest results despite leakage, bad costs, or timing errors.

Open only the needed `quant-backtesting` and `sql-dialects` drawers through `reference_pointers`. Keep detailed quant, SQL, option-pricing, and stochastic-volatility knowledge in the drawers and keep this procedure focused on validation: timing, leakage, costs, query semantics, benchmark evidence, and result support.
