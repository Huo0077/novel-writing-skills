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

## 缺信息与用户选项
作者协作路线遵守 `.novel/schemas/clarification-contract.md`：先查已有资料，一次问一个当前关键问题，给2–3个有差异的方向及影响，允许自定义或暂不决定，不替用户默认选。答复只确认明确范围，缺答案时暂停依赖步骤。
reader独立阅读路线不读作者协议或候选答案；只中性询问阅读材料/范围缺口，不给作者真相选项、不恢复含秘密的档案。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
