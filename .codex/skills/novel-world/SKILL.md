---
name: novel-world
description: Maintain and test novel world rules, limits, costs and exceptions. Use when designing worldbuilding, checking whether a scene violates established rules, resolving conflicting lore or proposing a new rule without silently changing canon.
---

# 世界规则管理

## 输入
当前任务、相关世界规则、场景原文、信息边界和变更来源。读取 references/record-format.md 与作品根目录下 .novel/schemas/story-record.md；缺项目/协议则请求初始化。

## 执行
1. 分清建规则、查规则或修规则；只补齐当前任务相关机制，不填满无用百科。
2. 区分客观规则、传说、制度宣传与角色误信。角色说“绝不可能”不自动成为世界真理。
3. 写出“条件 → 可以/不可以的行动 → 代价/违反后果”，说明地域、人群、时段和失效条件。
4. 核对行动前提、实际支付代价与例外来源；没有依据的例外不能自动救场。
5. 给出 confirmed_conflict / possible_conflict / insufficient_information，分别引用规则与原文证据。
6. 优先提出保持正史的修复：改变行动、满足既有资格、体现既有代价。改规则的方案单独列下游影响，不默认采用。
7. 一次问一个阻塞点，例如“这是客观事实还是角色说辞？”；未知标 unknown。
8. 把记录或变更交 novel-canon 分级，不直接覆盖已确认档案。

## 输出
规则切片与来源；冲突证据和判断强度；最小修复候选；before/after、risk、受影响人物/事件；未决问题与下一步安全动作。

## 权限
新增核心能力、取消代价、关键例外可能高风险；普通世界细节也要检查是否改变谜题解法。查规则不等于润色整章或决定主线。

## 资料
- 记录格式：references/record-format.md
- 示例：references/worked-example.md
