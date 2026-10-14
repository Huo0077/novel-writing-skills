"""Validate the durable state contract for a novel project."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - exercised only on minimal installs
    yaml = None

ALLOWED_STATES = {"CANON", "TENTATIVE", "PROPOSAL", "DRAFT", "REJECTED", "ARCHIVED"}
ALLOWED_RISKS = {"low", "medium", "high"}
REQUIRED_PROJECT_KEYS = {"project_id", "title", "mode", "genre", "current", "schema_version"}
REQUIRED_PROPOSAL_KEYS = {
    "change_id", "status", "risk", "source_ref", "change_type", "summary",
    "affected_entities", "requires_confirmation", "creator_decision",
}
REQUIRED_FILES = (
    Path(".novel/project.yaml"),
    Path(".novel/config/modes.yaml"),
    Path(".novel/config/style-profile.yaml"),
)


def load_yaml(path: Path) -> dict[str, Any]:
    if yaml is None:
        raise RuntimeError("PyYAML is required to validate this project")
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: top-level YAML value must be a mapping")
    return data


def validate_project(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required file: {path}")

    project_path = root / ".novel/project.yaml"
    if project_path.is_file():
        try:
            project = load_yaml(project_path)
        except Exception as exc:
            errors.append(f"{project_path}: cannot load YAML: {exc}")
        else:
            missing = sorted(REQUIRED_PROJECT_KEYS - set(project))
            if missing:
                errors.append(f"{project_path}: missing required keys: {', '.join(missing)}")
            if project.get("mode") not in {"author_assistant", "co_author", "semi_automatic"}:
                errors.append(f"{project_path}: unknown mode: {project.get('mode')!r}")

    proposals = root / ".novel/proposals"
    if proposals.is_dir():
        for path in sorted(proposals.glob("*.y*ml")):
            try:
                data = load_yaml(path)
            except Exception as exc:
                errors.append(f"{path}: cannot load YAML: {exc}")
                continue
            errors.extend(validate_status_change(data, path))
    return errors


def validate_status_change(data: dict[str, Any], source: Path) -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED_PROPOSAL_KEYS - set(data))
    if missing:
        errors.append(f"{source}: missing required proposal fields: {', '.join(missing)}")
    state = data.get("status")
    if state is not None and state not in {"proposed", "accepted", "modified", "rejected"}:
        errors.append(f"{source}: unknown state/status: {state!r}")
    risk = data.get("risk")
    if risk is not None and risk not in ALLOWED_RISKS:
        errors.append(f"{source}: unknown risk: {risk!r}")
    decision = data.get("creator_decision")
    if decision is not None and decision not in {"pending", "accepted", "modified", "rejected"}:
        errors.append(f"{source}: unknown creator_decision: {decision!r}")
    if risk == "high" and data.get("requires_confirmation") is not True:
        errors.append(f"{source}: high-risk change requires_confirmation must be true")
    if not isinstance(data.get("affected_entities"), list):
        errors.append(f"{source}: affected_entities must be a list")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path)
    args = parser.parse_args(argv)
    errors = validate_project(args.project_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"VALID: {args.project_root.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
