relevant-when: Open this drawer when interpreting option strategy backtests or option-derived risk metrics.

# Option Pricing Context

- Option-pricing knowledge is reference knowledge here, not a standalone
  option-pricing skill or activation path.
- Option strategy backtests depend on payoff shape, moneyness, tenor, exercise
  style, contract multiplier, expiration handling, liquidity, and corporate
  action treatment.
- Greeks describe local sensitivities to underlying price, volatility, time,
  rates, and dividends; they do not by themselves establish full path risk or
  scenario behavior.
- Implied volatility, realized volatility, and model volatility are distinct.
  Reconciliation should state which volatility surface, date, maturity, strike,
  and interpolation convention is used.
- Pricing assumptions should name the model, inputs, dividend treatment,
  interest-rate curve, calendar conventions, and whether prices are mid, bid,
  ask, theoretical, or executable.
- Option backtests should account for spread, slippage, assignment or exercise,
  margin, funding, contract selection rules, and survivorship of listed
  contracts.
