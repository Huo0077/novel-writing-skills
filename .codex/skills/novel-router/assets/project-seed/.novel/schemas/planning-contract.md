# 规划与正文交接协议 v1.0

作品根目录按 story-record.md 定位。规划资料与真实故事状态分开；领域真值标签保持原义。

## 计划共用字段
```yaml
plan_id: SCENE-001
plan_type: scene
plan_status: proposal
source_ref:
  - "任务或已确认上级计划来源"
revision: 1
approval_ref: null
based_on: []
entry_state: {}
target_delta: []
reveal_budget:
  allowed: []
  forbidden_operations: []
exit_condition: "场景完成的可观察条件"
handoff:
  status: blocked
  next_skill: novel-scene-plan
  artifact_refs: []
```

- plan_type：outline / chapter / scene。plan_status：proposal / approved / superseded。
- approved 要有具体 approval_ref（创作者决定或批准范围），不自行填“用户已批准”。总体技能开发授权不等于批准某本小说的情节。
- based_on：上级计划与相关状态记录，保留版本；旧计划失效时关联下级标为待检查，不静默覆盖。
- entry_state：当前故事时点已证实状态；暂定事实/未决提案标注来源和状态，不冒充 CANON。
- target_delta：预期改变，不是实际发生。
- observed_delta：只来自实际正文回审；不得因已批准 target_delta 就宣布 achieved。
- reveal_budget：这个单位允许透露的事实/局部推测、明确禁止的操作。禁止用答案内容写“不要揭示……”来污染公开包。
- exit_condition：本单元何时结束，避免继续生成顺手回收伏笔。
- handoff.status：ready / blocked / paused / review_pending / creator_pending / complete。

## 总纲与章计划
作者版可包含 author_notes 和隐藏真相，必须清楚标记；不整份发送给正文生成。
总纲约束阶段问题、承诺/回收窗口、冲突层级和弧光目标，可采用探索型短滚动纲，结局 unknown 不强补。
章节与场景应引用上级计划，注明揭示增量、情绪变化、余波/停顿和不做的事；不硬性要求每章反转或每场冲突升级。

## 正文公开任务
- 输入为批准的当前范围、public_packet、入口状态、已授权声音特征、临近正文（不泄密版）。
- 输出 DRAFT 正文与独立写作记录；正文不混入“本段推进了伏笔”等解释。
- 默认一场，或使用创作者明确批准的有限批量；半自动模式不是无限连写。
- 缺视角、关键动作资格、当前目标或已确认入口状态时 blocked，问一个当前阻塞问题。
- 高风险变化先 paused，确认问题及影响记录在作者分析材料，不在正文泄露。已有同一时点/动作的具体批准可引用，但总纲的一般安排不自动授权现在揭示。
- 信息包隔离是行为约束，不是技术安全边界。同一会话知道答案时仍需遵守权限，不称盲测。

## 回审与状态提交
1. 使用 novel-segment-review 按实际正文提取 facts_observed / inferences / state_changes。
2. 比较 target_delta 与 observed_delta，未实现就标未实现，不能为匹配计划修改报告。
3. 将实际变化按 status-change.md 送 novel-canon，保留 source_ref、before/after、风险与下游影响。
4. 低风险可 TENTATIVE；中风险阶段汇总；高风险立即暂停。未确认中风险可以在同一批准批量内作为显式候选分支推进，不能成为已确认前提，也不能越过高风险门槛。
5. 保存 novel-checkpoint，列明仍待确认内容、禁止揭示项和下一步状态。
6. 交接是当前助手执行协议，不是假定工具已自动执行；缺文件/执行证据就不能标 complete。

## 修订与声音
同一计划修订递增 revision、记录 supersedes/影响清单；不覆盖历史草稿。声音候选中的新人物特征要分级确认。
对白语言改写不得暗改人物获知、承诺、关键动作或关系；如改变，转事实修订而非风格优化。
