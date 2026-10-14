"""Test packaging and non-overwriting bootstrap using isolated fake projects."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
SCRIPT = Path(__file__).resolve().parents[1]/"scripts/suite.py"
spec = importlib.util.spec_from_file_location("suite_tools",SCRIPT)
mod = importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

def fixture(root):
    skill = root/".codex/skills/novel-router"
    (skill/"references").mkdir(parents=True)
    (skill/"agents").mkdir()
    (skill/"SKILL.md").write_text('---\nname: novel-router\ndescription: Route a novel request.\n---\n\n# Router\n`references/routes.md`\n',encoding="utf-8")
    (skill/"references/routes.md").write_text("Routes",encoding="utf-8")
    (skill/"agents/openai.yaml").write_text('interface:\n  display_name: "Router"\n  short_description: "Route novel requests with a clear bounded workflow"\n  default_prompt: "Use $novel-router for the task."\n',encoding="utf-8")
    (skill/"references/catalog.json").write_text(json.dumps({"version":"1.0","skills":[{"name":"novel-router","role":"router"}],"routes":[{"intent":"test","chain":["novel-router"]}]}),encoding="utf-8")
    seed=skill/"assets/project-seed/.novel"
    (seed/"schemas").mkdir(parents=True)
    (seed/"project.yaml").write_text('title: "未命名小说"\n',encoding="utf-8")
    (seed/"schemas/test.md").write_text("Protocol",encoding="utf-8")
    return skill

class SuiteTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)/"source";self.skill=fixture(self.root)
    def tearDown(self): self.tmp.cleanup()
    def test_valid_minimal_suite(self):
        self.assertEqual(mod.validate_suite(self.root)["errors"],[])
    def test_missing_catalogued_skill_is_error(self):
        p=self.skill/"references/catalog.json";d=json.loads(p.read_text());d["skills"].append({"name":"novel-missing","role":"x"});p.write_text(json.dumps(d))
        self.assertTrue(any("missing skill" in x for x in mod.validate_suite(self.root)["errors"]))
    def test_frontmatter_name_mismatch(self):
        p=self.skill/"SKILL.md";p.write_text(p.read_text().replace('name: novel-router','name: novel-other'))
        self.assertTrue(any("name mismatch" in x for x in mod.validate_suite(self.root)["errors"]))
    def test_ui_length_error(self):
        p=self.skill/"agents/openai.yaml";p.write_text(p.read_text().replace('Route novel requests with a clear bounded workflow','x'))
        self.assertTrue(any("short_description" in x for x in mod.validate_suite(self.root)["errors"]))
    def test_missing_local_reference(self):
        (self.skill/"references/routes.md").unlink()
        self.assertTrue(any("missing reference" in x for x in mod.validate_suite(self.root)["errors"]))
    def test_route_to_unknown_module(self):
        p=self.skill/"references/catalog.json";d=json.loads(p.read_text());d["routes"][0]["chain"]=["novel-unknown"];p.write_text(json.dumps(d))
        self.assertTrue(any("unknown route" in x for x in mod.validate_suite(self.root)["errors"]))
    def test_preview_does_not_create_target(self):
        target=Path(self.tmp.name)/"preview";r=mod.bootstrap_project(self.root,target)
        self.assertEqual(r["mode"],"preview");self.assertFalse(target.exists());self.assertTrue(r["create"])
    def test_apply_creates_skill_and_clean_project(self):
        target=Path(self.tmp.name)/"new";mod.bootstrap_project(self.root,target,apply=True)
        self.assertTrue((target/".codex/skills/novel-router/SKILL.md").is_file());self.assertTrue((target/".novel/project.yaml").is_file())
    def test_apply_preserves_existing_file_and_is_idempotent(self):
        target=Path(self.tmp.name)/"existing";(target/".novel").mkdir(parents=True)
        p=target/".novel/project.yaml";p.write_text("MY PRIVATE NOVEL",encoding="utf-8");before=p.read_bytes()
        result=mod.bootstrap_project(self.root,target,apply=True)
        self.assertIn(".novel/project.yaml",result["preserve"]);self.assertEqual(p.read_bytes(),before)
        self.assertEqual(mod.bootstrap_project(self.root,target,apply=True)["create"],[])
    def test_symlink_target_rejected_before_writes(self):
        target=Path(self.tmp.name)/"link";actual=Path(self.tmp.name)/"actual";actual.mkdir()
        try: target.symlink_to(actual,target_is_directory=True)
        except OSError: self.skipTest("OS does not permit symlinks for this account")
        with self.assertRaises(ValueError): mod.bootstrap_project(self.root,target,apply=True)
    def test_package_uses_seed_not_real_story(self):
        private=self.root/".novel/canon/secret.md";private.parent.mkdir(parents=True);private.write_text("PRIVATE AUTHOR ANSWER",encoding="utf-8")
        (self.root/".novel/project.yaml").write_text("title: PRIVATE TITLE",encoding="utf-8")
        log=self.root/".novel/tests/local-run-report.json";log.parent.mkdir(parents=True);log.write_text("PRIVATE RUN LOG",encoding="utf-8")
        out=Path(self.tmp.name)/"bundle.zip";mod.build_bundle(self.root,out)
        with zipfile.ZipFile(out) as z:
            self.assertNotIn(".novel/canon/secret.md",z.namelist())
            self.assertNotIn(".novel/tests/local-run-report.json",z.namelist())
            self.assertNotIn(b"PRIVATE",z.read(".novel/project.yaml"))
    def test_package_refuses_overwrite(self):
        out=Path(self.tmp.name)/"existing.zip";out.write_bytes(b"keep")
        with self.assertRaises(FileExistsError): mod.build_bundle(self.root,out)
        self.assertEqual(out.read_bytes(),b"keep")
    def test_inspect_checks_hashes(self):
        out=Path(self.tmp.name)/"ok.zip";mod.build_bundle(self.root,out)
        self.assertEqual(mod.inspect_bundle(out)["errors"],[])
        with zipfile.ZipFile(out) as z: files={n:z.read(n) for n in z.namelist()}
        files[".novel/project.yaml"]=b"tampered"
        bad=Path(self.tmp.name)/"bad.zip"
        with zipfile.ZipFile(bad,"w") as z:
            for name,data in files.items(): z.writestr(name,data)
        self.assertTrue(any("hash mismatch" in x for x in mod.inspect_bundle(bad)["errors"]))
    def test_inspect_rejects_path_traversal(self):
        out=Path(self.tmp.name)/"escape.zip"
        with zipfile.ZipFile(out,"w") as z: z.writestr("../escape.txt","bad")
        self.assertTrue(any("unsafe archive path" in x for x in mod.inspect_bundle(out)["errors"]))
    def test_cli_validate_returns_json(self):
        with contextlib.redirect_stdout(io.StringIO()) as out: status=mod.main(["validate","--root",str(self.root)])
        self.assertEqual(status,0);self.assertEqual(json.loads(out.getvalue())["skill_count"],1)
    def test_invalid_catalog_is_reported(self):
        (self.skill/"references/catalog.json").write_text('{bad',encoding="utf-8")
        self.assertTrue(mod.validate_suite(self.root)["errors"])

if __name__ == "__main__": unittest.main()
