# 信息项模板

共用元数据：record_id / record_type / truth_status / lifecycle / source_ref / valid_from / depends_on / supersedes。格式见 .novel/schemas/story-record.md。

## 作者包
- author_truth / truth_source / truth_confirmed：隐藏事实、来源与确定程度。
## 知识与证据
- character_beliefs：角色、时段、knows/suspects/misbelieves/unknown、获知来源。
- reader_evidence / narrator_permission：读者已見证据与叙述者权限。
- reveal_gate / earliest_reveal / risk：揭示条件、时机与风险。
## public_packet（与作者包分开）
- audience / viewpoint / allowed_facts / visible_clues：接收者、视角和当前可用内容。
- forbidden_operations：用信息 ID 和禁止操作，不复述隐藏答案。
- unresolved_questions / source_window：未解问题与来源窗口。
lifecycle：hidden / hinted / partial / revealed。全知戏剧性反讽必须明确批准。
