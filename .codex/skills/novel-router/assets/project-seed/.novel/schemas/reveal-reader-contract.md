# 真相、线索、读者测试与回收协议 v1.0

沿用 story-record / planning-contract / audit-revision-contract 的来源、权限与确认规则。
作者设计、读者所见、读者猜测、回收效果必须分产物。

## 四类信息

- design_truth：作者设计真相，truth_status与批准来源明确；尚未决定则unknown或PROPOSAL。
- visible_evidence：揭示前实际正文，含source_ref/窗口/载体/表层功能，不把预定线索写成已出现。
- reader_guess：测试者仅凭已见正文的解释、证据与不确定度；没有运行则null，不能从作者脑补填入。
- payoff_outcome：揭示怎样改变旧场景理解、人物关系/目标/情绪、实际行动与代价。

## 作者记录

secret_id / design_truth / truth_status / source_ref / known_by / stakes / thematic_function / consequences / open_questions。
每条线索记录clue_id、secret_ref、surface_function、carrier、window、visible_evidence、source_ref、salience、competing_explanations、next_step。
分布需实际读到的多窗口，不按“每三章出现一次”公式；保护意象可反复出现，但出现有不同当前功能。
重要谜团默认至少两种合理解释，普通象征/预示不强制。每种解释需要当时证据与局限，不能作者编假事实诱骗。

## 揭示门槛

reveal_gate包含当前剧情需要、读者/角色证据成熟度、允许呈现层级、最早窗口及具体批准来源。
异常→猜测→局部验证→完整揭示不是必须固定四步，更不是章数刻度。允许戏剧性反讽和读者比人物知道更多，前提是视角与目标已批准。
核心揭示/改变真相/重大回收为high，按novel-canon暂停或引用已有相同时点和内容的具体许可；一般规划批准不是现在明示许可。
猜对不自动失败，猜不到也不保证公平；可预测真相仍可因代价与情感令人难忘。

## 读者测试三条路线

### 准备（作者侧）
选择真正已见正文，去除含答案标题/文件名/标注/未来正文/解释。保留中性窗口范围，必须说明是完整章节还是选段；选段结果不能冒称完整阅读。
准备reader-input.json，仅packet_id/scope/passages/reader_request。passages只id/text，不附秘密标签或预期解释。
prepare_reader_packet.py只拒绝额外字段、检查类型，不能语义判断正文是否泄题。文本/请求/ID/scope仍要人工查，不能把工具通过当“零泄露”。
输出prepared_not_run，不产reader_guess，也不自动调用模型。

### 阅读（独立接收侧）
先检查上下文是否曾见答案；只读读者材料，不读取项目配置/检查点/作者档案/未来章或本技能作者示例。
开放阅读优先，避免“这里有反转，找出来”诱导。可以记录多种解释、支持/反证、相对确定度与哪些句子过度强调。
答案污染则标manual_rehearsal而非independent_test。数字自信为测试者主观判断，不能当总体读者概率。

### 作者对照（响应后）
保留reader_response原始结果与材料版本，再引入作者真相核对。不能把答案或预期判断发回测试者以改变第一次回答。
记录支持的假设竞争、过度醒目位置、依据缺口和建议，不只计“猜中/没猜中”。多个测试有差异要保留，不挑选自己满意的结果。

## 测试状态
- prepared_not_run：材料准备好但未执行独立阅读。
- manual_rehearsal：作者已知答案的人工检查。
- independent_test：有实际独立来源/新上下文记录、材料版本和原始reader_response；不能只改标签。
独立环境无技术隔离证据时记录unknown，不声称保证；用户没有授权独立执行时只交付材料。

## 节奏与回收

报告coverage.read_sources/not_read；按当前冲突、信息负荷、情绪积累、局部兑现与余波检视。
揭示前证据和揭示内容逐条双来源对照，记录重解释、仍未解释与新造证据。
结果必须有足够后果；未读之后章节只能列待核，不断言没有代价。不要为惊喜硬加死亡、加谜团或否定已建立规则。
修订可能改变线索显眼度而不改词次，交novel-impact-review；由novel-canon分级，再保存checkpoint。
