relevant-when: Open this drawer when endpoint work needs invalid-input, auth, conflict, or server-error behavior guidance.

# Validation And Errors

- Validation belongs at the API boundary before data reaches business logic.
  Invalid path, query, header, and body input should produce predictable
  status codes and machine-readable error details where the project supports
  them.
- Error semantics should distinguish caller mistakes, authentication failures,
  authorization failures, missing resources, conflicts, rate limits, validation
  failures, and server faults without leaking sensitive internals.
