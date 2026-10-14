"""Strict, read-only validation of novel configuration and state-change proposals.

Unknown creative facts remain questions for the creator. Structural validation
neither authenticates creator decisions nor detects prose contradictions.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
from typing import Any
try:
    import yaml
except ImportError:
    yaml = None

ALLOWED_STATES = {"CANON", "TENTATIVE", "PROPOSAL", "DRAFT", "REJECTED", "ARCHIVED"}
ALLOWED_RISKS = {"low", "medium", "high"}
ALLOWED_MODES = {"author_assistant", "co_author", "semi_automatic"}
ALLOWED_CHANGE_TYPES = {"add_fact", "update_state", "relation_change", "reveal", "rule_change", "retcon"}
STATUS_DECISION = {"proposed": "pending", "accepted": "accepted", "modified": "modified", "rejected": "rejected"}
REQUIRED_PROJECT_KEYS = {"project_id", "title", "mode", "genre", "current", "schema_version"}
REQUIRED_PROPOSAL_KEYS = {"change_id", "status", "risk", "source_ref", "change_type", "summary", "affected_entities", "requires_confirmation", "creator_decision"}
REQUIRED_FILES = (Path(".novel/project.yaml"), Path(".novel/config/modes.yaml"), Path(".novel/config/style-profile.yaml"))
RISK_POLICY = {"low": {"storage": "TENTATIVE", "confirmation": "none"},
               "medium": {"storage": "PROPOSAL", "confirmation": "batch"},
               "high": {"storage": "PROPOSAL", "confirmation": "immediate"}}


def load_yaml(path: Path) -> dict[str, Any]:
    if yaml is None:
        raise RuntimeError("PyYAML is required to validate this project")
    class UniqueSafeLoader(yaml.SafeLoader):
        pass
    def unique_mapping(loader, node, deep=False):
        loader.flatten_mapping(node)
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            try:
                duplicate = key in result
            except TypeError as exc:
                raise ValueError(f"{path}: unhashable YAML key") from exc
            if duplicate:
                raise ValueError(f"{path}: duplicate YAML key: {key!r}")
            result[key] = loader.construct_object(value_node, deep=deep)
        return result
    UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
    data = yaml.load(Path(path).read_text(encoding="utf-8-sig"), Loader=UniqueSafeLoader)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: top-level YAML value must be a mapping (not empty/null)")
    return data


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _require_text(data, names, source, errors):
    for name in names:
        if not _text(data.get(name)):
            errors.append(f"{source}: {name} must be a nonempty string")


def _enum(value, choices, name, source, errors):
    if not isinstance(value, str) or value not in choices:
        errors.append(f"{source}: unknown {name}: {value!r}")
        return False
    return True


def _strings(value, name, source, errors, nonempty=False, unique=False):
    if not isinstance(value, list) or any(not _text(x) for x in value) or (nonempty and not value):
        errors.append(f"{source}: {name} must be {'a nonempty ' if nonempty else 'a '}list of nonempty strings")
    elif unique and len(set(value)) != len(value):
        errors.append(f"{source}: {name} contains duplicate entries")


def validate_status_change(data: dict[str, Any], source: Path) -> list[str]:
    errors = []
    if not isinstance(data, dict):
        return [f"{source}: proposal must be a mapping"]
    missing = sorted(REQUIRED_PROPOSAL_KEYS - set(data))
    if missing:
        errors.append(f"{source}: missing required proposal fields: {', '.join(missing)}")
    _require_text(data, ("change_id", "summary", "source_ref"), source, errors)
    status_ok = _enum(data.get("status"), STATUS_DECISION, "state/status", source, errors)
    risk_ok = _enum(data.get("risk"), ALLOWED_RISKS, "risk", source, errors)
    decision_ok = _enum(data.get("creator_decision"), set(STATUS_DECISION.values()), "creator_decision", source, errors)
    _enum(data.get("change_type"), ALLOWED_CHANGE_TYPES, "change_type", source, errors)
    if type(data.get("requires_confirmation")) is not bool:
        errors.append(f"{source}: requires_confirmation must be a boolean, not a string or number")
    if risk_ok and data["risk"] in {"medium", "high"} and data.get("requires_confirmation") is not True:
        errors.append(f"{source}: {data['risk']}-risk change requires_confirmation must be true")
    if status_ok and decision_ok and STATUS_DECISION[data["status"]] != data["creator_decision"]:
        errors.append(f"{source}: status/creator_decision inconsistent: {data['status']!r}/{data['creator_decision']!r}")
    _strings(data.get("affected_entities"), "affected_entities", source, errors, nonempty=True, unique=True)
    if "downstream_impact" in data:
        _strings(data["downstream_impact"], "downstream_impact", source, errors)
    return errors


def validate_project_config(data, source):
    errors = []
    missing = sorted(REQUIRED_PROJECT_KEYS - set(data))
    if missing:
        errors.append(f"{source}: missing required keys: {', '.join(missing)}")
    _require_text(data, ("project_id", "title", "genre", "schema_version"), source, errors)
    _enum(data.get("mode"), ALLOWED_MODES, "mode", source, errors)
    current = data.get("current")
    if not isinstance(current, dict):
        errors.append(f"{source}: current must be a mapping")
    else:
        for field in ("volume", "chapter", "scene"):
            if type(current.get(field)) is not int or current[field] < 0:
                errors.append(f"{source}: current.{field} must be a nonnegative integer")
    return errors


def validate_modes_config(data, source):
    errors = []
    _require_text(data, ("schema_version",), source, errors)
    policy = data.get("risk_policy")
    if not isinstance(policy, dict):
        errors.append(f"{source}: risk_policy must be a mapping")
    else:
        for risk, expected in RISK_POLICY.items():
            entry = policy.get(risk)
            if not isinstance(entry, dict):
                errors.append(f"{source}: risk_policy.{risk} must be a mapping; review the current schema with the creator")
                continue
            for key, value in expected.items():
                if entry.get(key) != value:
                    errors.append(f"{source}: risk_policy.{risk}.{key} must be {value!r}")
    modes = data.get("modes")
    if not isinstance(modes, dict):
        errors.append(f"{source}: modes must be a mapping")
    else:
        for name in sorted(ALLOWED_MODES):
            entry = modes.get(name)
            if not isinstance(entry, dict):
                errors.append(f"{source}: missing/invalid mode entry: {name}")
                continue
            _require_text(entry, ("display_name",), f"{source}: modes.{name}", errors)
            _enum(entry.get("initiative"), {"low", "medium", "high"}, f"modes.{name}.initiative", source, errors)
            for field in ("batch_scope", "checkpoint_cadence"):
                _enum(entry.get(field), {"task", "scene", "chapter", "phase"}, f"modes.{name}.{field}", source, errors)
    return errors


def validate_style_config(data, source):
    errors = []
    _require_text(data, ("schema_version", "viewpoint", "narrative_distance", "tone"), source, errors)
    # unspecified/unknown are legal unresolved creative facts, not silently chosen values.
    for name in ("forbidden_phrases", "preferred_transitions"):
        _strings(data.get(name), name, source, errors)
    protected = data.get("protected_repetitions")
    if not isinstance(protected, list):
        errors.append(f"{source}: protected_repetitions must be a list")
    else:
        for i, entry in enumerate(protected):
            if _text(entry):
                continue
            if isinstance(entry, dict) and _text(entry.get("value")) and _text(entry.get("reason")):
                continue
            errors.append(f"{source}: protected_repetitions[{i}] requires a nonempty phrase or value/reason record")
    return errors


def validate_project(root: Path) -> list[str]:
    root = Path(root).resolve()
    errors = []
    validators = (validate_project_config, validate_modes_config, validate_style_config)
    for relative, validator in zip(REQUIRED_FILES, validators):
        source = root / relative
        if not source.is_file():
            errors.append(f"missing required file: {source}")
            continue
        try:
            data = load_yaml(source)
        except Exception as exc:
            errors.append(f"{source}: cannot load YAML: {exc}")
        else:
            errors.extend(validator(data, source))
    seen_ids = {}
    proposals = root / ".novel/proposals"
    if proposals.is_dir():
        for source in sorted(proposals.iterdir()):
            if not source.is_file() or source.suffix not in {".yaml", ".yml"}:
                continue
            try:
                data = load_yaml(source)
            except Exception as exc:
                errors.append(f"{source}: cannot load YAML: {exc}")
                continue
            errors.extend(validate_status_change(data, source))
            id_ = data.get("change_id")
            if _text(id_):
                if id_ in seen_ids:
                    errors.append(f"{source}: duplicate change_id {id_!r}; already in {seen_ids[id_]}")
                else:
                    seen_ids[id_] = source
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path)
    args = parser.parse_args(argv)
    errors = validate_project(args.project_root)
    if errors:
        for error in errors:
            print("ERROR: " + error)
        return 1
    print(f"VALID: {args.project_root.resolve()}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
