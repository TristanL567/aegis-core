"""Build a throwaway git repo from a design-ticket fixture, for testing validate's design mode.

Usage: make_repo.py <fixture dir> <new empty dest dir>

The repo gets a base commit on `main` with stand-in product code (README.md,
src/app.py, the validate skill), a branch `aegis/DES-001` with the fixture's
design files committed on top, and the prototype on `aegis/DES-001-prototype`.
Validate ticket DES-001 there with base ref `main`.
"""
import shutil
import subprocess
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[3] / ".claude" / "skills" / "validate" / "SKILL.md"


def git(dest, *args):
    subprocess.run(["git", "-C", str(dest), *args], check=True, capture_output=True)


def main(fixture, dest):
    fixture, dest = Path(fixture), Path(dest)
    if dest.exists() and any(dest.iterdir()):
        sys.exit(f"{dest} is not empty")
    dest.mkdir(parents=True, exist_ok=True)
    git(dest, "init", "-q", "-b", "main")
    git(dest, "config", "user.email", "fixture@example.invalid")
    git(dest, "config", "user.name", "fixture")
    (dest / "README.md").write_text("# Portfolio app (fixture)\n", encoding="utf-8")
    (dest / "src").mkdir()
    (dest / "src" / "app.py").write_text("def main():\n    return 'portfolio app'\n", encoding="utf-8")
    skill = dest / ".claude" / "skills" / "validate"
    skill.mkdir(parents=True)
    shutil.copy(SKILL, skill / "SKILL.md")
    git(dest, "add", "-A")
    git(dest, "commit", "-q", "-m", "base")
    git(dest, "switch", "-q", "-c", "aegis/DES-001")
    shutil.copytree(fixture, dest, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("prototype"))
    git(dest, "add", "-A")
    git(dest, "commit", "-q", "-m", "[DES-001] Design dividend calendar")
    # The prototype is never merged: it lives on its own branch.
    git(dest, "switch", "-q", "-c", "aegis/DES-001-prototype")
    proto = Path(".aegis") / "design" / "DES-001" / "prototype"
    shutil.copytree(fixture / proto, dest / proto)
    git(dest, "add", "-A")
    git(dest, "commit", "-q", "-m", "DES-001 prototype")
    git(dest, "switch", "-q", "aegis/DES-001")
    print(f"repo ready: {dest} (branch aegis/DES-001, base main, prototype on aegis/DES-001-prototype)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
