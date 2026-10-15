---
name: novel-clue-distribution
description: Plan and audit clue distribution across loaded novel chapters using surface functions, varied carriers, evidence windows and reveal dependencies. Use when clues feel too concentrated, conspicuous, repetitive or missing, while preserving intentional motifs and distinguishing planned clues from actual prose.
---

# 线索跨窗口分布

## 输入
作者真相、已读正文、线索卡、总纲/章节窗口、保护意象和读者当前证据。读 .novel/schemas/reveal-reader-contract.md，声明coverage。

## 执行
1. 收集实际出现线索source_ref，计划但未出现单列，不能用表格伪造公平性。
2. 为每条记录当前场景用途、载体、出现窗口、相对显眼度和竞争解释；删除真相后仍应自然。
3. 检查是否只有同物件反复凝视、是否所有异常一处集中、是否每次都由旁白高亮。
4. 变换行动/规则/关系/缺失/后果等载体，前后可变形但真正证据须兼容同一真相。
5. 区分有意主题复现与线索过度强调，不为“隐蔽”删掉关键可见证据。
6. 安排局部验证/反证/再解释窗口，为揭示留准备和余波；不按固定章间距公式。
7. 核查修改对时空、人物知识与其他线索依赖，交novel-impact-review。新增重大规则/回收交 novel-canon 分级。

## 输出
已出现/计划线索分布表、功能/载体/依据、拥挤与缺口、修改候选、覆盖盲点与下一窗口。

## 权限
只评已读材料；没有完整正文不宣称全书布置完毕。显眼度为主观编辑判断，不是猜中概率。

## 资料
- 分布卡：references/workflow-details.md
- 作者侧例子：references/worked-example.md

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
