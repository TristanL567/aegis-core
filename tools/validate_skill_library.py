from __future__ import annotations

import argparse
from collections import Counter
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
REQUIRED_PROCEDURAL_FRONTMATTER = {
    "trigger",
    "non_trigger",
    "failure_modes_addressed",
    "attention_signals",
    "procedure",
    "scope_boundary",
    "composition_points",
    "reference_pointers",
    "verification",
    "output_contract",
}
REQUIRED_REFERENCE_POINTER_KEYS = {"ref", "section", "open_when"}
REQUIRED_OUTPUT_FIELDS = {
    "status",
    "summary",
    "artifacts",
    "findings",
    "next_recommended_role",
}
ALLOWED_ROLES = {"master", "worker", "validator"}
ALLOWED_HANDOFFS = {"master", "worker", "validator", "human"}
PROCEDURAL_CLOSET_LINE_BUDGET = 200
REFERENCE_INDEX_LINE_BUDGET = 120
REFERENCE_SECTION_LINE_BUDGET = 150
INDEX_READMES = {
    "roles": ("roles/README.md", "role"),
    "procedures": ("procedures/README.md", "procedure"),
    "references": ("references/README.md", "reference"),
}


@dataclass
class SkillRecord:
    path: Path
    name: str
    role: str
    handoffs: list[str]


@dataclass
class ProcedureRecord:
    path: Path
    name: str
    standalone: bool
    routed: bool


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


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


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


def validate_procedural_skill(path: Path, role_paths: list[Path]) -> ProcedureRecord:
    lines = line_count(path)
    if lines > PROCEDURAL_CLOSET_LINE_BUDGET:
        raise ValueError(
            "exceeds closet budget: "
            f"{lines} lines > {PROCEDURAL_CLOSET_LINE_BUDGET}"
        )

    data = extract_frontmatter(path)
    missing = REQUIRED_PROCEDURAL_FRONTMATTER - set(data.keys())
    if missing:
        raise ValueError(f"missing procedural frontmatter keys: {sorted(missing)}")

    pointers = data["reference_pointers"]
    if not isinstance(pointers, list):
        raise ValueError("reference_pointers must be a list")

    for index, pointer in enumerate(pointers):
        if not isinstance(pointer, dict):
            raise ValueError(f"reference_pointers[{index}] must be a mapping")

        missing_pointer_keys = REQUIRED_REFERENCE_POINTER_KEYS - set(pointer.keys())
        if missing_pointer_keys:
            raise ValueError(
                "reference_pointers["
                f"{index}] missing keys: {sorted(missing_pointer_keys)}"
            )

        ref = pointer["ref"]
        section = pointer["section"]
        open_when = pointer["open_when"]
        if not all(isinstance(value, str) and value for value in (ref, section, open_when)):
            raise ValueError(
                f"reference_pointers[{index}] ref, section, and open_when must be non-empty strings"
            )

        reference_dir = SKILLS_DIR / "references" / ref
        if not reference_dir.is_dir():
            raise ValueError(
                f"unresolved reference pointer: ref '{ref}' does not exist"
            )

        section_path = reference_dir / "sections" / f"{section}.md"
        if not section_path.is_file():
            raise ValueError(
                "unresolved reference pointer: "
                f"'{ref}/{section}' does not resolve to sections/{section}.md"
            )

    procedure_name = path.parent.name
    route = f"skills/procedures/{procedure_name}/SKILL.md"
    routed = any(route in role_path.read_text(encoding="utf-8") for role_path in role_paths)
    standalone = data.get("standalone") is True
    return ProcedureRecord(
        path=path,
        name=procedure_name,
        standalone=standalone,
        routed=routed,
    )


def extract_index_table_ids(readme_path: Path, id_column: str) -> list[str]:
    lines = readme_path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue

        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if id_column not in cells:
            continue

        id_index = cells.index(id_column)
        table_ids: list[str] = []
        for table_line in lines[index + 2 :]:
            table_stripped = table_line.strip()
            if not table_stripped:
                if table_ids:
                    break
                continue
            if not table_stripped.startswith("|"):
                if table_ids:
                    break
                continue

            row_cells = [cell.strip() for cell in table_stripped.strip("|").split("|")]
            if len(row_cells) <= id_index:
                continue
            table_ids.append(row_cells[id_index])

        if table_ids:
            return table_ids
        raise ValueError(f"index table has no {id_column} ids")

    raise ValueError(f"missing index table with {id_column} column")


