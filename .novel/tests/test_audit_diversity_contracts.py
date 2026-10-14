"""Fixed artifact checks, not tests of LLM reasoning."""
import re
import unittest
from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / ".novel/tests/fixtures/audit-diversity"
SKILLS = ("novel-continuity-audit", "novel-causality-audit", "novel-style-audit", "novel-expression-diversify", "novel-style-revise", "novel-impact-review")
def load(name):
    return yaml.safe_load((FIX/name).read_text(encoding="utf-8"))
class AuditContracts(unittest.TestCase):
    def test_six_skills_and_ui(self):
        for name in SKILLS:
            with self.subTest(skill=name):
                p = ROOT / ".codex/skills" / name
                s = (p/"SKILL.md").read_text(encoding="utf-8")
                self.assertTrue(s.startswith("---\n"))
                self.assertEqual(yaml.safe_load(s.split("---\n", 2)[1])["name"], name)
                for field in ("输入", "输出", "novel-canon"):
                    self.assertIn(field, s)
                self.assertNotIn("???", s)
                self.assertLess(len(s.splitlines()), 500)
                ui = yaml.safe_load((p/"agents/openai.yaml").read_text(encoding="utf-8"))["interface"]
                self.assertTrue(25 <= len(ui["short_description"]) <= 64)
                self.assertIn("$"+name, ui["default_prompt"])

    def test_skill_references_and_protocol(self):
        for name in SKILLS:
            p = ROOT / ".codex/skills" / name
            refs = set(re.findall(r"references/[a-z-]+\.md", (p/"SKILL.md").read_text(encoding="utf-8")))
            self.assertGreaterEqual(len(refs), 2)
            for ref in refs:
                self.assertTrue((p/ref).is_file())
        protocol = (ROOT/".novel/schemas/audit-revision-contract.md").read_text(encoding="utf-8")
        for field in ("scope", "coverage", "meaning_constraints", "protection_decision", "new_facts", "downstream_impact"):
            self.assertIn(field, protocol)

    def test_motif_preserved_in_revised_sample(self):
        before = (FIX/"original.txt").read_text(encoding="utf-8")
        after = (FIX/"revised.txt").read_text(encoding="utf-8")
        self.assertEqual(before.count("银戒指"), 3)
        self.assertEqual(after.count("银戒指"), 3)
        decisions = load("decisions.yaml")
        self.assertEqual(decisions["motif"]["protection_decision"], "keep")

    def test_rewrite_candidates_have_semantic_constraints(self):
        for item in load("alternatives.yaml")["alternatives"]:
            self.assertTrue(item["meaning_constraints"])
            self.assertIsInstance(item["new_facts"], list)
            self.assertIn(item["risk"], {"low", "medium", "high"})
        self.assertTrue(any(x["new_facts"] for x in load("alternatives.yaml")["alternatives"]))

    def test_impact_declares_known_and_unknown_coverage(self):
        report = load("impact.yaml")
        self.assertTrue(report["coverage"]["read_sources"])
        self.assertTrue(report["coverage"]["not_read"])
        self.assertFalse(report["whole_novel_verified"])
        self.assertTrue(report["downstream_impact"])
        self.assertEqual(report["creator_decision"], "pending")

    def test_revision_is_not_canon_and_needs_reverse_review(self):
        report = load("revision.yaml")
        self.assertEqual(report["truth_status"], "DRAFT")
        self.assertEqual(report["handoff_status"], "creator_pending")
        self.assertTrue(report["review_ref"])
        self.assertTrue(report["new_facts"])
        self.assertEqual(report["protected_terms_preserved"], ["银戒指"])
if __name__ == "__main__":
    unittest.main()
