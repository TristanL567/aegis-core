relevant-when: Open this drawer when framework implementation details affect the accessible behavior.

# Framework Accessibility Patterns

- Framework knowledge is reference material here, not a frontend, React, CSS, or
  accessibility procedural skill.
- Component abstractions should preserve native semantics and avoid hiding the
  element type or accessible name behind styling-only wrappers.
- React and similar frameworks need stable ids for label relationships,
  descriptions, controlled inputs, hydration, and server-rendered markup.
- Portals can change DOM location while preserving visual location; dialogs,
  popovers, and tooltips need explicit focus and ownership handling when
  rendered outside the visual parent.
- State-driven UI should keep ARIA states, disabled states, live text, and
  visible state synchronized.
- Component libraries should be verified in the exact composition used. A
  library primitive can be accessible alone and still fail after custom styling,
  slots, wrappers, or event overrides.
