---
name: novel-chapter-plan
description: Plan a novel chapter from approved outline scope and current state. Use when deciding chapter function, scene sequence, tension and aftermath, reveal budget or chapter stopping conditions without recycling the same cliffhanger or treating target changes as actual events.
---

# 章节功能与场景序列

## 输入
当前阶段总纲、章节范围、前章检查点、人物/事件有效状态、读者当前疑问和信息权限。读取 .novel/schemas/planning-contract.md；作者资料与正文包分开。

## 执行
1. 确认本章要解决/推进哪一问题，和明确不做什么；没有作者范围则请求一次澄清。
2. 写 entry_state 与 target_delta：目标是预期，不代表已经发生；引用上级计划 ID 和版本。
3. 列少量必要场景，每场至少有事件、情绪、关系或认知作用；删除后无损时评估合并，但不机械删留白。
4. 为场景写依赖和先后，检查人物进出、时段、伤势和上场未兑现后果。
5. 安排张弛、情绪积累和余波；避免连续“意外—升级—反转—神秘结尾”模板。结尾可用决定、局部结果或未解问题。
6. 指定本章 reveal_budget：可观察异常、可形成猜测、能验证的局部事实，以及不能揭示的 I-ID/操作。
7. 设 exit_condition 和下一步安全任务；达到就收束，不顺手公布核心真相。
8. 用 proposal/approved 状态保存 planning/chapters/<id>.md，真实批准有 approval_ref；重大事件变更交 novel-canon。
9. 交 novel-scene-plan 当前一场；依赖未确认事实时标候选分支，不冒充稳定前提。

## 输出
章功能卡、场景序列/依赖、张弛与余波、信息增量、target_delta、结束条件、风险/问题和场景交接。

## 权限
不为了填字数增加无用场景；不强制章节长度和高潮比例。通用剧本模板只是可选工具，不凌驾作者作品方向。

## 资料
- 章字段与去重检查：references/workflow-details.md
- 小目标示例：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。
