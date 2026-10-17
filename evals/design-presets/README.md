# Design presets test (AEGIS-019)

Do saved presets make a product's first `DESIGN.md` reuse the right design
conditions, and leave them out where they don't fit?

## Setup

There were 18 blind runs, all fresh Opus subagents. Each run had its own
repo, named `r01` to `r18` in shuffled order. `runs.map` gives each run's
arm and product.

**Arms:**
- `without`: the design-track skill as it is on `main`.
- `with`: round 1 of the presets. The validator rejected it, for the
  reasons below.
- `with2`: the presets after the fixes. This is the version shipped.

**Products:**
- `budget`: a household budgeting web app for Austrian families.
- `recipe`: a recipe-sharing web app.

Every run got the same prompt: draft `DESIGN.md` the way the first design
ticket would. No human was available, so the agent took its recommended
answers and listed them under `## Open questions`.

`grade.py <dir holding dp/ and dp.map>` counts four things in each draft:
- the "Presets" line;
- the four finance-eu format strings: `1.595,39 €`, `2,66 %`, `17.10.2026`
  and `inputmode="decimal"`;
- four data-portal marks: `data-label`, `role="img"`, "never scrolls
  sideways" and `44x44`;
- the open questions.

The grader only checks that the format strings appear. "Unchanged" was
confirmed by reading the drafts.

## Results (2026-10-17)

| Arm, product | Presets adopted | finance-eu formats (of 4) | data-portal marks (of 4) | Open questions | Tokens per run |
|---|---|---|---|---|---|
| with2, budget | finance-eu + data-portal, 3 of 3 | 4, 4, 4 | 4, 4, 4 | 10, 12, 13 (11.7) | 65,797 |
| without, budget | none | 2, 2, 1 | 1, 1, 1 | 16, 14, 13 (14.3) | 64,730 |
| with2, recipe | none, 3 of 3 | 1, 1, 1 | 2, 2, 2 | 10, 12, 11 (11.0) | 66,537 |
| without, recipe | none | 1, 1, 1 | 1, 1, 1 | 12, 14, 14 (13.3) | 63,904 |

**Budget**
- With presets, all 3 runs adopted both presets. All 3 copied the formats
  unchanged, and all 3 used 390x844.
- Phone navigation: 2 of 3 (r17, r18) replaced data-portal's band with a
  bottom bar and said so in the "Presets" line, and r16 kept the band. All 3
  listed phone navigation as an open question. Overriding is allowed,
  because the product's own choices win.
- Without presets, the drafts disagreed on the money format: one used
  `€ 1.234,56`, two used `1.234,56 €`. Presets add consistency across
  products.

**Recipe**
- No run adopted finance-eu (0 of 3).
- All 3 considered data-portal, turned it down, and gave the reason in the
  "Presets" line.

**Both products**
- With presets, the drafts had fewer open questions: 11.7 against 14.3 for
  budget, 11.0 against 13.3 for recipe.
- No draft asked "which presets?" as an open question.
- Presets cost +1.6% tokens on budget and +4.1% on recipe, from reading the
  preset files. The token counts come from the subagents' usage reports.

## Round 1 (rejected)

Round 1 used the first version of the skill and presets.

| Arm, product | Open questions |
|---|---|
| with, budget (r08, r09, r11) | 14, 14, 14 |
| with, recipe (r05, r07, r12) | 16, 14, 12 |

The validator found three problems:
- **Too many open questions.** Every one of the 6 runs asked "which presets
  apply?", so recipe drafts had more open questions with presets than
  without: 42 against 40.
- **Phone width.** data-portal carried EasyRep's 375x812 instead of
  aegis-core's 390x844. All 3 budget runs raised this conflict.
- **Wrong summary.** The first version of this README understated both
  findings.

The fixes:
- the skill now says the human confirms the preset choice together with the
  draft, not as an open question;
- data-portal now uses 390x844;
- the template gained a "Look" section to hold the dark-mode and colour-token
  rules.
