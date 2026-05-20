relevant-when: Open this drawer when simulated returns depend on implementability or trading-cost assumptions.

# Transaction Costs And Execution

- Net performance should account for commissions, fees, bid-ask spread,
  slippage, borrow costs, financing, taxes where relevant, and market impact
  when trade size is material.
- Cost assumptions should vary with asset class, liquidity, volatility, trade
  size, venue, order type, and historical period rather than defaulting to a
  single universal haircut.
- Rebalance assumptions need implementable timing: signal timestamp, order
  submission time, fill price convention, market close or next open, and partial
  fill handling.
- Liquidity constraints should cover volume participation, turnover, capacity,
  borrow availability, short-sale restrictions, contract expiry, and minimum lot
  or contract sizing.
- High turnover can convert a statistically attractive signal into an
  uneconomic strategy; reconcile turnover, holding period, and expected edge
  before accepting net performance.
- Execution assumptions are part of the evidence surface. If they are omitted,
  reported returns should be interpreted as idealized gross returns.
