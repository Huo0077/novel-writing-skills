# 小说创作 Skills v1.2 · 快速开始

## 1. 在作品目录安装

准备Node.js/npm；本次实测安装器skills@1.7.2要求Node>=22.20。
```bash
npx skills add Huo0077/novel-writing-skills
```
选择全部31技能和目标助手。Codex的明确安装例：
```bash
npx skills@1.7.2 add Huo0077/novel-writing-skills --agent codex --skill '*' --copy
```
标准安装器可能替换同名skill，请先备份你修改过的技能。作品资料的保护在下一步，不混作一条保证。

## 2. 初始化作品（无需Python）

Codex项目安装路径为.agents/skills；其他助手以实际输出为准。
```bash
node .agents/skills/novel-router/scripts/init-project.mjs --target .
```
先看预览，允许后执行：
```bash
node .agents/skills/novel-router/scripts/init-project.mjs --target . --apply
node .agents/skills/novel-router/scripts/init-project.mjs --check
```
只补缺失.novel文件，不覆盖旧稿、不复制QA、不创建正史。--check只验证安装资源，不评小说事实。
全局安装加--global；使用全局脚本的实际绝对路径，并用--target指定每本作品，不能在全局skill文件夹写小说。

## 3. 告诉助手

> 请读取实际安装的novel-router/SKILL.md。我的任务是……缺关键资料时一次问一个问题，给不同方向及影响；允许我自定义或暂缓，不默认补设定。

作者助手、协同作者、半自动长篇可选；低风险暂定、中风险阶段确认、高风险暂停。
计划不等于发生，草稿不自动正史。人物伤势、物品、认知、关系和伏笔由来源记录维护。

## 备用与验证

ZIP解压到空目录，保留隐藏目录；source布局为.codex/skills，同一个Node脚本从该位置运行即可。不要解压覆盖旧作品。
安装/初始化只需Node；可选的表达统计/读者材料/完整QA仍需Python。开发repo执行npm test仅运行Node测试；完整回归还需Python/PyYAML。
详情：README.md、README.en.md、docs/installation-v1.2.md和docs/novel-skills/skills组使用指南.md。
MIT随skill的LICENSE.txt与ZIP的LICENSE分发。独立读者/真实文学效果仍需测试，文件安装不代表所有客户端UI自动发现。
