# 小说创作 Skills 组 v1.1

31个模块，以 `novel-router` 为统一入口；支持作者助手、协同作者、半自动长篇三种模式。

v1.1修复六类校验漏洞，并加入全组用户提问与选项协议。

功能包括故事状态档案、章节/场景规划、正文回审、表达统计和多样化、伏笔分布/揭示/回收、节奏审查。
缺关键资料时向创作者提问，已有正史不静默覆盖；真实效果和独立读者评测仍待实际作品验证。

## 开始

阅读 `小说skills-快速开始.md` 和 `docs/novel-skills/skills组使用指南.md`。
将 `.codex/skills/novel-router/SKILL.md` 作为助手入口。当前是项目内文件，不宣称全局安装或UI自动发现已经通过。

## 验收

Python环境需要PyYAML。准备依赖后，在根目录运行：

```powershell
python .codex/skills/novel-router/scripts/suite.py validate --tests
```

测试/示例是虚构QA材料，不是创作者正史。默认项目为空白种子。统计与结构测试不证明文学质量、用户授权真实性或长篇绝不遗忘。

## 版本

GitHub Releases将分别提供原始v1.0和v1.1下载包及SHA-256。摘要用于完整性，不是签名。
仓库源码来自对应版本的已核验包，没有复制当前真实小说正文、正史、提案或检查点。
