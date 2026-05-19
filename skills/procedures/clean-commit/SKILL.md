---
trigger:
  - "A role is preparing, reviewing, or describing a git commit for a single ticket-owned change."
  - "The ticket envelope names an allowed write area, must-not-touch paths, acceptance criteria, or verification commands that must be reflected in the commit evidence."
  - "git status --short, staged files, a proposed commit message, or a completion report is available for mechanical commit hygiene review."
non_trigger:
  - "No commit, staged diff, proposed commit message, or commit readiness review is being prepared."
  - "The task is only code implementation, validation, issue triage, or documentation review and does not require commit hygiene decisions."
  - "The user explicitly asks not to stage, commit, or prepare commit readiness evidence."
  - "The work spans multiple tickets and needs orchestration by the master role before a commit can be assessed."
failure_modes_addressed:
  - "Dirty worktree blindness where unrelated modified or untracked files are ignored before commit preparation."
  - "Unrelated staged-file inclusion where files outside the ticket envelope are staged with the ticket-owned change."
  - "Missing ticket ID in the commit message, branch summary, or completion evidence."
  - "Weak commit messages that describe generic activity instead of the ticket goal and user-visible change."
  - "Missing validation evidence where tests, validators, or skipped-check rationale are absent from the completion report."
attention_signals:
  - "The ticket ID, goal, allowed write area, must-not-touch paths, acceptance criteria, and verification commands in the ticket envelope."
  - "git status --short entries that include paths outside the ticket allowed area or pre-existing untracked files."
  - "git diff --stat output showing changed files that must map directly to the ticket scope."
  - "Staged files that differ from unstaged files or include generated artifacts not named by the ticket."
  - "A proposed commit message that omits the ticket ID, specific outcome, or validation evidence."
procedure:
  - "Read the ticket envelope and identify the ticket ID, allowed write area, must-not-touch paths, acceptance criteria, and required verification commands."
  - "Inspect git status --short and separate ticket-owned changes from unrelated dirty worktree entries without reverting or staging unrelated work."
  - "Inspect staged files, when any exist, and confirm every staged path is ticket-owned and permitted by the envelope."
  - "Check the commit message or proposed message for the ticket ID, a concise statement of the actual change, and no broad or speculative claims."
  - "Check validation evidence for each required command, including pass/fail status, skipped-command rationale, and remaining risk."
  - "Run or review git diff --stat and compare the changed-file summary against the ticket envelope before declaring commit readiness."
  - "If validate_ticket_scope.py is referenced, state that it is pending because the script does not exist until AEGIS-SKILL-007; do not implement it in this procedure."
  - "Produce a human-readable summary that names the staged files, unstaged or unrelated files left alone, validation evidence, and any commit blockers."
scope_boundary:
  - "Covers commit-readiness hygiene for one ticket: ticket ID presence, staged-file scope, dirty-worktree awareness, commit message quality, validation evidence, and human-readable summary."
  - "Does not implement ticket scope tooling, scope-firewall automation, validators, role prompts, execution runbooks, provider adapters, or repository policy."
  - "Does not decide cross-ticket orchestration, perform validator approval, open pull requests, push branches, merge changes, or override explicit human instructions."
composition_points:
  - "Operating discipline supplies the always-on rules for one-ticket scope, surgical diffs, protected areas, verification, and reporting."
  - "The worker role uses this procedure before presenting commit readiness evidence for the assigned ticket."
  - "The validator role checks the reported evidence and blocks approval when staged files, message content, or validation evidence do not match the ticket envelope."
  - "The master role handles cross-ticket sequencing, role handoffs, and decisions that exceed this procedure's single-ticket boundary."
  - "No adjacent procedure is bundled here; broader scope enforcement remains with operating discipline and validator review unless a separate procedure is explicitly assigned."
verification:
  - "Run git status --short and verify unrelated dirty or untracked files are identified and not claimed as ticket-owned."
  - "Run git diff --stat and compare every changed path against the ticket envelope allowed write area and must-not-touch list."
  - "If staged files exist, compare the staged path list against the ticket envelope and block readiness for unrelated staged files."
  - "Confirm the proposed commit message includes the ticket ID and a specific summary of the actual change."
  - "Confirm the completion evidence names required validation commands, their results, and any skipped-command rationale."
  - "When validate_ticket_scope.py becomes available, use it as an additional mechanical check; until AEGIS-SKILL-007 provides it, report that this verifier is pending rather than attempting to run or create it."
output_contract:
  - "status: ready, blocked, or not_applicable."
  - "ticket_id: the ticket ID found in the envelope and expected in the commit message."
  - "staged_files: staged paths reviewed, or an empty list when no files are staged."
  - "dirty_worktree: unrelated modified or untracked paths observed and intentionally left untouched."
  - "commit_message_check: whether the message includes the ticket ID and a specific change summary."
  - "validation_evidence: commands reviewed or run, results, skipped checks, and remaining risk."
  - "summary: short human-readable statement of the commit-ready change and blockers, if any."
---

# Clean Commit

Use this procedure only for commit hygiene on one ticket. It checks that the ticket ID is present, staged files match the ticket envelope, unrelated dirty worktree entries are preserved, the commit message names the actual change, validation evidence is reported, and the final summary is readable by a human reviewer.

It does not stage files, create commits, push branches, approve work, implement scope tooling, or expand the ticket. Operating discipline owns the always-on scope rules, the worker role owns implementation evidence, the validator role owns approval, and the master role owns cross-ticket sequencing.
