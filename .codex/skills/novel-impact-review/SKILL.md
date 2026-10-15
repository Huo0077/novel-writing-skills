---
name: novel-impact-review
description: Review downstream effects of a novel revision using explicit record references and loaded prose. Use before canon retcons, changing key facts, revising a clue or promise, or synchronizing character states, timeline, plans and later chapters without claiming unseen material has been verified.
---

# 修订下游影响

## 输入
before/after、原文/新稿、实际回审、相关记录ID与depends_on、获准范围。使用 .novel/schemas/audit-revision-contract.md。

## 执行
1. 判定纯措辞、事实改变、信息显眼度变化或来源移动；不同类别有不同同步要求，不一律重写全书。
2. 标scope/coverage：实际读取、未读取、缺失索引。没有完整覆盖不能声明无下游影响。
3. 先查显式ID/source_ref/depends_on，再逐个已读实体检查知识、资源、时段、关系、承诺、世界例外及伏笔推理。
4. 追踪直接/间接依赖，列dependency_path、证据、certainty和required_action。标已确认影响/可能影响/无法判断，不凭文件名推断内容。
5. 检查揭示门槛/线索显眼度变化：没有改变故事客观事实也可能影响读者猜测。
6. 给同步顺序和最小范围，旧来源移动可修引用而非改剧情；不自动删除后续章或判废全部计划。
7. 改核心事实、关键事件或重大回收交 novel-canon 高风险确认；待决定不先同步正史。
8. 获准后相关技能更新记录、再审依赖窗口，novel-checkpoint保存剩余未知。当前没有自动图数据库，须实际执行并记录。

## 输出
改动类型、coverage、直接/间接影响路径、待检查文件、同步顺序、风险/待确认决定、剩余盲点。

## 权限
不假定depends_on完美，全文未读不全书背书。复杂影响可以暂停补资料，不用猜测把矛盾修成新正史。

## 资料
- 影响记录：references/workflow-details.md
- 例子：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
