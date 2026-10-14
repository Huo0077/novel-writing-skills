"""Check explicitly supplied reader material and build a read-only test packet.

This tool never scans a project, infers hidden answers or calls a model.
A valid field shape is NOT proof that prose is free of spoilers.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

KEYS = {"packet_id", "scope", "passages", "reader_request"}
REQUESTS = {
    "open_reading": "请按首次阅读这些已见文段的方式回应：说出你注意的问题、可能解释、依据和不确定处；如果没有明显疑问也如实说。不要强迫找反转。",
    "hypothesis_comparison": "仅依据所给文段提出可能解释，比较支持与反对证据，保留无法判断的部分。没有必要给确定答案，也不要调用外部作品资料。",
}

def _nonempty(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(field + " must be a nonempty string")
    return value

def prepare_packet(data: dict) -> dict:
    if not isinstance(data, dict):
        raise ValueError("input must be an object")
    if set(data) != KEYS:
        extra = sorted(set(data) - KEYS)
        missing = sorted(KEYS - set(data))
        raise ValueError(f"unexpected fields={extra}; missing fields={missing}")
    packet_id = _nonempty(data["packet_id"], "packet_id")
    scope = _nonempty(data["scope"], "scope")
    request = data["reader_request"]
    if not isinstance(request, str) or request not in REQUESTS:
        raise ValueError("reader_request must be open_reading or hypothesis_comparison")
    raw_passages = data["passages"]
    if not isinstance(raw_passages, list) or not raw_passages:
        raise ValueError("passages must be a nonempty list")
    passages = []
    seen = set()
    for index, raw in enumerate(raw_passages):
        if not isinstance(raw, dict) or set(raw) != {"id", "text"}:
            raise ValueError(f"passages[{index}] only allows id and text")
        id_ = _nonempty(raw["id"], f"passages[{index}].id")
        text = _nonempty(raw["text"], f"passages[{index}].text")
        if id_ in seen:
            raise ValueError("duplicate passage id: " + id_)
        seen.add(id_)
        passages.append({"id": id_, "text": text})
    return {
        "schema_version": "1.0", "packet_id": packet_id, "scope": scope,
        "audience": "reader_test", "test_status": "prepared_not_run",
        "passages": passages, "reader_request": REQUESTS[request],
        "context_rule": "只读本材料；不读取作者笔记、项目档案、未来章节、回收解释、参考示例或带答案的历史会话。已知答案时必须报告非独立。",
        "limitations": ["not_semantic_secret_detection", "no_model_run_performed", "no_technical_context_isolation", "human_selection_required"],
    }

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.input.read_text(encoding="utf-8-sig"))
        print(json.dumps(prepare_packet(data), ensure_ascii=False, indent=2))
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 2

if __name__ == "__main__": sys.exit(main())
