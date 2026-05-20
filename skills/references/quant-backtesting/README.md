# Quant Backtesting Reference

## Scope

Reference scope: Axis-2 knowledge for quantitative backtesting and risk metric
reconciliation, including backtest design, time-series data integrity,
transaction costs, performance and risk metrics, statistical evidence,
stochastic volatility context, and option-pricing context.

It is not a procedural skill and is not independently executable.

## Consuming Skills

- `backtest-validation`: expected `reference_pointers` sections are
  `backtest-design`, `data-and-lookahead-integrity`,
  `transaction-costs-and-execution`, `benchmark-and-statistical-evidence`,
  `stochastic-volatility-context`, and `option-pricing-context`.
- `risk-metric-reconciliation`: expected `reference_pointers` sections are
  `performance-risk-metrics`, `benchmark-and-statistical-evidence`,
  `data-and-lookahead-integrity`, `stochastic-volatility-context`, and
  `option-pricing-context`.

## Sections

| id | topic | open when |
| --- | --- | --- |
| backtest-design | Backtest objective, hypothesis, sample window, benchmark, and comparability. | Open when validating whether a backtest design can support its stated claim. |
| data-and-lookahead-integrity | Time alignment, survivorship, restatement, leakage, and corporate-action boundaries. | Open when backtest evidence depends on historical data hygiene or information timing. |
| transaction-costs-and-execution | Fees, spreads, slippage, market impact, liquidity, and rebalance assumptions. | Open when simulated returns depend on implementability or trading-cost assumptions. |
| performance-risk-metrics | Return, drawdown, volatility, Sharpe, Sortino, VaR, CVaR, and exposure metrics. | Open when reconciling reported performance or risk metrics across artifacts. |
| benchmark-and-statistical-evidence | Baselines, multiple testing, uncertainty, confidence intervals, and robustness checks. | Open when a backtest claim needs benchmark comparison or statistical support. |
| stochastic-volatility-context | Volatility clustering, heteroskedasticity, regime changes, and volatility-model evidence boundaries. | Open when interpreting backtests or risk metrics that rely on stochastic volatility assumptions. |
| option-pricing-context | Greeks, implied volatility, moneyness, payoff shape, and option valuation evidence boundaries. | Open when interpreting option strategy backtests or option-derived risk metrics. |

## Out Of Scope

- Activation rules, workflow steps, output contracts, or procedural behavior.
- Model-family procedural skills; stochastic volatility and option-pricing
  knowledge remain reference drawers only.
- Trading recommendations, portfolio mandates, execution system design,
  production monitoring policy, or validator tooling.
