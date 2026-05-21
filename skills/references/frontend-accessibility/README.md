# Frontend Accessibility Reference

## Scope

Reference scope: Axis-2 knowledge for accessible frontend component work and
accessibility review, including semantic structure, keyboard interaction,
focus management, names and descriptions, state communication, visual
perception, forms, dynamic content, and framework implementation boundaries.

It is not a procedural skill and is not independently executable.

## Consuming Skills

- `frontend-component-implementation`: expected `reference_pointers` sections
  are `semantic-structure`, `keyboard-and-focus`, `names-states-and-aria`,
  `forms-and-errors`, `visual-and-responsive-accessibility`, and
  `framework-accessibility-patterns`.
- `accessibility-audit`: expected `reference_pointers` sections are
  `semantic-structure`, `keyboard-and-focus`, `names-states-and-aria`,
  `dynamic-content-and-announcements`,
  `visual-and-responsive-accessibility`, and `audit-evidence`.

## Sections

| id | topic | open when |
| --- | --- | --- |
| semantic-structure | Landmarks, headings, native elements, lists, tables, and document order. | Open when component or page accessibility depends on meaningful structure. |
| keyboard-and-focus | Keyboard access, focus order, focus visibility, traps, and roving focus. | Open when interaction must work without a pointer or needs focus management review. |
| names-states-and-aria | Accessible names, descriptions, roles, states, properties, and ARIA limits. | Open when controls, icons, widgets, or regions need assistive technology semantics. |
| forms-and-errors | Labels, instructions, validation, error summaries, and required fields. | Open when form fields or user input flows need accessible feedback. |
| dynamic-content-and-announcements | Live regions, loading states, route changes, dialogs, and async updates. | Open when UI changes after load and users need perceivable status or context changes. |
| visual-and-responsive-accessibility | Contrast, text scaling, motion, target size, layout reflow, and responsive behavior. | Open when visual design or responsive states may block perception or operation. |
| framework-accessibility-patterns | React, component libraries, hydration, portals, refs, and state-driven accessibility boundaries. | Open when framework implementation details affect the accessible behavior. |
| audit-evidence | Manual checks, automated scan limits, assistive technology evidence, and issue reporting. | Open when accessibility findings need evidence, severity, or reproducible review notes. |

## Out Of Scope

- Activation rules, workflow steps, output contracts, or procedural behavior.
- Frontend, React, CSS, or accessibility procedural skill definitions.
- Brand design systems, visual polish standards, performance tuning, automated
  test tooling changes, role prompt content, or validator tooling.
