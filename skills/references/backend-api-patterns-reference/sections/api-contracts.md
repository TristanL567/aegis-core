relevant-when: Open this drawer when endpoint work needs caller-visible request or response shape knowledge.

# API Contracts

- Request contracts should make the caller-visible boundary explicit: method,
  route or callable name, path variables, query parameters, headers, body
  schema, defaults, required fields, allowed values, and type coercion rules.
- Response contracts should name success status, response body shape,
  content type, empty-response behavior, pagination metadata, and relevant
  error response shapes.
