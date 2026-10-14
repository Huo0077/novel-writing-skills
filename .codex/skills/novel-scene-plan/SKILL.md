---
name: novel-scene-plan
description: Create a bounded scene plan with current state, viewpoint, goals, obstacles, choices, costs, reveal limits and an authorized writer packet. Use before drafting a scene, checking whether a scene changes anything, or preparing safe stopping conditions for a novel-writing task.
---

# 场景计划与写作任务

## 输入
批准范围内章计划、当前人物/时空状态、场景目标、视角、信息权限与可用角色声音。读取 .novel/schemas/planning-contract.md。

## 执行
1. 检查当前场景资格：上级范围、入口状态、视角、重要行动前提是否明确。缺一个关键条件时 blocked，问一个问题，不猜完全部。
2. 写 goal、obstacle、choices、cost，说明人物为什么此时行动；安静场景可目标为消化后果或改变关系，不硬塞敌人。
3. 标 target_delta、可观察 exit_condition；角色想达成的目标允许失败，不把人物目标等同作者保证成功。
4. 逐角色检查知情来源、身体限制、关系和可用物品；承接前场，不把伤势或怀疑归零。
5. 给 novel-information 制作 public_packet，只含当前可见事实、允许线索与禁止操作 ID。不能把完整作者真相附在场景旁注。
6. 选择有限细节锚点和动作空间，为留白留空间；不要把所有动作/每句台词锁死成流水账。
7. 高风险事件或完整核心揭示在生成前 paused，交 novel-canon；有同范围具体批准才可引用，不凭一般纲要许可。
8. 保存 planning/scenes/<id>.md 与分开的 <id>-public.yaml；批准后 handoff.ready，交 novel-draft 默认一场。

## 输出
场景卡、入口约束、选择/代价、target_delta、reveal_budget、exit_condition、公开包引用、风险与 handoff 状态。

## 权限
计划不更新 CANON、不宣称事件 happened。暂定关系变化允许候选设计，但依赖它的后场不能写成已确认事实。

## 资料
- 场景字段与公开包：references/workflow-details.md
- 交易场景示例：references/worked-example.md
