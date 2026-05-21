relevant-when: Open this drawer when interaction must work without a pointer or needs focus management review.

# Keyboard And Focus

- Every interactive control should be reachable and operable by keyboard unless
  it is intentionally hidden or disabled.
- Focus order should follow a predictable path that matches the visible layout
  and task flow.
- Focus indicators need to be visible against adjacent colors and should not be
  removed without an equivalent replacement.
- Dialogs, menus, popovers, and drawers often need focus placement on open,
  contained keyboard navigation while active, Escape handling where expected,
  and focus restoration on close.
- Composite widgets can use roving `tabindex` or `aria-activedescendant`, but
  the chosen pattern must align with the widget role and keyboard expectations.
- Pointer-only affordances such as hover controls, drag handles, and gesture
  actions need keyboard-accessible alternatives.
