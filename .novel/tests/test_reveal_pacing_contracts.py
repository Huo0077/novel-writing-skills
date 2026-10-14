"""Fixed artifact contracts; no independent reader or model execution."""
import json
from pathlib import Path
import re
import unittest
import yaml
ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / ".novel/tests/fixtures/reveal-pacing"
SKILLS = ("novel-secret-design", "novel-clue-distribution", "novel-misdirection", "novel-reveal-calibration", "novel-reader-hypothesis-test", "novel-payoff-audit", "novel-pacing-audit")
def load(name): return yaml.safe_load((FIX/name).read_text(encoding="utf-8"))
class RevealContracts(unittest.TestCase):
    def test_seven_skills_and_metadata(self):
        for name in SKILLS:
            with self.subTest(skill=name):
                folder = ROOT/".codex/skills"/name
                text = (folder/"SKILL.md").read_text(encoding="utf-8")
                meta = yaml.safe_load(text.split("---\n", 2)[1])
                self.assertEqual(meta["name"], name);self.assertEqual(set(meta), {"name", "description"})
                self.assertLess(len(text.splitlines()), 500);self.assertNotIn("???", text)
                for term in ("输入", "输出", "novel-canon"): self.assertIn(term, text)
                ui = yaml.safe_load((folder/"agents/openai.yaml").read_text(encoding="utf-8"))["interface"]
                self.assertTrue(25 <= len(ui["short_description"]) <= 64);self.assertIn("$"+name, ui["default_prompt"])
    def test_references_and_shared_protocol(self):
        for name in SKILLS:
            folder = ROOT/".codex/skills"/name
            refs = set(re.findall(r"references/[a-z-]+\.md", (folder/"SKILL.md").read_text(encoding="utf-8")))
            self.assertGreaterEqual(len(refs), 2)
            for ref in refs: self.assertTrue((folder/ref).is_file())
        text = (ROOT/".novel/schemas/reveal-reader-contract.md").read_text(encoding="utf-8")
        for field in ("design_truth", "visible_evidence", "reader_guess", "payoff_outcome", "prepared_not_run", "manual_rehearsal", "independent_test", "reveal_gate", "coverage"): self.assertIn(field, text)
    def test_distribution_has_surface_functions_and_varied_carriers(self):
        rows = load("distribution.yaml")["clues"]
        self.assertGreaterEqual(len({r["carrier"] for r in rows}), 3)
        for row in rows:
            self.assertTrue(row["surface_function"]);self.assertTrue(row["visible_evidence"]);self.assertTrue(row["source_ref"])
    def test_competing_explanations_have_evidence_not_fake_facts(self):
        report = load("misdirection.yaml")
        self.assertGreaterEqual(len(report["hypotheses"]), 2)
        for item in report["hypotheses"]:
            self.assertTrue(item["evidence_refs"]);self.assertTrue(item["limitations"])
        self.assertFalse(report["narrator_false_assertion_allowed"])
    def test_reveal_gates_do_not_auto_authorize_core_reveal(self):
        report = load("calibration.yaml")
        self.assertEqual(report["core_reveal"]["risk"], "high")
        self.assertEqual(report["core_reveal"]["creator_decision"], "pending")
        self.assertTrue(report["core_reveal"]["reveal_gate"])
        self.assertNotEqual(report["local_reveal"]["stage"], report["core_reveal"]["stage"])
    def test_reader_packet_has_no_explicit_author_answer(self):
        packet = json.loads((FIX/"reader-packet.json").read_text(encoding="utf-8"))
        secret = load("secret.yaml")["design_truth"]
        rendered = json.dumps(packet, ensure_ascii=False)
        self.assertNotIn(secret, rendered);self.assertNotIn("design_truth", rendered)
        self.assertEqual(packet["test_status"], "prepared_not_run")
        state = load("reader-status.yaml");self.assertFalse(state["independent_run_performed"])
        self.assertIsNone(state["reader_guess"]);self.assertEqual(state["result_status"], "prepared_not_run")
    def test_payoff_requires_pre_reveal_evidence_and_consequence(self):
        payoff = load("payoff.yaml")
        self.assertEqual(payoff["evaluation_mode"], "manual_rehearsal")
        self.assertTrue(payoff["pre_reveal_evidence"]);self.assertTrue(payoff["retrospective_changes"])
        self.assertTrue(payoff["payoff_outcome"]["character_cost"])
        self.assertFalse(payoff["whole_novel_verified"])
    def test_pacing_coverage_and_aftermath(self):
        report = load("pacing.yaml")
        self.assertTrue(report["coverage"]["read_sources"]);self.assertTrue(report["coverage"]["not_read"])
        self.assertTrue(report["aftermath_required"])
        self.assertFalse(report["fixed_twist_every_chapter"])
if __name__ == "__main__": unittest.main()
