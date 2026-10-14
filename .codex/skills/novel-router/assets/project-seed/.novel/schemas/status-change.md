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
