relevant-when: Open this drawer when endpoint work depends on relational data access or query semantics.

# SQL Idioms

- SQL knowledge is reference material here, not a SQL procedural skill or a
  database migration procedure.
- Query shape should make cardinality, joins, filters, grouping, ordering, and
  pagination explicit.
- Null semantics are not the same as false, zero, or empty string. Comparisons,
  aggregates, unique constraints, and outer joins need deliberate null handling.
- Transactions should match the consistency requirement and keep the critical
  section no broader than necessary.
- Parameterized queries or structured query builders should be used at external
  input boundaries instead of string-built SQL.
- Index usefulness depends on predicates, join columns, sort order, selectivity,
  partial conditions, and whether the database can use the index for the query
  plan.
- Endpoint code should distinguish no rows, one row, many rows, constraint
  conflict, timeout, deadlock, and connectivity failure where behavior differs.
