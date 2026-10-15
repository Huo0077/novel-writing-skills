---
name: novel-timeline
description: Maintain a novel timeline and test time, travel and concurrent actions. Use when sequencing events, checking ages, elapsed time, injuries or alibis, comparing simultaneous scenes, or repairing chronology without inventing dates or travel capabilities.
---

# 时间线与空间状态

## 输入
事件、人物时段、地点距离、行程规则、正文时间提示和已确认日历。读取 references/record-format.md；不自动套现实日历。

## 执行
1. 抽取显式时间和相对先后；区分故事顺序与正文倒叙/插叙顺序。
2. 用起止、上下界、精度和 uncertainty 表示时间；只有黄昏时不虚构分钟。
3. 按故事时钟列人物占用时段、地点和到达条件，对齐并行事件。
4. 核对先后、重叠、最短行程、等待、恢复和年龄；判断依据必须有档案来源或授权假设。
5. 已知上限小于下限判 confirmed_conflict；缺耗时/路线/机制则标 unknown 或 possible_conflict。
6. 提出改时间、改参与者或改为记录/转述的候选，不偷偷增加传送或缩短已确认行程。
7. 列出对不在场证明、线索顺序、角色获知时间的影响；改变关键真相立即请求确认。
8. 变更交 novel-canon，并建议 novel-checkpoint 保存当前故事时间。

## 输出
事件时间表、人物行程、冲突不等式与双来源、未知清单、修复方案与影响、一个需要确认的时间条件。

## 权限
只断言证据支持的矛盾。不包含自动约束求解器，人工推理注明依据。不把格式验收称为验证过全书时空。

## 资料
- 记录格式：references/record-format.md
- 示例：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
