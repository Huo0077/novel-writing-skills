# 文段回审报告

回审必须区分正文明确写出的事实、合理推断和未决问题。

```yaml
review_id: REVIEW-0001
source_ref: chapter-01/scene-01
severity: none | low | medium | high
facts_observed:
  - "正文明确发生的事实"
inferences:
  - "根据正文推断但未明说的内容"
state_changes:
  - entity: character:角色名
    before: "前状态"
    after: "后状态"
contradictions: []
information_leaks: []
narrative_function:
  changed: "本段改变了什么"
  missing: "如果没有有效改变，说明原因"
foreshadowing_changes: []
style_observations: []
proposal_candidates: []
creator_questions: []
```
