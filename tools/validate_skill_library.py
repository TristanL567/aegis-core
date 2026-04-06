from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REQUIRED_FRONTMATTER = {
    "name",
    "role",
    "description",
    "inputs_expected",
    "outputs_produced",
    "allowed_handoffs",
    "blocking_rules",
    "provider_notes",
}
REQUIRED_OUTPUT_FIELDS = {
    "status",
    "summary",
    "artifacts",
    "findings",
    "next_recommended_role",
}
ALLOWED_ROLES = {"master", "worker", "validator"}
ALLOWED_HANDOFFS = {"master", "worker", "validator", "human"}


@dataclass
class SkillRecord:
    path: Path
    name: str
    role: str
    handoffs: list[str]


def extract_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter opening delimiter")

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("missing YAML frontmatter closing delimiter")

    frontmatter_text = parts[1]
    data = yaml.safe_load(frontmatter_text) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter did not parse into a mapping")
    return data


def validate_skill(path: Path) -> SkillRecord:
    data = extract_frontmatter(path)
    missing = REQUIRED_FRONTMATTER - set(data.keys())
    if missing:
        raise ValueError(f"missing frontmatter keys: {sorted(missing)}")

    role = data["role"]
    if role not in ALLOWED_ROLES:
        raise ValueError(f"invalid role: {role}")

    outputs = set(data["outputs_produced"])
    missing_outputs = REQUIRED_OUTPUT_FIELDS - outputs
    if missing_outputs:
        raise ValueError(f"missing output fields: {sorted(missing_outputs)}")

    handoffs = data["allowed_handoffs"]
    invalid_handoffs = sorted(set(handoffs) - ALLOWED_HANDOFFS)
    if invalid_handoffs:
        raise ValueError(f"invalid handoff targets: {invalid_handoffs}")

    provider_notes = data["provider_notes"]
    for provider in ("codex", "claude_code", "antigravity"):
        if provider not in provider_notes:
            raise ValueError(f"missing provider note for: {provider}")

    return SkillRecord(
        path=path,
        name=str(data["name"]),
        role=role,
        handoffs=list(handoffs),
    )


def main() -> int:
    skill_paths = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_paths:
        print("No skills found.")
        return 1

    records: list[SkillRecord] = []
    errors: list[str] = []

    for path in skill_paths:
        try:
            records.append(validate_skill(path))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path.relative_to(ROOT)}: {exc}")

    roles_present = {record.role for record in records}
    missing_roles = ALLOWED_ROLES - roles_present
    if missing_roles:
        errors.append(f"missing canonical roles: {sorted(missing_roles)}")

    if errors:
        print("Skill library validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill library validation passed.\n")
    for record in records:
        rel_path = record.path.relative_to(ROOT)
        handoffs = ", ".join(record.handoffs)
        print(f"- {record.name} [{record.role}] -> {handoffs} ({rel_path})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
