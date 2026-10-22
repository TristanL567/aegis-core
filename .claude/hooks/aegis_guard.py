"""AEGIS guard: enforces the rules that must always hold.

Modes (first argument). Claude Code hooks, wired in .claude/settings.json, pass
their JSON on stdin:
  edit           PreToolUse on Edit|Write|MultiEdit|NotebookEdit: the path must be
                 inside the active ticket's allowed_areas and outside must_not_touch.
  bash           PreToolUse on Bash|PowerShell: no `git stash`.
  subagent-stop  SubagentStop: records the validator's verdict for the active ticket.
Git's own hook, .githooks/commit-msg, passes the message file:
  commit-msg     the subject starts with `[<ID>] ` and the ticket has an APPROVED
                 verdict; a `[<ID>] WIP` commit (squashed before pushing) and the
                 commit that concludes a merge need none.

Exit 2 blocks and shows stderr. Anything unexpected fails open (exit 0) with a
warning, so a broken guard never stops work.
"""
import datetime
import json
import re
import sys
from pathlib import Path

VERDICT = re.compile(r"^\s*(?:```\w*\s*)?Ticket:\s*(\S+)\s*\n\s*VERDICT:\s*(APPROVED|FIXES_REQUIRED|BLOCKED)\b")
SEPARATORS = set(";&|(){}`")
PREFIX_WORDS = {"if", "then", "else", "elif", "do", "while", "until", "!", "time", "command", "env", "nohup",
                "exec", "sudo", "xargs", "builtin"}
GIT_GLOBALS_WITH_VALUE = {"-C", "-c", "--git-dir", "--work-tree", "--namespace", "--exec-path"}


def deny(reason):
    print(f"AEGIS guard: {reason}", file=sys.stderr)
    sys.exit(2)


def warn(message):
    print(f"AEGIS guard warning: {message}", file=sys.stderr)


def repo_root(start):
    p = Path(start).resolve()
    for d in [p, *p.parents]:
        if (d / ".git").exists():
            return d
    return None


def active_ticket(root):
    """Return (id, fields) for the active ticket, or (None, None)."""
    f = root / ".aegis" / "active-ticket"
    if not f.exists():
        return None, None
    tid = f.read_text(encoding="utf-8-sig").strip()
    if not tid:
        return None, None
    tf = root / ".aegis" / "tickets" / f"{tid}.yaml"
    try:
        return tid, parse_ticket(tf.read_text(encoding="utf-8-sig"))
    except OSError:
        warn(f"active ticket {tid} has no readable .aegis/tickets/{tid}.yaml; not enforcing scope")
        return tid, None


def parse_ticket(text):
    """Read the scalar and list fields the guard needs, without a YAML library."""
    fields, key = {}, None
    for raw in text.splitlines():
        line = re.sub(r"\s+#.*$", "", raw).rstrip()
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            key, value = m.group(1), m.group(2).strip()
            if value.startswith("["):
                fields[key] = [v.strip().strip("'\"") for v in value.strip("[]").split(",") if v.strip()]
            elif value in ("", ">", "|"):
                fields[key] = []
            else:
                fields[key] = value.strip("'\"")
            continue
        m = re.match(r"^\s*-\s+(.*)$", line)
        if m and key and isinstance(fields.get(key), list):
            fields[key].append(m.group(1).strip().strip("'\""))
    return fields


def norm(path):
    path = path.replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path


def matches(path, patterns):
    for pat in patterns:
        pat = norm(pat)
        if (pat.endswith("/") and path.startswith(pat)) or path == pat:
            return True
    return False


def guard_edit(data):
    tool_input = data.get("tool_input") or {}
    target = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not target:
        return
    cwd = Path(data.get("cwd") or ".")
    target = Path(target) if Path(target).is_absolute() else cwd / target
    root = repo_root(target.parent) or repo_root(cwd)
    if root is None:
        return
    try:
        rel = norm(target.resolve().relative_to(root).as_posix())
    except ValueError:
        return  # outside the repository: not the ticket's business
    if rel.startswith(".aegis/verdicts/"):
        deny("verdicts are written only by the hook that reads the validator's output. Never write one yourself; "
             "only the human records an override.")
    if rel.startswith(".aegis/"):
        return
    tid, t = active_ticket(root)
    if not tid or t is None:
        return
    if matches(rel, t.get("must_not_touch") or []):
        deny(f"{rel} is in must_not_touch of ticket {tid}. Never change it; if the work needs it, stop and ask the human.")
    if not matches(rel, t.get("allowed_areas") or []):
        deny(f"{rel} is outside the allowed_areas of ticket {tid}. Change only those paths; if the work needs more, "
             "stop and ask the human to widen the scope.")


