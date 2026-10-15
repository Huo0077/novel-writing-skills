# 故事记录协议 v1.1

适用于所有故事状态 skills。作品根目录以用户指定路径为准；否则向上查找 `.novel/project.yaml`。缺少项目则调用 novel-project-init，不擅自另建同名项目。
作品相对路径以作品根目录为基准；references 以当前 skill 目录为基准。缺协议须询问或初始化，不假装已经读取。

## 共用字段
```yaml
record_id: W-001
record_type: world
truth_status: PROPOSAL
lifecycle: proposed
source_ref:
  - "creator-decision-001 或 chapter-01#paragraph-3"
valid_from: "scene-01 或 unknown"
depends_on: []
supersedes: null
```

- record_id：稳定 ID。W 世界、C 人物、T 时段、E 事件、I 信息、F 线索。
- record_type：world / character / timeline / event / information / foreshadow。
- truth_status：CANON / TENTATIVE / PROPOSAL / DRAFT / REJECTED / ARCHIVED。
- lifecycle：对象阶段，不能替代确认状态。
- source_ref：来源列表，可定位创作者决定、原稿段落或档案。推测不冒充观察事实。
- valid_from：故事内生效时点，不是修改文件的时间。
- depends_on：直接依赖的记录 ID；缺失项明确 unknown。
- supersedes：旧版/提案引用或 null；留存修订链。

## 状态维度
CANON + planned：作者确认将来安排，人物尚未经历。
PROPOSAL + happened：草稿写出事件，但尚未批准。
proposal.status（proposed/accepted/modified/rejected）为审议进度，和 truth_status 不同。
旧档案混写“状态”时先解释和提案迁移；可以直接更新空模板，不能静默迁移已确认事实。

## 来源与动态变化
区分正文观察、角色说辞、推断、作者确认。角色撒谎不是世界规则冲突。
动态状态保留有效时段、before/after/reason/source_ref，不只覆盖当前值。
两个 CANON 冲突需双来源与创作者决策，不能按最近修改优先。

## 领域职责与位置
| skill | 批准后的记录位置 | 职责 |
|---|---|---|
| novel-world | canon/world.md | 条件、限制与代价 |
| novel-character | canon/characters/<id>.md | 稳定档案、动态状态 |
| novel-timeline | canon/timeline.md | 时段、行程与并行事件 |
| novel-plot | canon/events/<id>.md、planning/outline.md | 因果、关键节点与下一步 |
| novel-information | canon/information-map.md | 真相、认知与揭示权限 |
| novel-foreshadow-craft | canon/foreshadowing/<id>.md | 场景化线索、解释竞争 |

文件放在 canon/ 不代表其所有条目自动成为 CANON。候选放 proposals/，分析放 reviews/。

## 更新事务
1. 读取来源与任务窗口，列出未知。
2. 领域 skill 生成候选记录或诊断，不直接改已确认档案。
3. 按 status-change.md 填 source_ref、before/after、affected_entities、downstream_impact。
4. 交 novel-canon：低风险暂存 TENTATIVE，中风险批量确认，高风险立即暂停。
5. 获得创作者决定后保留旧版与决定来源，再提交有关档案更新。
6. 用 novel-checkpoint 保存进度与未决项。

作者真相与正文公开材料分别成产物；“禁止揭示”提示也不得写出隐藏答案。本协议是行为规约，不是自动事实推理数据库。

缺信息与冲突依据 .novel/schemas/clarification-contract.md 逐项向用户提供选项；不默认批准候选，也不自动把一处回答扩成全局授权。

## v1.2 安装路径
本协议由已安装router/assets/project-seed随技能携带。源仓库.codex/skills是开发布局，不是所有客户端安装路径。项目级技能可在.agents/skills等集合目录，全局技能可位于作品之外；references/scripts/assets按skill自身位置解析，作品.novel始终按用户明确作品根目录。Node初始化只补作品资源，不把QA/模板例子当故事，也不自动安装Python。
