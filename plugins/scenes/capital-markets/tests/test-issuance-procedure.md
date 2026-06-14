---
target: skills/issuance-procedure-advisor/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["债券", "发行", "证监会", "注册制", "审核"]
  - no_placeholder: true
expected:
  - section: "输出格式"
    type: must
  - section: "升级决策门"
    type: must
trigger_phrases:
  - 资本市场
  - IPO
  - 发债
  - issuance procedure
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---
