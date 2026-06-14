---
target: skills/gap-surfacer/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["企业所得税", "税务", "风险"]
  - no_placeholder: true
  - starts_with_header: true
expected:
  - section: "风险等级"
    type: must
  - section: "合规差距"
    type: should
trigger_phrases:
  - 自测
  - 功能测试
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---

# 税务合规差距分析自测

**测试场景：** 用户提交公司上一年度的企业所得税汇算清缴数据和关联交易台账，要求 AI 进行税务合规差距扫描。验证 skill 是否正确识别转让定价文档缺失、发票合规漏洞、税收优惠适用错误、以及跨境交易预提所得税申报遗漏等风险点。重点检查企业所得税法及配套法规引用的准确性。
