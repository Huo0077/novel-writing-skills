---
name: novel-reveal-calibration
description: Calibrate novel reveal timing and salience using narrative need, evidence maturity, character knowledge and approved reveal gates. Use when secrets are exposed too early, mysteries stall or readers have only one obvious explanation; distinguish local payoff from full truth and do not promise surprise scores.
---

# 揭示时机与程度

## 输入
当前场景目的、读者可见证据、人物知识、作者真相、已有测试响应（若有）及批准范围。读 .novel/schemas/reveal-reader-contract.md。

## 执行
1. 判断当前需要观察异常、提出猜测、局部验证或完整答案；不是按章节序号自动递进。
2. 检查角色获知路径、证据是否充分、叙述权限及当前reveal_gate；作者知道不等于此时能写。
3. 区分过早解释核心与必要早呈现冲突；主线阻力可以立刻存在，背景原因不一定讲透。
4. 若读者几乎只有一个合理解释，优先检查表层功能/竞争解释/过度强调；不能靠删公平证据或改唯一真相逃避。
5. 若悬念拖延，给解决当前行动问题的局部答案或新后果，不无限添谜团。
6. 测试已运行则引用原始反馈，没有就unknown/待测试；数字显眼度不是猜中概率。
7. 核心提前揭示、改变门槛、重大回收交 novel-canon 高风险确认；有同范围具体批准可引用，不重复拦截。

## 输出
当前允许层级、证据成熟/缺口、局部与核心reveal_gate、过早/拖延风险、候选修订/影响、待确认决定。

## 权限
不要求所有小说都隐藏核心冲突，也不固定“第几章必须揭示”。揭示后的情绪/关系后果交pacing/payoff模块。

## 资料
- 校准字段：references/workflow-details.md
- 作者侧例子：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。
