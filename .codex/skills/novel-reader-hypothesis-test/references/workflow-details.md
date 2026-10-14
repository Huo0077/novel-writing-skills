# 作者准备说明（读者路线不得打开）
CLI：python scripts/prepare_reader_packet.py reader-input.json，JSON输出stdout，报告写新路径，不重定向到输入。
允许packet_id、scope、passages、reader_request；passages项只id/text。reader_request为open_reading或hypothesis_comparison。
输入不自动扫描小说目录，输出不包括原路径/作者答案；ID/scope/text仍可能泄题，须人工筛选。
材料状态prepared_not_run；真正independent_test要求独立来源、实际上下文记录、材料版本和原始响应。多位读者结果不一致要保留。
作者对照用自身事实，但不把这些写回首次读材料。猜中不必改答案；发现证据缺口优先补公平性。
