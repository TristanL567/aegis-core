"""Grade the DESIGN.md drafts in dp/rNN against dp.map (arm, product)."""
import re
import sys
from pathlib import Path

base = Path(sys.argv[1])
rows = [l.split() for l in (base / "dp.map").read_text().splitlines() if l.strip()]
FIN = ["1.595,39 €", "2,66 %", "17.10.2026", "inputmode=\"decimal\""]
print("run arm product presets_line fin_formats(of 4) data_portal_marks open_q words")
for run, arm, prod in rows:
    f = base / "dp" / run / "DESIGN.md"
    if not f.exists():
        print(run, arm, prod, "MISSING")
        continue
    s = f.read_text(encoding="utf-8")
    m = re.search(r"^Presets:\s*(.+)$", s, re.M | re.I)
    presets = m.group(1).strip() if m else "-"
    fin = sum(x in s for x in FIN)
    dp = sum(x in s for x in ["data-label", "role=\"img\"", "never scrolls sideways", "44x44"])
    oq = s.split("## Open questions", 1)
    nq = len(re.findall(r"^\s*(?:[-*]|\d+\.)\s", oq[1], re.M)) if len(oq) > 1 else 0
    print(run, arm, prod, repr(presets), fin, dp, nq, len(s.split()))
