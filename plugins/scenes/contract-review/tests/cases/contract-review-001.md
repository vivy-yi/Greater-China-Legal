---
case_id: contract-review-001
scene: contract-review
difficulty: standard
created_at: 2026-06-18
created_by: mock-dry-run

# ===== 输入 =====
input:
  type: contract-clause
  content: |
    第四条 违约责任
    4.1 任何一方未按约定履行本合同的，应向守约方支付违约金，
        违约金比例为合同总金额的50%。
    4.2 守约方有权要求违约方继续履行、采取补救措施或赔偿损失。
  user_query: "请审查这段付款条款，对方要求违约金50%，合理吗？"

# ===== 法律事实 =====
expected_facts:
  parties: ["甲方", "乙方"]
  contract_type: "服务合同（推定）"
  amount: "未在条款中明确"
  penalty_clause: "违约金 50% 合同总金额"
  governing_law: "未在条款中明确"

# ===== 期望输出特征 =====
expected_output:
  must_contain_laws:
    - "民法典 585"      # 违约金一般规定
    - "民法典 584"      # 违约责任一般规定
  must_flag_risks:
    - "违约金过高"       # 50% 通常被认为过高
  must_have_sections:
    - "## 风险等级"
    - "## 修改建议"
  must_contain_advice:
    - "130%"             # 应提示法院调整阈值为实际损失的130%
  must_not_contain:
    - "建议删除该条款"
    - "50% 违约金完全合理"

# ===== 评估维度 =====
evaluation_dimensions:
  - law_citation_accuracy
  - risk_coverage
  - advice_soundness
  - format_compliance

# ===== 测试元数据 =====
priority: high
tags: ["违约金", "过高风险", "标准服务合同", "dry-run"]

# ===== 来源标注 =====
provenance:
  source: "mock-dry-run"
  anonymization: "完全虚构，仅用于验证 evolution 闭环流转"
  reviewer: "N/A"
  reviewed_at: 2026-06-18
---

# Contract Review 001 — 违约金过高风险识别（mock）

## 测试背景

本测试用例为 evolution 闭环 dry-run 专用。
故意设计一个"易挂"场景：用户问"违约金 50% 是否合理"——
- 期望 skill 引用民法典 585 条 + 130% 阈值
- 若 skill 触发词覆盖不全或 SKILL.md 未引导到违约金专项检查 → 评估挂
- 此用例的失败恰好是 evolution REFL 阶段的典型输入

## 输入详情

合同片段：违约金条款（50% 比例）
用户 query：询问该违约金是否合理

## 期望分析路径

1. legal-element-extraction：识别违约金条款、比例、缺失的金额/法律
2. legal-norm-validity-check：验证民法典 585 条当前有效（2021-01-01 生效）
3. deductive-reasoning：50% 违约金 → 是否过高 → 民法典 585 + 司法解释 65
4. legal-risk-assessment：风险等级 MEDIUM-HIGH（视金额而定）
5. argument-strength-evaluation：标注论证强度
6. 输出：必须含 "## 风险等级"、"## 修改建议"、"130%"、"民法典 585"

## 评分说明

- **must_contain_laws**：民法典 585 是违约金问题的核心法条，缺此 = 评估 FAIL
- **must_flag_risks**：50% 比例本身即过高信号
- **must_contain_advice**：必须提示 130% 调整阈值（场景 CLAUDE.md 规则）
- **must_not_contain**：禁止"完全合理"等错误判断

---

*contract-review mock test case 001 — dry-run 专用*
