---
target: skills/online-loan-compliance/SKILL.md
type: functional
priority: medium
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["互联网金融", "合规", "监管", "资质", "违规"]
  - no_placeholder: false
expected:
  - section: "输出格式"
    type: must
  - section: "升级决策门"
    type: must
trigger_phrases:
  - online-loan-compliance
  - internet_finance
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---
