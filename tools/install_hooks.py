"""Install or update the AEGIS hooks in a repository, without touching its own hooks.

Usage: python tools/install_hooks.py <aegis-core checkout> <target repo> [--dry-run]

What it does, and prints:
- copies .claude/hooks/aegis-guard.sh, .claude/hooks/aegis_guard.py,
  .githooks/commit-msg and .githooks/post-commit, replacing only missing files
  or earlier AEGIS versions (a same-named file without AEGIS's exact header
  line is the repo's own and is left alone), and stages the scripts as
  executable;
- sets the AEGIS "hooks" entries in .claude/settings.json, replacing older
  AEGIS entries and keeping every other setting;
- adds .aegis/active-ticket, .aegis/verdicts/ and .claude/worktrees/ to
  .gitignore;
- activates the commit check (commit-msg) and the ticket clearing
  (post-commit): sets core.hooksPath to .githooks when the repo has no hooks
  of its own, otherwise adds one line to each shell hook in use (husky's
  .husky/<hook> under husky), changing no other byte. That line does nothing
  on a branch without the AEGIS files. A hooks folder outside the repo, or a
  hook in another language or encoding, is never changed: the report says the
  check is not active and gives the line to add by hand. core.hooksPath is
  per clone.

Every check runs before the first write; on a problem nothing is changed.
"""
import json
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path

FILES = [".claude/hooks/aegis-guard.sh", ".claude/hooks/aegis_guard.py", ".githooks/commit-msg",
         ".githooks/post-commit"]
EXECUTABLE = {".claude/hooks/aegis-guard.sh", ".githooks/commit-msg", ".githooks/post-commit"}
IGNORES = [".aegis/active-ticket", ".aegis/verdicts/", ".claude/worktrees/"]
# Does nothing on a branch without the AEGIS files, so other branches still commit.
CHAIN = ('g="$(git rev-parse --show-toplevel)/.claude/hooks/aegis-guard.sh"; '
         '[ ! -f "$g" ] || sh "$g" commit-msg "$1" || exit $?  # AEGIS')
CHAIN_POST = ('g="$(git rev-parse --show-toplevel)/.claude/hooks/aegis-guard.sh"; '
              '[ ! -f "$g" ] || sh "$g" post-commit  # AEGIS')
# Each git hook AEGIS activates: (line chained into a repo's own hook, report label, what to call by hand).
HOOKS = {
    "commit-msg": (CHAIN, "commit check", "Call .claude/hooks/aegis-guard.sh commit-msg <message file> from it, "
                                          "and stop the commit when it fails."),
    "post-commit": (CHAIN_POST, "ticket clearing", "Call .claude/hooks/aegis-guard.sh post-commit from it."),
}
SHELLS = re.compile(r"^#!\s*(?:/usr/bin/env\s+)?(?:\S*/)?(?:sh|bash|dash|zsh|ksh)\b")


