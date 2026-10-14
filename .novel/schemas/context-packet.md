# 上下文包

上下文包只装当前任务必要的信息，不代替完整作品档案。

```yaml
task_id: task-0001
task_type: draft | review | plan | revise | inspect
project_location:
  volume: 1
  chapter: 1
  scene: 1
included_context:
  - path: .novel/canon/characters/lin-du.md
    reason: "当前场景参与者"
excluded_context:
  - path: .novel/canon/events/unrelated.md
    reason: "与当前任务无直接依赖"
active_constraints:
  - "本场景不能揭示核心真相"
uncertainties:
  - "守门人的真实身份仍未确认"
source_window:
  - "chapter-01/scene-01"
```
