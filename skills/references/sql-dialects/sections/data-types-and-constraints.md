relevant-when: Open this drawer when database work depends on cross-dialect type or constraint behavior.

# Data Types And Constraints

- Type names that look similar across dialects may differ in precision,
  storage, comparison, casts, rounding, and default behavior.
- Numeric choices should account for scale, precision, overflow, monetary
  rounding, aggregate behavior, and driver mapping into application types.
- Text comparisons can differ by collation, case sensitivity, padding,
  character set, locale, and whether empty string is distinct from `NULL`.
- Boolean values may be native, numeric, character-coded, or constrained by
  convention depending on dialect and schema history.
- Identity, serial, sequence, trigger, and default-generated values differ in
  migration semantics and in how inserted keys are returned to application
  code.
- Constraints include primary key, foreign key, unique, check, not null,
  exclusion, deferrable, partial, expression, and generated-value boundaries.
- Constraint names, enforcement timing, and index coupling can affect migration
  rollback, error handling, and compatibility with application assumptions.
