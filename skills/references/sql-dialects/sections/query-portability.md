relevant-when: Open this drawer when a query or migration needs cross-dialect compatibility review.

# Query Portability

- Portable SQL should avoid dialect-specific functions unless the dialect
  dependency is deliberate and documented.
- Common portability risks include date arithmetic, string concatenation,
  regular expressions, row limiting, generated keys, temporary tables, analytic
  functions, merge or upsert behavior, and JSON handling.
- Pagination and ordering must be deterministic. Sorting by nonunique columns
  without a tie-breaker can produce unstable pages and validation differences.
- Common table expressions may be optimized differently across dialects; verify
  whether they act as optimization fences or inlineable query blocks.
- Analytic functions are widely available but differ in default frames, null
  ordering, ordered-set aggregates, and function availability.
- Migration checks should compare row counts, checksums, null counts, boundary
  dates, duplicate keys, constraint violations, and representative query
  outputs.
- Project-private schemas, credentials, connection strings, and environment
  details do not belong in this reference.
