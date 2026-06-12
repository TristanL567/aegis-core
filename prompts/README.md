# Prompt Library

This is the only human-facing prompt surface for AEGIS-CORE. Use this routing
table to choose a prompt, then follow that prompt's Next step table.

Canonical invocation, canonical source: `prompts/01-init/use-aegis-core.md`

```text
Reference AEGIS-CORE. Load AEGIS.md first, follow its Bootstrap Load Order,
use ticketing, route work through master -> worker -> validator -> master, and
pass the AEGIS.md Conformance Gate before reporting completion.
```

## I Want To

| I want to... | File | Status |
| --- | --- | --- |
| bind an agent to AEGIS-CORE | `prompts/01-init/use-aegis-core.md` | ready |
| check whether a session is correctly bound | `prompts/01-init/verify-binding.md` | ready |
| force a strict binding acknowledgment before work | `prompts/01-init/bind-strict.md` | ready |
| apply AEGIS-CORE to a target project | `prompts/01-init/apply-to-project.md` | ready |
| start an epic planning session | `prompts/02-plan/init-master-planner.md` | ready |
| turn a broad idea into an epic | `prompts/02-plan/epic-from-idea.md` | ready |
| turn a small idea into one ticket | `prompts/02-plan/ticket-from-idea.md` | ready |
| produce a planner handoff package | `prompts/02-plan/planner-handoff.md` | ready |
| dispatch a master-agent in relay mode | `prompts/03-execute/relay/dispatch-master-agent.md` | ready |
| relay a ticket to a worker | `prompts/03-execute/relay/relay-to-worker.md` | ready |
| relay completed worker output to a validator | `prompts/03-execute/relay/relay-to-validator.md` | ready |
| relay epic evidence to the master-validator | `prompts/03-execute/relay/relay-to-master-validator.md` | ready |
| run one ticket with declared checkpoints | `prompts/03-execute/checkpointed/run-ticket-checkpointed.md` | ready |
| resume from a checkpoint summary | `prompts/03-execute/checkpointed/resume-from-checkpoint.md` | ready |
| run an epic autonomously until a gate or error | `prompts/03-execute/autonomous/run-epic-autonomous.md` | ready |
| state the autonomous supervision contract | `prompts/03-execute/autonomous/supervision-contract.md` | ready |
| resume autonomous work from the ledger | `prompts/03-execute/autonomous/resume-from-ledger.md` | ready |
| validate one completed ticket | `prompts/04-validate/validate-ticket.md` | ready |
| check a run against the Conformance Gate | `prompts/04-validate/conformance-check.md` | ready |
| authorize a human override of a validator finding | `prompts/04-validate/authorize-override.md` | ready |
| halt and correct scope drift | `prompts/04-validate/drift-correction.md` | ready |
| request a completion report | `prompts/05-finish/completion-report.md` | ready |
| prepare a ticket-bound commit | `prompts/05-finish/clean-commit.md` | ready |
| close an epic after validation | `prompts/05-finish/close-epic.md` | ready |
| ask for current ledger-format status | `prompts/06-control/status-report.md` | ready |
| halt a session while preserving state | `prompts/06-control/halt.md` | ready |
| recover context after interruption | `prompts/06-control/recover-context.md` | ready |
| configure Claude Code for AEGIS | `prompts/07-providers/claude-code-setup.md` | ready |
| configure Codex for AEGIS | `prompts/07-providers/codex-setup.md` | ready |
| configure Antigravity for AEGIS | `prompts/07-providers/antigravity-setup.md` | ready |
| create provider custom instructions | `prompts/07-providers/custom-instructions.md` | ready |

## Mode Picker

| Mode | Human role | Agent routing | Best fit |
| --- | --- | --- | --- |
| relay | Human routes every handoff, maximum overview | Agents return envelopes and wait for the human to paste the next prompt | High control, audits, new workflows |
| checkpointed | Human approves declared gates | Agents self-route between declared checkpoints | Normal epic execution with bounded autonomy |
| autonomous | Human sees start, checkpoints on error, and end | Agents self-route until gate failure, critical error, or merge gate | Mature workflows with trusted evidence |

Across all modes, supervisors never edit project files. The flow composes as:
planner -> master-agent -> workers -> validator -> master-validator. Prompts
invoke roles and cite contracts; role behavior stays in `skills/roles/`, and
invariants stay in `contracts/`.

## Conventions

Every prompt file must follow `prompts/00-conventions.md`.
