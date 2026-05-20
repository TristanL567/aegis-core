relevant-when: Open this drawer when backtest evidence depends on historical data hygiene or information timing.

# Data And Lookahead Integrity

- Backtest inputs must respect information availability at the decision time:
  prices, fundamentals, constituents, macro series, analyst data, and risk-free
  rates all have publication or effective-date boundaries.
- Lookahead appears when future prices, revised values, final index membership,
  post-event classifications, or full-sample normalization influence historical
  decisions.
- Survivorship bias appears when delisted, merged, bankrupt, suspended, or
  otherwise inactive instruments are missing from the historical universe.
- Corporate actions, splits, dividends, contract rolls, ticker changes, and
  currency conversions need consistent treatment between signal generation and
  return measurement.
- Time-zone, market-close, stale-price, and holiday mismatches can create
  artificial predictability, especially across global assets or mixed-frequency
  data.
- Derived features should be fit or estimated only with data available up to the
  decision timestamp; full-sample scaling, smoothing, or imputation can leak
  future information.
