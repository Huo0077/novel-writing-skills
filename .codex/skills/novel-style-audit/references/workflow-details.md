# 统计器使用
`python scripts/analyze_expression.py 原稿.txt --config 配置.json`，输出JSON至stdout。CLI只读，默认不保存；如需要报告，由执行者另存新路径。
配置：terms为字面词组列表；protected为value/reason列表；min_count>=2、ngram_size=2..12、max_candidates=1..200。
默认仅列常见表达字面匹配，不代表所有高频词。汉字n-gram跨字窗口不是分词；候选上限只限制片段条目，不保证完整语义统计。
每项offset/end_offset为0基字符位置，line/column为1基，surface为原文。重叠匹配计数，省略号/破折号连续写法按token归类。
坐标针对实际传入文本；若输入含Markdown标题/注释也会统计，建议提供纯正文，不声称自动去除作者笔记。
protected_count是出现位置包含在保护字串的次数，不隐藏计数、不批准改写。
rough_sentence_lengths只是按标点/换行分割粗略字符长度。所有findings均needs_context_review。

输出findings只含达到min_count的项目；未列出不能断言出现零次。比较前后须同时核对原文或配置的确切次数。
