"""Actual strict-validation boundaries; all malformed values return diagnostics."""
import importlib.util
from pathlib import Path
import copy
import tempfile
import unittest
import yaml
ROOT=Path(__file__).resolve().parents[4]
spec=importlib.util.spec_from_file_location("strict_canon", ROOT/".codex/skills/novel-canon/scripts/validate_novel_project.py")
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def proposal():
    return {"change_id":"SC-01","status":"proposed","risk":"medium","source_ref":"chapter-1#p2","change_type":"add_fact","summary":"新增线索","affected_entities":["C-001"],"requires_confirmation":True,"creator_decision":"pending"}
class BoundaryTests(unittest.TestCase):
    def test_valid_status_decision_pairs(self):
        for status,decision in (("proposed","pending"),("accepted","accepted"),("modified","modified"),("rejected","rejected")):
            d=proposal();d.update(status=status,creator_decision=decision)
            self.assertEqual(mod.validate_status_change(d,Path("test.yaml")),[])
    def test_all_invalid_status_decision_combinations(self):
        pairs={"proposed":"pending","accepted":"accepted","modified":"modified","rejected":"rejected"}
        for status in pairs:
            for decision in set(pairs.values())-{pairs[status]}:
                d=proposal();d.update(status=status,creator_decision=decision)
                self.assertTrue(mod.validate_status_change(d,Path("test.yaml")), (status,decision))
    def test_text_fields_require_nonblank_strings(self):
        for key in ("change_id","summary","source_ref"):
            for bad in (None,"", "  ",2,[],{}):
                with self.subTest(key=key,bad=bad):
                    d=proposal();d[key]=bad
                    self.assertTrue(mod.validate_status_change(d,Path("test.yaml")))
    def test_enum_type_errors_do_not_crash(self):
        for key in ("status","risk","change_type","creator_decision"):
            for bad in (None,[],{},True,1):
                with self.subTest(key=key,bad=bad):
                    d=proposal();d[key]=bad
                    self.assertTrue(mod.validate_status_change(d,Path("test.yaml")))
    def test_confirmation_requires_real_boolean(self):
        for bad in ("true",1,0,None,[],{}):
            d=proposal();d["requires_confirmation"]=bad
            self.assertTrue(mod.validate_status_change(d,Path("test.yaml")))
    def test_both_medium_and_high_must_confirm(self):
        for risk in ("medium","high"):
            d=proposal();d.update(risk=risk,requires_confirmation=False)
            self.assertTrue(mod.validate_status_change(d,Path("test.yaml")))
    def test_low_can_remain_tentative_without_confirmation(self):
        d=proposal();d.update(risk="low",requires_confirmation=False)
        self.assertEqual(mod.validate_status_change(d,Path("test.yaml")),[])
    def test_nonempty_unique_entities(self):
        for bad in ([],[""],["  "],[{}],[2],["C-001","C-001"],"C-001",None):
            d=proposal();d["affected_entities"]=bad
            self.assertTrue(mod.validate_status_change(d,Path("test.yaml")))
    def test_nonmapping_proposal_does_not_crash(self):
        for bad in ([],None,"text",5):
            self.assertTrue(mod.validate_status_change(bad,Path("test.yaml")))
    def test_supported_change_types(self):
        for value in ("add_fact","update_state","relation_change","reveal","rule_change","retcon"):
            d=proposal();d["change_type"]=value
            self.assertEqual(mod.validate_status_change(d,Path("test.yaml")),[])
    def test_duplicate_yaml_keys_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/"bad.yaml";p.write_text("risk: high\nrisk: low\n",encoding="utf-8")
            with self.assertRaises(ValueError): mod.load_yaml(p)
    def test_empty_yaml_does_not_get_silently_coerced(self):
        with tempfile.TemporaryDirectory() as t:
            for i,text in enumerate(("", "[]", "false", "null")):
                p=Path(t)/f"bad-{i}.yaml";p.write_text(text,encoding="utf-8")
                with self.assertRaises(ValueError): mod.load_yaml(p)
    def project_case(self,mutator):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);base=ROOT/".codex/skills/novel-router/assets/project-seed/.novel"
            for rel in ("project.yaml","config/modes.yaml","config/style-profile.yaml"):
                dest=root/".novel"/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes((base/rel).read_bytes())
            mutator(root/".novel")
            return mod.validate_project(root)
    def change_yaml(self,path,change):
        data=yaml.safe_load(path.read_text(encoding="utf-8"));change(data);path.write_text(yaml.safe_dump(data,allow_unicode=True),encoding="utf-8")
    def test_unknown_project_mode_type_is_diagnostic(self):
        self.assertTrue(self.project_case(lambda p:self.change_yaml(p/"project.yaml",lambda d:d.update(mode=[]))))
    def test_invalid_current_progress(self):
        for bad in ([],{}, {"volume":0,"chapter":True,"scene":0},{"volume":0,"chapter":-1,"scene":0}):
            self.assertTrue(self.project_case(lambda p:self.change_yaml(p/"project.yaml",lambda d:d.update(current=bad))))
    def test_mode_risk_policy_cannot_weaken_confirmation(self):
        def mutate(p):
            self.change_yaml(p/"config/modes.yaml",lambda d:d["risk_policy"]["medium"].update(confirmation="none"))
        self.assertTrue(self.project_case(mutate))
    def test_missing_mode_entry_rejected(self):
        self.assertTrue(self.project_case(lambda p:self.change_yaml(p/"config/modes.yaml",lambda d:d["modes"].pop("co_author"))))
    def test_malformed_style_yaml_rejected(self):
        self.assertTrue(self.project_case(lambda p:(p/"config/style-profile.yaml").write_text("tone: [broken",encoding="utf-8")))
    def test_style_lists_and_protection_record_types(self):
        for bad in ("phrase",[None],[{}]):
            self.assertTrue(self.project_case(lambda p:self.change_yaml(p/"config/style-profile.yaml",lambda d:d.update(protected_repetitions=bad))))
    def test_valid_unresolved_style_is_allowed(self):
        self.assertEqual(self.project_case(lambda p:None),[])
    def test_duplicate_change_ids_rejected(self):
        def mutate(p):
            (p/"proposals").mkdir()
            for name in ("a","b"):(p/"proposals"/(name+".yaml")).write_text(yaml.safe_dump(proposal(),allow_unicode=True),encoding="utf-8")
        self.assertTrue(self.project_case(mutate))
    def test_validation_is_read_only(self):
        d=proposal();before=copy.deepcopy(d);mod.validate_status_change(d,Path("test.yaml"));self.assertEqual(d,before)
if __name__=="__main__":unittest.main()
