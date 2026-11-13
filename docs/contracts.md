# 资料及接口契约

支持等值复合ON，null不匹配；动作类别matched(update/delete)、not_matched_by_target(insert)、not_matched_by_source(update/delete)，每类有顺序条件。条件只含eq/gt/is_null/and和常量，不执行SQL字符串。先生成完整匹配关系，再选动作；一个目标若有超过一个源匹配，即使只有一个源条件成立也拒绝整句。多个源均不匹配可各插入，但最终唯一键冲突拒绝；唯一键列均非null。not_matched_by_source仅在整个source关系完整后成立。table.py提供完整候选版本CAS和旧像核对，不实现MERGE。

所有记录为合成仓资料；data/source.json保存原始字段和身份。storage.py负责摘要读取，table.py保存独立关系版本，relations.py保留SQL三值和袋语义。inspect只调用现有基础接口，不提供新增查询或管理能力。
