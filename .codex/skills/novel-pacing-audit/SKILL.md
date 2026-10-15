---
name: novel-pacing-audit
description: Audit novel pacing across actual loaded passages using scene function, information load, emotional accumulation, conflict layers and aftermath. Use when reveals or core conflicts are explained too early, scenes drag, escalation repeats or emotional turns lack preparation; avoid fixed twist-per-chapter formulas.
---

# 节奏、信息与情绪

## 输入
已读正文/窗口、章节与场景功能、人物状态、类型/作者目标、揭示许可。读 .novel/schemas/reveal-reader-contract.md，记录scope/coverage。

## 执行
1. 依实际正文标场景功能和变化，比较计划目标但不替实际结果写成功。
2. 区分动作速度、信息速度、情绪速度和故事时间；短句多不代表剧情推进快。
3. 核信息负荷：新名词/规则/真相集中是否阻碍当前问题理解；必要规则先给，远期解释可留白。
4. 查冲突层级：表层阻力可早现，深层原因/主谋不必早解释；根据类型目标而非“所有核心冲突必须晚出现”。
5. 核情绪积累与关系转折，爆发/信任/原谅要有触发和过程；高潮/揭示后留反应、代价和新行动空间。
6. 查功能与开合套路重复，保留有意回环和安静关系场；不强制每章升级反转悬念尾句。
7. 给有限修复：删冗解释、分开信息、补已设后果、改场景顺序；新事实/改变揭示交 novel-canon 与impact-review。

## 输出
场景功能/信息/情绪曲线（主观编辑判断）、过早/拖延/重复证据、余波缺口、范围内修订候选与未读盲点。

## 权限
不输出伪读者紧张度/节奏分数，不以字数比例替代文本判断。未读全章就只对选段建议。

## 资料
- 节奏判读：references/workflow-details.md
- 作者侧例子：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
