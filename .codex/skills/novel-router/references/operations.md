# v1.2 安装、初始化与开发验收

## 用户安装

标准安装器：npx skills add Huo0077/novel-writing-skills；选择全部31技能和目标assistant。
已实测skills@1.7.2、Node26；安装器要求Node>=22.20。
明确Codex本项目安装：
```bash
npx skills@1.7.2 add Huo0077/novel-writing-skills --agent codex --skill '*' --copy
```
--copy避免symlink依赖；标准安装器更新可能覆盖同名技能文件，先备份自定义skill。不要宣称npx安装器本身保留所有自定义技能。
本次Codex输出.agents/skills；source repo是.codex/skills。其他agent以实际安装位置为准，不把已测Codex扩展为所有客户端自动发现已验证。

## Node作品初始化（无需Python）

找到实际安装的novel-router脚本，按当前作品/用户指定作品执行：
```bash
node .agents/skills/novel-router/scripts/init-project.mjs --target .
node .agents/skills/novel-router/scripts/init-project.mjs --target . --apply
node .agents/skills/novel-router/scripts/init-project.mjs --check
```
以上路径是Codex项目安装示例。全局源用实际绝对路径传给node，--target仍是作品目录，不由脚本位置推断。
默认只预览。--apply复制shared seed的缺失.novel文件，保留原文件；不重装skill、不复制QA、不写用户已确认设定。--check只验资源/兄弟模块存在，不解析作品事实或YAML。
缺任何已登记skill就停止说明，建议重新选择全31模块；不能假装只router即有全部执行能力。
目标在skill目录内或symlink/junction会拒绝；存在旧文件保留后需问用户如何处理格式/内容差异，不自动迁移。
失败后可能已新增部分文件，不自动回滚删除；重试保持只增原则。目录并发变化不在强事务保证内。

## 全局技能与作品生命周期

全局安装可加--global，仅改变技能位置。每本书独立--target，不能把多本书写进全局目录。
卸载skill只由标准安装器管理，不删除作品.novel。更新skill与更新作品schema不是同一操作，旧作品保留，按用户授权补缺/迁移。
reader路线仍只读取公开材料，不因为安装检查而恢复含答案作者档案。

## 开发与ZIP迁移

source repo或Release ZIP可运行scripts/suite.py的validate --tests（需要Python/PyYAML及Node）：
```bash
python .codex/skills/novel-router/scripts/suite.py validate --tests
python .codex/skills/novel-router/scripts/suite.py package dist/novel-writing-skills-v1.2.zip
python .codex/skills/novel-router/scripts/suite.py inspect dist/novel-writing-skills-v1.2.zip
```
Python开发suite支持.codex/.agents/.claude资源集合定位，但完整固定QA仍在仓库/ZIP运行；不要把用户项目缺QA误称故事损坏。
ZIP带31技能、shared clean seed、隔离QA、Node脚本、MIT、README及封面；真实canon/drafts/proposals/checkpoints不出包。
旧Python bootstrap仍是整组ZIP布局复制工具，不是用户npm安装步骤；默认preview、apply新增不覆盖。无需为npm安装运行它。
inspect校验路径/摘要而不解压。SHA-256不是签名。v1.0/v1.1标签及ZIP保留。
