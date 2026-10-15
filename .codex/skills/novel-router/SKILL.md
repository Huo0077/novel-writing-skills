---
name: novel-router
description: Route natural-language novel creation, drafting, review, revision and project-management requests to the smallest relevant skill workflow. Use as the unified entry for this novel-writing suite, including initialization, mode selection, continuity, expression diversity, foreshadowing, pacing, checkpoints and safe project migration; handle reader-only tests before loading author state.
---

# 小说创作总控

## 输入
创作者当前任务、明确作品目录、期望产物、现有材料与协作模式。先判是否reader首次阅读，再判断需不需要读取项目，不能所有任务先读全书。

## 执行
1. reader/首次阅读任务只交 novel-reader-hypothesis-test 的 reader路线，跳过项目恢复、目录种子、catalog作者说明及带答案参考，未见响应不自称已测试。
2. 其他任务定位作品根目录，读取最少必要project/mode/当前进度。不存在或协议缺失交novel-project-init，先预览空白种子，不代用户编设定。
3. 用 references/routes.md 和 references/catalog.json 选择最短工作链；混合任务按依赖分阶段，不加载全部31项。
4. 明确当前目标、将读取资料、产出和停止条件。权限/事实缺口仅问一个当前阻塞点，并提供有差异选项、自定义/暂缓入口；未选不编故事，不重新要求填满百科。
5. A作者助手、B协同作者、C半自动长篇可选；模式只改变主动程度/批量范围，统一低风险暂定、中风险阶段确认、高风险暂停。
6. 写作从批准场景/公开包开始；审查依据实际正文；修订先意义约束/影响，再另存版本，不自动覆盖事实。
7. 只有novel-canon按来源/创作者决定处理正史。未来计划不当过去事实，目标差量不当实际完成。
8. 任务结束按实际产物报告已做/未做、风险、下一步，并交novel-checkpoint保存可恢复状态。工具未运行、文件未保存就不标complete。

## 输出
本次路由、任务范围、必要上下文、最小调用链、实际产物/路径、待确认问题、停止理由和下一步状态。面向创作者用普通语言，不要求记住模块名。

## 维护与迁移
用户安装使用标准npx skills add并选择完整31技能；首次作品初始化按 references/operations.md 使用 `scripts/init-project.mjs`，无需Python。--target明确作品目录，默认预览，--apply只补缺失.novel资源，不复制技能/QA或覆盖作品。scripts/suite.py保留开发验收与ZIP迁移能力，不混成npm包发布命令。
不得写入无授权外部目录或宣称全局安装/新会话自动发现已通过。单个skill依赖共享协议，迁移整组而不是只复制SKILL.md。

## 边界
这是助手执行规约，不是后台自动多代理系统。真实独立读者验证尚待新上下文或真人响应；文学效果不由格式测试担保。

## 资料
- 最短路由：references/routes.md
- 安全操作：references/operations.md

## 缺信息与用户选项
作者协作路线遵守 `.novel/schemas/clarification-contract.md`：先查已有资料，一次问一个当前关键问题，给2–3个有差异的方向及影响，允许自定义或暂不决定，不替用户默认选。答复只确认明确范围，缺答案时暂停依赖步骤。
reader独立阅读路线不读作者协议或候选答案；只中性询问阅读材料/范围缺口，不给作者真相选项、不恢复含秘密的档案。

## 安装位置与作品目录
仅作者协作执行以下资源恢复；reader首次阅读仍跳过作者档案和带答案资源。技能内references/scripts/assets相对于本SKILL.md所在目录；兄弟技能相对于同一已安装技能集合查找，不假定一定在.codex/skills。作品资料的.novel路径相对用户当前作品根目录，不能相对全局技能目录。缺共享资料时由novel-project-init运行router随附的Node初始化预览，经允许再应用；缺技能时提示安装完整组，不假装已读取。
