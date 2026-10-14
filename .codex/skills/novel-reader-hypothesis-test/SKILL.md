---
name: novel-reader-hypothesis-test
description: Prepare or conduct reader hypothesis testing for novel passages without leaking author answers. Use when checking obvious hints, competing interpretations, missing evidence or first-read reactions. Select preparation, reader-only response or post-response author comparison; never label an answer-aware review as an independent blind test.
---

# 读者材料与首次阅读

## 输入
先确定路线：prepare（作者准备）、reader（独立阅读）、compare（响应后作者对照）。路线不清只问一个问题。不得先恢复作者项目再声称盲测。

## 读者路线：优先执行
1. 若当前任务为reader，只读取给定读者包和中性任务；不要打开共享作者协议、项目/checkpoint/未来章或本技能作者侧示例。
2. 检查会话已见答案或作者诊断；有污染标manual_rehearsal，说明局限，不伪称independent_test。
3. 按首次读文本指出关注问题、可能解释、支持/反证、哪些表达过度强调及无法判断处。不强迫找反转，不查外部作品。
4. 保存原始响应与材料版本，自信只是主观判断；本路线不读novel-canon作者记录、不提交正史。

## 作者准备/对照路线
1. 读取 .novel/schemas/reveal-reader-contract.md，划定真实已见正文窗口，人工去除答案标题/注释/未来正文；选段测试注明缺完整阅读上下文。
2. 按references/workflow-details.md准备reader-input.json，运行scripts/prepare_reader_packet.py，另存新包。工具只拒绝额外字段，不语义保证无答案。
3. 仅prepared_not_run，不自动调用新模型。需独立执行时由创作者选择新上下文或真实读者；未授权不启动代理。
4. 获得原始响应后再做compare，引入作者真相核公平性/竞争解释，不能将预期答案回传修改首次回答。
5. 修改真相/伏笔/门槛交 novel-canon 分级及impact-review；报告独立来源、实际覆盖和未运行部分。

## 输出
prepare：材料包及prepared_not_run；reader：原始reader_guess与污染声明；compare：证据对照、建议和范围。没有运行reader就reader_guess=null。

## 权限
作者真相不混入阅读任务；读者所猜是解释，不自动事实。工具检查只是字段约束，不是技术隔离或语义泄题检测。

## 资料
仅prepare/compare路线可读，reader路线跳过：
- 材料工具：references/workflow-details.md
- 作者侧演练：references/worked-example.md
