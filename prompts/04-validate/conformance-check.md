---
id: conformance-check
stage: validate
mode: any
audience: human
target_role: skills/roles/master-validator/
pairs_with:
  - prompts/04-validate/validate-ticket.md
  - prompts/05-finish/close-epic.md
requires:
  - AEGIS.md
  - contracts/kernel.md
  - skills/roles/master-validator/SKILL.md
returns:
  - conformance verdict
  - standard role envelope
---

# Conformance Check

## When to use

Use this prompt to audit a ticket, ticket series, or epic against the AEGIS.md
Conformance Gate.

## Preconditions

- The relevant ticket or epic evidence is available.
- Validator verdicts and completion reports are available when work completed.
- Any override records are available.

## Prompt

```text
Apply the full AEGIS.md Conformance Gate against observable evidence.

Use:
- AEGIS.md
- contracts/kernel.md
- contracts/swarm-contract.md
- contracts/ticket-contract.md
- contracts/epic-contract.md
- skills/roles/master-validator/SKILL.md when epic-level evidence is present

Evidence package:
[EVIDENCE_PACKAGE]

Check every gate item:
1. ticket envelope existed before implementation;
2. exactly one ticket was executed;
3. master -> worker -> validator -> master handoff occurred or blocked safely;
4. validator approval exists, or a human override was requested and recorded;
5. standard role envelope fields are present;
6. full completion report fields are present for completed tickets;
7. changed files stay inside allowed_areas and outside must_not_touch;
8. no project-file edits are attributable to master-planner or master-agent,
   except ledger and checkpoint artifacts;
9. every worker dispatch references an existing role path under skills/roles/;
10. work relied on skills/ and contracts/ rather than re-authoring behavior.

Return a blocking finding for every failed or unevidenced item. Findings must
include evidence paths, ticket IDs, or the missing artifact.
```

## Expected response

- Gate verdict.
- Finding IDs for each failed or missing evidence item.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/05-finish/close-epic.md` |
| fixes_required | master | `prompts/04-validate/drift-correction.md` |
| blocked | master | `prompts/04-validate/authorize-override.md` |
| needs_clarification | human | `prompts/06-control/status-report.md` |
