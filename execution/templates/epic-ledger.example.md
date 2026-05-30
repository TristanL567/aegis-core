# Example Epic Ledger

Canonical ledger fields and event types live in `contracts/epic-contract.md`.
Each row is illustrative.

| timestamp | ticket_id | event_type | decision | notes | commit_sha |
| --- | --- | --- | --- | --- | --- |
| 2026-05-30T09:00:00Z | EXAMPLE-EPIC-001 | dispatched | dispatched master-agent | Started first ticket with `dispatched_by: master-planner`. | null |
| 2026-05-30T09:20:00Z | EXAMPLE-EPIC-001 | validator_approved | accepted ticket output | Validator approved scope, tests, and completion report. | abc1234 |
| 2026-05-30T09:45:00Z | EXAMPLE-EPIC-002 | fixes_required | retry 1/5 | Validator found missing regression evidence. | null |
| 2026-05-30T10:05:00Z | EXAMPLE-EPIC-002 | validator_blocked | escalated to planner | Validator returned blocked because scope conflict needs planner decision. | null |
| 2026-05-30T10:15:00Z | EXAMPLE-EPIC-002 | validator_needs_clarification | paused for planner clarification | Validator needs clarified acceptance criteria before review can continue. | null |
| 2026-05-30T10:30:00Z | EXAMPLE-EPIC-002 | checkpoint_hit | paused for human checkpoint | Ticket is listed in `human_checkpoint_tickets`. | null |
| 2026-05-30T10:45:00Z | EXAMPLE-EPIC-002 | human_approved | continued after checkpoint | Human approved continuation with noted risk. | null |
| 2026-05-30T11:00:00Z | EXAMPLE-EPIC-003 | human_overrode_validator | continued with override | Human explicitly overrode validator finding after planner escalation. | null |
| 2026-05-30T12:00:00Z | EXAMPLE-EPIC | epic_merged | merged to base | Merge policy satisfied; epic branch merged to `main`. | def5678 |
| 2026-05-30T12:30:00Z | EXAMPLE-EPIC | epic_aborted | aborted without merge | Abort reason recorded; epic branch preserved. | null |
