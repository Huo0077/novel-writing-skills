---
name: novel-mode
description: "Select or change the operating mode for a novel project: author assistant, co-author, or semi-automatic long-form writing. Use when the creator wants to choose how proactively AI plans, writes, confirms changes, or checkpoints progress."
---

# Novel Mode

## Modes

- `author_assistant`：以整理、提案、回审和润色为主；默认一次推进一个任务。
- `co_author`：允许主动提出剧情、人物选择和伏笔方案；重大变更仍需确认。
- `semi_automatic`：沿着已确认大纲连续推进低风险内容；遇到高风险变更立即暂停。

## Workflow

1. 读取 `.novel/project.yaml` 和 `.novel/config/modes.yaml`。
2. 如果用户没有明确选择，说明三种模式的差异并询问一次；不要替用户静默选择高主动模式。
3. 更新 `project.yaml` 的 `mode`，同时输出本次模式的主动程度、批量范围和检查点频率。
4. 无论模式如何变化，都保留统一规则：低风险写入 `TENTATIVE`，中风险批量确认，高风险立即请求确认。
5. 若切换模式会影响未决提案或当前任务，列出影响，但不自动批准提案。

## Safety

模式改变的是推进范围和确认频率，不改变正史安全边界。不得因为半自动模式而静默修改 `CANON`，不得因为作者助手模式而丢弃已有状态。

## Resource

- 统一决策规则：`../novel-canon/references/decision-rules.md`（相对于本skill目录）

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
