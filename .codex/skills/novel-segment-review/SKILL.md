---
name: novel-segment-review
description: Reverse-review a novel passage after drafting to extract explicit facts, character and world-state changes, information leaks, contradictions, narrative function, foreshadowing changes, and state-change proposals. Use after writing or importing prose before updating canon.
---

# Novel Segment Review

## Workflow

1. Read the prose, its context packet, relevant canon, and current scene plan.
2. Pass one: extract only facts explicitly written in the segment; separate inferences.
3. Pass two: compare facts against character states, timeline, information boundaries, world rules, and prior review reports.
4. Pass three: identify what the segment changes—event, relationship, knowledge, risk, resource, goal, or unresolved question. Flag scenes that change nothing.
5. Pass four: identify foreshadowing, repeated motifs, and possible style observations without rewriting the passage.
6. Produce `.novel/schemas/review-report.md` format.
7. Convert real state changes into risk-classified proposal candidates for `novel-canon`; do not directly update canon.

## Required distinctions

- Observed fact vs inference.
- Contradiction vs intentional mystery.
- Information leak vs permitted dramatic irony.
- Useful repetition vs unintentional repetition.
- Existing canon vs text that is only DRAFT.

## Escalate immediately when

- The passage reveals a high-risk secret or changes a core rule.
- A character knows information outside the current information map.
- The passage makes a CANON contradiction that cannot be resolved by viewpoint, timing, or deliberate deception.
- The prose introduces a fact that would invalidate multiple downstream records.

## Resource

- Review checklist: `references/review-checklist.md`

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
