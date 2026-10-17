---
name: ux-test
description: Usability-test a prototype or web app as an inspector who drives every key task like a user at phone and desktop width, probes inputs and recovery, and reports deduplicated findings with severity and evidence. Can add persona subagents that see only the screen when the human asks. Use in an AEGIS design round, or whenever asked to usability-test, UX-test, or test a UI with personas or user profiles. Not for code review or visual taste.
---

# UX test

AI testers are good at mechanical problems: dead ends, missing states,
hidden or covered controls, silent failures. They are bad at realism: they
over-succeed and give confident opinions. So this procedure covers every
task at both widths, reports only what it saw happen, and labels opinions.
The findings are evidence for a design decision, never proof that real users
succeed.

Run this as a fresh subagent that did not build the prototype. If you built
it, start a fresh subagent and give it this skill, the URL and the tasks.

## 1. Set up

- **URL.** Test a served copy: a temp directory outside the repo, holding
  only what the app needs, on a free port bound to 127.0.0.1. Never open
  source files, tickets, answer keys or `.aegis/`. Test only the app as the
  browser shows it.
- **Tasks.** Use T1..Tn from the ticket or the request, each with its
  success criterion.
- **Coverage grid.** Rows are tasks. The columns are phone 390x844 and
  desktop 1440x900. You must cover every cell; an empty cell is a gap you
  report.

## 2. Inspect

**Browser tools.**
- **Built-in** (`mcp__Claude_Browser__*`): open your own tab with
  `tabs_create` and pass its `tabId` on every call. If `tabs_create` fails
  because the pane is closed, open it with `preview_start` and the URL. Set
  the size with `resize_window`, and act with `computer` (`left_click`,
  `type`, `key`, `scroll`).
- **Without the built-in browser** (CLI, cloud, CI): use Playwright MCP
  started with `--isolated`. Installing it needs the human's OK.

Read state cheaply with `get_page_text` or `read_page`. Take a screenshot
(`scale` 0.5 is enough) when layout matters: after each width change, when
a dialog opens, and whenever something might be covered, clipped or
off-screen. Retry a screenshot that times out.

Act like a user. Never set field values or click by script, never use hidden
elements, and never type a URL other than the start URL. Ignore the task
badges (T1..) and anything marked as a stub: they are prototype scaffolding.

For each task, first at 390x844 and then at 1440x900:

1. Take the happy path the way a first-time user would, and check the
   success criterion.
2. Probe it:
   - each input with an invalid value, an empty value, another common
     format (dates, decimal commas) and long text;
   - leaving out optional fields;
   - cancel, Escape and back in mid-flow;
   - repeating the action, then changing filters, tabs or years;
   - whether the result is visible and confirmed;
   - whether every control and value can be reached without anything
     covering it or clipping it;
   - one keyboard-only pass (Tab, Enter, Escape) per dialog.
3. Note anything that names one thing two ways, or shows state only by
   colour.
4. **Parity.** After both widths, compare them task by task:
   - List every piece of information, every action, label and input the
     task shows at 1440x900, and check each one at 390x844.
   - Report each item that is missing, renamed, unreachable, clipped or
     covered on the phone as its own finding, even when several share one
     cause. Give both widths as evidence.
   - Then check the phone for touch. Look for:
     - information that only appears on hover;
     - tap targets under 44x44 px;
     - number fields without a numeric keyboard (`type` or `inputmode`);
     - wide tables or charts without a phone form.

The budget is about 15 actions per task per width. Two failed attempts to
recover count as a finding. Reproduce each finding once more before you
report it.

## 3. Report

Deduplicate by cause, not by symptom, except parity gaps, which stay one per item. Rate each finding once, from what you
saw, on Nielsen's scale:
- 4: blocks a key task on a target device, or loses or corrupts data;
- 3: causes failure or a wrong result for many users, or has no visible
  recovery;
- 2: slows or confuses, but users recover;
- 1: cosmetic.

Mark each finding `confirmed` (reproduced through the UI) or `opinion`
(judgement, not observed failure). An opinion is never rated above 2.

Write findings in this shape, ordered by severity, into the design round's
`findings.yaml` when there is one:

```yaml
- id: U01
  task: T1
  viewport: phone          # phone | desktop | both
  where: Add transaction dialog, save button
  problem: The bottom navigation covers the save button, so it cannot be tapped.
  evidence: At 390x844, open Add transaction, fill all fields; the save button sits under the nav; tapping it opens Report.
  severity: 4
  status: confirmed        # confirmed | opinion
```

Reply with:
- the coverage grid and any gaps;
- per task and width, whether the success criterion was met;
- the findings as a numbered list, one problem per item, with severity and
  status;
- one line stating that these are AI test results and need a real-user check
  before they count as validation.

In a design round, also save this reply as `.aegis/design/<ID>/report.md`,
next to `findings.yaml`.

Don't propose redesigns unless asked.

## Optional: persona pass

Run this only when the human explicitly asks for a persona pass or persona
subagents, for example before freezing a high-stakes design. It costs about
three times as much as the inspection. A plain request to test "with
personas" doesn't trigger it. Instead, name three personas in the inspection
report, and for each finding say which of them it would hit.

Start one fresh subagent per persona, one at a time: they share the browser
pane. Use the `ux-persona` agent type when it exists. Otherwise use a
general-purpose subagent, and afterwards check that its tool calls were only
screenshots, clicks, typing, keys and scrolling.

Take personas from `.aegis/personas.yaml`, or draft them with the human. A
behaviour card covers tech fluency, device, reading style, patience (the
number of actions without progress before giving up), how they react to
errors, the formats they type, and one goal sentence per task.

Brief each persona with:

> You are <card>. Your goal: <goal text>. Set the viewport to <size>. See
> the app only through screenshots and act only on what is visible; never
> read page code, the accessibility tree or files. Before every action, log
> `I see | I intend | I expect`. After it, log
> `what changed | confusion 1-5`. Give up when <n> actions pass without
> progress. End each task with Completed, Partial, Failed or Abandoned at
> step N, and say whether you believe you succeeded.

Merge their output:
- Every step rated 3 or higher, every give-up, and every "I succeeded" that
  the success criterion contradicts becomes a candidate.
- Mark a candidate `confirmed` only if you reproduce it. Otherwise mark it
  `synthetic` and rate it no higher than 2.
- Add a matrix of personas × tasks giving the outcome and the highest
  confusion rating. If every cell is Completed with no rating of 3 or
  higher, call the result suspicious, not good.
