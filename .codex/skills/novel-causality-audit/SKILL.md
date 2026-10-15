---
name: novel-causality-audit
description: Audit novel causal chains, character agency, costs and consequences. Use when a plot turn feels forced, a solution is unearned, actions have no aftermath or a scene seems redundant, while preserving deliberate coincidence, quiet emotional scenes and supported character mistakes.
---

# 因果与人物能动性

## 输入
当前事件/正文、人物目标与认知、前置节点、章节功能、后续已读材料。使用 .novel/schemas/audit-revision-contract.md。

## 执行
1. 根据实际写出的事实列“触发—目标—阻力—选择—代价—结果—延迟后果”。
2. 检查角色可见选项及行为理由：不是要求正确决策，而是需要可理解的理由和反馈。
3. 标missing_trigger、unsupported_choice、unearned_solution、missing_consequence或functional_repeat，并给证据。
4. 巧合可以制造麻烦，不机械禁止所有偶遇；用巧合收拾关键困境则检查前置依据。
5. 检查配角独立目标、反派资源与反应、承诺/胜负余波；代价不一定死亡/牺牲，可以时间、关系或机会。
6. 安静场景可改变情绪理解、关系或主题体验，不能因没有打斗就判无效。
7. 提出有限最小候选，不为增强冲突硬加新阴谋；如改变主线/关键结果交 novel-canon 高风险确认。

## 输出
因果链、角色选择依据、缺口/延迟后果清单、保留功能、修复候选、风险与scope/coverage。

## 权限
不自动决定情节、不规定每事件都付巨大代价。没读后文只能说后果尚未见，不能断言没有回收。

## 资料
- 因果判断细节：references/workflow-details.md
- 例子：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
