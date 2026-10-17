"""Build a throwaway repo with one UI ticket, to test the validator's parity rule.

Usage: make_repo.py clean|gap <new empty dest dir>

The script creates two branches.

`main` holds:
- a small holdings page at `src/index.html`;
- a filled-in `DESIGN.md`;
- this repo's validate skill.

`aegis/UI-001` adds a "Last dividend" field to every holding. The two
variants differ in how that field behaves on a phone:
- `clean` shows it at both widths.
- `gap` hides it at phone width.

Validate ticket UI-001 with base ref `main`.
"""
import shutil
import subprocess
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[3] / ".claude" / "skills" / "validate" / "SKILL.md"

DESIGN = """# DESIGN.md: Holdings demo

## Parity rule

One product, two layouts. Every task, piece of information, action and label
on desktop exists on the phone. Layout may differ; capability and names may
not.

## Breakpoints

- Phone: 390x844. Desktop: 1440x900.
- Tables become cards on the phone. Each card shows every column as a
  labelled value.

## Navigation

None. This is a single page.

## Touch and input

- Tap targets are at least 44x44 px.
- No information appears only on hover.

## Formats

- Dates: DD.MM.YYYY
- Money: EUR, two decimals, for example €1,234.50.

## Glossary

| Concept | Term | Never use |
|---|---|---|
| A position held | Holding | Position, asset |
| Units held | Shares | Quantity, units |
| Current worth | Market value | Worth, value now |
| Most recent dividend received | Last dividend | Latest payout |

## Content priority per screen

| Screen | First on phone | Reachable via |
|---|---|---|
| Holdings | Name, market value | The rest of the card |
"""

TICKET = """id: UI-001
goal: Every holding shows its last dividend, with amount and date, on phone and desktop.
context: >
  Investors want to see at a glance when each holding last paid and how much.
epic: null
depends_on: []
human_gates: []
allowed_areas:
  - .aegis/tickets/UI-001.yaml
  - src/index.html
must_not_touch:
  - DESIGN.md
non_goals:
  - Dividend history or forecasts.
acceptance_criteria:
  - The holdings table has a "Last dividend" column showing amount and date (DD.MM.YYYY), or "None yet" when a holding has never paid.
  - Each touched task works at 390x844 and at 1440x900 with the same information and actions.
  - Labels match the glossary in DESIGN.md.
verify:
  - grep -q "Last dividend" src/index.html
smoke:
  - Serve a copy of src/ with py -3.10 -m http.server on a free port.
  - At 390x844 and at 1440x900, every holding shows its market value and its last dividend (amount and date, or "None yet").
manual_checks: []
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Holdings</title>
<style>
  * { box-sizing: border-box; }
  body { margin: 0; font: 16px/1.5 system-ui, sans-serif; color: #1f2933; background: #f5f7fa; }
  main { max-width: 900px; margin: 0 auto; padding: 16px; }
  h1 { font-size: 22px; }
  table { width: 100%; border-collapse: collapse; background: #fff; }
  th, td { text-align: left; padding: 10px 12px; border-bottom: 1px solid #d9e2ec; }
  th { color: #52606d; font-size: 14px; }
  .num { text-align: right; }
  .lbl { display: none; color: #52606d; font-size: 14px; }
  @media (max-width: 600px) {
    thead { display: none; }
    table, tbody, tr, td { display: block; width: 100%; }
    tr { border-bottom: 1px solid #d9e2ec; padding: 8px 0; }
    td, td.num { border: 0; padding: 2px 12px; text-align: left; }
    .lbl { display: inline; }
__EXTRA__  }
</style>
</head>
<body>
<main>
  <h1>Holdings</h1>
  <table>
    <thead><tr><th>Holding</th><th class="num">Shares</th><th class="num">Market value</th>__TH__</tr></thead>
    <tbody>
__ROWS__
    </tbody>
  </table>
</main>
</body>
</html>
"""

HOLDINGS = [
    ("Erste Group", 40, "€2,092.00", "€120.00 on 12.03.2025"),
    ("OMV AG", 25, "€1,046.25", "€81.25 on 02.06.2025"),
    ("Verbund AG", 12, "€820.80", "None yet"),
]


def page(with_dividend, hide_on_phone):
    th = '<th>Last dividend</th>' if with_dividend else ""
    rows = []
    for name, shares, value, div in HOLDINGS:
        cells = (f'<td><strong>{name}</strong></td>'
                 f'<td class="num"><span class="lbl">Shares: </span>{shares}</td>'
                 f'<td class="num"><span class="lbl">Market value: </span>{value}</td>')
        if with_dividend:
            cells += f'<td class="last-div"><span class="lbl">Last dividend: </span>{div}</td>'
        rows.append(f"      <tr>{cells}</tr>")
    extra = "    .last-div { display: none; }\n" if hide_on_phone else ""
    return PAGE.replace("__TH__", th).replace("__ROWS__", "\n".join(rows)).replace("__EXTRA__", extra)


def git(dest, *args):
    subprocess.run(["git", "-C", str(dest), *args], check=True, capture_output=True)


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def main(variant, dest):
    if variant not in ("clean", "gap"):
        sys.exit(__doc__)
    dest = Path(dest)
    if dest.exists() and any(dest.iterdir()):
        sys.exit(f"{dest} is not empty")
    dest.mkdir(parents=True, exist_ok=True)
    git(dest, "init", "-q", "-b", "main")
    git(dest, "config", "user.email", "fixture@example.invalid")
    git(dest, "config", "user.name", "fixture")
    write(dest / "README.md", "# Holdings demo (fixture)\n")
    write(dest / "DESIGN.md", DESIGN)
    write(dest / "src" / "index.html", page(False, False))
    (dest / ".claude" / "skills" / "validate").mkdir(parents=True)
    shutil.copy(SKILL, dest / ".claude" / "skills" / "validate" / "SKILL.md")
    git(dest, "add", "-A")
    git(dest, "commit", "-q", "-m", "base")
    git(dest, "switch", "-q", "-c", "aegis/UI-001")
    write(dest / ".aegis" / "tickets" / "UI-001.yaml", TICKET)
    write(dest / "src" / "index.html", page(True, variant == "gap"))
    git(dest, "add", "-A")
    git(dest, "commit", "-q", "-m", "[UI-001] Show last dividend per holding")
    print(f"repo ready: {dest} (branch aegis/UI-001, base main)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
