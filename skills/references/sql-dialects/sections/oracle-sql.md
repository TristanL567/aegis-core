relevant-when: Open this drawer when SQL behavior depends on Oracle SQL conventions or migration from Oracle-specific constructs.

# Oracle SQL

- Oracle SQL knowledge is reference material here, not a SQL procedural skill.
- Oracle treats the empty string as `NULL` for character values, which can
  change uniqueness, comparison, and migration behavior.
- Common Oracle functions include `NVL`, `DECODE`, `TO_DATE`, `TO_CHAR`,
  `TRUNC`, `ADD_MONTHS`, `MONTHS_BETWEEN`, and analytic functions with
  `OVER`.
- Row limiting may appear as `ROWNUM`, analytic ranking filters, or
  `FETCH FIRST` in newer versions; ordering must be applied at the correct
  query layer.
- Sequences are commonly accessed with `sequence_name.NEXTVAL`; identity
  columns are available in newer Oracle versions but legacy schemas often use
  explicit sequences and triggers.
- PL/SQL packages, procedures, exception handling, and autonomous transactions
  are Oracle-specific boundaries, not portable SQL features.
- Optimizer behavior can depend on statistics, hints, bind peeking, indexes,
  partitions, materialized views, and execution plan stability.
