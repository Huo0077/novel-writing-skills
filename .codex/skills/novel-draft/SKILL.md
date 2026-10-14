---
name: novel-draft
description: Draft a bounded novel scene from an approved scene plan, authorized public packet and current state, then reverse-review actual prose and hand off changes for confirmation. Use when writing, continuing or expanding narrative prose without inventing canon, leaking secrets or exceeding the approved scene scope.
---

# 有边界的正文生成

## 输入
当前批准场景、public_packet、入口状态、公开声音资料、创作者给出的文风样本及紧邻正文。读取 .novel/schemas/planning-contract.md。不读取整份含答案总纲/作者笔记来“补灵感”。

## 执行
1. 检查 plan_status、approval_ref、任务范围、handoff、视角和信息包；不是批准范围就 blocked，问一个关键问题。技能开发授权不是小说剧情授权。
2. 仅装配当前可用事实，维护伤势、信任、角色知识与时间；保留已声明未知，不能由模型猜测变正史。
3. 默认一次一场；若批准有限多场，每场结束回审再判断能否继续。半自动模式也遵守同一风险边界。
4. 根据人物欲望和阻力生成动作/对话，不填“这个细节以后很重要”的作者提示。禁止自行回收核心伏笔、新增核心能力或让角色作未批准不可逆决定。
5. 遵守 exit_condition，场景目标失败也可停止，不为凑成功扩大范围。文风避免机械句式，但本模块不替代尚未实现的全章词频审查。
6. 正文作为 DRAFT 保存在 drafts/chapters/<scene-id>-v<revision>.md；不覆盖已确认正文。正文中不混入执行记录或解释性评语。
7. 实际执行 novel-segment-review，从写出的正文提取 facts_observed/inferences/state_changes；比较 observed_delta 与 target_delta，未实现就如实标记。
8. 用真实变化生成状态提案交 novel-canon；低风险暂存，中风险阶段确认，高风险立即暂停且将冲突稿保留为 DRAFT，不提交正史。
9. 实际保存 novel-checkpoint，列未决项与下一步状态。未执行回审/提交/保存时 handoff.review_pending/creator_pending，不能说“已完整完成”。

## 输出
分开的 DRAFT 正文、写作范围/停止理由、实际回审报告、分级变化、检查点引用与下一步状态。没有实际文件就交付文本并标未保存，不虚构路径。

## 权限
同一会话读过作者答案时不称独立隔离；仍约束只能将授权信息写出。对白/细节的新增事实必须回审。回审者知道作者真相可查泄露，但不是盲测读者。
遇高风险先说明影响并询问，不能先写答案再问是否采用。涉及事实的重写另走变更流程。

## 按需审查与修订
具体连续性/因果问题可交 novel-continuity-audit / novel-causality-audit；表达重复交 novel-style-audit → novel-expression-diversify → novel-style-revise。
信息/情绪/冲突释放问题可交 novel-pacing-audit，完整回收检查交 novel-payoff-audit。这些模块按任务触发，不默认每段运行全部检查。事实或线索变化交 novel-impact-review 与 novel-canon；语境改写也不得绕过回审。

## 资料
- 写作、回审与提交：references/workflow-details.md
- 完成与暂停示例：references/worked-example.md
