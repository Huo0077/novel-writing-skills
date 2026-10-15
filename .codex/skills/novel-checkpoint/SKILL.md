---
name: novel-checkpoint
description: Save and restore a resumable checkpoint for a novel project after a task, scene, chapter, or writing phase. Use when finishing a writing session, switching tasks, pausing automation, or recovering from a previous session without losing story state or pending decisions.
---

# Novel Checkpoint

## Workflow

1. Read the current project state, latest review report, accepted decisions, tentative changes, and pending proposals.
2. Record the exact story location and the selected collaboration mode.
3. Summarize confirmed canon separately from tentative changes and unresolved proposals.
4. Record completed work, the next safe action, unresolved questions, and information that must not be revealed next.
5. List the context files needed for recovery and the files intentionally excluded.
6. Save a new checkpoint under `.novel/checkpoints/` using `.novel/schemas/checkpoint.md`.
7. On resume, load the newest checkpoint first, then verify that its referenced files still exist and that no newer high-risk proposal is pending.

## Safety

A checkpoint is a snapshot, not a license to approve proposals. Do not fold tentative or proposed content into confirmed canon while saving it.

## Cadence

- Author assistant: after each task or explicit pause.
- Co-author: after each scene and before major-choice confirmation.
- Semi-automatic: after each chapter and whenever a high-risk item pauses progress.

## Resource

- Checkpoint schema: `.novel/schemas/checkpoint.md`
- Recovery rules: `references/checkpoint-rules.md`

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
