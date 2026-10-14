"""Read-only expression statistics. Frequencies are clues, never rewrite decisions."""
from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import defaultdict
import json
from pathlib import Path
import re
import sys

DEFAULT_TERMS = ["微微一怔", "缓缓说道", "意味深长", "眼神复杂", "不由得", "这一刻"]
DEFAULTS = {"terms": DEFAULT_TERMS, "protected": [], "min_count": 2, "ngram_size": 4, "max_candidates": 30}
HAN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]+")
SYMBOLS = re.compile(r"…+|\.{3,}|—{2,}|[，。！？；：、]")
PATTERNS = [("不是…而是", re.compile(r"不是[^。！？!?\n]{0,60}?而是")),
            ("仿佛…一般", re.compile(r"仿佛[^。！？!?\n]{0,60}?一般"))]


def _config(config: dict | None) -> dict:
    if config is not None and not isinstance(config, dict):
        raise ValueError("config must be an object")
    config = {} if config is None else config
    unknown = set(config) - set(DEFAULTS)
    if unknown:
        raise ValueError("unknown config keys: " + ", ".join(sorted(unknown)))
    out = {**DEFAULTS, **config}
    for name, low, high in (("min_count", 2, 1000000), ("ngram_size", 2, 12), ("max_candidates", 1, 200)):
        value = out[name]
        if type(value) is not int or not low <= value <= high:
            raise ValueError(f"{name} must be an integer between {low} and {high}")
    if not isinstance(out["terms"], list) or any(not isinstance(x, str) or not x.strip() for x in out["terms"]):
        raise ValueError("terms must be a list of nonempty strings")
    out["terms"] = list(dict.fromkeys(out["terms"]))
    if not isinstance(out["protected"], list):
        raise ValueError("protected must be a list")
    for item in out["protected"]:
        if not isinstance(item, dict) or set(item) != {"value", "reason"} or any(not isinstance(item[k], str) or not item[k].strip() for k in ("value", "reason")):
            raise ValueError("protected entries require nonempty value and reason")
    return out


def _matches(text: str, value: str):
    start = 0
    while True:
        index = text.find(value, start)
        if index < 0:
            return
        yield index, index + len(value)
        start = index + 1


def analyze_text(text: str, config: dict | None = None) -> dict:
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    cfg = _config(config)
    newline_offsets = [index for index, char in enumerate(text) if char == "\n"]
    protection = [(a, b, item["reason"]) for item in cfg["protected"] for a, b in _matches(text, item["value"])]

    def occurrence(start: int, end: int) -> dict:
        line_index = bisect_right(newline_offsets, start)
        previous_newline = newline_offsets[line_index - 1] if line_index else -1
        return {"offset": start, "end_offset": end, "line": line_index + 1,
                "column": start - previous_newline, "surface": text[start:end],
                "protection_reasons": sorted({reason for a, b, reason in protection if a <= start and end <= b})}

    findings = []

    def add(kind: str, value: str, spans: list[tuple[int, int]]) -> None:
        if len(spans) < cfg["min_count"]:
            return
        occurrences = [occurrence(a, b) for a, b in spans]
        findings.append({"kind": kind, "value": value, "count": len(spans),
                         "protected_count": sum(bool(x["protection_reasons"]) for x in occurrences),
                         "occurrences": occurrences, "judgment": "needs_context_review"})

    for term in cfg["terms"]:
        add("term", term, list(_matches(text, term)))
    for label, pattern in PATTERNS:
        add("pattern", label, [(m.start(), m.end()) for m in pattern.finditer(text)])
    symbols = defaultdict(list)
    for match in SYMBOLS.finditer(text):
        raw = match.group()
        key = "ellipsis" if raw.startswith(("…", ".")) else "dash" if raw.startswith("—") else raw
        symbols[key].append((match.start(), match.end()))
    for value in sorted(symbols):
        add("punctuation", value, symbols[value])

    fragments = defaultdict(list)
    n = cfg["ngram_size"]
    for match in HAN.finditer(text):
        run = match.group()
        for index in range(len(run) - n + 1):
            start = match.start() + index
            fragments[run[index:index+n]].append((start, start+n))
    ranked = sorted(((value, spans) for value, spans in fragments.items() if len(spans) >= cfg["min_count"]), key=lambda x: (-len(x[1]), x[0]))
    for value, spans in ranked[:cfg["max_candidates"]]:
        add("han_fragment", value, spans)

    openings = defaultdict(list)
    sentence_lengths = []
    for match in re.finditer(r"[^。！？!?\n]+[。！？!?]?", text):
        raw = match.group()
        length = len(re.sub(r"\s", "", raw))
        if length:
            sentence_lengths.append(length)
        opening = re.match(r"[\s\"'“‘（(]*([\u3400-\u4dbf\u4e00-\u9fff]{3})", raw)
        if opening:
            start = match.start() + opening.start(1)
            openings[opening.group(1)].append((start, start+3))
    for value in sorted(openings):
        add("sentence_opening", value, openings[value])
    return {
        "schema_version": "1.0", "source_scope": "supplied_text_only",
        "metrics": {"characters": len(text), "han_characters": sum(len(m.group()) for m in HAN.finditer(text)),
                    "rough_sentence_count": len(sentence_lengths), "rough_sentence_lengths": sentence_lengths},
        "settings": cfg, "findings": findings,
        "limitations": ["not_word_segmentation", "not_ai_detection", "not_semantic_audit",
                        "protection_is_annotation_not_permission", "overlapping_matches_counted", "no_automatic_rewrite"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--config", type=Path)
    args = parser.parse_args(argv)
    try:
        text = args.input.read_text(encoding="utf-8-sig")
        config = json.loads(args.config.read_text(encoding="utf-8-sig")) if args.config else None
        report = analyze_text(text, config)
        report["source_ref"] = str(args.input.resolve())
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
