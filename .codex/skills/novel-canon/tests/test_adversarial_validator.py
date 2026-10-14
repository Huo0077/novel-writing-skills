"""New refusal tests: expose defects without modifying production code."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[4]
SCRIPT = ROOT / ".codex/skills/novel-canon/scripts/validate_novel_project.py"
spec = importlib.util.spec_from_file_location("canon_probe", SCRIPT)
mod = importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def valid():
    return {"change_id":"SC-PROBE","status":"proposed","risk":"medium","source_ref":"chapter-1#p1","change_type":"add_fact","summary":"新承诺","affected_entities":["C-test"],"requires_confirmation":True,"creator_decision":"pending"}
class AdversarialRefusalTests(unittest.TestCase):
    def test_medium_risk_requires_confirmation(self):
        data=valid();data["requires_confirmation"]=False
        self.assertTrue(mod.validate_status_change(data,Path("test.yaml")),"medium-risk confirmation bypass accepted")
    def test_blank_source_rejected(self):
        data=valid();data["source_ref"]=""
        self.assertTrue(mod.validate_status_change(data,Path("test.yaml")),"empty source accepted")
    def test_unknown_change_type_rejected(self):
        data=valid();data["change_type"]="rewrite_everything"
        self.assertTrue(mod.validate_status_change(data,Path("test.yaml")),"unknown change type accepted")
    def test_accepted_status_requires_accepted_creator_decision(self):
        data=valid();data["status"]="accepted";data["creator_decision"]="pending"
        self.assertTrue(mod.validate_status_change(data,Path("test.yaml")),"accepted/pending contradiction accepted")
    def test_null_risk_rejected(self):
        data=valid();data["risk"]=None
        self.assertTrue(mod.validate_status_change(data,Path("test.yaml")),"null risk accepted")
    def test_malformed_mode_config_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);novel=root/".novel";(novel/"config").mkdir(parents=True)
            (novel/"project.yaml").write_text('project_id: p\ntitle: t\nmode: author_assistant\ngenre: x\nschema_version: "1.0"\ncurrent:\n  volume: 0\n  chapter: 0\n  scene: 0\n',encoding="utf-8")
            (novel/"config/modes.yaml").write_text('modes: [unterminated',encoding="utf-8")
            (novel/"config/style-profile.yaml").write_bytes((ROOT/".codex/skills/novel-router/assets/project-seed/.novel/config/style-profile.yaml").read_bytes())
            errors = mod.validate_project(root)
            self.assertTrue(any("modes.yaml" in e and "cannot load YAML" in e for e in errors),errors)
if __name__ == "__main__":unittest.main()
