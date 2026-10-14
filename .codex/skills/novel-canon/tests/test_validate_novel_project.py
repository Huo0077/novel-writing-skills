import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SCRIPT = ROOT / ".codex" / "skills" / "novel-canon" / "scripts" / "validate_novel_project.py"
spec = importlib.util.spec_from_file_location("validate_novel_project", SCRIPT)
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class ValidateNovelProjectTests(unittest.TestCase):
    def test_valid_fixture_has_no_errors(self):
        fixture = ROOT / ".novel" / "tests" / "fixtures" / "valid-project"
        self.assertEqual(validator.validate_project(fixture), [])
        self.assertEqual(validator.main([str(fixture)]), 0)

    def test_invalid_fixture_reports_state_risk_and_required_field_errors(self):
        fixture = ROOT / ".novel" / "tests" / "fixtures" / "invalid-project"
        errors = validator.validate_project(fixture)
        joined = "\n".join(errors)
        self.assertIn("unknown state", joined)
        self.assertIn("unknown risk", joined)
        self.assertIn("source_ref", joined)
        self.assertEqual(validator.main([str(fixture)]), 1)

    def test_high_risk_change_requires_confirmation(self):
        data = {
            "change_id": "SC-9",
            "status": "proposed",
            "risk": "high",
            "source_ref": "chapter-1",
            "change_type": "reveal",
            "summary": "Reveal the secret",
            "affected_entities": ["character:Lin"],
            "requires_confirmation": False,
            "creator_decision": "pending",
        }
        errors = validator.validate_status_change(data, Path("proposal.yaml"))
        self.assertTrue(any("requires_confirmation" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
