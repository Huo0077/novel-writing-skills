---
name: novel-plot
description: Maintain novel plot threads, causal events and next-step progress. Use when designing a key event, checking motivation-action-consequence chains, identifying consequence-free conflicts, or revising a plot node while tracing downstream dependencies.
---

# 情节因果与进度

## 输入
主支线目标、当前人物状态、相关事件、章节任务和未决问题。读取 references/record-format.md，分清已确认计划和发生事实。

## 执行
1. 确定本阶段要推进的问题，不重建整部大纲。
2. 展开“触发 → 目标 → 阻力 → 可选行动 → 选择 → 即时代价 → 结果 → 延迟后果”。
3. 检查选择是否由当前认知与需求支持；避免仅靠巧合或作者强推。
4. 标记关键 E-ID，关联前置记录、人物/关系/谜团线与下游节点。
5. 检查删掉事件影响哪些后文；没有情节变化时仍检查独立情绪/主题功能，不能一律删除安静场景。
6. 维护 stage_goal、completed、pending、blocked_by、next_safe_action、cannot_reveal。
7. 给少量差异明确的候选，说明代价和伏笔影响；作者已确定方向时不强迫三个备选。
8. 改关键结果或主线方向立即交 novel-canon 高风险确认；未来计划不能写成人物过去。

## 输出
事件因果卡、主支线依赖、关键事件标记、缺后果/断裂清单、候选代价、下一步进度卡和状态变更候选。

## 权限
不要求每章必反转、每场必打斗，不为戏剧性硬造伤亡。配角有自身目标，不只是发任务工具。
全书结构规划交 novel-outline，本 skill 维护事件因果与当前进度；不能因已批准大纲就把未来计划当过去事实。

## 资料
- 记录格式：references/record-format.md
- 示例：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。
