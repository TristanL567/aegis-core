# AEGIS Conformance Check

Paste this helper prompt to make an agent self-audit its work against the AEGIS
Conformance Gate before it reports a task complete. `AEGIS.md` is the canonical
source for the Conformance Gate; if this helper ever differs from `AEGIS.md`,
follow `AEGIS.md`.

A validator should also run this gate independently at the ticket gate; a worker self-audit does not replace validator review.

```text
Before you report this work as done, audit it against the AEGIS conformance gate.
Answer each item with pass or fail and cite the concrete evidence.

1. Ticket envelope: did a ticket envelope with objective, allowed_areas,
   must_not_touch, acceptance criteria, and validation commands exist before
   implementation began?
2. One ticket: was exactly one ticket executed in this run?
3. Loop: did work flow master -> worker -> validator -> master?
4. Validator gate: did a validator review the worker output and return a
   blocking status? Any override was authorized by the human, not the agent.
5. Scope: are all changed files inside the ticket's allowed_areas, with every
   must_not_touch path left untouched?
6. Envelope: did each skill response return the standard role envelope, and did
   the completed ticket return the full completion report -- changed_files,
   verification, human_readability per contracts/ticket-contract.md?
7. Canonical source: was role and contract behavior loaded from skills/ and
   contracts/ rather than re-authored downstream?

If every item passes, report the work as done and include this audit in your output.
If any item fails, do not report done. Return status fixes_required or blocked,
name each failed item, and route back through the master.
```
