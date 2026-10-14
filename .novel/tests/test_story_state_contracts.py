"""Structural contract tests; not a test of literary quality or model reasoning."""
import re
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ("novel-world", "novel-character", "novel-timeline", "novel-plot", "novel-information", "novel-foreshadow-craft")
STATES = {"CANON", "TENTATIVE", "PROPOSAL", "DRAFT", "REJECTED", "ARCHIVED"}
FIXTURES = ROOT / ".novel/tests/fixtures/story-state"

class StoryStateContracts(unittest.TestCase):
    def test_chinese_content_preserved(self):
        paths = [ROOT / ".novel/schemas/story-record.md"]
        paths.extend(ROOT / ".codex/skills" / name / "SKILL.md" for name in SKILLS)
        for path in paths:
            with self.subTest(path=str(path)):
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("???", text)
                self.assertTrue(any("\u4e00" <= c <= "\u9fff" for c in text))

    def test_six_skill_files_exist(self):
        for name in SKILLS:
            with self.subTest(skill=name):
                self.assertTrue((ROOT / ".codex/skills" / name / "SKILL.md").is_file())

    def test_skill_frontmatter_and_size(self):
        for name in SKILLS:
            with self.subTest(skill=name):
                text = (ROOT / ".codex/skills" / name / "SKILL.md").read_text(encoding="utf-8")
                self.assertTrue(text.startswith("---\n"))
                data = yaml.safe_load(text.split("---\n", 2)[1])
                self.assertEqual(data["name"], name)
                self.assertEqual(set(data), {"name", "description"})
                self.assertLess(len(text.splitlines()), 500)
                self.assertIn("\u8f93\u5165", text)
                self.assertIn("\u8f93\u51fa", text)
                self.assertIn("novel-canon", text)

    def test_referenced_material_exists(self):
        for name in SKILLS:
            directory = ROOT / ".codex/skills" / name
            text = (directory / "SKILL.md").read_text(encoding="utf-8")
            refs = re.findall(r"references/[a-z-]+\.md", text)
            self.assertGreaterEqual(len(set(refs)), 2)
            for ref in refs:
                self.assertTrue((directory / ref).is_file(), f"{name}: {ref}")

    def test_ui_metadata(self):
        for name in SKILLS:
            with self.subTest(skill=name):
                data = yaml.safe_load((ROOT / ".codex/skills" / name / "agents/openai.yaml").read_text(encoding="utf-8"))
                self.assertIn("$" + name, data["interface"]["default_prompt"])
                self.assertGreaterEqual(len(data["interface"]["short_description"]), 25)
                self.assertLessEqual(len(data["interface"]["short_description"]), 64)

    def test_shared_record_protocol(self):
        text = (ROOT / ".novel/schemas/story-record.md").read_text(encoding="utf-8")
        for field in ("record_id", "record_type", "truth_status", "lifecycle", "source_ref", "valid_from", "depends_on", "supersedes"):
            self.assertIn(field, text)
        self.assertIn("proposal.status", text)
        for state in STATES:
            self.assertIn(state, text)

    def test_six_record_examples_have_distinct_status_and_lifecycle(self):
        data = yaml.safe_load((FIXTURES / "records.yaml").read_text(encoding="utf-8"))
        records = data["records"]
        self.assertEqual({x["record_type"] for x in records}, {"world", "character", "timeline", "event", "information", "foreshadow"})
        self.assertEqual(len(records), 6)
        for record in records:
            self.assertIn(record["truth_status"], STATES)
            self.assertNotIn(record["lifecycle"], STATES)
            self.assertTrue(record["source_ref"])
            self.assertIsInstance(record["depends_on"], list)

    def test_reader_packet_has_evidence_not_author_answer(self):
        records = yaml.safe_load((FIXTURES / "records.yaml").read_text(encoding="utf-8"))["records"]
        packet = yaml.safe_load((FIXTURES / "public-packet.yaml").read_text(encoding="utf-8"))
        self.assertEqual(packet["audience"], "draft_writer")
        self.assertIn("allowed_facts", packet)
        self.assertIn("forbidden_operations", packet)
        public_text = yaml.safe_dump(packet, allow_unicode=True)
        info = next(x for x in records if x["record_type"] == "information")
        self.assertNotIn(info["author_truth"], public_text)
        self.assertNotIn("author_truth", public_text)

    def test_six_raw_scenarios_are_separate_from_answers(self):
        cases = yaml.safe_load((FIXTURES / "scenarios.yaml").read_text(encoding="utf-8"))["scenarios"]
        self.assertEqual({x["skill"] for x in cases}, set(SKILLS))
        for case in cases:
            self.assertTrue(case["request"])
            self.assertTrue(case["raw_material"])
            self.assertNotIn("expected_answer", case)

if __name__ == "__main__":
    unittest.main()
