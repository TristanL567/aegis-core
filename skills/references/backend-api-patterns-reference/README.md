# Backend API Patterns Reference

## Scope

Reference scope: Axis-2 knowledge for backend API endpoint work, including
request and response contracts, validation boundaries, error semantics,
idempotency, pagination and filtering conventions, compatibility, and test
evidence expectations.

It is not a procedural skill and is not independently executable. The
consuming skill is `new-api-endpoint`.

## API Pattern Knowledge

- Request contracts should make the caller-visible boundary explicit: method,
  route or callable name, path variables, query parameters, headers, body
  schema, defaults, required fields, allowed values, and type coercion rules.
- Response contracts should name success status, response body shape,
  content type, empty-response behavior, pagination metadata, and relevant
  error response shapes.
- Validation belongs at the API boundary before data reaches business logic.
  Invalid path, query, header, and body input should produce predictable
  status codes and machine-readable error details where the project supports
  them.
- Error semantics should distinguish caller mistakes, authentication failures,
  authorization failures, missing resources, conflicts, rate limits, validation
  failures, and server faults without leaking sensitive internals.
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
- API test evidence should cover the boundary: successful request behavior,
  request validation failure, expected error semantics, response shape, and any
  contract artifact or OpenAPI update the ticket owns.

## Out Of Scope

- Workflow steps, activation rules, output contracts, or procedure behavior.
- Role prompt content or backend-worker routing.
- Database migrations, auth boundary redesign, infrastructure changes,
  frontend integration, or validator tooling.
