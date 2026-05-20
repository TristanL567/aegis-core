relevant-when: Open this drawer when validating whether a backtest design can support its stated claim.

# Backtest Design

- A backtest should name the hypothesis or decision claim it is meant to
  evaluate. A return series alone is not enough to establish what was tested.
- Define the trading universe, eligible instruments, sample period, rebalance
  schedule, signal timing, holding period, benchmark, and capital constraints.
- Keep in-sample development, validation, and final evaluation boundaries
  distinct. Reusing the final test window for strategy selection weakens the
  evidence, even when the reported metrics are calculated correctly.
- Benchmark selection should match the claim: cash, passive exposure, factor
  exposure, sector peer, or risk-matched baseline depending on what the
  strategy purports to improve.
- A strategy comparison is credible only when data frequency, rebalance timing,
  leverage, cash treatment, missing data policy, and risk budget are comparable.
- Report whether results are gross or net, annualized or period-specific,
  arithmetic or geometric, and whether returns are simple, log, excess, or total
  returns.
