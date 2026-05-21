relevant-when: Open this drawer when implementation details depend on TypeScript or JavaScript conventions.

# TypeScript JavaScript Idioms

- Prefer TypeScript types that express the boundary: request and response
  shapes, component props, nullable values, discriminated unions, and state
  transitions.
- Narrow unknown input before use. Runtime validation is still needed at
  external boundaries even when internal types are strong.
- Use async and promise handling consistently. Avoid unhandled promises and make
  cancellation or stale-result behavior explicit for user-facing flows.
- Prefer immutable updates for state that feeds rendering, memoization, or
  comparison logic.
- Keep modules cohesive: parsing, data access, rendering, state management, and
  formatting are easier to test when not fused into one function.
- Avoid relying on truthiness when `0`, empty string, `false`, or empty arrays
  are valid domain values.
- Use optional chaining and nullish coalescing when absence is expected, but do
  not hide required-data bugs behind broad fallback values.
