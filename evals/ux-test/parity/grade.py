"""Run the shared ../grade.py with parity/gaps.yaml as the answer key.

Usage is the same as ../grade.py: <matches.yaml> | --summary <dir> | --self-test.
For the parity test bed, judge with ../judge.md, reading parity/gaps.yaml for
flaws.yaml and parity/prototype/index.html for prototype/index.html.
"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("grade", HERE.parent / "grade.py")
grade = importlib.util.module_from_spec(spec)
spec.loader.exec_module(grade)
grade.KEY = HERE / "gaps.yaml"

if __name__ == "__main__":
    sys.exit(grade.main(sys.argv[1:]))
