# Judge prompt

Give this to a fresh subagent (Sonnet 5.5), once per run. Never tell it which
arm produced the findings, and give it only the two files named below.

---

You are matching a usability tester's findings to an answer key of planted
flaws in a prototype. Read `<run>/findings.md` (the tester's numbered
findings), `evals/ux-test/flaws.yaml` (the key) and
`evals/ux-test/prototype/index.html` (the prototype's source, to check whether
a finding is true). Read no other file.

For every numbered finding, pick exactly one label:

- a flaw id (`F01`..`F10`) when the finding describes that flaw's problem at
  that location, even in other words. The finding must name the actual
  problem, not just the area: "the save button is hard to find" matches F01;
  "the form is confusing" matches nothing.
- `unplanted` when it describes a real, checkable problem in the prototype
  that is not in the key.
- `invalid` when it is wrong, not a usability problem, or too vague to act
  on.

If one finding covers two flaws, label it with the more severe one and note
the other in `why`. Then write `<run>/matches.yaml`:

```yaml
tokens: <leave as given>
matches:
  - finding: 1
    match: F03
    why: one short sentence
```
