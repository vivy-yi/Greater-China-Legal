---
# Test Case Schema — contract-review
# 这是 A（测试集）的契约模板。复制本文件，填入实际数据，
# 保存为 plugins/legal-scenes/contract-review/tests/cases/<case-id>.md

# ===== 必填字段 =====
case_id: contract-review-NNN    # 唯一 ID，NNN 3 位顺序号
scene: contract-review
difficulty: standard             # standard | complex | edge
created_at: YYYY-MM-DD
created_by: <lawyer-id | 来源标注>

# ===== 输入 =====
input:
  type: contract-clause | full-contract | user-query
  content: |
    （脱敏后的真实合同片段 / 用户问题）
  user_query: "请审查这段付款条款"  # 可选：无 query 时用纯 content

# ===== 法律事实（可选，但推荐） =====
# 调用 legal-element-extraction 后应得出的结构化事实
# auto-test runner 可用此字段对比 skill 提取的事实是否完整
expected_facts:
  parties: ["甲公司", "乙公司"]
  contract_type: "服务合同"
  amount: "80万"
  governing_law: "中华人民共和国法律"
  # ...

# ===== 期望输出特征（auto-test EVAL 评分依据） =====
expected_output:
  # 必须包含的法条（law_citation_accuracy 维度）
  must_contain_laws:
    - "民法典 585"
    - "民法典 526"
  # 必须识别的风险点（risk_coverage 维度）
  must_flag_risks:
    - "违约金过高"
  # 必须包含的章节（format_compliance 维度）
  must_have_sections:
    - "## 风险等级"
    - "## 修改建议"
  # 必须包含的建议（advice_soundness 维度）
  must_contain_advice:
    - "建议将违约金调整为不超过实际损失的130%"
  # 不应包含的错误建议（advice_soundness 反向检查）
  must_not_contain:
    - "建议删除该条款"
    - "美国法律适用"

# ===== 评估维度（每个维度独立打分 0.0-1.0） =====
evaluation_dimensions:
  - law_citation_accuracy    # 法条引用准确度
  - risk_coverage            # 风险覆盖度
  - advice_soundness         # 建议合理性
  - format_compliance        # 格式合规度

# ===== 测试元数据 =====
priority: high                 # high | medium | low
tags: ["违约金", "金额-80万", "标准服务合同"]

# ===== 真实来源标注（脱敏要求） =====
provenance:
  source: "<律所案例库 | 北大法宝 | 真实合同脱敏 | 用户上传>"
  anonymization: "已脱敏：去除真实公司名、身份证、银行账号"
  reviewer: "<律师签字 or 'N/A - 公开案例'>"
  reviewed_at: YYYY-MM-DD
---

# [测试名称] — [测试场景描述]

## 测试背景

（简述这个测试用例的现实来源和考察意图）

## 输入详情

（展开 input.content 的关键片段，便于人工 review 时理解）

## 期望分析路径

（律师视角：正确的分析应该走哪几步、引用哪些法条、得出什么结论）

## 评分说明

（解释为什么 must_contain_laws 必须有这些法条，must_not_contain 为什么不能有那些表述）

---



---

## 法条引用规范化规则（重要！）

dry-run 暴露的真实问题：同一法条可能有多种写法，字符串 `in` 检查会失败。
**所有 must_contain_laws 必须用以下规范格式**：

| 规范格式 | 示例 |
|---------|------|
| `<法源简称> <条号>` | `民法典 585` |
| ❌ 禁止 | `民法典第585条`（带"第...条"）|
| ❌ 禁止 | `《民法典》第 585 条`（带书名号+第...条）|
| ❌ 禁止 | `Civil Code Art. 585`（英文）|

**理由**：runner 评估时会对 skill 输出做 normalize（去除《》、第、条、空格），
再与 must_contain_laws 比对。schema 写规范格式是为了**人 review case 时一眼看懂**。

**评估器 normalize 逻辑**（未来实现）：
```python
def normalize_law_ref(text: str) -> str:
    # 去除《》书名号、第X条、空白
    import re
    return re.sub(r'[《》\s第条]', '', text)

# 例:
# normalize("《民法典》第 585 条") == normalize("民法典 585") == "民法典585"
```

**runner 检查法条引用时**：
1. 对 skill 输出全文 normalize
2. 对 expected.must_contain_laws 逐项 normalize
3. 比对：normalize 后 expected in normalize(skill_output) ?

*contract-review 测试用例 schema v1.0.0*
