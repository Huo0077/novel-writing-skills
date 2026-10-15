---
name: novel-outline
description: Plan or revise a novel outline from premise to volumes and arcs while preserving canon, reveal windows and exploratory unknowns. Use when the creator asks for a whole-story outline, rolling outline, act structure, arc dependencies or macro pacing without inventing unapproved endings.
---

# 总纲与阶段结构

## 输入
创作者命题、目标类型/篇幅、已有总纲、世界与人物约束、当前进度、已确认/待定结局。使用 .novel/schemas/planning-contract.md；先判断作者分析任务，不把隐藏真相传入正文包。

## 执行
1. 判定新建或局部修订；读相关资料，不因重新规划而抹去已有正文。
2. 缺命题/主角目标等阻塞项时一次问一个；不要求填完整百科再开始。
3. 提供固定纲与滚动纲的合适粒度；作者未知结局时保留 unknown 和分支，不硬补“终极反派”。
4. 逐阶段写当前问题、角色目标、阻力、选择代价、情绪任务及阶段后果，引用相关事件/人物记录。
5. 分开表层困境、持续对立和深层问题。核心冲突可以早出现，但不必须早解释；悬疑、恋爱、冒险等节奏按作品目标决定，不强制隐藏一切。
6. 排列承诺/伏笔、局部答案与完整揭示窗口，标 dependencies 和 reveal_budget；给必要铺垫与高潮余波空间。
7. 检查人物弧光是否通过选择和后果形成，支线是否有自身功能，阶段是否重复同一套路。
8. 所有新剧情以 proposal 写入 planning/outline-<id>.md；已有 planning/outline.md 仅在范围批准后更新，保留旧版。计划批准不等于事件发生。
9. 改主线、结局、核心动机或世界规则，交 novel-canon 高风险确认；可续作方向不擅自变正史。

## 输出
作者版阶段总纲、事件依赖与弧光表、揭示/回收窗口、未决问题、风险变更和下级章计划交接。author_notes 单独标注，不直接发送 novel-draft。

## 权限
不强求固定三幕或每卷击败更强敌人；不把篇幅比例当成功标准。当前只实现协议，不保证叙事节奏被自动量化验证。

## 资料
- 细化步骤与产物：references/workflow-details.md
- 滚动纲示例：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
