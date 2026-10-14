"""Real deterministic analyzer tests; not model or literary-quality tests."""
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/analyze_expression.py"
spec = importlib.util.spec_from_file_location("expression_analyzer", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def find(report, kind, value):
    return next(x for x in report["findings"] if x["kind"] == kind and x["value"] == value)

class ExpressionTests(unittest.TestCase):
    def test_empty_text_has_no_findings(self):
        report = mod.analyze_text("")
        self.assertEqual(report["findings"], [])
        self.assertEqual(report["metrics"]["characters"], 0)

    def test_explicit_term_count(self):
        item = find(mod.analyze_text("他微微一怔。她微微一怔。", {"terms": ["微微一怔"]}), "term", "微微一怔")
        self.assertEqual(item["count"], 2)

    def test_overlapping_occurrences(self):
        item = find(mod.analyze_text("哈哈哈", {"terms": ["哈哈"]}), "term", "哈哈")
        self.assertEqual([x["offset"] for x in item["occurrences"]], [0, 1])

    def test_one_based_line_column_and_zero_based_offset(self):
        report = mod.analyze_text("前\n微微一怔\n微微一怔", {"terms": ["微微一怔"]})
        item = find(report, "term", "微微一怔")
        self.assertEqual((item["occurrences"][0]["offset"], item["occurrences"][0]["line"], item["occurrences"][0]["column"]), (2, 2, 1))
        self.assertEqual(item["occurrences"][1]["line"], 3)

    def test_ellipsis_runs_are_tokens(self):
        item = find(mod.analyze_text("等等……再等..."), "punctuation", "ellipsis")
        self.assertEqual(item["count"], 2)
        self.assertEqual([x["surface"] for x in item["occurrences"]], ["……", "..."])

    def test_dash_runs_are_tokens(self):
        self.assertEqual(find(mod.analyze_text("她——我——"), "punctuation", "dash")["count"], 2)

    def test_pattern_count_does_not_cross_sentence(self):
        report = mod.analyze_text("不是怕而是等。不是恨而是疼。不是。下一句而是。")
        self.assertEqual(find(report, "pattern", "不是…而是")["count"], 2)

    def test_repeated_sentence_openings(self):
        item = find(mod.analyze_text("他看着门。他看着窗。"), "sentence_opening", "他看着")
        self.assertEqual(item["count"], 2)

    def test_ngram_is_labeled_fragment_not_word(self):
        item = find(mod.analyze_text("打开窗户。打开窗户。", {"terms": [], "ngram_size": 4}), "han_fragment", "打开窗户")
        self.assertEqual(item["count"], 2)
        self.assertIn("not_word_segmentation", mod.analyze_text("")["limitations"])

    def test_protected_occurrences_are_not_suppressed(self):
        cfg = {"terms": ["银戒指"], "protected": [{"value": "银戒指", "reason": "主题回环"}]}
        item = find(mod.analyze_text("银戒指，银戒指。", cfg), "term", "银戒指")
        self.assertEqual(item["count"], 2)
        self.assertEqual(item["protected_count"], 2)
        self.assertEqual(item["occurrences"][0]["protection_reasons"], ["主题回环"])

    def test_partial_protection_is_per_occurrence(self):
        cfg = {"terms": ["戒指"], "protected": [{"value": "银戒指", "reason": "象征"}]}
        item = find(mod.analyze_text("银戒指，铜戒指。", cfg), "term", "戒指")
        self.assertEqual(item["protected_count"], 1)
        self.assertEqual(item["occurrences"][1]["protection_reasons"], [])

    def test_duplicate_terms_are_deduplicated(self):
        report = mod.analyze_text("等待等待", {"terms": ["等待", "等待"]})
        self.assertEqual(len([x for x in report["findings"] if x["kind"] == "term"]), 1)

    def test_invalid_settings_are_rejected(self):
        for cfg in ({"min_count": 1}, {"ngram_size": 1}, {"max_candidates": 0}, {"typo": 2}, {"terms": "词"}, {"protected": [{"value": "", "reason": "x"}]}, {"min_count": True}):
            with self.subTest(cfg=cfg), self.assertRaises(ValueError):
                mod.analyze_text("文本", cfg)

    def test_threshold_and_candidate_limit(self):
        report = mod.analyze_text("甲乙丙甲乙丙甲乙丙", {"terms": [], "ngram_size": 2, "max_candidates": 1, "min_count": 3})
        fragments = [x for x in report["findings"] if x["kind"] == "han_fragment"]
        self.assertEqual(len(fragments), 1)
        self.assertGreaterEqual(fragments[0]["count"], 3)

    def test_cli_json_and_input_unchanged(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "input.txt"
            p.write_text("微微一怔。微微一怔。", encoding="utf-8")
            before = p.read_bytes()
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                status = mod.main([str(p)])
            self.assertEqual(status, 0)
            self.assertIn("findings", json.loads(output.getvalue()))
            self.assertEqual(p.read_bytes(), before)

    def test_cli_missing_input_returns_two(self):
        output = io.StringIO()
        with contextlib.redirect_stderr(output):
            status = mod.main(["nonexistent-for-test.txt"])
        self.assertEqual(status, 2)
        self.assertIn("ERROR", output.getvalue())

if __name__ == "__main__":
    unittest.main()
