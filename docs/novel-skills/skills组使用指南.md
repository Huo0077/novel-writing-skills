# 小说创作 skills 组使用指南

版本：v1.1（验证器修复 + 全组渐进提问），2026-10-14。
本项目技能在 .codex/skills/，资料在 .novel/。这不是全局安装证明；当前会话若不能自动发现，可明确提供 SKILL.md 绝对路径并要求遵循。目录存在不代表某工具已经自动执行。

## 已实现的 31 项

| 组 | skill | 职责 |
|---|---|---|
| 总控 | novel-router | 自然语言任务入口、最短路由与整组维护 |
| 基础 | novel-project-init | 分阶段提问、初始化/恢复项目 |
| 基础 | novel-mode | 三种协作主动程度，统一确认边界 |
| 基础 | novel-canon | 正史保护、状态分级、接受/拒绝决定 |
| 基础 | novel-context | 最小必要上下文、接收者信息权限 |
| 基础 | novel-segment-review | 实际正文反向事实/状态回审 |
| 基础 | novel-checkpoint | 当前进度、未决项与安全恢复 |
| 状态 | novel-world | 世界条件、限制、代价与例外 |
| 状态 | novel-character | 人物伤势、关系、知识与选择 |
| 状态 | novel-timeline | 时间、地点、行程与并行事件 |
| 状态 | novel-plot | 情节因果、节点与下一步进度 |
| 状态 | novel-information | 作者真相、角色认知、读者证据与公开包 |
| 状态 | novel-foreshadow-craft | 场景表层功能、多解线索与回看价值 |
| 规划 | novel-outline | 总纲、卷/篇章结构与滚动规划 |
| 规划 | novel-chapter-plan | 章节功能、场景依赖、节奏和信息增量 |
| 规划 | novel-scene-plan | 入口状态、目标/阻力/选择、退出条件 |
| 正文 | novel-draft | 批准范围内小批正文、实际回审与交接 |
| 正文 | novel-character-voice | 关注点、对白策略、场合/压力变体 |
| 审查 | novel-continuity-audit | 双来源连续性核对与覆盖范围 |
| 审查 | novel-causality-audit | 目标、选择、代价与延迟后果 |
| 审查 | novel-style-audit | 字面词组/句式/符号统计＋有效重复判读 |
| 多样化 | novel-expression-diversify | 语境候选与原意约束、新事实标记 |
| 修订 | novel-style-revise | 获准范围新版本、保护意象与回审 |
| 修订 | novel-impact-review | 直接/间接依赖影响与未读盲点 |
| 伏笔 | novel-secret-design | 真相价值、隐瞒动机与人物后果 |
| 伏笔 | novel-clue-distribution | 跨窗口线索、载体和表层功能 |
| 伏笔 | novel-misdirection | 有依据的解释竞争与错误解释破除 |
| 揭示 | novel-reveal-calibration | 证据成熟度、局部验证与核心许可 |
| 测试 | novel-reader-hypothesis-test | 无答案材料、独立条件、原始响应与作者对照 |
| 回收 | novel-payoff-audit | 前置依据、回看新含义与情感/行动代价 |
| 节奏 | novel-pacing-audit | 信息负荷、冲突层级、情绪积累和余波 |

尚未实现：全局安装/界面自动发现验收、最终润色等。总控、共享空白种子、只增初始化、迁移包和整组验收工具现已建立。独立读者测试技能和材料协议已建立，但实际独立测试/真人评测尚未执行。当前表达统计不是中文分词，也不包含自动语义重复识别。

## 开始创作

1. 从 novel-router 统一入口说出任务；新项目会交 novel-project-init，一次解决一个关键问题。
2. 用 novel-mode 选作者助手、协同作者或半自动长篇。
3. novel-outline 先整理当前阶段结构；未知结局允许 unknown。
4. novel-chapter-plan / novel-scene-plan 限定当前任务，交付可批准计划和公开包。
5. 创作者确认范围，再由 novel-draft 写当前一场；可配 novel-character-voice。
6. novel-segment-review 按实际写出的内容回审，不抄计划目标。
7. novel-canon 分级处理变化；novel-checkpoint 保存结果和待确认事项。

