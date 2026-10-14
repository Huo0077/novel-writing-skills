# 时间段模板

共用元数据：record_id / record_type / truth_status / lifecycle / source_ref / valid_from / depends_on / supersedes。格式见 .novel/schemas/story-record.md。

- calendar / start / end / precision / uncertainty：日历、起止、精度与不确定性。
- participants / location：人物和地点。
- travel_mode / travel_lower_bound / travel_source：交通、最短耗时和依据。
- before_ids / parallel_ids / narration_position：先后、并行与叙述顺序。
- conflict_evidence / open_questions：矛盾证据与未知。
lifecycle：planned / occurred / disputed。未知耗时不能用于确定性断言。