def git(target, *args):
    p = subprocess.run(["git", "-C", str(target), *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.stdout.strip() if p.returncode == 0 else None


def read_text(path):
    """(text, newline) of a UTF-8 file, keeping its line ending; raises on other encodings."""
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    return text.replace("\r\n", "\n"), ("\r\n" if b"\r\n" in raw else "\n")


def write_text(path, text, newline="\n"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.replace("\n", newline).encode("utf-8"))


def header(path):
    """The first comment line after the shebang: AEGIS's signature in its own files."""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return None
    for line in lines[:5]:
        if line.startswith(("#", '"""')) and not line.startswith("#!"):
            return line.strip()
    return None


# Each AEGIS file's exact header line, in every version so far (case-sensitive).
HEADERS = {
    ".claude/hooks/aegis-guard.sh": ("# Runs aegis_guard.py with the first Python that really starts (on Windows,",),
    ".claude/hooks/aegis_guard.py": ('"""AEGIS guard: enforces the rules that must always hold.',),
    ".githooks/commit-msg": ("# AEGIS: a commit's subject names the active ticket, and the validator approved",),
    ".githooks/post-commit": ("# AEGIS: the active ticket's own commit finishes it, so .aegis/active-ticket is",),
}


def is_aegis(path, rel):
    """An AEGIS file, maybe an older version: its header is one of AEGIS's own.

    A repo's hook that had the AEGIS line chained into it, that merely
    mentions "aegis", or whose own header starts with "# AEGIS:", keeps its
    own header, so it is never mistaken for one."""
    return header(path) in HEADERS[rel]


def split_lines(text):
    """Lines with their own endings, so a file with mixed endings is written back as it was."""
    return re.findall(r"[^\n]*\n|[^\n]+$", text)


def inside(path, roots):
    path = Path(path).resolve()
    return any(path == r or r in path.parents for r in roots)


def settings_problem(path):
    """Why .claude/settings.json can't be merged, or None."""
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (ValueError, OSError):
        return "is not valid UTF-8 JSON"
    if not isinstance(data, dict):
        return "is not a JSON object"
    hooks = data.get("hooks", {})
    if not isinstance(hooks, dict):
        return 'has a "hooks" value that is not an object'
    for event, groups in hooks.items():
        if not isinstance(groups, list) or not all(isinstance(g, dict) for g in groups):
            return f"has hooks.{event} that is not a list of objects"
        for g in groups:
            inner = g.get("hooks", [])
            if not isinstance(inner, list) or not all(isinstance(h, dict) for h in inner):
                return f'has a hooks.{event} entry whose "hooks" is not a list of objects'
    return None


def is_aegis_command(hook):
    return any(name in str(hook.get("command", "")) for name in ("aegis-guard.sh", "aegis_guard.py"))


class Installer:
    def __init__(self, source, target, dry_run):
        self.source, self.target, self.dry = source, target, dry_run
        self.report = []

    def do(self, message, action):
        if self.dry:
            self.report.append("would " + message)
            return
        result = action()
        self.report.append(result if isinstance(result, str) else message)

    # --- checks: everything that can fail, before the first write --------------------------

    def preflight(self):
        """Return an error, or None after working out the whole plan."""
        missing = [rel for rel in [*FILES, ".claude/settings.json"] if not (self.source / rel).is_file()]
        if missing:
            return f"{self.source} is not an aegis-core checkout (missing {', '.join(missing)})"
        hooks = git(self.target, "rev-parse", "--path-format=absolute", "--git-path", "hooks")
        common = git(self.target, "rev-parse", "--path-format=absolute", "--git-common-dir")
        if hooks is None or common is None:
            return "this git is too old (2.31 or newer is needed)"
        problem = settings_problem(self.target / ".claude/settings.json")
        if problem:
            return f".claude/settings.json {problem}"
        gi = self.target / ".gitignore"
        try:
            self.gitignore = read_text(gi) if gi.exists() else ("", "\n")
        except (OSError, UnicodeDecodeError):
            return ".gitignore can't be read as UTF-8"
        self.own_githooks = {name for name in HOOKS if (self.target / ".githooks" / name).exists()
                             and not is_aegis(self.target / ".githooks" / name, f".githooks/{name}")}
        self.plan = self.plan_activation(Path(hooks), Path(common))
        return None

    def plan_activation(self, hooks_dir, common):
        """A list of ('note', message) | ('config', message) | ('chain', hook, text, message)."""
        local = git(self.target, "config", "--local", "--type=path", "--get", "core.hooksPath")
        anywhere = git(self.target, "config", "--type=path", "--get", "core.hooksPath")  # expands ~
        if anywhere:
            p = Path(anywhere)
            hooks_dir = (p if p.is_absolute() else self.target / p).resolve()
        both = "commit check and ticket clearing"
        if not inside(hooks_dir, [self.target.resolve(), common.resolve()]):
            where = "this repo's core.hooksPath" if local else "a global or system core.hooksPath"
            manual = "; ".join(f"near the top of the {name} hook git uses: {line}" for name, (line, _, _) in HOOKS.items())
            return [("note", f"{both}: NOT active. Git runs hooks from {hooks_dir}, outside this repo "
                             f"({where}), which this script leaves alone. To activate them, add this line {manual}")]
        githooks = (self.target / ".githooks").resolve()
        if anywhere and hooks_dir == githooks and not self.own_githooks:
            return [("note", f"{both}: active (core.hooksPath is .githooks)")]
        own_hooks = [p for p in hooks_dir.glob("*") if p.is_file() and not p.name.endswith(".sample")] \
            if hooks_dir.is_dir() else []
        if not anywhere and not own_hooks and not self.own_githooks:
            dormant = sorted(p.name for p in githooks.glob("*") if p.is_file() and p.name not in HOOKS)
            note = f"; this also turns on .githooks/{', .githooks/'.join(dormant)}" if dormant else ""
            return [("config", f"{both}: set core.hooksPath to .githooks (repeat in every other clone){note}")]
        if hooks_dir.name == "_" and hooks_dir.parent.name == ".husky":
            hooks_dir = hooks_dir.parent  # husky runs .husky/<hook>; .husky/_ is generated
        return [self.plan_chain(hooks_dir / name, name, common) for name in HOOKS]

    def plan_chain(self, hook, name, common):
        """Add or update the AEGIS line in one hook, changing no other byte of it."""
        chain, label, by_hand = HOOKS[name]
        manual = f"To activate it, add this line near the top of the {name} hook git uses: {chain}"
        if hook.resolve() == (self.target / ".githooks" / name).resolve() and name not in self.own_githooks:
            return ("note", f"{label}: active (.githooks/{name} is AEGIS's)")
        if hook.is_symlink() and not inside(hook.resolve(), [self.target.resolve(), common.resolve()]):
            return ("note", f"{label}: NOT active. {hook} links to {hook.resolve()}, outside this repo, "
                            f"which this script leaves alone. {manual}")
        if not hook.exists():
            return ("chain", hook, "#!/bin/sh\n" + chain + "\n", f"{label}: created {hook}")
        try:
            text = hook.read_bytes().decode("utf-8")
        except (OSError, UnicodeDecodeError):
            return ("note", f"{label}: NOT active. {hook} isn't UTF-8 text, so it was left alone. {manual}")
        parts = split_lines(text)
        lines = [p.rstrip("\r\n") for p in parts]
        ends = [p[len(l):] for p, l in zip(parts, lines)]
        first = lines[0].lstrip("﻿") if lines else ""
        if first.startswith("#!") and not SHELLS.match(first):
            return ("note", f"{label}: NOT active. {hook} isn't a shell script ({first}), so it was "
                            f"left alone. {by_hand}")
        aegis_lines = [i for i, l in enumerate(lines) if "aegis-guard.sh" in l and l.rstrip().endswith("# AEGIS")]
        if aegis_lines:
            if all(lines[i] == chain for i in aegis_lines):
                return ("note", f"{label}: already called from {hook}")
            for i in aegis_lines:
                parts[i] = chain + ends[i]
            return ("chain", hook, "".join(parts), f"{label}: updated the AEGIS line in {hook}")
        if "aegis-guard.sh" in text:
            return ("note", f"{label}: {hook} already calls aegis-guard.sh in its own way; left alone")
        newline = next((e for e in ends if e), "\n")
        at = 1 if first.startswith("#!") else 0
        if at and not ends[0]:
            parts[0] += newline  # a lone shebang line without an ending
        parts.insert(at, chain + newline)
        return ("chain", hook, "".join(parts), f"{label}: added one line to {hook}, which keeps its own checks")

    # --- writes ------------------------------------------------------------------------------

    def copy_files(self):
        for rel in FILES:
            src, dst = self.source / rel, self.target / rel
            if dst.exists() and dst.read_bytes() == src.read_bytes():
                self.report.append(f"{rel}: up to date")
                continue
            if dst.exists() and not is_aegis(dst, rel):
                self.report.append(f"{rel}: kept the repo's own file of the same name")
                continue

            def write(src=src, dst=dst, rel=rel):
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)
                if rel in EXECUTABLE:
                    dst.chmod(dst.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
            self.do(f"{rel}: {'updated' if dst.exists() else 'added'}", write)
            if rel in EXECUTABLE:
                # Git on Unix skips hooks that aren't executable; with core.fileMode=false
                # (Windows) only the index carries the bit, so stage the file with it.
                def stage(rel=rel):
                    if git(self.target, "add", "--chmod=+x", "--", rel) is None:
                        return (f"{rel}: NOT staged (git add failed, for example because the path is "
                                "ignored); commit it with git add --chmod=+x")
                    return f"{rel}: staged as executable (git add --chmod=+x)"
                self.do(f"{rel}: staged as executable (git add --chmod=+x)", stage)

    def merge_settings(self):
        src = json.loads((self.source / ".claude/settings.json").read_text(encoding="utf-8"))
        dst_path = self.target / ".claude/settings.json"
        if dst_path.exists():
            text, newline = read_text(dst_path)
            settings = json.loads(text)
        else:
            settings, newline = {}, "\n"
        hooks = settings.setdefault("hooks", {})
        changed = []
        for event, groups in src.get("hooks", {}).items():
            current = hooks.get(event, [])
            ours = [g for g in current if any(is_aegis_command(h) for h in g.get("hooks", []))]
            if ours == groups:
                continue
            kept = []  # every non-AEGIS entry, as it was
            for g in current:
                rest = [h for h in g.get("hooks", []) if not is_aegis_command(h)]
                if rest:
                    kept.append(dict(g, hooks=rest))
            hooks[event] = kept + groups
            changed.append(event)
        if not changed:
            self.report.append(".claude/settings.json: AEGIS hooks up to date")
            return
        self.do(f".claude/settings.json: set the AEGIS hooks for {', '.join(changed)}, other settings kept",
                lambda: write_text(dst_path, json.dumps(settings, indent=2, ensure_ascii=False) + "\n", newline))

    def ignore(self):
        text, newline = self.gitignore
        missing = [i for i in IGNORES if i not in text.split("\n")]
        if not missing:
            return
        if text and not text.endswith("\n"):
            text += "\n"
        self.do(f".gitignore: added {', '.join(missing)}",
                lambda: write_text(self.target / ".gitignore", text + "".join(m + "\n" for m in missing), newline))

    def activate(self):
        for plan in self.plan:
            self.activate_one(plan)

    def activate_one(self, plan):
        kind = plan[0]
        if kind == "note":
            self.report.append(plan[1])
        elif kind == "config":
            def configure():
                if git(self.target, "config", "core.hooksPath", ".githooks") is None:
                    return "commit check and ticket clearing: NOT active (git config core.hooksPath .githooks failed)"
                return plan[1]
            self.do(plan[1], configure)
        else:
            _, hook, text, message = plan

            def chain():
                write_text(hook, text)
                hook.chmod(hook.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                git_dir = Path(git(self.target, "rev-parse", "--path-format=absolute", "--git-common-dir"))
                if inside(hook, [self.target.resolve()]) and not inside(hook, [git_dir.resolve()]):
                    # A hook kept in the repo is committed; give it the executable bit in the index.
                    rel = hook.resolve().relative_to(self.target.resolve()).as_posix()
                    if git(self.target, "add", "--chmod=+x", "--", rel) is None:
                        return message + f"; NOT staged, commit {rel} with git add --chmod=+x"
                    return message + f"; staged {rel} as executable"
                return message
            self.do(message, chain)


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = [a for a in argv if a != "--dry-run"]
    if len(args) != 2:
        print(__doc__)
        return 2
    source, target = Path(args[0]).resolve(), Path(args[1]).resolve()
    top = git(target, "rev-parse", "--show-toplevel")
    if top is None:
        print(f"{target} is not a git repository")
        return 1
    inst = Installer(source, Path(top), "--dry-run" in argv)
    problem = inst.preflight()
    if problem:
        print(f"{problem}; fix it first. Nothing was changed.")
        return 1
    inst.copy_files()
    inst.merge_settings()
    inst.ignore()
    inst.activate()
    print("\n".join(inst.report))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
