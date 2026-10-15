---
name: novel-expression-diversify
description: Generate context-aware alternatives for ineffective novel repetition. Use after expression audit to vary word choice, syntax, sentence groups, action or perspective while preserving meaning, voice, uncertainty and information limits; flag new facts rather than silently applying synonyms.
---

# 语境表达候选

## 输入
已审查问题、原段上下文、人物公开声音、叙述视角、保护项、获准范围。使用 .novel/schemas/audit-revision-contract.md。

## 执行
1. 为每个待改处写meaning_constraints：动作、认知、承诺、语气强度、时间、指代和视角。
2. 先判断能否删无功能重复/调整信息顺序，再考虑词组、句法、句群和段落。不是必须用更华丽的近义词。
3. 抽象情绪可转行动/停顿/环境反应，但明确new_facts，不称自动语义等价。当前角色行为和空间条件必须容许。
4. 同义替换检验搭配、语域与指代；同一世界专名、主题意象和保护词默认保持。
5. 一般给两种方向即可，不给大量无差异方案；作者要求最小修改时优先仅句法/删改。
6. 逐项写原意保持/未保持、new_facts和风险；新增承诺/线索/知情至少重新评估，核心变化交 novel-canon 高风险确认。
7. 只生成候选，不应用未批准的实质变化；交novel-style-revise在范围内处理。

## 输出
candidate_id、original_ref、operation、meaning_constraints、replacement、new_facts、保护决策、risk与待确认问题。

## 权限
不靠新比喻替换所有短句，不故意复杂化文字。不把“可能知道”改成“知道”，不把“戒备合作”改成“全然信任”。

## 资料
- 语义核对：references/workflow-details.md
- 例子：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
