---
name: novel-misdirection
description: Design fair competing explanations for novel clues and track how mistaken hypotheses are challenged. Use when a mystery is immediately obvious or misdirection feels dishonest; preserve narrator truth, character knowledge and evidence-backed ambiguity instead of random red herrings.
---

# 合理解释竞争

## 输入
已见证据、作者真相、视角权限、角色误信来源和阶段目标。读 .novel/schemas/reveal-reader-contract.md；作者侧任务，不给读者附答案。

## 执行
1. 从actual visible_evidence形成解释，不从想要读者猜错的结果倒造假证据。
2. 重要谜团默认至少两条当时合理解释，每条列支持、反证、局限和谁可能相信。
3. 真实解释同样受证据约束；不新增未设能力、秘密孪生或临时证人解决困难。
4. 误导可来自人物动机/偏见/合理误会；客观旁白不说假话，已批准不可靠叙述另列范围。
5. 为错误解释留可破除条件，局部证伪应增加理解而非只告诉读者之前全白看。
6. 保留人物行动功能，误导线索不是无关噪音。普通象征不硬凑两假答案。
7. 新事实或核心误信变更交 novel-canon；真相重写/大回收高风险暂停。

## 输出
解释竞争表、支持与反证来源、合理局限、破除窗口、视角公平性、风险和下一项澄清。

## 权限
读者猜对仍可成立；不是保证没法猜中。不能以作者故意不写视角角色明确所知关键答案作弊。

## 资料
- 竞争表：references/workflow-details.md
- 作者侧例子：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
