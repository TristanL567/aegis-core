relevant-when: Open this drawer when query correctness depends on temporal or null semantics across dialects.

# Date Time And Null Semantics

- Date and timestamp types differ in stored precision, timezone handling,
  implicit casts, formatting, arithmetic, and driver conversion.
- Timestamp with timezone semantics vary by dialect; verify whether values are
  normalized, stored with zone labels, displayed in session timezone, or treated
  as local wall time.
- Date arithmetic should make units explicit: days, months, business calendars,
  intervals, month ends, daylight saving changes, and inclusive or exclusive
  boundaries.
- Null comparison requires `IS NULL` or dialect-safe null-aware logic. `= NULL`
  does not mean equality to missing value.
- Aggregates usually ignore nulls except where functions explicitly preserve or
  count them; this can change reconciliation totals.
- Empty strings, whitespace, zero values, and nulls are distinct in many systems
  but not always in Oracle character semantics.
- Backtest and migration queries should make effective-date, load-date,
  timezone, and missing-value conventions explicit.
