from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]


def normalize_path(path: str) -> str:
    normalized = path.replace("\\", "/").strip()
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def parse_ticket_envelope(ticket_path: Path) -> dict:
    text = ticket_path.read_text(encoding="utf-8-sig")
    lines = text.splitlines(keepends=True)
    if lines and lines[0].strip() == "---":
        closing_index = next(
            (index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"),
            None,
        )
        if closing_index is None:
            raise ValueError("ticket is missing YAML frontmatter closing delimiter")
        yaml_text = "".join(lines[1:closing_index])
        source_description = "ticket frontmatter"
    else:
        yaml_text = text
        source_description = "ticket YAML"

    data = yaml.safe_load(yaml_text) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{source_description} did not parse into a mapping")
    return data


def normalize_patterns(values: object, field_name: str) -> list[str]:
    if values is None:
        return []
    if not isinstance(values, list):
        raise ValueError(f"{field_name} must be a list")

    patterns: list[str] = []
    for value in values:
        if not isinstance(value, str):
            raise ValueError(f"{field_name} entries must be strings")
        patterns.append(normalize_path(value))
    return patterns


def matches_pattern(path: str, pattern: str) -> bool:
    if pattern.endswith("/"):
        return path.startswith(pattern)
    return path == pattern


def read_staged_paths() -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or "git staged path lookup failed"
        raise RuntimeError(message)
    return [line for line in result.stdout.splitlines() if line.strip()]


def validate_paths(
    changed_files: list[str],
    allowed_areas: list[str],
    must_not_touch: list[str],
) -> list[str]:
    violations: list[str] = []

    for changed_file in changed_files:
        path = normalize_path(changed_file)
        blocked_by = [pattern for pattern in must_not_touch if matches_pattern(path, pattern)]
        if blocked_by:
            violations.append(
                f"{path}: under must_not_touch ({', '.join(blocked_by)})"
            )
            continue

        allowed_by = [pattern for pattern in allowed_areas if matches_pattern(path, pattern)]
        if not allowed_by:
            allowed_text = ", ".join(allowed_areas) if allowed_areas else "no allowed_areas declared"
            violations.append(f"{path}: outside allowed_areas ({allowed_text})")

    return violations


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate changed file paths against a ticket envelope's "
            "allowed_areas and must_not_touch declarations."
        )
    )
    parser.add_argument(
        "--ticket",
        required=True,
        help="Path to a plain YAML ticket envelope or markdown file containing YAML frontmatter.",
    )
    parser.add_argument(
        "--changed-file",
        action="append",
        default=[],
        help=(
            "Changed file path to validate. Repeat this option for multiple paths. "
            "Paths are normalized to use / separators and no leading ./."
        ),
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help=(
            "Also validate staged paths from 'git diff --cached --name-only'. "
            "The git command runs from the repository root."
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    ticket_path = Path(args.ticket)
    if not ticket_path.is_absolute():
        ticket_path = ROOT / ticket_path

    try:
        data = parse_ticket_envelope(ticket_path)
        allowed_areas = normalize_patterns(data.get("allowed_areas"), "allowed_areas")
        must_not_touch = normalize_patterns(data.get("must_not_touch"), "must_not_touch")

        changed_files = list(args.changed_file)
        if args.staged:
            changed_files.extend(read_staged_paths())

        normalized_files = [normalize_path(path) for path in changed_files]
        violations = validate_paths(normalized_files, allowed_areas, must_not_touch)
    except Exception as exc:  # noqa: BLE001
        print(f"Scope validation error: {exc}", file=sys.stderr)
        return 2

    if violations:
        print("Scope validation failed:")
        for violation in violations:
            print(f"- {violation}")
        return 1

    if normalized_files:
        print(f"Scope validation passed: {len(normalized_files)} changed file(s) within ticket scope.")
    else:
        print("Scope validation passed: no changed files to check.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
