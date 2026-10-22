# AEGIS ticket format

A ticket lives in `.aegis/tickets/<ID>.yaml`.

```yaml
id: PROJ-012                  # uppercase letters, digits, hyphens; = file name
goal: The outcome, in one sentence.
context: >                    # why it matters, who it serves, and the design
  ...                         # intent or architecture boundary to keep
epic: null                    # epic ID if the ticket belongs to one
depends_on: []                # ticket IDs or conditions; [] means none
human_gates: []               # ticket, merge; [] means fully automatic
allowed_areas:                # the only paths you may change
  - .aegis/tickets/PROJ-012.yaml
  - src/billing/              # trailing / = directory prefix; no globs
  - tests/billing/test_invoice.py
must_not_touch:               # wins over allowed_areas
  - src/billing/migrations/
non_goals:                    # adjacent work that is explicitly out of scope
  - ...
acceptance_criteria:          # each one objectively checkable
  - ...
verify:                       # commands the validator runs
  - pytest tests/billing
smoke:                        # how to start the dev environment, then what
  - Start the app with npm run dev on a free port   # to check in it;
  - Open /invoices/42; every line shows its VAT     # [] if nothing runs
manual_checks: []             # ordered checks only a human can do
```

## Short ticket

When the whole change can be stated in one sentence, a short ticket is
enough: `id`, `goal`, `allowed_areas`, `acceptance_criteria` and `verify`;
add `non_goals` or `must_not_touch` only if a neighbour is at risk. It is
still validated:

```yaml
id: PROJ-013
goal: The footer links to the privacy page.
allowed_areas: [.aegis/tickets/PROJ-013.yaml, templates/footer.html]
acceptance_criteria: [The footer has a link to /privacy labelled "Privacy".]
verify: ['grep -q "href=\"/privacy\">Privacy<" templates/footer.html']
```

A design ticket (`kind: design`) adds `appetite`, `personas` and `tasks`;
see the `design-track` skill.
