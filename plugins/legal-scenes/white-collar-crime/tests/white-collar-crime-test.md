---
target: skills/recovery-procedure-advisor/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["刑法", "犯罪", "风险"]
  - no_placeholder: true
  - starts_with_header: true
expected:
  - section: "风险等级"
    type: must
  - section: "追缴路径"
    type: should
trigger_phrases:
  - 自测
  - 功能测试
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---

# 涉案资产追缴程序自测

**测试场景：** 用户发现公司财务人员涉嫌挪用资金（涉案金额约500万元）并已向公安机关报案，要求 AI 输出涉案资产追缴程序指引。验证 skill 是否正确识别挪用资金罪的构成要件、刑事追缴与民事追偿的路径选择、涉案财产的保全措施及时效要求。重点检查刑法第272条引用及刑事附带民事诉讼程序分析。
