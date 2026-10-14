# 审查、改写与影响协议 v1.0

作品根目录遵循 story-record.md；规划和作者/正文权限遵循 planning-contract.md。

## 审查字段

```yaml
audit_id: AUDIT-001
scope:
  source_ref: "原稿文件及版本"
  start: "审查开始位置"
  end: "审查结束位置"
coverage:
  read_sources: []
  not_read: []
  unresolved_sources: []
findings:
  - finding_id: FIND-001
    category: "continuity / causality / expression"
    evidence: []
    judgment: "confirmed / possible / unknown"
    severity: "hard_conflict / high_risk / style_concern / optional"
    protection_decision: "keep / clarify / revise"
    reason: "结合当前场景的解释"
```

scope 明确本段/本章/已读取跨章窗口。未看全文就不能写“全书无矛盾”。没有找到不等于不存在。
统计输出仅是候选，词典terms与汉字han_fragment必须区分；标点频繁不是自动错误，更不是AI来源鉴定。
有效重复、可疑重复、无效重复由上下文判读；主题/象征/口头禅/回环可以保护，且保护可以按出现位置重新评估，不全局盲保。

## 候选改写

```yaml
candidate_id: ALT-001
finding_ref: FIND-001
original_ref: "段落来源"
operation: "词组/句式/句群/段落"
meaning_constraints:
  - "必须保留的动作、知识、承诺、时间和叙述权限"
replacement: "候选文本"
new_facts: []
risk: low
protection_decision: revise
creator_decision: pending
```

meaning_constraints 应覆盖语义强度和模态：似乎/怀疑不变成肯定，暂时合作不变成信任，拒绝不变成承诺。
抽象情绪改成动作不保证语义等价；新增手部动作、物品和心理推论要标 new_facts，再决定风险。
不要为多样性滥用生僻词，不把朴素表达改成更长比喻。能删无功能重复时无需同义替代。
候选和作者批准分开；语境判断无法确定则 clarify，问一次关键问题。

## 风格修订

保留原稿，获准范围内另存DRAFT版本。记录应用/未应用的候选、变更位置、new_facts、保护项与统计对比。
回审新稿的实际事实，用 novel-segment-review。需要状态变化则按 status-change.md 交 novel-canon。
减少计数不是成功标准：同时检验角色声音、信息边界、节奏与原意。
含新承诺、线索或高风险真相的改写不能冒称纯语言润色。缺批准的实质变化保留候选，不能静默提交。

## 修订影响

downstream_impact：直接/间接受影响的角色状态、时间线、事件、伏笔、知识和章节计划。
每项标 evidence / dependency_path / certainty / required_action / source_ref。dependency_path 指明因何关联，不只列一堆文件。
先查显式depends_on和source_ref，再用已读内容补语义依赖；仅ID索引无法发现所有文学关联。
coverage.not_read 和缺失依赖须列；whole_novel_verified 默认 false，只有完成定义清晰的覆盖才谈已审查范围。
区别事实变更、来源移动和纯措辞更改，不因任何形容词替换就重写全书。
修订顺序：确认变更 → 更新源事实 → 同步受影响记录/草稿（获准范围内）→ 再回审 → 保存检查点。
不能自动批准/删除旧正史或废弃后续章。

## 输出归档

审查写 reviews/对应类别，候选写 proposals/，新稿写 drafts/新版本，历史保留。统计报告文件用新路径，严禁把重定向写到输入原稿；CLI本身只读取原文。
本协议描述助手执行步骤，不表示已部署后台自动审查器。
