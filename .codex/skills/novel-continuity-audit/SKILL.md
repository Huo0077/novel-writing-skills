---
name: novel-continuity-audit
description: Audit novel continuity against source records and actual prose. Use when checking injuries, possessions, knowledge, relationships, chronology, world limits or revisions for contradictions without treating rumors, plans or deliberate lies as confirmed truth.
---

# 连续性与状态审查

## 输入
当前原稿/版本、回审报告、相关CANON和有效时段、计划/检查点。使用 .novel/schemas/audit-revision-contract.md；novel-context 明确读取范围。

## 执行
1. 列scope与coverage，先抽正文实际事实，不抄计划的target_delta。
2. 对每条事实核source_ref和生效时间，区分CANON、暂定、草稿及未来计划。
3. 检查地点/行程、伤势/恢复、物品转移、关系变化、承诺履行和知情来源；必要时交已有world/character/timeline/information模块。
4. 用正文证据与约束证据形成双来源：明确反例是confirmed，条件欠缺为possible/unknown。
5. 区分角色说谎、传闻、误信、不可靠叙述与客观机制。不要把多解悬念强行修成唯一解释。
6. 提供保持正史的最小修复、另列改正史的下游影响；不自行新增失忆/瞬移/快速痊愈。
7. 高风险矛盾或关键变更交 novel-canon 暂停确认；未知问一个关键问题。

## 输出
事实核对表、双来源问题、严重性、最小修复/风险、coverage盲点和下一步。没有问题时仅声明已审窗口未发现，不称全书绝无矛盾。

## 权限
只审查与提案，不直接覆盖正文、批准事实或强制“人物不能犯错”。纯表达问题交style-audit，不混成硬错误。

## 资料
- 判定细节：references/workflow-details.md
- 例子：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。
