# Understand Anything

## Source

- Repository URL: <https://github.com/Lum1104/Understand-Anything>
- README URL: <https://github.com/Lum1104/Understand-Anything/blob/main/README.md>
- Raw README URL: <https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/README.md>
- CLAUDE.md URL: <https://github.com/Lum1104/Understand-Anything/blob/main/CLAUDE.md>
- Raw CLAUDE.md URL: <https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/CLAUDE.md>
- Retrieved: 2026-05-25

## Retrieval Context

Claims below come from the README and CLAUDE.md retrieved on 2026-05-25. The
README describes Understand Anything as a tool that turns a codebase, knowledge
base, or docs into an interactive knowledge graph for exploration, search, and
questions. It also describes a multi-agent analysis pipeline, structural graph,
business-domain view, guided tours, semantic search, diff impact analysis,
dashboard exploration, and generated `.understand-anything/knowledge-graph.json`
artifacts. CLAUDE.md describes the project as combining LLM intelligence with
static analysis to produce interactive dashboards for understanding codebases,
and notes that graph JSON is written under `.understand-anything/`.

## Summary

Understand Anything is an external context and architecture mapping tool. It can
scan a project, extract structural and semantic relationships, and present them
as an interactive graph and dashboard. Its useful outputs are evidence for
understanding a codebase; they are not AEGIS governance.

## Usefulness For Agentic Coding

- Architecture overview: reveal files, functions, classes, dependencies, and
  architectural layers before a worker changes code.
- Codebase graph: provide navigable structure for onboarding and impact review.
- Domain or business logic map: expose business domains, flows, and process
  steps that may inform design clarification or language mapping.
- Guided tours: help an agent read the codebase in dependency order.
- Fuzzy and semantic search: locate relevant code by meaning as well as name.
- Diff impact analysis: show possible ripple effects before commit or review.

## Fit With AEGIS

Understand Anything helps agents understand a system. AEGIS governs how work is
planned, executed, validated, and reported.

AEGIS remains authoritative for ticketing, roles, validators, contracts,
one-ticket execution, conformance gates, and completion reports. Understand
Anything may provide optional context evidence for an AEGIS ticket, but it must
not replace the ticket envelope, `master -> worker -> validator -> master`
routing, validator approval, scope validation, or `AEGIS.md` Conformance Gate.

## Useful AEGIS Combinations

- `design-clarification-interview`: use graph or domain-flow evidence to ask
  sharper questions about product, workflow, or architecture intent.
- `ubiquitous-language-map`: compare user terms with code, docs, schema, route,
  or UI names found through graph/search evidence.
- `module-boundary-review`: inspect public interfaces, dependencies, layers, and
  coupling before allowing a boundary change.
- `test-first-change`: use graph context to locate likely test seams and
  relevant regression checks before implementation.
- `code-validator`: use graph or diff-impact evidence as review context, while
  keeping validator judgment independent.
- `ticket-scope-validation`: graph evidence may explain impact, but changed-file
  scope still comes from the ticket and scope firewall.

## What It Should Not Be Used For

- Do not use Understand Anything as a replacement for AEGIS ticketing,
  validators, contracts, or conformance gates.
- Do not treat generated summaries, graph clusters, or guided tours as
  authoritative without checking source files.
- Do not let visual exploration expand a ticket beyond `allowed_areas`.
- Do not commit `.understand-anything/` artifacts unless a ticket explicitly
  allows generated graph artifacts and states the artifact policy.
- Do not install or run the tool as part of this reference ticket.

## Artifact Policy

Generated artifacts are not committed by default. AEGIS distinguishes local
scratch artifacts from shareable graph artifacts:

- Local scratch artifacts are temporary run products and must stay out of
  commits. This includes `.understand-anything/intermediate/` and
  `.understand-anything/diff-overlay.json`.
- Shareable graph artifacts, such as a durable graph JSON intended for team
  onboarding or review, may be committed only when an explicit ticket allows
  them and names the generated artifact paths in `allowed_areas`.
- Graph claims are advisory until source confirmation is performed. Before using
  generated graph output as AEGIS evidence, confirm the claim against source
  files, tests, docs, routes, schemas, or other primary project evidence.
- A completion report that uses graph evidence must state the artifact policy:
  what was generated, what was ignored, what was committed if explicitly
  allowed, and what source confirmation was performed.

## Risks

- Stale graph artifacts can mislead agents after code changes.
- Generated summaries can create false authority if not checked against source.
- Graphs and dashboards can add context bloat when the ticket only needs a small
  code slice.
- Visual exploration can replace ticket discipline if the agent follows the
  graph instead of the ticket.
- Generated artifacts can pollute the repo if committed without policy.

## Candidate Integration Tickets

Future candidates only:

- `AEGIS-UA-002`: Add Understand Anything runbook.
- `AEGIS-UA-003`: Add codebase-map-generation procedure.
- `AEGIS-UA-004`: Compose existing procedures with graph evidence.
- `AEGIS-UA-005`: Define graph artifact policy.
