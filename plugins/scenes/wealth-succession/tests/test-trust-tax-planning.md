---
target: skills/trust-tax-planning-advisor/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["信托", "税务", "遗产", "继承", "受益人"]
  - no_placeholder: true
expected:
  - section: "输出格式"
    type: must
  - section: "升级决策门"
    type: must
trigger_phrases:
  - 信托
  - 税务
  - 顾问
  - 财富传承
  - 遗嘱
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---
