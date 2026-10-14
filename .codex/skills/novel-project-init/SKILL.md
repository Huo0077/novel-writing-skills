---
name: novel-project-init
description: Initialize or resume a novel project with a durable .novel story-state structure. Use when starting a new novel, importing an existing draft, resuming an incomplete project, or progressively collecting the creator's world, character, plot, and collaboration preferences.
---

# Novel Project Initialization

## Purpose

建立或恢复一个可长期维护的小说项目。不要一次要求创作者填写整套设定；按阶段提问，把已确认内容写入 `.novel/`，把未知内容明确标记为未确定。

## Workflow

1. 检查项目根目录是否已有 `.novel/project.yaml`。
2. 没有时，先使用 novel-router/scripts/suite.py bootstrap <作品目录> 预览；确认后加 --apply 复制共享空白种子、技能和隔离QA，仅新增缺失文件。已有同路径档案原样保留，再校验兼容性。已有项目时，只读取检查点与待确认提案。
3. 按 `references/question-flow.md` 逐阶段提问；阶段是路线图，一次仅问其中一个当前关键问题，提供2–3个方向及自定义/暂缓。
4. 将创作者明确确认的内容写入 `CANON`；将未决定的 AI 建议写入 `PROPOSAL`，不得假装成正史。
5. 每轮完成后报告：已确认内容、尚未确定内容、下一组问题和可以安全进行的下一步。
6. 初始化完成后，创建第一个检查点，记录当前模式、当前进度和未决问题。

## Rules

- 不用 AI 默认补全创作者没有确认的核心事实。
- 不为了填满档案而制造世界观、人物秘密或伏笔。
- 如果用户提供现有正文，先把正文视为 `DRAFT`，通过 `novel-segment-review` 回审后再提出状态变更。
- 若发现已有正史与新输入冲突，暂停写入并交给 `novel-canon` 处理。

## Resources

- 提问顺序：`references/question-flow.md`
- 状态协议：`.novel/schemas/status-change.md`
- 检查点协议：`.novel/schemas/checkpoint.md`

## 可迁移资源
共享协议与模板来自项目内 `.codex/skills/novel-router/assets/project-seed/.novel/`，默认配置不是作者已确认设定。缺少种子时停下说明，不假装完成初始化。

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。
