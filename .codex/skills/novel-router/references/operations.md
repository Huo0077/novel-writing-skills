# 整组校验、空白初始化与迁移

工具：scripts/suite.py，Python环境需要PyYAML用于原有元数据/测试。没有依赖则说明，不能假装已检验。
在作品根目录运行如下命令（需shell工作区写权限），不使用外部全局安装。

```powershell
python .codex/skills/novel-router/scripts/suite.py validate --tests
python .codex/skills/novel-router/scripts/suite.py bootstrap 新项目目录
python .codex/skills/novel-router/scripts/suite.py bootstrap 新项目目录 --apply
python .codex/skills/novel-router/scripts/suite.py package dist/novel-writing-skills-v1.1.zip
python .codex/skills/novel-router/scripts/suite.py inspect dist/novel-writing-skills-v1.1.zip
```

所有支持--root的命令可明确源项目；默认按工具自身位置取根目录。bootstrap未指定--apply仅预览不写；apply复制共享空白项目与skills，已有同路径文件preserve、不会覆盖删除。存在旧协议/旧skill时保留后要重新validate，不等于自动升级。
目标soft link/junction会拒绝；检查不能防御所有并发环境变化，执行前确认目标/权限/其他程序没有改动目录。首次写失败可能已新增部分文件，工具不自动删除它们；重试会保留已经存在文件。
使用构造的新目录作为迁移目标，不把“保留”误认为旧小说所有状态已完整合并。

包仅包含catalog模块、空白seed、隔离QA测试和使用说明；不复制真实canon/drafts/proposals/checkpoints或用户标题。QA里的演练故事不是真实正史。
ZIP含路径摘要清单；inspect校验成员/摘要并拒绝路径遍历，不解压、不执行内容。SHA-256不是数字签名或可信作者证明。
迁移包需解压到空的新目录，再运行包内validate --tests。向已有目录直接解压可能由解压工具覆盖文件，本套工具不能保障外部解压器；已有作品使用bootstrap预览/只增模式。
目录发现/界面自动显示未通过测试，不声称全局安装完毕。新会话若不识别skill，明确给novel-router/SKILL.md绝对路径；不要让模型默默忽略协议。

validate现在同时解析实际项目配置与顶层状态提案，失败时先询问用户相关资料/意图并按当前schema补齐；不要为凑通过伪造确认。
