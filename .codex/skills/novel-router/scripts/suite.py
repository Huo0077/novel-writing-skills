"""Portable novel skill-suite validation, additive bootstrap and packaging.

No global installation; no automatic story approval; no archive extraction.
Run with filesystem permissions for the intended target. Hashes are not signatures.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import zipfile

ALLOWED_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".json", ".txt", ".mjs", ".png"}
MANIFEST = "novel-suite-manifest.json"


def _skills(root):
    root = Path(root)
    for relative in (".codex/skills", ".agents/skills", ".claude/skills"):
        folder = root / relative
        if (folder / "novel-router/SKILL.md").is_file():
            return folder
    return root / ".codex/skills"

def _router(root): return _skills(root) / "novel-router"

def _seed(root): return _router(root) / "assets/project-seed"

def _linked(path):
    return path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction())

def _safe_destination(path):
    raw = Path(os.path.abspath(path))
    for part in [raw, *raw.parents]:
        if _linked(part): raise ValueError("linked destination is not permitted: " + str(part))
    return raw

def _catalog(root):
    data = json.loads((_router(root)/"references/catalog.json").read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict) or not isinstance(data.get("skills"), list) or not isinstance(data.get("routes"), list):
        raise ValueError("catalog requires skills and routes lists")
    names = []
    for item in data["skills"]:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str) or not re.fullmatch(r"novel-[a-z0-9-]+", item["name"]):
            raise ValueError("invalid catalog skill")
        names.append(item["name"])
    if len(names) != len(set(names)): raise ValueError("duplicate catalog skill")
    return data


def validate_suite(root: Path) -> dict:
    root = Path(root).resolve()
    report = {"root": str(root), "skill_count": 0, "errors": [], "warnings": []}
    errors = report["errors"]
    try:
        import yaml
        catalog = _catalog(root)
    except (ImportError, OSError, ValueError) as exc:
        errors.append("cannot load catalog/dependency: " + str(exc));return report
    names = [x["name"] for x in catalog["skills"]]
    report["skill_count"] = len(names)
    actual = {p.parent.name for p in _skills(root).glob("novel-*/SKILL.md")}
    for name in sorted(actual-set(names)): errors.append("uncatalogued skill: " + name)
    for route in catalog["routes"]:
        if not isinstance(route, dict) or not isinstance(route.get("chain"), list) or not route["chain"]:
            errors.append("invalid route entry");continue
        for name in route["chain"]:
            if name not in names: errors.append("unknown route module: " + str(name))
    for name in names:
        folder = _skills(root)/name
        p = folder/"SKILL.md"
        if not p.is_file(): errors.append("missing skill: " + name);continue
        try:
            text = p.read_text(encoding="utf-8")
            match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
            if not match: raise ValueError("invalid UTF-8 frontmatter")
            meta = yaml.safe_load(match.group(1))
            if not isinstance(meta, dict) or set(meta) != {"name", "description"}: raise ValueError("name/description fields required")
            if meta["name"] != name: errors.append("name mismatch: " + name)
            if not isinstance(meta["description"], str) or not meta["description"].strip(): errors.append("missing description: " + name)
            if len(text.splitlines()) >= 500: errors.append("oversized SKILL.md: " + name)
            ui = yaml.safe_load((folder/"agents/openai.yaml").read_text(encoding="utf-8-sig"))["interface"]
            if not 25 <= len(ui.get("short_description", "")) <= 64: errors.append("short_description length: " + name)
            if "$"+name not in ui.get("default_prompt", ""): errors.append("default_prompt missing skill: " + name)
            for ref in re.findall(r"`([^`]+\.md)`", text):
                if ref.startswith(("references/", "assets/")): target = folder/ref
                elif ref.startswith(".novel/"):
                    target = root/ref
                    if not target.is_file(): target = _seed(root)/ref
                elif ref.startswith(".codex/skills/"): target = _skills(root)/ref[len(".codex/skills/"): ]
                else: continue
                if not target.is_file(): errors.append("missing reference: " + name + " -> " + ref)
        except (OSError, ValueError, TypeError, KeyError, yaml.YAMLError) as exc:
            errors.append(name + ": " + str(exc))
    seed = _seed(root)/".novel"
    if not (seed/"project.yaml").is_file(): errors.append("missing clean project seed")
    for category in ("schemas", "templates"):
        source = root/".novel"/category
        if source.is_dir():
            for p in source.glob("*.md"):
                target = seed/category/p.name
                if not target.is_file() or target.read_bytes() != p.read_bytes():
                    errors.append("seed mismatch: " + category + "/" + p.name)
    # A static skill check must not silently skip broken live state/configuration.
    if (root/".novel/project.yaml").is_file():
        validator_path = _skills(root)/"novel-canon/scripts/validate_novel_project.py"
        if not validator_path.is_file():
            errors.append("missing live-project validator: " + str(validator_path))
        else:
            try:
                spec = importlib.util.spec_from_file_location("novel_live_validator", validator_path)
                validator = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(validator)
                errors.extend(validator.validate_project(root))
            except Exception as exc:
                errors.append("live-project validation failed: " + str(exc))
    report["warnings"].append("Static checks do not establish literary quality or independent reader performance.")
    return report


def _files(folder):
    if not folder.is_dir(): raise ValueError("missing source directory: " + str(folder))
    for p in sorted(folder.rglob("*")):
        if "__pycache__" in p.parts or ".git" in p.parts: continue
        if _linked(p): raise ValueError("linked source is not packaged: " + str(p))
        if p.is_file() and (p.suffix in ALLOWED_SUFFIXES or p.name == ".keep"):
            yield p


def _inventory(root, include_tests=False, include_docs=False):
    root = Path(root).resolve()
    catalog = _catalog(root)
    items = {}
    for entry in catalog["skills"]:
        folder = _skills(root)/entry["name"]
        for p in _files(folder):
            name = (Path(".codex/skills")/entry["name"]/p.relative_to(folder)).as_posix()
            items[name] = p.read_bytes()
    for p in _files(_seed(root)):
        items[p.relative_to(_seed(root)).as_posix()] = p.read_bytes()
    if include_tests and (root/".novel/tests").is_dir():
        for p in _files(root/".novel/tests"):
            rel = p.relative_to(root/".novel/tests")
            # Export only test code and explicitly isolated fixtures, not local logs.
            if rel.parts[0] == "fixtures" or (len(rel.parts) == 1 and p.name.startswith("test_") and p.suffix == ".py"):
                items[p.relative_to(root).as_posix()] = p.read_bytes()
    if include_docs:
        for name in ("README.md", "README.en.md", "LICENSE", "requirements.txt", "package.json", "docs/assets/novel-writing-skills-cover.png", "docs/installation-v1.2.md", "小说skills-快速开始.md", "docs/novel-skills/skills组使用指南.md"):
            p=root/name
            if p.is_file(): items[name]=p.read_bytes()
    return items, catalog


def bootstrap_project(root: Path, target: Path, apply=False) -> dict:
    target = _safe_destination(target)
    items, _ = _inventory(root, include_tests=True, include_docs=True)
    report = {"mode": "apply" if apply else "preview", "target": str(target), "create": [], "preserve": []}
    for name in items:
        path = _safe_destination(target/name)
        if path.exists():
            if not path.is_file(): raise ValueError("file destination is a directory: " + str(path))
            report["preserve"].append(name)
        else:
            for parent in path.parents:
                if parent.exists() and not parent.is_dir(): raise ValueError("parent is not a directory: " + str(parent))
            report["create"].append(name)
    if apply:
        for name in report["create"]:
            path = target/name
            path.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive write: an intervening file is preserved, not truncated.
            with path.open("xb") as handle: handle.write(items[name])
    return report


def build_bundle(root: Path, output: Path) -> dict:
    output = _safe_destination(output)
    if output.exists(): raise FileExistsError("refusing to overwrite archive: " + str(output))
    items, catalog = _inventory(root, include_tests=True, include_docs=True)
    manifest = {"format": "novel-writing-skills", "version": catalog.get("version", "1.0"),
                "skills": [x["name"] for x in catalog["skills"]],
                "files": {name: hashlib.sha256(data).hexdigest() for name, data in sorted(items.items())},
                "data_policy": "clean_seed_and_isolated_test_fixtures_not_live_story"}
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as handle:
        with zipfile.ZipFile(handle, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name, data in sorted(items.items()): archive.writestr(name, data)
            archive.writestr(MANIFEST, json.dumps(manifest, ensure_ascii=False, indent=2)+"\n")
    return {"output": str(output), "skill_count": len(manifest["skills"]), "file_count": len(items), "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}


def _unsafe_member(name):
    p = PurePosixPath(name)
    return not name or "\\" in name or ":" in name or name.startswith("/") or ".." in p.parts or name.endswith("/")

def inspect_bundle(path: Path) -> dict:
    report = {"archive": str(path), "errors": [], "file_count": 0, "skill_count": 0}
    errors = report["errors"]
    try:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            if len(names) != len(set(names)): errors.append("duplicate archive members")
            for name in names:
                if _unsafe_member(name): errors.append("unsafe archive path: " + name)
            if errors: return report
            if MANIFEST not in names:
                errors.append("missing manifest");return report
            manifest = json.loads(z.read(MANIFEST))
            files = manifest.get("files")
            if not isinstance(files, dict) or not isinstance(manifest.get("skills"), list):
                errors.append("invalid manifest shape");return report
            if set(files) != set(names)-{MANIFEST}: errors.append("manifest member set mismatch")
            for name, digest in files.items():
                if not isinstance(name, str) or _unsafe_member(name): errors.append("unsafe manifest path: " + str(name));continue
                if name not in names: continue
                if hashlib.sha256(z.read(name)).hexdigest() != digest: errors.append("hash mismatch: " + name)
            report["file_count"] = len(files);report["skill_count"] = len(manifest["skills"])
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile) as exc:
        errors.append("cannot inspect archive: " + str(exc))
    return report


def _run_tests(root):
    groups = [("contracts", ".novel/tests", "test_*contracts.py"),
              ("canon", ".codex/skills/novel-canon/tests", "test*.py"),
              ("expression", ".codex/skills/novel-style-audit/tests", "test*.py"),
              ("reader_packet", ".codex/skills/novel-reader-hypothesis-test/tests", "test*.py"),
              ("suite", ".codex/skills/novel-router/tests", "test*.py")]
    results=[]
    for name, path, pattern in groups:
        if not (root/path).is_dir():
            results.append({"group": name, "status": "missing", "returncode": 1});continue
        proc=subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", path, "-p", pattern, "-v"],cwd=root,capture_output=True,text=True,encoding="utf-8",env={**os.environ,"PYTHONUTF8":"1"})
        log=proc.stdout+proc.stderr
        match=re.search(r"Ran (\d+) tests?",log)
        results.append({"group":name,"returncode":proc.returncode,"test_count":int(match.group(1)) if match else 0,"log":log})
    node_test = _router(root)/"tests/test-init-project.mjs"
    if node_test.is_file():
        try:
            proc = subprocess.run(["node", "--test", str(node_test)], cwd=root, capture_output=True, text=True, encoding="utf-8")
            log = proc.stdout + proc.stderr
            matches = re.findall(r"(?:#|ℹ) tests (\d+)", log)
            count = int(matches[-1]) if matches else 0
            results.append({"group":"node_init","returncode":proc.returncode,"test_count":count,"log":log})
        except OSError as exc:
            results.append({"group":"node_init","returncode":1,"test_count":0,"log":"Node.js is required for v1.2 installation tests: "+str(exc)})
    return results


def main(argv=None) -> int:
    default_root=Path(__file__).resolve().parents[4]
    parser=argparse.ArgumentParser(description=__doc__)
    commands=parser.add_subparsers(dest="command",required=True)
    validate=commands.add_parser("validate");validate.add_argument("--root",type=Path,default=default_root);validate.add_argument("--tests",action="store_true")
    bootstrap=commands.add_parser("bootstrap");bootstrap.add_argument("target",type=Path);bootstrap.add_argument("--root",type=Path,default=default_root);bootstrap.add_argument("--apply",action="store_true")
    package=commands.add_parser("package");package.add_argument("output",type=Path);package.add_argument("--root",type=Path,default=default_root)
    inspect=commands.add_parser("inspect");inspect.add_argument("archive",type=Path)
    args=parser.parse_args(argv)
    try:
        if args.command=="validate":
            result=validate_suite(args.root)
            if args.tests and not result["errors"]:
                result["test_groups"]=_run_tests(args.root.resolve())
                for group in result["test_groups"]:
                    if group["returncode"]: result["errors"].append("test failure: "+group["group"])
                result["test_count"]=sum(g.get("test_count",0) for g in result["test_groups"])
        elif args.command=="bootstrap":result=bootstrap_project(args.root,args.target,args.apply)
        elif args.command=="package":
            checked=validate_suite(args.root)
            if checked["errors"]: raise ValueError("suite validation failed: "+str(checked["errors"]))
            result=build_bundle(args.root,args.output)
        else:result=inspect_bundle(args.archive)
        print(json.dumps(result,ensure_ascii=False,indent=2))
        return 1 if result.get("errors") else 0
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print("ERROR: "+str(exc),file=sys.stderr);return 2

if __name__=="__main__":sys.exit(main())
