---
trigger:
  - "A ticket or task asks for a new API endpoint, route, handler, controller action, RPC method, webhook receiver, or externally callable backend surface."
  - "An existing backend worker is implementing an API entry point and must decide the request contract, response contract, validation behavior, and endpoint-level tests."
  - "A code review or completion report claims a new API surface was added and endpoint behavior can be checked against request and response expectations."
non_trigger:
  - "The task only changes internal service logic, background jobs, data access helpers, or backend utilities without adding or changing an externally callable route surface."
  - "The task primarily changes database schema, migrations, persistence models, or seed data; use the future database-migration procedure when that concern is present."
  - "The task primarily changes authentication, authorization, permissions, tenancy boundaries, or access policy; use the future auth-boundary-change procedure when that concern is present."
  - "The task is broad backend implementation planning, infrastructure configuration, frontend integration, or API consumer work without endpoint ownership."
failure_modes_addressed:
  - "Hidden auth changes where a model adds, removes, weakens, or strengthens access behavior while presenting the work as a simple endpoint addition."
  - "Missing request validation where path parameters, query parameters, headers, and request bodies are accepted without explicit boundary checks."
  - "Unverified response shapes where status codes, success payloads, error payloads, and content types are not asserted or contract-checked."
  - "Route implementation without tests where a handler is wired but no focused endpoint test covers success, validation failure, and expected error behavior."
  - "Accidental database schema work where an endpoint task silently creates migrations, schema edits, or persistence model changes outside the endpoint surface."
attention_signals:
  - "Route names, HTTP methods, path patterns, RPC names, webhook topics, controller actions, handler files, router registration, and OpenAPI or contract references."
  - "Request boundary details including path variables, query parameters, headers, body fields, required fields, defaults, type coercion, and invalid-input behavior."
  - "Response boundary details including status codes, success payload fields, error shape, empty responses, pagination fields, and content type."
  - "Authentication, authorization, tenancy, ownership, role checks, or permission language that may indicate an auth-boundary-change concern rather than ordinary endpoint wiring."
  - "Migration files, schema declarations, ORM model changes, generated database artifacts, or persistence constraints that indicate a database-migration concern."
procedure:
  - "Confirm the task is specifically adding or changing an API endpoint surface, then identify the endpoint name, method, route path or callable name, owning handler, and caller-visible behavior."
  - "Separate endpoint surface work from excluded concerns before editing: database schema changes belong to the future database-migration procedure, and auth boundary changes belong to the future auth-boundary-change procedure."
  - "Define the request contract at the boundary, including accepted parameters, body shape, required fields, validation failures, and any existing framework validator or schema to use."
  - "Define the response contract, including success status, success payload shape, error status codes, error payload shape, and content type or serializer behavior."
  - "Wire the route using existing router, controller, handler, middleware, validation, and error-handling patterns already present in the codebase."
  - "Add focused endpoint tests or update existing endpoint-level tests for the normal case, request validation failure, and relevant response shape or status-code behavior."
  - "Check that no database schema files, migration files, auth policy files, or permission-boundary behavior changed unless a separate assigned procedure or ticket explicitly owns that work."
  - "Report the endpoint contract, tests run, request validation coverage, response shape checks, and any excluded concern handed to another procedure or role."
scope_boundary:
  - "Covers the narrow procedure for adding or changing one API endpoint surface: route registration, handler entry point, request validation, response shape, endpoint-level tests, and completion evidence."
  - "Does not cover database schema changes, migration files, persistence model ownership, seed data, or data backfill work."
  - "Does not cover auth boundary changes, new permission models, tenant isolation policy, access-control redesign, or security policy decisions."
  - "Does not replace the backend-worker role, general backend design, service-layer implementation discipline, infrastructure work, frontend work, or broad API architecture planning."
composition_points:
  - "Backend-worker composes with this procedure when the assigned backend task includes a new route or externally callable API surface."
  - "Future database-migration procedure owns database schema, migration, persistence model, seed, and backfill concerns that may be discovered while adding an endpoint."
  - "Future auth-boundary-change procedure owns authentication, authorization, tenancy, permission, and access-policy concerns that may be discovered while adding an endpoint."
  - "Ticket-scope-validation can verify that changed files stay inside the ticket envelope before endpoint completion evidence is trusted."
  - "Clean-commit can review staged endpoint files, validation evidence, and commit-message specificity after implementation is complete."
verification:
  - "Run the relevant endpoint unit, integration, or API test command for the changed route and report the exact command and result."
  - "Check request validation by testing or contract-checking at least one invalid request for required fields, type or format errors, and rejected unsupported input where applicable."
  - "Check response shape by asserting status code, required response fields, error payload shape, and content type or serializer output for the relevant success and failure paths."
  - "Inspect the changed-file list and confirm no database schema, migration, auth policy, permission boundary, or protected adjacent concern changed under this procedure."
  - "When an API contract artifact exists, compare the implemented route behavior against the documented or generated contract and update only endpoint-owned contract details if the ticket permits it."
output_contract:
  - "status: completed, blocked, or not_applicable."
  - "endpoint_surface: method and path, RPC name, webhook topic, or other externally callable route identifier."
  - "request_contract: parameters, body shape, validation behavior, and invalid-request evidence."
  - "response_contract: status codes, success shape, error shape, and response shape verification evidence."
  - "tests: exact endpoint test or contract-check commands run, results, and any skipped-command rationale."
  - "excluded_concerns: database-migration or auth-boundary-change items discovered and explicitly left for their owning procedure or role."
  - "changed_files_scope: confirmation that endpoint work did not include database schema changes, auth boundary changes, or unrelated backend role work."
---

# New API Endpoint

Use this procedure when a backend task adds or changes an externally callable API surface. It keeps the work centered on the route boundary: what request is accepted, how invalid requests are rejected, what response shape is returned, and which endpoint-level tests prove that behavior.

This procedure composes with `backend-worker` for implementation, but it is not a general backend checklist. If endpoint work reveals database schema or migration needs, hand that concern to a future `database-migration` procedure. If it reveals authentication, authorization, tenancy, or permission-boundary changes, hand that concern to a future `auth-boundary-change` procedure.

Completion evidence must name the endpoint surface, request validation behavior, response contract, relevant tests or contract checks, and excluded concerns that were intentionally left outside this procedure.
