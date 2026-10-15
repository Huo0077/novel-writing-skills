---
name: novel-character
description: Maintain novel character identity, motivations, dynamic states and voices. Use when creating characters, checking a scene against injuries, relationships or knowledge, tracking promises and possessions, or testing whether a choice is supported by prior character development.
---

# 人物状态管理

## 输入
人物档案、前场景状态、待核查原文、关系对象与当前知识权限。读取 references/record-format.md 与共享 story-record 协议；不用性格标签代替证据。

## 执行
1. 分开稳定约束（价值观、底线、长期需求）与动态状态（位置、伤势、信任、认知、物品）。
2. 检查每个动作的身体条件、知识前提和资源；检查信息、物品与承诺来源。
3. 对关键选择写“欲望—可见选项—阻力—选择—代价”；人物可矛盾，成长需触发依据。
4. 用 before/after/reason/source_ref 追加有效时段。未观察到痊愈、和解或学习，不自动重置。
5. 区分信任、依赖、怨恨等关系维度；信任下降不等于拒绝合作，合作不等于信任恢复。
6. 查语言关注点、回避和句法；允许场合差异，不把口癖铺满所有对白。
7. 证据不足标 possible_drift；不把成长、伪装或判断失误一律判错。只问当前选择的一个关键空位。
8. 将状态候选交 novel-canon；根本动机、生死、永久离场为高风险。

## 输出
状态切片；证据支持的冲突/可能漂移；选择链；最小修复候选；分级状态变更；后续不得回滚的约束。知情状态附获知来源。

## 权限
新动机、失忆或隐藏人格仅是 PROPOSAL。不得为了推动剧情直接改核心底线，不负责重写整章对白或决定长篇弧光结局。

## 资料
- 记录格式：references/record-format.md
- 示例：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
