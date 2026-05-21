# Language Idioms Reference

## Scope

Reference scope: Axis-2 knowledge for language-specific implementation idioms
used by backend endpoint and frontend component work, including Python,
TypeScript and JavaScript, SQL, HTML and CSS, and shell or configuration
boundary conventions.

languages are references only, not procedural skills or activation paths.

It is not a procedural skill and is not independently executable.

## Consuming Skills

- `new-api-endpoint`: expected `reference_pointers` sections are
  `python-idioms`, `typescript-javascript-idioms`, `sql-idioms`, and
  `shell-config-idioms`.
- `frontend-component-implementation`: expected `reference_pointers` sections
  are `typescript-javascript-idioms`, `html-css-idioms`, and
  `shell-config-idioms`.

## Sections

| id | topic | open when |
| --- | --- | --- |
| python-idioms | Python API, typing, errors, resource, and testability idioms. | Open when implementation details depend on Python conventions or backend Python code shape. |
| typescript-javascript-idioms | TypeScript and JavaScript module, typing, async, object, and UI state idioms. | Open when implementation details depend on TypeScript or JavaScript conventions. |
| sql-idioms | SQL query shape, joins, transactions, migrations, nulls, and performance boundaries. | Open when endpoint work depends on relational data access or query semantics. |
| html-css-idioms | HTML structure, CSS layout, styling, responsive behavior, and browser primitives. | Open when frontend component work depends on markup or styling conventions. |
| shell-config-idioms | Shell commands, environment variables, config files, scripts, and boundary quoting. | Open when implementation needs command, environment, or configuration conventions. |

## Out Of Scope

- Activation rules, workflow steps, output contracts, or procedural behavior.
- Python, TypeScript, SQL, frontend, CSS, or language procedural skills.
- Tooling changes, formatter configuration, package installation, role prompt
  content, validator changes, or provider-specific runtime docs.
