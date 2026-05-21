relevant-when: Open this drawer when database behavior depends on write safety, contention, or transactional guarantees.

# Transactions And Concurrency

- Isolation levels with the same name can have different implementation details
  across dialects; review actual dirty read, nonrepeatable read, phantom, and
  serialization behavior.
- Locks can be row, page, table, advisory, metadata, predicate, or index-range
  related depending on dialect and query plan.
- DDL transactionality differs. Some systems auto-commit around DDL or restrict
  rollback behavior for schema changes.
- Upsert and merge semantics differ across `MERGE`, `ON CONFLICT`, unique
  constraints, trigger side effects, and concurrent insert behavior.
- Long transactions can hold locks, block vacuum or cleanup, retain undo, grow
  logs, or create stale read behavior.
- Migration review should consider lock duration, batch size, timeout policy,
  retry behavior, deadlock handling, and rollback path.
- Read replicas and replication lag can affect validation queries when writes
  and reads are split across endpoints.
