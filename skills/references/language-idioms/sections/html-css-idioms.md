relevant-when: Open this drawer when frontend component work depends on markup or styling conventions.

# HTML CSS Idioms

- HTML and CSS knowledge is reference material here, not a frontend, CSS, or
  component procedural skill.
- Use semantic HTML before adding roles or custom interaction layers. Native
  controls usually provide stronger browser and accessibility behavior.
- CSS layout should state the relationship it is modeling: flow, grid, flex,
  absolute positioning, intrinsic sizing, containment, or responsive wrapping.
- Prefer stable sizing constraints for repeated UI elements so text, icons,
  loading states, and hover styles do not shift the layout unexpectedly.
- Keep visual state and DOM state aligned for disabled, selected, expanded,
  invalid, loading, and hidden UI.
- Responsive CSS should preserve readable order, usable target size, content
  visibility, and control availability across breakpoints.
- Styling hooks should avoid depending on fragile DOM depth when a component
  API, class, data attribute, or state variant is available.
