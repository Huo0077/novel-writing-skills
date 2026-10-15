---
name: novel-character-voice
description: Design or revise distinct character voices for a novel using attention, word domains, syntax, social strategies and pressure variants. Use when dialogue sounds interchangeable, a speaker drifts from approved voice anchors, or creating a public voice profile without changing facts or inventing stereotyped catchphrases.
---

# 角色声音与对白辨识

## 输入
人物已确认经历/语言特征、当前场合和关系、可知信息、原对白及创作者语言样本。读取 .novel/schemas/planning-contract.md；只将公开声音特征传给 writer，不附人物隐藏动机答案。

## 执行
1. 分析 attention、词域、句法节奏、speech_strategy、avoidance，而不单靠“他很冷酷”等标签。
2. 保留人物之间关注差异：同一事件一个先问出口，一个先问交换条件；差异需已有档案或新特征提案来源。
3. 记录面对不同人、正式场合、压力下的变体；不让每句长度、每个结尾完全固定。
4. 缺口癖或地域语言依据时填 unknown，不发明刻板方言或装饰性口头禅。
5. 检查台词是否越过角色知识、承诺和关系：怀疑不能改成知道，敷衍不能改成真心答应。
6. 给原意等价候选，标哪些只改表达、哪些引入新动作/事实。事实变更交 novel-canon，不当作无风险润色。
7. 可做匿名对白辨识的人工回审，承认无法靠标签正确率证明真人一定辨认；已有答案的会话不称盲测。
8. 输出公开 profile 与短对照，未知保持 unknown。根本人格或重要身份变化仍高风险暂停。

## 输出
voice-profile、依据/候选特征、场合与压力变体、原意保持的对白样例、信息边界问题、风险/未决项。

## 权限
novel-character 管事实与状态，本 skill 管表达策略；不改角色关系来获得更“有个性”的台词。不把词汇生僻度或同义词数量当质量。

## 资料
- 声音字段与回审：references/workflow-details.md
- 同场不同关注示例：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
