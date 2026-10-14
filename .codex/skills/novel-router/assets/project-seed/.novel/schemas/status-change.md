# 状态变更提案

使用 YAML 表示变更，用 Markdown 解释影响。任何涉及 CANON 的更新都必须保留来源和创作者决定。

```yaml
change_id: SC-0001
status: proposed
risk: low
source_ref: chapter-01/scene-01
change_type: add_fact
summary: "简短描述"
before: "修改前状态；新增事实可写 null"
after: "修改后状态"
affected_entities:
  - character:角色名
downstream_impact:
  - "对后续剧情的约束"
requires_confirmation: false
creator_decision: pending
```

风险规则：

- `low`：可以写入 `TENTATIVE`，不打断当前任务。
- `medium`：写入 `PROPOSAL`，在任务或阶段结束时批量确认。
- `high`：写入 `PROPOSAL`，立即暂停并请求确认；`requires_confirmation` 必须为 `true`。

状态标签：`CANON`、`TENTATIVE`、`PROPOSAL`、`DRAFT`、`REJECTED`、`ARCHIVED`。

## v1.1 严格校验
必填字段必须有合法类型和实际值，不以键存在代替信息完整。change_id/summary/source_ref为非空字符串；affected_entities为非空、不重复的字符串列表；requires_confirmation必须是布尔值，medium与high均为true。
change_type仅add_fact/update_state/relation_change/reveal/rule_change/retcon。
审议对：proposed→pending，accepted→accepted，modified→modified，rejected→rejected。modified原案保留修订决定，新候选另建proposed/pending条目，不直接提交未经许可的修改。
来源缺失或状态冲突先按clarification-contract向用户核实，不能替用户补虚假的确认。结构一致也不证明实际决定有效，仍需助手查来源与授权范围。
