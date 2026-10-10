"""Score UX-test runs against the planted flaws in flaws.yaml.

A run directory holds the tester's findings and a matches.yaml written by a
judge who saw the findings and flaws.yaml, never which arm produced them:

    tokens: 81234                # tester tokens, judge excluded
    matches:
      - finding: 1               # the tester's finding number
        match: F03               # a flaw id, "unplanted" or "invalid"

Usage:
    grade.py <matches.yaml>      score one run
    grade.py --summary <dir>     mean per arm over <dir>/<arm>/<run>/matches.yaml
    grade.py --self-test
"""
import statistics
import sys
from pathlib import Path

import yaml

KEY = Path(__file__).with_name("flaws.yaml")
OTHER = {"unplanted", "invalid"}


def flaw_ids():
    return [f["id"] for f in yaml.safe_load(KEY.read_text(encoding="utf-8"))]


def score(doc, ids):
    found, unplanted, invalid = set(), 0, 0
    for m in doc.get("matches") or []:
        label = str(m["match"])
        if label in ids:
            found.add(label)
        elif label == "unplanted":
            unplanted += 1
        elif label == "invalid":
            invalid += 1
        else:
            raise ValueError(f"unknown match label {label!r}")
    return {"found": sorted(found), "recall": len(found), "unplanted": unplanted,
            "invalid": invalid, "tokens": doc.get("tokens")}


def show(name, s, total):
    print(f"{name}: recall {s['recall']}/{total} {s['found']}, "
          f"unplanted {s['unplanted']}, invalid {s['invalid']}, tokens {s['tokens']}")


def summary(root, ids):
    arms = {}
    for path in sorted(Path(root).glob("*/*/matches.yaml")):
        arm = path.parent.parent.name
        arms.setdefault(arm, []).append(score(yaml.safe_load(path.read_text(encoding="utf-8")), ids))
    if not arms:
        print(f"no runs under {root}")
        return 1
    for arm, runs in arms.items():
        mean = lambda k: statistics.mean(r[k] for r in runs)
        toks = [r["tokens"] for r in runs if r["tokens"] is not None]
        tok = f"{statistics.mean(toks):.0f}" if toks else "n/a"
        print(f"{arm}: {len(runs)} runs, recall {mean('recall'):.2f}/{len(ids)}, "
              f"unplanted {mean('unplanted'):.2f}, invalid {mean('invalid'):.2f}, tokens {tok}")
    return 0


def self_test(ids):
    doc = {"tokens": 100, "matches": [
        {"finding": 1, "match": "F01"}, {"finding": 2, "match": "F01"},
        {"finding": 3, "match": "F09"}, {"finding": 4, "match": "unplanted"},
        {"finding": 5, "match": "invalid"}, {"finding": 6, "match": "invalid"}]}
    s = score(doc, ids)
    assert len(ids) == 10 and len(set(ids)) == 10, ids
    assert s["recall"] == 2 and s["found"] == ["F01", "F09"], s
    assert s["unplanted"] == 1 and s["invalid"] == 2, s
    try:
        score({"matches": [{"finding": 1, "match": "F99"}]}, ids)
    except ValueError:
        pass
    else:
        raise AssertionError("unknown label accepted")
    print("self-test passed")
    return 0


def main(argv):
    ids = flaw_ids()
    if argv[:1] == ["--self-test"]:
        return self_test(ids)
    if argv[:1] == ["--summary"] and len(argv) == 2:
        return summary(argv[1], ids)
    if len(argv) == 1:
        show(argv[0], score(yaml.safe_load(Path(argv[0]).read_text(encoding="utf-8")), ids), len(ids))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
