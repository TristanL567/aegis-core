relevant-when: Open this drawer when interpreting backtests or risk metrics that rely on stochastic volatility assumptions.

# Stochastic Volatility Context

- Stochastic volatility knowledge is reference knowledge here, not a standalone
  model-family skill or activation path.
- Volatility clustering, leverage effects, heteroskedasticity, jumps, and regime
  shifts can make constant-volatility assumptions understate risk or distort
  annualized metrics.
- GARCH-style models, stochastic volatility state-space models, realized
  volatility, and implied volatility each represent different evidence sources
  and measurement assumptions.
- Volatility estimates should be tied to horizon, sampling frequency, lookback
  window, decay rate, treatment of missing data, and whether returns overlap.
- Risk estimates based on volatility forecasts should be checked against
  realized drawdowns, tail events, and forecast-error behavior, not only average
  fit.
- Volatility-targeted strategies need clear leverage, rebalance, transaction
  cost, and capacity assumptions because turnover can rise during unstable
  regimes.
