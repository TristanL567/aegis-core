relevant-when: Open this drawer when form fields or user input flows need accessible feedback.

# Forms And Errors

- Each input needs a persistent programmatic label, not only placeholder text.
- Instructions, constraints, units, examples, and required-field indicators
  should be available before the user submits.
- Error messages should identify the field, explain the problem, and provide a
  recovery path where possible.
- Error summaries help users understand page-level failure after submit,
  especially in long forms or multi-section flows.
- `aria-invalid`, `aria-describedby`, grouped labels, fieldsets, legends, and
  native validation states should match the visible form behavior.
- Dynamic validation should avoid stealing focus repeatedly; focus movement is
  most useful after submit or when a blocking error prevents progress.
