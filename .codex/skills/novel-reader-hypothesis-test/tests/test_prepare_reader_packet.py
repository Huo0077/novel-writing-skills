"""Deterministic field checks, not semantic secrecy or model performance tests."""
import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
SCRIPT = Path(__file__).resolve().parents[1] / "scripts/prepare_reader_packet.py"
spec = importlib.util.spec_from_file_location("reader_packet", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
def valid():
    return {"packet_id": "READER-001", "scope": "章节一至三的已见片段", "passages": [{"id": "P1", "text": "门口的队伍很长。"}], "reader_request": "open_reading"}
class PacketTests(unittest.TestCase):
    def test_valid_packet_has_reader_audience(self):
        result = mod.prepare_packet(valid())
        self.assertEqual(result["audience"], "reader_test")
        self.assertEqual(result["passages"], valid()["passages"])
    def test_top_level_answer_field_rejected(self):
        data = valid(); data["author_truth"] = "答案"
        with self.assertRaises(ValueError): mod.prepare_packet(data)
    def test_nested_metadata_rejected(self):
        data = valid(); data["passages"][0]["clue_explanation"] = "真相"
        with self.assertRaises(ValueError): mod.prepare_packet(data)
    def test_missing_required_field(self):
        data = valid(); del data["scope"]
        with self.assertRaises(ValueError): mod.prepare_packet(data)
    def test_empty_passages_rejected(self):
        data = valid(); data["passages"] = []
        with self.assertRaises(ValueError): mod.prepare_packet(data)
    def test_empty_text_rejected(self):
        data = valid(); data["passages"][0]["text"] = " "
        with self.assertRaises(ValueError): mod.prepare_packet(data)
    def test_wrong_types_rejected(self):
        for data in (None, [], {**valid(), "scope": 2}, {**valid(), "passages": "text"}):
            with self.subTest(data=data), self.assertRaises(ValueError): mod.prepare_packet(data)
    def test_duplicate_passage_ids_rejected(self):
        data = valid(); data["passages"].append({"id": "P1", "text": "第二段。"})
        with self.assertRaises(ValueError): mod.prepare_packet(data)
    def test_unknown_reading_request_rejected(self):
        data = valid(); data["reader_request"] = "guess_the_secret_king"
        with self.assertRaises(ValueError): mod.prepare_packet(data)
    def test_prepared_packet_is_not_test_result_and_input_is_unchanged(self):
        data = valid(); before = copy.deepcopy(data); out = mod.prepare_packet(data)
        self.assertEqual(data, before)
        self.assertEqual(out["test_status"], "prepared_not_run")
        self.assertNotIn("reader_hypotheses", out)
        self.assertIn("not_semantic_secret_detection", out["limitations"])
    def test_cli_json_and_source_unchanged(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"input.json";p.write_text(json.dumps(valid(), ensure_ascii=False), encoding="utf-8")
            before = p.read_bytes();output = io.StringIO()
            with contextlib.redirect_stdout(output): status = mod.main([str(p)])
            self.assertEqual(status, 0)
            self.assertEqual(json.loads(output.getvalue())["test_status"], "prepared_not_run")
            self.assertEqual(p.read_bytes(), before)
    def test_cli_invalid_input_returns_two(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"bad.json";p.write_text("{bad", encoding="utf-8")
            with contextlib.redirect_stderr(io.StringIO()) as err: status = mod.main([str(p)])
            self.assertEqual(status, 2);self.assertIn("ERROR", err.getvalue())
if __name__ == "__main__": unittest.main()
