---
target: skills/related-party-transaction/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["关联交易", "公司法", "风险"]
  - no_placeholder: true
  - starts_with_header: true
expected:
  - section: "风险等级"
    type: must
  - section: "审批程序"
    type: should
trigger_phrases:
  - 自测
  - 功能测试
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---

# 关联交易合规审查自测

**测试场景：** 用户公司拟与控股股东控制的另一家关联公司签署一份年度采购框架协议（预计金额3000万元），要求 AI 进行关联交易合规审查。验证 skill 是否正确识别关联方认定、关联交易公允性判断、董事会/股东会审议程序要求（含关联董事/股东回避表决）、信息披露义务及潜在税务调整风险。重点检查公司法及上市公司关联交易监管规定引用。
