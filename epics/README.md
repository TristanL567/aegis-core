# AEGIS Epics

This folder holds active or planned epic envelopes and their ticket backlogs.
An epic is a project-level unit that groups multiple tickets under one
architectural goal.

Each tracked epic should use this shape:

- `epics/<epic_id>/envelope.yaml`: the epic envelope and project-level scope.
- `epics/<epic_id>/tickets/<ticket_id>.yaml`: one executable ticket per file.

Tickets are still executed one at a time. The presence of an epic folder does
not authorize batched implementation. Completed epics are summarized in
`docs/completed-work.md`; stale completed ticket files should not be kept here.