这是一套助手执行协议，不是已部署的后台自动工作流。需要实际保存文件和完成各步才能声称相应步骤完成。

## 常用请求

### 当前章太散
“使用 novel-chapter-plan，读取现有状态和当前阶段目标，指出每场作用、重复功能和可合并位置。先给方案，不直接改正史。”

### 续写一场
“先用 novel-context 和 novel-scene-plan，保留伤势、关系和知识边界。获得我对当前范围的确认后，用 novel-draft 写一场；达到退出条件就停，回审实际变化并提交提案。”

### 对话分不清角色
“使用 novel-character-voice，保持原意与已知信息，用注意焦点和说话策略区分人物。新增动机或承诺单列，不把它们当纯润色。”

### 伏笔太显眼
“使用 novel-foreshadow-craft，保留当前场景任务，给线索自然用途和有证据的竞争解释；真相未定先问，不自作主张定答案。”

### 收工或换任务
“使用 novel-checkpoint，保存确定、暂定、待确认的区别和下一步不能揭示的内容。”

## 正史与计划

低风险 TENTATIVE；中风险阶段汇总；高风险立即暂停。
CANON + planned 不代表已经发生；plan_status=approved 是计划被批准，不代表 target_delta 已实现。
章节/场景批准只在指定范围有效，不能推导当前允许完整核心揭示。已有具体批准可引用，避免重复追问。

共享协议：story-record.md、planning-contract.md、audit-revision-contract.md、reveal-reader-contract.md、clarification-contract.md、status-change.md、context-packet.md、review-report.md、checkpoint.md，位于 .novel/schemas/。
把技能移用到另一项目时一并准备所需协议/模板/配置，但不要覆盖目标正史，不复制测试人物/情节为作品事实。

## 验证与能力边界

- quick_validate 检查技能格式，不评价文章好坏。
- unittest 检查固定产物的字段、引用、编码和已知信息交接，不调用模型，也不识别所有语义矛盾。
- 原基础验证器依赖已有 PyYAML，只校验基础文件/配置/提案，不是自动事实或时间推理数据库。
- 当前会话人工演练是流程检查，不是独立模型/真人读者盲测。
- 表达统计工具已实现字面词组、汉字窗口、句式、句首和标点候选；语境多样化与风格修订通过技能执行，不能把统计等同语义审查。

公开包分离只是行为约束，不是加密或实际访问隔离；同一会话读过真相后不能称盲测。


## 检查重复并改稿

“使用 novel-style-audit，先实际统计当前正文，再把候选分为有效、可疑、无效重复。保护我的主题意象和角色口吻；不能只按频次替换。”
“使用 novel-expression-diversify，对无效重复给少量语境候选，写清meaning_constraints和new_facts。获得范围批准后由 novel-style-revise另存新稿，回审实际变化。”
“任何新增动作、线索强调或承诺变化交 novel-impact-review，列已读/未读依赖；涉及正史交 novel-canon，不自动覆盖。”

### 实际统计工具

工具位于 .codex/skills/novel-style-audit/scripts/analyze_expression.py；只读传入文本，输出JSON，不自动替换。
JSON配置中的terms可填写要查的词组，protected指定value与reason。工具不直接读取风格YAML：由执行者把已确认保护意图转换为本次配置，保留来源。
既可检查一段也可合并明确的跨章窗口；合并后坐标相对于传入文本，要保留章/原文件映射。默认不会扫描整部小说目录。
输出另存新报告路径，不得将其重定向到原稿。零散Markdown注释也会被统计，优先使用纯正文。

高频不是劣质，显眼度变化也不一定改变词次。统计下降只是现象，文学判断需要读上下文和创作者反馈。


## 完整伏笔与揭示流程

作者侧：novel-secret-design → novel-foreshadow-craft → novel-clue-distribution / novel-misdirection → novel-reveal-calibration。
当前任务按需使用，不要求每个象征和小细节都过全链。
揭示候选/草稿：novel-payoff-audit查前置依据和后果，novel-pacing-audit查信息/情绪释放；改变事实/时机交impact-review与canon。
核心揭示仍高风险；已有具体时点内容批准可引用，不能拿一般纲要批准代替。

