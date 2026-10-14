---
name: novel-information
description: Maintain author truth, character beliefs, reader evidence and reveal permissions for a novel. Use when checking viewpoint leaks, who knows what and when, dramatic irony, early reveals or preparing a spoiler-free context packet for drafting or reader hypothesis testing.
---

# 信息边界与揭示权限

## 输入
相关 I-记录、场景视角、读者已见正文、角色获知来源与揭示门槛。读取 references/record-format.md；缺视角先问，不默认全知。

## 执行
1. 作者分析为 author_notes，正文可用材料为 public_packet，分产物保存；公开包不附隐藏真相。
2. 记录真实/待定事实、人物 knows/suspects/misbelieves/unknown、读者证据与最早获知时点。
3. 检查从谁、何时、凭何证据获知；猜测不是知道，作者知识不灌入人物。
4. 区分限知、全知、转述与不可靠叙述；已批准的戏剧性反讽不是自动错误。
5. 设异常、猜测、局部验证、完整揭示的 reveal_gate 与风险，不用“很神秘”代替计划。
6. 制作 public_packet：allowed_facts、visible_clues、行为约束、未解问题。禁止条目用 I-ID/操作，不复述真相。
7. 错误解释须由已有证据支持，不能叙述者撒假话作弊，除非不可靠叙述已设定且批准。
8. 改真相/完整核心揭示交 novel-canon 高风险确认；局部线索按影响分级。

## 输出
分开的作者信息表与公开包、泄露清单/双来源、获知路径、揭示许可、修复候选/风险和下一项澄清问题。

## 隔离边界
同一会话已读答案时不能声称盲测。真正独立测试须新上下文且只见已读正文/公开包。
目录分区不是加密或实际访问控制，指令只降低误用风险，不保证模型绝不泄露。

## 资料
- 记录格式：references/record-format.md
- 示例：references/worked-example.md
