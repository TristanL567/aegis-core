relevant-when: Open this drawer when reconciling reported performance or risk metrics across artifacts.

# Performance Risk Metrics

- Return metrics should state compounding convention, annualization factor,
  cash treatment, leverage, and whether returns are gross, net, excess, total,
  simple, or log.
- Volatility, Sharpe, Sortino, information ratio, beta, alpha, tracking error,
  drawdown, VaR, and CVaR measure different risk surfaces and should not be
  treated as interchangeable.
- Annualization assumes a frequency and dependence structure. Serial
  correlation, overlapping returns, illiquidity, and volatility clustering can
  make square-root-time scaling misleading.
- Drawdown metrics depend on path, compounding, horizon, and valuation
  frequency. Two strategies with similar volatility can have materially
  different drawdown profiles.
- VaR and CVaR estimates depend on distributional assumptions, lookback window,
  confidence level, horizon, and tail sample size. Tail metrics are unstable
  when extreme events are sparse.
- Metric reconciliation should check units, date ranges, missing-period
  treatment, benchmark excess-return construction, and whether reported
  statistics are before or after costs.
