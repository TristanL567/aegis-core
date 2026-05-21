relevant-when: Open this drawer when controls, icons, widgets, or regions need assistive technology semantics.

# Names States And ARIA

- Interactive controls need accessible names that explain their purpose in
  context. Icon-only controls usually need a programmatic label.
- Accessible descriptions should add useful context without duplicating visible
  text or creating noisy output.
- ARIA should fill semantic gaps, not override correct native HTML. Native
  semantics are usually more robust than recreating behavior with roles.
- State attributes such as `aria-expanded`, `aria-pressed`, `aria-selected`,
  `aria-current`, `aria-invalid`, and `aria-disabled` should reflect current UI
  state.
- Roles imply behavior. Adding a role without the expected keyboard interaction
  and state model can make a component more confusing than leaving it plain.
- Hidden content should use the correct hiding mechanism for the intent:
  visually hidden but available to assistive technology, fully hidden from all
  users, or inert while a modal context is active.
