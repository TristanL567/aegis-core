relevant-when: Open this drawer when component or page accessibility depends on meaningful structure.

# Semantic Structure

- Prefer native HTML elements whose semantics match the job: `button` for
  actions, `a` for navigation, headings for hierarchy, lists for grouped items,
  and tables for tabular relationships.
- Landmark regions such as `header`, `nav`, `main`, `aside`, and `footer` help
  users move through a page when their labels and nesting are clear.
- Heading order should represent document structure rather than visual size.
  Skipped levels are not always fatal, but misleading hierarchy weakens
  navigation and comprehension.
- DOM order should match reading and interaction order. Visual rearrangement
  should not create a different meaning for keyboard or assistive technology
  users.
- Tables need explicit row and column relationships when data relationships are
  not obvious from simple structure.
- Avoid replacing semantic elements with generic containers unless the custom
  element supplies equivalent role, name, state, keyboard behavior, and focus
  handling.
