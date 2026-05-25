# Understand Anything Runbook

This runbook explains when an AEGIS operator or agent may use Understand
Anything as optional context evidence. The external reference lives in
`docs/cross-references/understand-anything.md`.

AEGIS remains authoritative for tickets, roles, validators, contracts, one-ticket
execution, conformance, and completion reporting. Understand Anything can inform
understanding; it does not govern execution.

## When To Use

Use Understand Anything when extra graph or context evidence would materially
reduce implementation risk:

- onboarding a new target project;
- architecture-impacting ticket planning or review;
- module-boundary uncertainty;
- domain or business flow discovery;
- diff impact review before validation or commit;
- locating relevant code, tests, routes, schemas, or docs when local context is
  too thin.

## When Not To Use

Do not use it when graph exploration would add more noise than evidence:

- small mechanical tickets;
- tickets with enough local context already present;
- narrow docs, prompt, formatting, or generated-file updates;
- any situation where exploration would expand scope beyond `allowed_areas`;
- any ticket where generated graph artifacts are not allowed and artifact policy
  is unclear.

## Suggested Workflow

1. Confirm the ticket envelope first, including `allowed_areas`,
   `must_not_touch`, validation commands, and completion report requirements.
2. Decide whether graph evidence is necessary for this ticket. If not, proceed
   without it.
3. If used, treat Understand Anything output as context evidence. Check any
   generated summary, tour, domain map, or impact view against source files.
4. Keep exploration bounded to the ticket question: architecture overview,
   module boundary, business flow, semantic search, or diff impact.
5. Report only the evidence that affected ticket decisions. Do not paste or
   commit large graph output.
6. Continue through normal AEGIS routing: master -> worker -> validator ->
   master. Validator approval remains blocking.

## Evidence To Report

When Understand Anything affects a ticket, the worker or validator should report:

- why graph/context evidence was needed;
- which command, dashboard view, graph output, or source-backed summary was used;
- which source files confirmed the generated evidence;
- what ticket decision changed because of the evidence;
- what uncertainty or risk remains.

## Artifact Guidance

Understand Anything may create graph artifacts such as files under
`.understand-anything/`. Treat those as generated artifacts.

Generated artifacts are not committed by default.

- Local scratch artifacts stay uncommitted. This includes
  `.understand-anything/intermediate/` and
  `.understand-anything/diff-overlay.json`.
- Shareable graph artifacts may be committed only when an explicit ticket allows
  them and lists the artifact paths in `allowed_areas`.
- Generated graph claims are advisory until source confirmation is performed.
  Confirm claims against source files, tests, docs, routes, schemas, or other
  primary evidence before using them as AEGIS evidence.
- Report the artifact policy in the completion report: generated artifacts,
  ignored scratch paths, any explicitly allowed shareable graph artifacts, and
  source confirmation performed.

## Risks

- Stale graph artifacts can mislead after code changes.
- Generated summaries can sound authoritative while missing source nuance.
- Graph exploration can bloat context and distract from a small ticket.
- Visual architecture maps can tempt agents to expand scope.
- Generated artifacts can pollute commits without an explicit policy.
