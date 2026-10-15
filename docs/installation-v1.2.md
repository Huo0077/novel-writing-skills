# v1.2 安装与初始化验收 / Installation validation

## 范围 / Scope

复用标准skills安装器，不发布独立同名npm包。安装技能与初始化作品分开，用户初始化无需Python。
The suite uses the standard skills CLI, not a separately published npm package. Skill installation and story initialization are separate; initialization needs no Python.

## 当前已实际验证 / Executed locally

- Windows，Node v26.3.0、npm 11.16.0、skills@1.7.2；安装器声明Node>=22.20。
- 标准CLI发现31模块；明确--agent codex --skill '*' --copy安装到隔离项目.agents/skills。
- 真实全局安装使用先核对过的隔离HOME/USERPROFILE，未修改使用者真实全局目录。
- 已安装的Node脚本能找到31模块与seed，不依赖源码根目录。
- preview不生成.novel；apply创建缺失资料；重复执行零新增；用户手改project.yaml字节不变。
- .novel不复制源码QA；每个skill携带MIT LICENSE.txt。
- 通过标准CLI在隔离项目卸载skill后，创作者.novel保持；不操作用户真实global目录。
- 新Node测试23项；Python便携目录/出包测试3项；旧122案例需与新增项一起回归。

本节为真实本地源码安装演练，不自动等于GitHub远程分发已通过。远程包的安装、完整回归和迁移结果将在发布前追加；不能根据源码演练宣称Linux/macOS或所有助手都已测。

## 命令 / Commands

```bash
npx skills@1.7.2 add Huo0077/novel-writing-skills --agent codex --skill '*' --copy
node .agents/skills/novel-router/scripts/init-project.mjs --target .
node .agents/skills/novel-router/scripts/init-project.mjs --target . --apply
node .agents/skills/novel-router/scripts/init-project.mjs --check
```

使用其他assistant需按实际输出定位；Codex仅是本次实测目标。global脚本用实际绝对路径，作品用--target指定，不能把user home当小说。
`--check`只验文件/模块存在；不解析故事、用户授权或YAML内容。旧项目保留不等于自动合并版本；新增缺口按用户问答协议处理。
`--copy`避免符号链接，但标准CLI更新可覆盖同名skill目录，手改skill先备份。

## 依赖与开发

用户安装/初始化：Node/npm/npx，零额外Node运行依赖，无postinstall。Python工具仍是可选依赖，不自动装Python。
开发source/ZIP保留完整QA，Python/PyYAML与Node用于完整验收；npm test只运行Node测试。
仓库源布局.codex/skills；npx Codex安装布局.agents/skills，两者不可混用硬编码。

## 保留限制

尚未进行真实跨平台UI自动发现、独立模型/真人文学评测。资源安装通过不保证模型始终遵循规则。
初始化预检冲突并独占新建，仍不是防并发文件系统事务；出现错误可能已新增部分文件，不会自动删作品回滚。
保留v1.0/v1.1 ZIP和标签；v1.2包附LICENSE/每skill许可，SHA-256不等于签名。
