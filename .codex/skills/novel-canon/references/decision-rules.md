# 正史与风险决策规则

## 风险判断

### low

不改变人物核心动机、关系、知识边界、世界规则、主线方向或重要伏笔。例如普通移动、普通环境细节、无后续影响的物品消耗。

### medium

会影响后续场景但仍可局部修正。例如关系轻微变化、新线索、新承诺、角色形成新的怀疑或心理状态改变。

### high

不可逆或大范围影响。例如揭示核心真相、改变世界规则、改变人物根本动机、改变关键事件结果、死亡/永久离场、回收重要伏笔、改变主线方向。

## 状态转换

```text
DRAFT → review report → PROPOSAL/TENTATIVE
PROPOSAL → accepted → CANON
PROPOSAL → modified → new PROPOSAL
PROPOSAL → rejected → REJECTED
TENTATIVE → creator confirmation → CANON
CANON → revision request → new proposal; preserve old source
```

## 必须暂停的情况

- 高风险提案的 `requires_confirmation` 不是 `true`。
- 正文与 CANON 冲突且无法通过明确的时间、视角或误导解释解决。
- 新事实需要新增世界规则，却没有说明规则适用范围和后果。
