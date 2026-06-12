from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = "prompts"
REQUIRED_FRONTMATTER = {
    "id",
    "stage",
    "mode",
    "audience",
    "target_role",
    "pairs_with",
    "requires",
    "returns",
}
REQUIRED_SECTIONS = [
    "## When to use",
    "## Preconditions",
    "## Prompt",
    "## Expected response",
    "## Next step",
]
ALLOWED_STAGES = {"init", "plan", "execute", "validate", "finish", "control", "providers"}
ALLOWED_MODES = {"relay", "checkpointed", "autonomous", "any"}
CANONICAL_INVOCATION = """Reference AEGIS-CORE. Load AEGIS.md first, follow its Bootstrap Load Order,
use ticketing, route work through master -> worker -> validator -> master, and
pass the AEGIS.md Conformance Gate before reporting completion."""
INLINE_KERNEL_TOKENS = [
    "TICKET: [TICKET_ID]",
    "GOAL: [GOAL]",
    "DEPENDS_ON: [DEPENDS_ON]",
    "ALLOWED_AREAS: [ALLOWED_AREAS]",
    "MUST_NOT_TOUCH: [MUST_NOT_TOUCH]",
    "ACCEPTANCE: [ACCEPTANCE]",
    "VERIFY: [VERIFY]",
]
PROMPT_REF_RE = re.compile(r"prompts/[A-Za-z0-9_./-]+\.md")
FORBIDDEN_BEHAVIOR_MARKERS = [
    "you are the canonical definition",
    "this prompt defines role behavior",
    "this file defines role behavior",
    "canonical role behavior lives here",
]


@dataclass
class PromptFile:
    path: Path
    rel: str
    text: str
    frontmatter: dict[str, object]


def normalize_slashes(path: str) -> str:
    return path.replace("\\", "/").strip()


def rel_path(path: Path, root: Path) -> str:
    return normalize_slashes(str(path.relative_to(root)))


def line_for(text: str, needle: str) -> int:
    index = text.find(needle)
    if index < 0:
        return 1
    return text[:index].count("\n") + 1


