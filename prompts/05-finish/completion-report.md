---
id: completion-report
stage: finish
mode: any
audience: human
target_role: skills/roles/master/
pairs_with:
  - prompts/04-validate/validate-ticket.md
  - prompts/05-finish/clean-commit.md
requires:
  - contracts/kernel.md
  - contracts/ticket-contract.md
  - contracts/swarm-contract.md
returns:
  - full completion report
  - standard role envelope
---

# Completion Report

## When to use

Use this prompt after validator approval or recorded human override to request
the full ticket completion report.

## Preconditions

- Ticket work has stopped.
- Validator verdict or explicit override evidence exists.
- Changed files and verification evidence are available.

## Prompt

```text
Prepare the full AEGIS ticket completion report.

Use:
- contracts/kernel.md
- contracts/ticket-contract.md Completion Report
- contracts/swarm-contract.md Output Envelope

Ticket envelope:
[TICKET_ENVELOPE]

Worker output:
[WORKER_OUTPUT]

Validator output or override record:
[VALIDATOR_OR_OVERRIDE]

Changed files:
[CHANGED_FILES]

Verification evidence:
[VERIFICATION_EVIDENCE]

Return the standard role envelope plus:
- changed_files;
- verification;
- human_readability with concise, unnecessary_elements_removed,
  abstraction_added, abstraction_rationale, diff_summary, layer_touched, and
  layer_separation_preserved.

Do not claim validation passed unless the evidence says it passed.
```

## Expected response

- Full completion report.
- Remaining risks or skipped checks.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/05-finish/clean-commit.md` |
| completed | validator | `prompts/04-validate/conformance-check.md` |
| needs_clarification | human | `prompts/06-control/status-report.md` |
| blocked | human | `prompts/06-control/halt.md` |
