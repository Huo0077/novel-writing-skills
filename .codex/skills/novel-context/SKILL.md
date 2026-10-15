---
name: novel-context
description: Assemble a minimal, task-specific context packet from a novel project's canon, plans, drafts, reviews, and checkpoints. Use before drafting, planning, reviewing, revising, or resuming work so the AI reads relevant state without loading the entire novel indiscriminately.
---

# Novel Context Assembly

## Workflow

1. Identify the audience before retrieving any project record: author analysis, draft writer, or reader hypothesis test. Identify task scope and source window. For a reader test, skip author records and answer-bearing checkpoints; follow the restricted Information permissions path below.
2. If the audience is reader hypothesis test, assemble only the explicitly provided reader material and return now. Do not run steps 3–7 or load project configuration/checkpoints. Otherwise read `.novel/project.yaml`, the latest checkpoint, and the current mode.
3. Retrieve only records that constrain the task: active participants, current location/time, immediate prior state, relevant rules, information boundaries, unresolved proposals, and nearby draft/review sources.
4. Add the current chapter or scene plan when one exists.
5. Explicitly list excluded files and why they are not needed. Do not hide uncertainty by omission.
6. Produce `.novel/schemas/context-packet.md` format with active constraints, uncertainties, and source window.
7. If a required fact is missing or contradictory, stop assembly at that point and ask a focused clarification question instead of inventing it.

## Information permissions

Before retrieving hidden records, identify the audience: author analysis, draft writer, or reader hypothesis test.
For a draft writer, request an authorized public packet from novel-information; use only current visible facts, allowed clues, and reveal restrictions. Keep author truth in separate author notes, not in the writer packet or its prohibition text.
For a reader hypothesis test, load only the provided pre-reveal prose and public packet. Do not read canon secrets, future outlines, payoff examples, or answer-bearing checkpoints. If this session has already seen the answer, label the result manual review, not an independent blind test.
If the required public packet is missing, ask for the missing permission/evidence or prepare it in author-analysis mode. Do not claim clean-room isolation in a session that has already read the author material.
Source paths and forbidden operations may refer to secret IDs, but must not state their hidden values.

## Planning handoff

For author planning, use the current approved scope and mark future targets as plans, not occurred events. For drafting, include only the authorized current scene slice, public packet, permitted voice profile and immediate prior prose; never attach an answer-bearing whole outline as convenience context.
Read `.novel/schemas/planning-contract.md` when handing off outline, chapter or scene planning to drafting. Missing scene scope, approval or public packet is a blocked prerequisite, not an invitation to invent it.
Keep target_delta separate from observed_delta until novel-segment-review reads the actual generated prose.

## Retrieval priorities

1. Current task and current checkpoint.
2. Directly participating characters, locations, events, and rules.
3. Information boundary and unrevealed secrets relevant to the task.
4. Immediate preceding prose and its review report.
5. Nearby plans and unresolved proposals.
6. Broader history only when a direct dependency is identified.

## Exclusions

Do not load unrelated chapters, archived drafts, rejected ideas, or distant lore merely because they exist. If a seemingly relevant record is excluded, explain the exclusion in the packet.

## Resource

- Detailed retrieval rules: `references/retrieval-rules.md`

## 缺信息与用户选项
作者协作路线遵守 `.novel/schemas/clarification-contract.md`：先查已有资料，一次问一个当前关键问题，给2–3个有差异的方向及影响，允许自定义或暂不决定，不替用户默认选。答复只确认明确范围，缺答案时暂停依赖步骤。
reader独立阅读路线不读作者协议或候选答案；只中性询问阅读材料/范围缺口，不给作者真相选项、不恢复含秘密的档案。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