def parse_frontmatter(text: str) -> tuple[dict[str, object], int]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML frontmatter opening delimiter")

    close_index: int | None = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            close_index = index
            break
    if close_index is None:
        raise ValueError("missing YAML frontmatter closing delimiter")

    data: dict[str, object] = {}
    current_list_key: str | None = None
    for line in lines[1:close_index]:
        if not line.strip():
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            if current_list_key is None:
                raise ValueError(f"list item without key: {stripped}")
            values = data.setdefault(current_list_key, [])
            if not isinstance(values, list):
                raise ValueError(f"frontmatter key is not a list: {current_list_key}")
            values.append(stripped[2:].strip())
            continue
        if ":" not in line:
            raise ValueError(f"unsupported frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            raise ValueError("empty frontmatter key")
        if value:
            data[key] = value
            current_list_key = None
        else:
            data[key] = []
            current_list_key = key

    return data, close_index + 1


def as_string_list(value: object, field: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError(f"{field} must be a list")
    result: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item:
            raise ValueError(f"{field} entries must be non-empty strings")
        result.append(item)
    return result


def iter_prompt_files(root: Path) -> list[Path]:
    prompts_root = root / PROMPTS_DIR
    return sorted(
        path
        for path in prompts_root.rglob("*.md")
        if path.name not in {"README.md", "00-conventions.md"}
    )


def load_prompts(root: Path) -> tuple[list[PromptFile], list[str]]:
    prompts: list[PromptFile] = []
    errors: list[str] = []
    for path in iter_prompt_files(root):
        rel = rel_path(path, root)
        text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        try:
            frontmatter, _ = parse_frontmatter(text)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{rel}:1: {exc}")
            frontmatter = {}
        prompts.append(PromptFile(path=path, rel=rel, text=text, frontmatter=frontmatter))
    return prompts, errors


def validate_frontmatter(prompt: PromptFile, root: Path) -> list[str]:
    errors: list[str] = []
    keys = set(prompt.frontmatter)
    missing = sorted(REQUIRED_FRONTMATTER - keys)
    if missing:
        errors.append(f"{prompt.rel}:1: missing frontmatter keys: {missing}")

    stage = prompt.frontmatter.get("stage")
    if isinstance(stage, str) and stage not in ALLOWED_STAGES:
        errors.append(f"{prompt.rel}:1: invalid stage: {stage}")

    mode = prompt.frontmatter.get("mode")
    if isinstance(mode, str) and mode not in ALLOWED_MODES:
        errors.append(f"{prompt.rel}:1: invalid mode: {mode}")

    target_role = prompt.frontmatter.get("target_role")
    if isinstance(target_role, str):
        normalized = normalize_slashes(target_role)
        if normalized != "none":
            role_path = root / normalized
            skill_path = role_path / "SKILL.md" if role_path.is_dir() else root / normalized / "SKILL.md"
            if not skill_path.is_file():
                errors.append(f"{prompt.rel}:1: target_role does not resolve: {target_role}")

    try:
        pairs_with = as_string_list(prompt.frontmatter.get("pairs_with"), "pairs_with")
    except ValueError as exc:
        errors.append(f"{prompt.rel}:1: {exc}")
        pairs_with = []
    for pair in pairs_with:
        normalized = normalize_slashes(pair)
        if not normalized.startswith("prompts/"):
            errors.append(f"{prompt.rel}:1: pairs_with must stay inside prompts/: {pair}")
            continue
        if not (root / normalized).is_file():
            errors.append(f"{prompt.rel}:1: pairs_with does not resolve: {pair}")

    return errors


def validate_sections(prompt: PromptFile) -> list[str]:
    errors: list[str] = []
    last_index = -1
    for section in REQUIRED_SECTIONS:
        index = prompt.text.find(section)
        if index < 0:
            errors.append(f"{prompt.rel}:1: missing mandatory section: {section}")
            continue
        if index < last_index:
            errors.append(f"{prompt.rel}:{line_for(prompt.text, section)}: section out of order: {section}")
        last_index = index
    if "```text" not in prompt.text:
        errors.append(f"{prompt.rel}:1: missing fenced text prompt block")
    return errors


def validate_prompt_references(prompt: PromptFile, root: Path) -> list[str]:
    errors: list[str] = []
    for match in PROMPT_REF_RE.finditer(prompt.text):
        ref = match.group(0)
        if not (root / ref).is_file():
            line = prompt.text[: match.start()].count("\n") + 1
            errors.append(f"{prompt.rel}:{line}: unresolved prompt reference: {ref}")
    return errors


def validate_canonical_invocation(root: Path) -> list[str]:
    errors: list[str] = []
    occurrences: list[str] = []
    for path in sorted((root / PROMPTS_DIR).rglob("*.md")):
        rel = rel_path(path, root)
        text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        count = text.count(CANONICAL_INVOCATION)
        occurrences.extend([rel] * count)

    use_path = "prompts/01-init/use-aegis-core.md"
    readme_path = "prompts/README.md"
    use_count = occurrences.count(use_path)
    readme_count = occurrences.count(readme_path)
    other = [item for item in occurrences if item not in {use_path, readme_path}]

    if use_count != 1:
        errors.append(f"{use_path}:1: canonical invocation must occur exactly once in canonical source")
    if readme_count > 1:
        errors.append(f"{readme_path}:1: canonical invocation may be quoted at most once")
    if other:
        errors.append(f"prompts:1: canonical invocation appears in non-canonical files: {sorted(set(other))}")
    if readme_count == 1:
        readme = (root / readme_path).read_text(encoding="utf-8").replace("\r\n", "\n")
        if "canonical source: `prompts/01-init/use-aegis-core.md`" not in readme:
            errors.append(f"{readme_path}:1: README quote must mark the canonical source")
    return errors


def validate_execute_kernel_blocks(prompts: list[PromptFile]) -> list[str]:
    errors: list[str] = []
    for prompt in prompts:
        if not prompt.rel.startswith("prompts/03-execute/"):
            continue
        for token in INLINE_KERNEL_TOKENS:
            if token not in prompt.text:
                errors.append(f"{prompt.rel}:1: missing inline kernel token: {token}")
    return errors


def validate_readme(root: Path) -> list[str]:
    errors: list[str] = []
    readme_path = root / PROMPTS_DIR / "README.md"
    text = readme_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if "pending:" in text:
        errors.append("prompts/README.md:1: pending markers remain")

    in_table = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped == "## I Want To":
            in_table = True
            continue
        if in_table and stripped.startswith("## ") and stripped != "## I Want To":
            break
        if not in_table or not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 3 or cells[0] in {"I want to...", "---"}:
            continue
        match = PROMPT_REF_RE.search(cells[1])
        if not match:
            errors.append(f"prompts/README.md:{line_number}: routing row lacks prompt path")
            continue
        ref = match.group(0)
        if not (root / ref).is_file():
            errors.append(f"prompts/README.md:{line_number}: routing row does not resolve: {ref}")
    return errors


def validate_duplicate_ids(prompts: list[PromptFile]) -> list[str]:
    errors: list[str] = []
    seen: dict[str, str] = {}
    for prompt in prompts:
        value = prompt.frontmatter.get("id")
        if not isinstance(value, str) or not value:
            continue
        if value in seen:
            errors.append(f"{prompt.rel}:1: duplicate prompt id '{value}' also used by {seen[value]}")
        else:
            seen[value] = prompt.rel
    return errors


def validate_behavior_markers(prompt: PromptFile) -> list[str]:
    lower_text = prompt.text.lower()
    errors: list[str] = []
    for marker in FORBIDDEN_BEHAVIOR_MARKERS:
        if marker in lower_text:
            errors.append(f"{prompt.rel}:{line_for(lower_text, marker)}: forbidden behavior ownership marker: {marker}")
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate the AEGIS prompt library.")
    parser.add_argument(
        "--root",
        default=str(ROOT),
        help="Repository root to validate. Defaults to the repository containing this script.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.root).resolve()
    prompts_root = root / PROMPTS_DIR
    if not prompts_root.is_dir():
        print(f"Prompt library validation failed:\n\n- prompts:1: missing {PROMPTS_DIR}/ directory")
        return 1

    prompts, errors = load_prompts(root)
    for prompt in prompts:
        errors.extend(validate_frontmatter(prompt, root))
        errors.extend(validate_sections(prompt))
        errors.extend(validate_prompt_references(prompt, root))
        errors.extend(validate_behavior_markers(prompt))
    errors.extend(validate_duplicate_ids(prompts))
    errors.extend(validate_canonical_invocation(root))
    errors.extend(validate_execute_kernel_blocks(prompts))
    errors.extend(validate_readme(root))

    if errors:
        print("Prompt library validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Prompt library validation passed: {len(prompts)} prompt file(s) checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
