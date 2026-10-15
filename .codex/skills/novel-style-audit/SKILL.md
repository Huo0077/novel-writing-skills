---
name: novel-style-audit
description: Audit novel expression repetition using read-only statistics and contextual judgment. Use when checking repeated phrases, sentence patterns, openings, punctuation, actions or motifs; distinguish useful recurrence from ineffective repetition before proposing changes, without claiming AI-text detection.
---

# 表达重复与风格审查

## 输入
原稿、明确文段/跨章窗口、人物公开声音与风格样本、保护意象及配置。共享 .novel/schemas/audit-revision-contract.md。

## 执行
1. 写scope/coverage，明确是本段、本章还是实际加载的跨章窗口，不拿单段频次冒充全书统计。
2. 运行 scripts/analyze_expression.py，保存输出到新的报告文件；输出路径不得与原稿相同。需要明确词组时传JSON terms，保护项写protected/value/reason。
3. 阅读高频候选的每个位置和上下文。词典匹配是字面terms；han_fragment是汉字窗口，不称中文分词词频。
4. 分有效、可疑、无效重复。相同意象可因主题/回环保留，角色口头禅看场合和密度，不能一键同义替换。
5. 审查重复动作、情绪命名、对白关注点、段落开合和隐喻；工具不识别这些语义关系，人工判断附证据。
6. 标点习惯是风格线索，不自动错误。保护依据不明时clarify，一次问一个意图问题。
7. 输出有理由的建议，交novel-expression-diversify生成候选；涉及知识/动作/承诺改变交 novel-canon 而非伪装风格调整。

## 输出
实际统计报告引用、候选位置、repetition_class/protection_decision及理由、优先修订处、明确保留处、疑问和覆盖盲点。

## 权限
不识别文字作者是不是AI、不给“AI味百分比”，不以生僻词/句长波动当质量分。不得默认修改工具列出的每项。

## 资料
- 工具配置和判断：references/workflow-details.md
- 例子：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
