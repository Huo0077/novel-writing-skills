"""Artifact contract tests. No model calls; no claim of literary quality."""
import re
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / ".novel/tests/fixtures/planning-drafting"
SKILLS = ("novel-outline", "novel-chapter-plan", "novel-scene-plan", "novel-draft", "novel-character-voice")

def load(name):
    return yaml.safe_load((FIX / name).read_text(encoding="utf-8"))

class PlanningDraftingContracts(unittest.TestCase):
    def test_five_skill_procedures_exist(self):
        for name in SKILLS:
            with self.subTest(skill=name):
                text = (ROOT / ".codex/skills" / name / "SKILL.md").read_text(encoding="utf-8")
                self.assertTrue(text.startswith("---\n"))
                meta = yaml.safe_load(text.split("---\n", 2)[1])
                self.assertEqual(meta["name"], name)
                self.assertEqual(set(meta), {"name", "description"})
                self.assertLess(len(text.splitlines()), 500)
                self.assertIn("输入", text)
                self.assertIn("输出", text)
                self.assertIn("novel-canon", text)
                self.assertNotIn("???", text)

    def test_each_skill_has_valid_metadata_and_references(self):
        for name in SKILLS:
            folder = ROOT / ".codex/skills" / name
            text = (folder / "SKILL.md").read_text(encoding="utf-8")
            refs = set(re.findall(r"references/[a-z-]+\.md", text))
            self.assertGreaterEqual(len(refs), 2)
            for ref in refs:
                self.assertTrue((folder / ref).is_file())
            ui = yaml.safe_load((folder / "agents/openai.yaml").read_text(encoding="utf-8"))["interface"]
            self.assertIn("$" + name, ui["default_prompt"])
            self.assertTrue(25 <= len(ui["short_description"]) <= 64)

    def test_planning_protocol_and_four_templates(self):
        text = (ROOT / ".novel/schemas/planning-contract.md").read_text(encoding="utf-8")
        for field in ("plan_id", "plan_type", "plan_status", "source_ref", "revision", "approval_ref", "based_on", "entry_state", "target_delta", "reveal_budget", "exit_condition", "handoff", "observed_delta"):
            self.assertIn(field, text)
        for name in ("outline-plan", "chapter-plan", "scene-plan", "voice-profile"):
            self.assertTrue((ROOT / ".novel/templates" / (name + ".md")).is_file())

    def test_plan_approval_is_not_event_occurrence(self):
        for name in ("outline", "chapter", "scene"):
            data = load(name + ".yaml")
            self.assertEqual(data["plan_status"], "approved")
            self.assertTrue(data["approval_ref"])
            self.assertTrue(data["source_ref"])
            self.assertNotIn("observed_delta", data)
            self.assertNotIn("CANON", data["plan_status"])

    def test_outline_chapter_scene_dependencies(self):
        outline, chapter, scene = (load(n + ".yaml") for n in ("outline", "chapter", "scene"))
        self.assertIn(outline["plan_id"], chapter["based_on"])
        self.assertIn(chapter["plan_id"], scene["based_on"])
        self.assertIn(scene["plan_id"], chapter["scene_ids"])
        self.assertTrue(scene["exit_condition"])

    def test_writer_packet_excludes_author_secret_and_future_answers(self):
        secret = load("outline.yaml")["author_notes"]["I-001"]
        packet = load("public-packet.yaml")
        self.assertEqual(packet["audience"], "draft_writer")
        rendered = yaml.safe_dump(packet, allow_unicode=True)
        self.assertNotIn(secret, rendered)
        self.assertNotIn("author_notes", rendered)
        self.assertNotIn("author_truth", rendered)
        self.assertIn("do_not_reveal:I-001", packet["forbidden_operations"])

    def test_sample_draft_keeps_injury_and_no_secret_assertion(self):
        text = (FIX / "draft.md").read_text(encoding="utf-8")
        self.assertIn("左手", text)
        self.assertNotIn(load("outline.yaml")["author_notes"]["I-001"], text)
        self.assertNotIn("挥起右手", text)

    def test_sample_review_preserves_target_vs_observed_difference(self):
        scene, review = load("scene.yaml"), load("review.yaml")
        self.assertIn("target_delta", scene)
        self.assertIn("observed_delta", review)
        self.assertNotIn("observed_delta", scene)
        self.assertTrue(review["facts_observed"])
        self.assertTrue(review["inferences"])
        self.assertEqual(review["source_ref"], "fixture:draft.md")

    def test_relation_is_not_automatically_reconciled(self):
        review = load("review.yaml")
        self.assertEqual(review["relation_observation"], "cooperation_without_reconciliation")
        self.assertTrue(load("scene.yaml")["entry_state"]["distrust_active"])

    def test_actual_changes_need_confirmation(self):
        changes = load("changes.yaml")["changes"]
        self.assertEqual({x["risk"] for x in changes}, {"low", "medium"})
        for change in changes:
            self.assertEqual(change["status"], "proposed")
            self.assertEqual(change["creator_decision"], "pending")
            self.assertTrue(change["source_ref"])
            self.assertIsInstance(change["affected_entities"], list)
            if change["risk"] == "medium":
                self.assertTrue(change["requires_confirmation"])

    def test_checkpoint_does_not_commit_unapproved_scene_result(self):
        changes = load("changes.yaml")["changes"]
        checkpoint = load("checkpoint.yaml")
        expected = {x["change_id"] for x in changes if x["risk"] == "medium"}
        self.assertEqual(set(checkpoint["pending_proposals"]), expected)
        self.assertEqual(checkpoint["next_action_status"], "creator_pending")
        self.assertNotIn("new_directions_obtained", checkpoint["confirmed_canon"])

    def test_high_risk_request_is_a_pause_not_draft_output(self):
        pause = load("pause-request.yaml")
        self.assertEqual(pause["risk"], "high")
        self.assertEqual(pause["handoff_status"], "paused")
        self.assertTrue(pause["requires_confirmation"])
        self.assertIsNone(pause["draft_ref"])
        self.assertTrue(pause["creator_question"])

    def test_voice_profiles_are_distinct_but_allow_unknown(self):
        voices = load("voice-profiles.yaml")["profiles"]
        self.assertEqual(len(voices), 2)
        self.assertNotEqual(voices[0]["attention"], voices[1]["attention"])
        self.assertNotEqual(voices[0]["speech_strategy"], voices[1]["speech_strategy"])
        for voice in voices:
            self.assertEqual(voice["catchphrase"], "unknown")
            self.assertTrue(voice["knowledge_refs"])
            self.assertIn("under_pressure", voice)

if __name__ == "__main__":
    unittest.main()
