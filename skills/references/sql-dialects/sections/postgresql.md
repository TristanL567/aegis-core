relevant-when: Open this drawer when SQL behavior depends on PostgreSQL conventions or migration into PostgreSQL constructs.

# PostgreSQL

- PostgreSQL knowledge is reference material here, not a PostgreSQL procedural
  skill.
- PostgreSQL has native `boolean`, `json`, `jsonb`, array, range, enum, UUID,
  generated column, and identity column support that may not map one-to-one
  from other dialects.
- Common PostgreSQL idioms include `COALESCE`, `NULLIF`, `RETURNING`,
  `DISTINCT ON`, `FILTER`, `ILIKE`, `ON CONFLICT`, common table expressions,
  and window functions.
- Identifier case is folded to lowercase unless quoted. Quoted identifiers are
  case-sensitive and can create portability friction.
- Pagination often uses `LIMIT` and `OFFSET`, but large offsets may be
  inefficient; keyset pagination can be more stable for ordered data.
- Extensions can add important behavior, but they are deployment dependencies
  and should be treated as part of the database contract.
- Query plans can depend on statistics, indexes, vacuum and analyze health,
  planner settings, partitioning, and parameter selectivity.
