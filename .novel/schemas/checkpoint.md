# 创作检查点

检查点必须足以让另一次会话从当前状态安全恢复。

```yaml
checkpoint_id: CP-0001
created_from: chapter-01/scene-01
mode: author_assistant
confirmed_canon:
  - "当前已确认的关键事实"
tentative_changes:
  - "尚未确认的低风险事实"
pending_proposals:
  - "等待创作者决定的中风险或高风险提案"
current_progress:
  location: "卷/章/场景"
  completed: []
  next_safe_action: "下一步低风险动作"
  must_not_reveal: []
  unresolved_questions: []
recovery_context:
  include: []
  exclude: []
```
