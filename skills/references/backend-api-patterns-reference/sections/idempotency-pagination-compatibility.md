relevant-when: Open this drawer when endpoint work includes retries, list endpoints, filters, sorting, versioning, or caller compatibility concerns.

# Idempotency, Pagination, And Compatibility

- Idempotency matters for retryable operations. Safe reads should avoid
  mutation, repeated create or update requests should have documented conflict
  or idempotency behavior, and webhook or external callbacks should account for
  duplicate delivery when applicable.
- Pagination, filtering, sorting, and search parameters should use existing
  project conventions and should state default limits, maximum limits, stable
  ordering, cursor or offset semantics, and how unsupported filters are handled.
- Compatibility should preserve existing callers unless the ticket explicitly
  owns a breaking change. Additive fields, versioned behavior, deprecation
  notes, and backwards-compatible defaults are preferable where the existing
  API contract requires stability.