### 读者测试必须分路线

- prepare：作者人工选择真正已见正文，工具检查字段并生成prepared_not_run包。
- reader：全新且未见答案的接收者只读包，不打开项目档案、未来章节、checkpoint或作者示例。
- compare：收到原始回答后作者再加载真相核对；不能回传答案改变第一次阅读。

同一会话已经知道答案，只能做manual_rehearsal；没有实际独立响应时reader_guess=null，不填“读者猜不中”。

### 材料工具

路径：.codex/skills/novel-reader-hypothesis-test/scripts/prepare_reader_packet.py。
输入JSON严格只允许packet_id/scope/passages/reader_request；passages只id/text。文本内容仍须人工查，字段通过不等于语义零泄漏。
工具不自动打开目录、不调用模型，只输出读者材料。保存新文件，不能重定向覆盖输入。scope明确选段/完整章节及阅读范围。

## 整组交付与后续验证

目前总控、可迁移资源与单命令校验已实现；后续重点转向创作者真实作品演练与独立阅读反馈，不继续无限增加细碎skill。
尚未建立的蓝图模块不必全做；独立测试需要创作者授权新上下文或真人反馈，不能用作者自评替代。


## 一句话使用

“使用 novel-router。我的任务是……先选择必要步骤，只读取当前相关资料；保持我的正史、保护意象和信息边界，重大改动先问我。”
如果当前应用未自动发现，可明确提供本项目 .codex/skills/novel-router/SKILL.md 的绝对路径，要求读取并遵循。应用自动发现本身尚未验收。

## 单命令校验与安全迁移

在作品根目录运行：
```powershell
python .codex/skills/novel-router/scripts/suite.py validate --tests
python .codex/skills/novel-router/scripts/suite.py bootstrap 新作品目录
python .codex/skills/novel-router/scripts/suite.py bootstrap 新作品目录 --apply
python .codex/skills/novel-router/scripts/suite.py package dist/novel-writing-skills-v1.1.zip
python .codex/skills/novel-router/scripts/suite.py inspect dist/novel-writing-skills-v1.1.zip
```
bootstrap默认只预览；--apply新增技能、空白种子、隔离QA与说明，不覆盖已有文件，也不自动合并旧协议。执行目标需具备工作区权限。
迁移ZIP包含31技能、9协议、18模板、默认配置及用于验收的虚构测试故事；测试在tests目录，不是创作者正史。包使用共享seed，非当前作品的canon/drafts/proposals/checkpoints。源文档/技能中的演练示例属于设计参考，不宣称包中“没有任何虚构故事”。
新目录可先检查包再解压；已有作品不要直接由外部解压器覆盖，先bootstrap预览。包内manifest的SHA-256保证一致性，不是来源签名。
完整测试会报告操作系统无法运行的项（例如缺软链接权限）为skipped；不能把“OK含跳过”说成每项实际执行通过。


## v1.1：缺关键资料就问用户

先查已给资料，当前关键空位/冲突才问；一次一个问题，提供2–3项不同方向、后果/新增事实，并允许自定义或暂不决定。推荐不等于默认选择。
用户选择后记录真实回复来源与范围，局部答复不授权整个故事；未知远期项可保持unknown，不强求完整设定百科。
暂停依赖这项信息的写作/变更；无关安全统计或整理可继续。作者已明确许可的范围不无限重复追问。
reader独立阅读只中性核阅读范围/缺文段，不提供真相候选或加载作者笔记。

原测试发现的六类漏洞已补回归：medium也需确认、非空来源、类型枚举、状态/决定一致、空风险拒绝、实际配置解析。还检查字段类型/空实体/重复ID和重复YAML键。
旧的早期简化配置格式不静默兼容/自动升级；校验提示缺字段，由用户选择按当前格式补齐，并保留旧配置。
校验器结构合法不等于实际用户确认真实有效，仍需助手核来源；不是自动语义闸门或授权认证系统。
历史v1.0报告仍保留为当时记录，新问题/修复看v1.1修复报告。
