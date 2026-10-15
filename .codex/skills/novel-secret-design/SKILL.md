---
name: novel-secret-design
description: Design a novel secret with causal, emotional and thematic value, separating author truth from public evidence. Use when defining a hidden identity, past event or mystery answer, comparing candidate truths, or revising a secret without inventing unsupported twists or silently changing canon.
---

# 真相与揭示价值

## 输入
故事问题、已确认世界/人物/事件、当前读者与角色认知、作者目标。读 .novel/schemas/reveal-reader-contract.md；先明确作者分析任务。

## 执行
1. 先确定隐藏事实是什么、由谁知晓、有何证据来源；未知真相写unknown/PROPOSAL，不强凑终极反派。
2. 检查揭示为何值得：改变角色选择、关系、过去理解或主题，而不只是宣布答案。
3. 写动机和因果：为什么隐瞒、隐瞒成本、谁误解、公开后谁获益/付代价。
4. 比较少量兼容已确认事实的候选真相，说明依赖/冲突与后果，不因为猜得出就强换答案。
5. 分开design_truth与visible_evidence；真相材料不发给正文或独立读者。
6. 为当前有价值的真相交novel-foreshadow-craft设计自然线索，后续由分布与揭示模块安排。
7. 真相新增/修改与关键动机改变交 novel-canon 分级，核心改变高风险暂停；引用具体批准，不假装同意。

## 输出
作者真相卡、价值/动机/成本、兼容证据与缺口、公开材料边界、候选后果、风险和一个阻塞问题。

## 权限
不自定全书结局，不把“惊天秘密”当设计。资料不足保留分支；不宣称这会让所有读者意外。

## 资料
- 细化：references/workflow-details.md
- 作者侧例子：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
