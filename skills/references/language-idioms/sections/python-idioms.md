relevant-when: Open this drawer when implementation details depend on Python conventions or backend Python code shape.

# Python Idioms

- Prefer clear module boundaries, small functions, explicit return values, and
  dependency injection where it keeps endpoint logic testable.
- Type hints should describe public interfaces and cross-module contracts.
  Avoid using `Any` or broad dictionaries when a dataclass, typed mapping, or
  framework schema already exists.
- Use exceptions for exceptional failures and explicit result values for
  expected business outcomes when that is the local pattern.
- Keep context managers around files, database sessions, locks, network clients,
  and other resources that need deterministic cleanup.
- Avoid mutable default arguments. Use `None` sentinels or factory helpers where
  a new collection is needed per call.
- Async Python code should avoid blocking calls inside event-loop paths unless
  the code intentionally delegates to a worker thread or process.
- Tests are easier to read when fixtures describe domain setup and assertions
  check behavior rather than implementation internals.
