# Backend API Patterns Reference

## Scope

Reference scope: Axis-2 knowledge for backend API endpoint work, including
request and response contracts, validation boundaries, error semantics,
idempotency, pagination and filtering conventions, compatibility, and test
evidence expectations.

It is not a procedural skill and is not independently executable.

## Consuming Skills

- `new-api-endpoint`

## Sections

| id | topic | open when |
| --- | --- | --- |
| api-contracts | Request and response contract boundaries. | Open when endpoint work needs caller-visible request or response shape knowledge. |
| validation-and-errors | Boundary validation and error semantics. | Open when endpoint work needs invalid-input, auth, conflict, or server-error behavior guidance. |
| idempotency-pagination-compatibility | Idempotency, pagination, filtering, sorting, and compatibility. | Open when endpoint work includes retries, list endpoints, filters, sorting, versioning, or caller compatibility concerns. |
| endpoint-test-evidence | Endpoint test and contract evidence. | Open when endpoint completion evidence or review needs endpoint-level test coverage expectations. |

## Out Of Scope

- Workflow steps, activation rules, output contracts, or procedure behavior.
- Role prompt content or backend-worker routing.
- Database migrations, auth boundary redesign, infrastructure changes,
  frontend integration, or validator tooling.
