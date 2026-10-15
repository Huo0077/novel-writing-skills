---
name: novel-payoff-audit
description: Audit novel clue payoff and retrospective meaning against pre-reveal prose. Use after planning or drafting a reveal to check fairness, emotional impact, consequences and unresolved details without inventing earlier evidence or assuming surprise is proven by an author-aware review.
---

# 回看依据与揭示后果

## 输入
揭示前实际正文、揭示稿/候选、作者真相、相关人物与事件、已读后果。读 .novel/schemas/reveal-reader-contract.md，明确coverage与evaluation_mode。

## 执行
1. 分开计划回收和实际稿，未来还没写的线索不能算已给读者。
2. 每项真相对照pre_reveal_evidence和reveal_source；缺关键前提标fairness_gap，不临时编早期段落声称一直存在。
3. 写旧场景如何获得不同含义，是否兼容原事实/视角/规则；仅新奇但无依据不是公平惊喜。
4. 检查误导解释为何被破除，仍有未解释细节如实列；不为了唯一解堵死所有文学留白。
5. 列payoff_outcome：人物情绪、关系、选择、代价和实际行动；只“公布答案”则考虑加强后果而非加说明篇幅。
6. 验证后续是否消化冲击/改变行为，未读后章列待核而非断言没写。
7. 修订回收或真相交 novel-canon 高风险确认与impact-review，保存checkpoint，不独自更改正史。

## 输出
双来源回看表、重解释、依据缺口/新造证据、情绪/行动后果、未解释项、覆盖与修订候选。

## 权限
当前会话知真相时不证明首次阅读意外度；不能以作者自评“惊艳”替代实际读者反馈。

## 资料
- 回收细化：references/workflow-details.md
- 作者侧例子：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
