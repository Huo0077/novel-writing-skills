# 情节事件模板

共用元数据：record_id / record_type / truth_status / lifecycle / source_ref / valid_from / depends_on / supersedes。格式见 .novel/schemas/story-record.md。

- thread_id / trigger / goal / obstacle：故事线、触发、目标与阻力。
- choice / alternative_choices：实际选择与替代选项。
- immediate_cost / result / delayed_consequences：代价、结果、延迟后果。
- preconditions / downstream_events：因果依赖与受影响事件。
- time_ref / participants / information_effects / foreshadow_refs：时空、人物、信息与伏笔。
- stage_goal / completed / pending / next_safe_action / cannot_reveal：当前阶段与下一步。
lifecycle：planned / partial / happened / delayed / rewritten / abandoned。
