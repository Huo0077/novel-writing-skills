# 最短任务路由

这些是任务选择表，不是机械关键词匹配程序。机器清单见catalog.json；仅引用真实存在的模块。

| 用户意图 | 首选入口 | 条件/追加 |
|---|---|---|
| 从零写小说/导入旧稿 | project-init | 一次关键提问；旧稿先segment-review |
| 切换作者助手/协作/半自动 | mode | 不改变风险边界 |
| 接着上次做 | context | 最新状态与必要来源，未决高风险先处理 |
| 设计世界/人物/时间/剧情 | 对应world/character/timeline/plot | 只补当前相关档案 |
| 总纲/这一章/这一场 | outline/chapter-plan/scene-plan | 创作者授权范围逐级明确 |
| 写下一场 | scene-plan→draft | 缺公开包先information；结束segment-review/canon/checkpoint |
| 前后不对/逻辑断裂 | continuity-audit/causality-audit | 双来源判断；相关领域核对 |
| 表达重复/同质化 | style-audit→expression-diversify→style-revise | 保护意象、含义；事实变化impact/canon |
| 不同角色说话一样 | character-voice | 场合变体，不盲加口头禅 |
| 伏笔一眼看穿 | foreshadow-craft/misdirection/reveal-calibration | 当前用途与有依据竞争；不保证猜不中 |
| 线索集中/忘回收 | clue-distribution/payoff-audit | 实际已读窗口，计划不当证据 |
| 揭得早/拖得久/情绪跳 | pacing-audit/reveal-calibration | 负荷、证据与余波，不固定公式 |
| 独立首次阅读 | reader-hypothesis-test的reader路线 | 只给材料，不context恢复作者资料 |
| 保存、确认事实 | canon/checkpoint | 分级决策与可恢复下一步 |

链接由总控按skill目录读取对应SKILL.md，不在此重复全部规则。
多个问题同时存在先排硬矛盾/权限，再因果/结构，再表达；用户仅要诊断就不要自动修改。
纯reader任务不读本路由中的作者说明，直接遵守SKILL.md的前置分支。
