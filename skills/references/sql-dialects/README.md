# SQL Dialects Reference

## Scope

Reference scope: Axis-2 knowledge for SQL dialect differences used by
quantitative validation and future database migration work, including Oracle
SQL, PostgreSQL, type and null semantics, date and time behavior, transactions,
query portability, and migration-risk interpretation.

SQL dialects are reference knowledge only, not SQL skills or activation paths.

It is not a procedural skill and is not independently executable.

## Consuming Skills

- `backtest-validation`: expected `reference_pointers` sections are
  `oracle-sql`, `postgresql`, `date-time-and-null-semantics`, and
  `query-portability`.
- `database-migration`: expected `reference_pointers` sections are
  `oracle-sql`, `postgresql`, `data-types-and-constraints`,
  `transactions-and-concurrency`, and `query-portability`.

## Sections

| id | topic | open when |
| --- | --- | --- |
| oracle-sql | Oracle SQL syntax, functions, row limiting, sequences, PL/SQL boundaries, and optimizer context. | Open when SQL behavior depends on Oracle SQL conventions or migration from Oracle-specific constructs. |
| postgresql | PostgreSQL syntax, functions, identity, JSON, arrays, extensions, and optimizer context. | Open when SQL behavior depends on PostgreSQL conventions or migration into PostgreSQL constructs. |
| data-types-and-constraints | Numeric, text, boolean, identity, sequence, default, unique, and constraint differences. | Open when database work depends on cross-dialect type or constraint behavior. |
| date-time-and-null-semantics | Date, timestamp, interval, timezone, empty string, null, and comparison behavior. | Open when query correctness depends on temporal or null semantics across dialects. |
| transactions-and-concurrency | Isolation, locking, DDL transactionality, upsert, merge, and concurrency behavior. | Open when database behavior depends on write safety, contention, or transactional guarantees. |
| query-portability | Portable SQL shape, dialect-specific functions, pagination, analytic functions, and migration checks. | Open when a query or migration needs cross-dialect compatibility review. |

## Out Of Scope

- Activation rules, workflow steps, output contracts, or procedural behavior.
- SQL procedural skills, database migration procedures, runtime docs, project
  schemas, credentials, connection strings, or environment details.
- Tooling changes, role prompt content, validator changes, or private database
  implementation details.
