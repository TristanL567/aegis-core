# Reference Authoring Template

References hold Axis-2 knowledge. They are not procedural skills, role prompts,
or operating discipline. Author references as indexed drawer sets so procedures
can open only the sections they need.

## Required Layout

```text
skills/references/<reference-name>/
  README.md
  sections/
    <section-id>.md
```

The `README.md` file is the reference index. Files under `sections/` are
addressable section drawers.

## README.md Index Contract

The `README.md` index must declare the reference scope and consuming skills,
then include a Sections table with these columns:

| id | topic | open when |
| --- | --- | --- |
| example-section | What this drawer contains | Condition for opening it |

Every `id` in the Sections table must resolve to `sections/<id>.md`.

The `README.md` index budget is at most 120 lines.

## Section Drawer Contract

Each section drawer is at most 150 lines.

Each section drawer begins with a one-line `relevant-when` header:

```markdown
relevant-when: Open this drawer when the procedure needs the specific knowledge named here.
```

After the `relevant-when` header, include only the domain knowledge needed for
that drawer. Do not include triggers, procedure steps, role behavior, validator
rules, or material that belongs in another indexed drawer.

## Authoring Rules

- Keep the index concise enough to scan before opening drawers.
- Prefer several addressable drawers over one broad drawer when topics have
  different open-when conditions.
- Keep section ids lowercase, hyphenated, and stable.
- Do not duplicate detailed drawer content in the index.
- Do not use a reference without at least one named consuming skill.
