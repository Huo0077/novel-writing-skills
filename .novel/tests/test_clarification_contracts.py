"""Clarification protocol/artifact checks, not autonomous dialogue tests."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
import yaml
ROOT=Path(__file__).resolve().parents[2]
FIX=ROOT/".novel/tests/fixtures/clarification"
class ClarificationContracts(unittest.TestCase):
    def test_shared_question_contract(self):
        text=(ROOT/".novel/schemas/clarification-contract.md").read_text(encoding="utf-8")
        for field in ("question_id","missing_information","options","custom_answer","undecided","blocking_scope","user_answer","source_ref","confirmation_scope"):
            self.assertIn(field,text)
    def test_all_skills_have_question_rule_or_reader_exception(self):
        for p in (ROOT/".codex/skills").glob("novel-*/SKILL.md"):
            s=p.read_text(encoding="utf-8")
            self.assertIn("clarification-contract.md",s,p.parent.name)
            if p.parent.name in ("novel-reader-hypothesis-test","novel-context","novel-router"):
                self.assertIn("reader",s)
                self.assertIn("作者",s)
    def test_question_options_are_distinct_and_no_default_choice(self):
        q=yaml.safe_load((FIX/"question.yaml").read_text(encoding="utf-8"))
        self.assertTrue(2<=len(q["options"])<=3)
        self.assertEqual(len({x["id"] for x in q["options"]}),len(q["options"]))
        for option in q["options"]:
            self.assertTrue(option["description"]);self.assertTrue(option["tradeoff"])
        self.assertTrue(q["custom_answer"]);self.assertTrue(q["undecided"])
        self.assertIsNone(q["selected_option"])
    def test_custom_answer_is_not_forced_to_existing_options(self):
        q=yaml.safe_load((FIX/"custom-answer.yaml").read_text(encoding="utf-8"))
        self.assertIsNone(q["selected_option"]);self.assertTrue(q["user_answer"])
        self.assertEqual(q["answer_status"],"custom")
        self.assertTrue(q["source_ref"])
    def test_unresolved_question_blocks_only_dependent_work(self):
        q=yaml.safe_load((FIX/"unresolved.yaml").read_text(encoding="utf-8"))
        self.assertEqual(q["answer_status"],"undecided");self.assertEqual(q["dependent_action_status"],"blocked")
        self.assertTrue(q["independent_safe_actions"]);self.assertFalse(q["canon_updated"])
    def test_partial_answer_has_limited_confirmation_scope(self):
        q=yaml.safe_load((FIX/"partial-answer.yaml").read_text(encoding="utf-8"))
        self.assertTrue(q["confirmation_scope"]);self.assertTrue(q["still_unknown"])
        self.assertFalse(q["all_options_approved"])
    def test_high_risk_answer_has_explicit_pending_decision(self):
        q=yaml.safe_load((FIX/"high-risk.yaml").read_text(encoding="utf-8"))
        self.assertEqual(q["risk"],"high");self.assertTrue(q["requires_confirmation"])
        self.assertEqual(q["creator_decision"],"pending");self.assertFalse(q["canon_updated"])
    def test_selected_option_records_only_the_chosen_scope(self):
        q=yaml.safe_load((FIX/"chosen-answer.yaml").read_text(encoding="utf-8"))
        self.assertEqual(q["selected_option"],"C")
        self.assertEqual(q["answer_status"],"chosen")
        self.assertTrue(q["source_ref"])
        self.assertEqual(q["confirmation_scope"],["当前场停在门外核查路线"])
        self.assertFalse(q["approved_key_return"])
        self.assertFalse(q["approved_core_reveal"])
    def test_contradiction_is_not_silently_overwritten(self):
        q=yaml.safe_load((FIX/"conflicting-answer.yaml").read_text(encoding="utf-8"))
        self.assertTrue(q["existing_source"])
        self.assertTrue(q["user_answer_source"])
        self.assertEqual(q["next_step_status"],"clarification_needed")
        self.assertFalse(q["canon_updated"])
    def test_suite_validation_checks_live_configuration(self):
        path=ROOT/".codex/skills/novel-router/scripts/suite.py"
        spec=importlib.util.spec_from_file_location("suite_integration",path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        with tempfile.TemporaryDirectory() as t:
            target=Path(t)/"new";mod.bootstrap_project(ROOT,target,apply=True)
            (target/".novel/config/modes.yaml").write_text("modes: [broken",encoding="utf-8")
            errors=mod.validate_suite(target)["errors"]
            self.assertTrue(any("modes.yaml" in e for e in errors),errors)
if __name__=="__main__":unittest.main()
