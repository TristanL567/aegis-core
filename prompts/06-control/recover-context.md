---
id: recover-context
stage: control
mode: any
audience: human
target_role: none
pairs_with:
  - prompts/06-control/status-report.md
  - prompts/03-execute/autonomous/resume-from-ledger.md
  - prompts/03-execute/checkpointed/resume-from-checkpoint.md
requires:
  - contracts/kernel.md
  - contracts/epic-contract.md
  - contracts/ticket-contract.md
returns:
  - recovered state
  - standard role envelope
---

# Recover Context

## When to use

Use this prompt after context loss, session interruption, or a manual halt to
rebuild the active role, mode, ticket, and next prompt from artifacts.

## Preconditions

- At least one recovery artifact exists: ledger, ticket envelope, checkpoint
  summary, completion report, validator verdict, or halt summary.
- The operator does not want new work until state is reconstructed.

## Prompt

```text
Recover AEGIS context from artifacts only.

Use:
- contracts/kernel.md
- contracts/epic-contract.md Recovery
- contracts/ticket-contract.md
- prompts/README.md

Known mode:
[relay | checkpointed | autonomous | unknown]

Artifacts:
- epic envelope: [EPIC_ENVELOPE]
- ticket envelope: [TICKET_ENVELOPE]
- epic ledger: [EPIC_LEDGER]
- checkpoint summary: [CHECKPOINT_SUMMARY]
- completion report: [COMPLETION_REPORT]
- validator verdict: [VALIDATOR_VERDICT]
- halt summary: [HALT_SUMMARY]

Rebuild:
1. active mode;
2. active role and role path;
3. active ticket ID and scope;
4. last completed transition;
5. unresolved validator findings or human checkpoints;
6. next safe prompt from prompts/README.md.

For relay mode, resume at the next row in the prior prompt's Next step table.
For checkpointed mode, resume from checkpoint summary. For autonomous mode,
resume from the epic ledger. If artifacts conflict, return blocked and list the
minimum human decision needed.
```

## Expected response

- Recovered state and next prompt.
- Contradictions or missing artifacts.
- Standard role envelope.

## Next step

| Returned status | next_recommended_role | Next prompt |
| --- | --- | --- |
| completed | master | `prompts/03-execute/relay/dispatch-master-agent.md` |
| completed | human | `prompts/03-execute/checkpointed/resume-from-checkpoint.md` |
| completed | validator | `prompts/03-execute/autonomous/resume-from-ledger.md` |
| blocked | human | `prompts/06-control/halt.md` |
