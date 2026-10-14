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
按 references/operations.md 使用 scripts/suite.py。bootstrap默认预览，--apply只增不覆盖；package只带技能、共享空白种子和隔离QA，不携带作品正文/正史/提案。
不得写入无授权外部目录或宣称全局安装/新会话自动发现已通过。单个skill依赖共享协议，迁移整组而不是只复制SKILL.md。

## 边界
这是助手执行规约，不是后台自动多代理系统。真实独立读者验证尚待新上下文或真人响应；文学效果不由格式测试担保。

## 资料
- 最短路由：references/routes.md
- 安全操作：references/operations.md

## 缺信息与用户选项
作者协作路线遵守 `.novel/schemas/clarification-contract.md`：先查已有资料，一次问一个当前关键问题，给2–3个有差异的方向及影响，允许自定义或暂不决定，不替用户默认选。答复只确认明确范围，缺答案时暂停依赖步骤。
reader独立阅读路线不读作者协议或候选答案；只中性询问阅读材料/范围缺口，不给作者真相选项、不恢复含秘密的档案。
