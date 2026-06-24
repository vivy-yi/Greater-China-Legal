---
target: skills/internal-investigation/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["劳动合同", "解除", "风险"]
  - no_placeholder: true
  - starts_with_header: true
expected:
  - section: "风险等级"
    type: must
  - section: "调查步骤"
    type: should
trigger_phrases:
  - 自测
  - 功能测试
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---

# 内部调查程序自测

**测试场景：** 用户汇报某员工涉嫌严重违反公司制度（如收受供应商回扣），要求 AI 输出内部调查法律操作指引。验证 skill 是否正确识别调查启动条件、规划取证步骤（含电子数据保全、面谈策略）、评估解除劳动合同的法律风险与合规路径。重点检查劳动合同法第39条引用及解除程序合规性分析。