def segments(command):
    """Split a Bash or PowerShell command into simple commands.

    Returns a list of (words, heredoc_bodies). Quoted text, PowerShell
    here-strings and heredoc bodies become single words or bodies, so text
    inside them is never mistaken for a command.
    """
    segs, words, bodies, pending = [], [], [], []
    buf, has_word, i, n = [], False, 0, len(command)

    def end_word():
        nonlocal buf, has_word
        if has_word:
            words.append("".join(buf))
        buf, has_word = [], False

    def end_segment():
        nonlocal words, bodies
        end_word()
        if words or bodies:
            segs.append((words, bodies))
        words, bodies = [], []

    while i < n:
        c = command[i]
        if c in "\\`" and command[i + 1:i + 2] in ("\n", "\r"):  # line continuation (Bash \, PowerShell `)
            end_word()
            i += 3 if command[i + 1:i + 3] == "\r\n" else 2
            continue
        if c == "\n":
            end_word()
            i += 1
            for delim, strip_tabs in pending:
                lines = []
                while i < n:
                    j = command.find("\n", i)
                    line = command[i:] if j < 0 else command[i:j]
                    i = n if j < 0 else j + 1
                    if (line.lstrip("\t") if strip_tabs else line).strip() == delim:
                        break
                    lines.append(line)
                bodies.append("\n".join(lines))
            pending = []
            end_segment()
            continue
        if c in " \t\r":
            end_word()
            i += 1
            continue
        if c == "#" and not has_word:
            j = command.find("\n", i)
            i = n if j < 0 else j
            continue
        if c == "@" and not has_word and command[i + 1:i + 2] in ("'", '"') and command[i + 2:i + 3] in ("\n", "\r"):
            q = command[i + 1]
            end = command.find("\n" + q + "@", i + 2)
            end = n if end < 0 else end
            buf.append(command[i + 2:end].lstrip("\r\n"))
            has_word = True
            i = end + 3
            continue
        if c == "'":
            end = command.find("'", i + 1)
            end = n if end < 0 else end
            buf.append(command[i + 1:end])
            has_word = True
            i = end + 1
            continue
        if c == '"':
            j, out = i + 1, []
            while j < n and command[j] != '"':
                if command.startswith("$(", j):
                    end = skip_substitution(command, j)
                    out.append(command[j:end])
                    j = end
                    continue
                if command[j] == "\\" and j + 1 < n:
                    out.append(command[j + 1])
                    j += 2
                    continue
                if command[j] == "`" and j + 1 < n:  # PowerShell escape
                    out.append(command[j + 1])
                    j += 2
                    continue
                out.append(command[j])
                j += 1
            buf.append("".join(out))
            has_word = True
            i = j + 1
            continue
        if command.startswith("<<<", i):
            end_word()
            i += 3
            continue
        m = re.match(r"<<(-?)\s*(['\"]?)(\w+)\2", command[i:])
        if m:
            end_word()
            pending.append((m.group(3), m.group(1) == "-"))
            i += m.end()
            continue
        if c in SEPARATORS or (c == "$" and command[i + 1:i + 2] == "("):
            end_segment()
            i += 2 if c == "$" else 1
            continue
        if c in "<>":
            end_word()
            i += 1
            continue
        buf.append(c)
        has_word = True
        i += 1
    end_segment()
    return segs


def skip_substitution(command, j):
    """Index just past the `)` closing the `$(` at j, skipping quotes and heredocs inside."""
    n, k, depth = len(command), j + 2, 1
    while k < n:
        m = re.match(r"<<-?\s*(['\"]?)(\w+)\1", command[k:]) if command.startswith("<<", k) else None
        if m and not command.startswith("<<<", k):
            delim, nl = m.group(2), command.find("\n", k)
            k = n if nl < 0 else nl + 1
            while k < n:
                e = command.find("\n", k)
                line = command[k:] if e < 0 else command[k:e]
                k = n if e < 0 else e + 1
                if line.strip() == delim:
                    break
            continue
        c = command[k]
        if c == "'":
            e = command.find("'", k + 1)
            k = n if e < 0 else e + 1
            continue
        if c == '"':
            k += 1
            while k < n and command[k] != '"':
                k += 2 if command[k] == "\\" else 1
            k += 1
            continue
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                return k + 1
        k += 1
    return n


def git_dir(root):
    dot = root / ".git"
    if dot.is_file():
        m = re.match(r"gitdir:\s*(.+)", dot.read_text(encoding="utf-8-sig").strip())
        if m:
            d = Path(m.group(1))
            return d if d.is_absolute() else root / d
    return dot


