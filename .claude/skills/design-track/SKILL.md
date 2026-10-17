---
name: design-track
description: Runs an AEGIS design ticket (kind design) from brief to frozen spec. It covers the personas and key tasks, up to three rounds of throwaway prototype, ux-test and a decision per finding, then the pass rule, the freeze at the merge gate, and conversion into an implementation epic. Use it when a new screen, flow or app feature has an open design, when asked to design, prototype or UX-plan something before building it, or when a ticket has kind design.
---

# Design track

A design ticket (`kind: design`) comes before the implementation epic. It
runs the normal AEGIS loop and always has `human_gates: [ticket, merge]`.

It adds three fields:
- `appetite`: the timebox, such as `2 days`; overruns go to the human.
- `personas`: IDs from `.aegis/personas.yaml`, the project's 3-5 user
  profiles, drafted by the first design ticket and confirmed by the human.
- `tasks`: T1..Tn, each a user goal with a success criterion.

`allowed_areas` is `.aegis/design/<ID>/`, the ticket file,
`.aegis/personas.yaml`, and `DESIGN.md`; product code goes in
`must_not_touch`.

## The product's DESIGN.md

`DESIGN.md` at the repo root is the product's design contract: the parity
rule, look, breakpoints, navigation, touch and input, formats, glossary, and
content priority.
- If the project has none, the first design ticket drafts it from
  `DESIGN-template.md` in this skill's folder. The human approves it at the
  `ticket` gate.
- Prototypes follow `DESIGN.md`.
- At the freeze, add the round's new patterns and terms to it.
- `presets/` holds saved design conditions, such as formats or phone
  patterns. A draft picks the presets that fit, copies their sections in,
  and lists them under "Presets" at its top; the human confirms that choice
  with the draft, not as an open question. The product's own choices
  override a preset.
- To save one, extract a product's generic sections into
  `presets/<name>.md` in aegis-core, as a ticket: what it is for, when not to
  use it, no product names.

## Rounds

Work in at most 3 rounds:
1. **Prototype.** Build or revise `.aegis/design/<ID>/prototype/`. It is one
   self-contained, throwaway file with fake data that includes edge cases.
   Label each screen with its task IDs, and build only the screens and
   states the tasks need.
2. **Test.** A fresh subagent runs the `ux-test` skill on a served copy and
   writes `report.md`.
3. **Decide.** Record the findings in `findings.yaml`, and record one
   decision per finding (fix, accept, defer, or kill) in the append-only
   `decisions.md`.

## Pass rule

The design passes when no confirmed severity 3-4 finding is open and every
task works at phone and desktop width. AI findings aren't user validation,
so `manual_checks` includes a real-user session. `spec.md` holds each task's
flow and each screen's empty, loading, and error states.

## Freeze

The `merge` gate freezes the design. The commit holds the ticket, personas,
`DESIGN.md`, `spec.md`, `report.md`, `decisions.md`, and `findings.yaml`.

The prototype is never imported or merged. As the one exception to one
branch and one commit per ticket, it goes to `aegis/<ID>-prototype`.

## Implementation

`write-ticket` then turns `spec.md` into an epic:
- Each of the epic's tickets names `design_ref: <ID>#<flow>`.
- Each takes its acceptance criteria from the spec's flows and states.
- The epic's validation reruns the `ux-test` inspection on the real build.

Changing a frozen design needs a new design ticket.