def validate_index(readme_path: Path, folder_dir: Path, id_column: str) -> None:
    if not readme_path.is_file():
        raise ValueError("missing index README")

    table_ids = extract_index_table_ids(readme_path, id_column)
    folder_ids = sorted(path.name for path in folder_dir.iterdir() if path.is_dir())
    id_counts = Counter(table_ids)

    duplicates = sorted(id_ for id_, count in id_counts.items() if count > 1)
    missing = sorted(set(folder_ids) - set(table_ids))
    extra = sorted(set(table_ids) - set(folder_ids))
    findings = []
    if missing:
        findings.append(f"missing rows: {missing}")
    if extra:
        findings.append(f"extra rows: {extra}")
    if duplicates:
        findings.append(f"duplicate rows: {duplicates}")
    if findings:
        raise ValueError("; ".join(findings))


def extract_sections_table_ids(readme_path: Path) -> list[str]:
    lines = readme_path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.strip() != "## Sections":
            continue

        table_ids: list[str] = []
        for table_line in lines[index + 1 :]:
            stripped = table_line.strip()
            if not stripped:
                if table_ids:
                    break
                continue
            if not stripped.startswith("|"):
                if table_ids:
                    break
                continue

            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if len(cells) < 3:
                continue
            if cells[0] in {"id", "---"}:
                continue
            table_ids.append(cells[0])

        if table_ids:
            return table_ids
        raise ValueError("Sections table has no section ids")

    raise ValueError("missing Sections table")


def validate_reference(readme_path: Path) -> None:
    lines = line_count(readme_path)
    if lines > REFERENCE_INDEX_LINE_BUDGET:
        raise ValueError(
            "reference index exceeds budget: "
            f"{lines} lines > {REFERENCE_INDEX_LINE_BUDGET}"
        )

    section_ids = extract_sections_table_ids(readme_path)
    reference_dir = readme_path.parent
    for section_id in section_ids:
        section_path = reference_dir / "sections" / f"{section_id}.md"
        if not section_path.is_file():
            raise ValueError(
                f"Sections table id '{section_id}' does not resolve to sections/{section_id}.md"
            )

    sections_dir = reference_dir / "sections"
    if sections_dir.exists():
        for section_path in sorted(sections_dir.glob("*.md")):
            section_lines = line_count(section_path)
            if section_lines > REFERENCE_SECTION_LINE_BUDGET:
                raise ValueError(
                    f"{section_path.relative_to(ROOT)} exceeds section budget: "
                    f"{section_lines} lines > {REFERENCE_SECTION_LINE_BUDGET}"
                )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the AEGIS skill library.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat orphan procedures as validation failures.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    skill_paths = sorted((SKILLS_DIR / "roles").glob("*/SKILL.md"))
    if not skill_paths:
        print("No skills found.")
        return 1
    procedural_skill_paths = sorted((SKILLS_DIR / "procedures").glob("*/SKILL.md"))
    reference_readme_paths = sorted((SKILLS_DIR / "references").glob("*/README.md"))

    records: list[SkillRecord] = []
    procedure_records: list[ProcedureRecord] = []
    errors: list[str] = []
    orphan_findings: list[str] = []

    for path in skill_paths:
        try:
            records.append(validate_skill(path))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path.relative_to(ROOT)}: {exc}")

    for path in procedural_skill_paths:
        try:
            procedure_records.append(validate_procedural_skill(path, skill_paths))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path.relative_to(ROOT)}: {exc}")

    for path in reference_readme_paths:
        try:
            validate_reference(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path.relative_to(ROOT)}: {exc}")

    for index_name, (readme_relative_path, id_column) in INDEX_READMES.items():
        try:
            validate_index(
                SKILLS_DIR / readme_relative_path,
                SKILLS_DIR / index_name,
                id_column,
            )
        except Exception as exc:  # noqa: BLE001
            errors.append(f"skills/{readme_relative_path}: {exc}")

    for procedure in procedure_records:
        if not procedure.routed and not procedure.standalone:
            orphan_findings.append(
                f"{procedure.path.relative_to(ROOT)} is neither routed by a role nor standalone"
            )

    if args.strict:
        errors.extend(orphan_findings)

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
    if orphan_findings:
        print("Orphan procedure findings:")
        for finding in orphan_findings:
            print(f"- {finding}")
        print()
    for record in records:
        rel_path = record.path.relative_to(ROOT)
        handoffs = ", ".join(record.handoffs)
        print(f"- {record.name} [{record.role}] -> {handoffs} ({rel_path})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