def git_call(words):
    """Return (subcommand index, -C directory) if the words run git, else (None, None)."""
    k = 0
    while k < len(words) and (words[k] in PREFIX_WORDS or re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", words[k])):
        k += 1
    if k >= len(words) or not re.search(r"(^|[/\\])git(\.exe)?$", words[k], re.I):
        return None, None
    k += 1
    cdir = None
    while k < len(words) and words[k].startswith("-"):
        if words[k] in GIT_GLOBALS_WITH_VALUE:
            if words[k] == "-C" and k + 1 < len(words):
                cdir = words[k + 1]
            k += 2
        else:
            k += 1
    return (k, cdir) if k < len(words) else (None, None)


def guard_bash(data):
    command = (data.get("tool_input") or {}).get("command") or ""
    for words, _ in segments(command):
        k, _ = git_call(words)
        if k is not None and words[k] == "stash":
            deny("git stash is forbidden: the stash is shared between worktrees. Set work aside with a "
                 "'[<ID>] WIP ...' commit on the ticket branch, squashed before pushing.")


def commit_msg(message_file):
    """git commit-msg hook: the subject names the ticket, and the validator approved it."""
    root = repo_root(Path.cwd())
    if root is None:
        return
    tid, t = active_ticket(root)
    if not tid:
        return
    if any((git_dir(root) / f).exists() for f in ("MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD")):
        return  # concluding a merge, cherry-pick or revert: the message is git's, not the agent's
    try:
        text = Path(message_file).read_text(encoding="utf-8-sig")
    except OSError:
        warn(f"could not read the commit message {message_file}; not enforcing")
        return
    lines = [l.strip() for l in text.splitlines() if l.strip() and not l.startswith("#")]
    subject = re.sub(r"^(?:(?:fixup|squash|amend)! )+", "", lines[0]) if lines else ""
    ids = [tid] + ([t["epic"]] if t and t.get("epic") not in (None, "", "null") else [])
    if not any(subject.startswith(f"[{i}] ") for i in ids):
        deny(f"commit subject must start with [{tid}] (got: {subject[:60]!r}).")
    if re.match(r"^\[[^\]]+\] WIP\b", subject):
        return  # work set aside on the ticket branch; squashed before pushing
    verdict = root / ".aegis" / "verdicts" / tid
    recorded = verdict.read_text(encoding="utf-8-sig") if verdict.exists() else ""
    if not re.match(r"\s*(APPROVED|OVERRIDDEN)\b", recorded):
        deny(f"no APPROVED verdict recorded for {tid} in .aegis/verdicts/{tid}. Run the validator subagent first "
             "(its output starts with 'Ticket: <ID>'); to set work aside, commit '[<ID>] WIP ...'. "
             "Only the human may record an override; never write the verdict file yourself.")


def strings_in(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from strings_in(v)
    elif isinstance(value, list):
        for v in value:
            yield from strings_in(v)


def find_verdict(data):
    """The subagent's verdict, from its last message or, failing that, its transcript."""
    m = VERDICT.match(data.get("last_assistant_message") or "")
    if m:
        return m
    path = data.get("agent_transcript_path")
    if not path or not Path(path).is_file():
        return None
    lines = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
    for line in reversed(lines[-50:]):
        try:
            entry = json.loads(line)
        except ValueError:
            continue
        message = entry.get("message") if isinstance(entry, dict) else None
        if not isinstance(message, dict) or message.get("role") != "assistant":
            continue
        for text in strings_in(message.get("content")):
            m = VERDICT.match(text)
            if m:
                return m
        return None  # only the last assistant turn counts
    return None


def record_verdict(data):
    m = find_verdict(data)
    if not m:
        return
    root = repo_root(Path(data.get("cwd") or "."))
    if root is None:
        return
    tid, _ = active_ticket(root)
    if not tid or m.group(1) != tid:
        return
    f = root / ".aegis" / "verdicts" / tid
    if m.group(2) == "APPROVED":
        f.parent.mkdir(parents=True, exist_ok=True)
        stamp = datetime.datetime.now().isoformat(timespec="seconds")
        f.write_text(f"APPROVED {stamp} by subagent {data.get('agent_type', '?')}\n", encoding="utf-8")
    elif f.exists():
        f.unlink()


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "commit-msg":
        try:
            commit_msg(sys.argv[2])
        except SystemExit:
            raise
        except Exception as exc:  # fail open
            warn(f"internal error ({exc!r}); not enforcing")
        return
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        warn("could not read the hook input; not enforcing")
        return
    try:
        {"edit": guard_edit, "bash": guard_bash, "subagent-stop": record_verdict}.get(mode, lambda d: None)(data)
    except SystemExit:
        raise
    except Exception as exc:  # fail open: a guard bug must never stop work
        warn(f"internal error ({exc!r}); not enforcing")


if __name__ == "__main__":
    main()
