---
target: skills/valuation-adjustment-advisor/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["对赌", "九民纪要", "回购", "股权", "估值"]
  - no_placeholder: true
expected:
  - section: "输出格式"
    type: must
  - section: "升级决策门"
    type: must
trigger_phrases:
  - 估值
  - 顾问
  - 私募
  - 基金
  - 投资
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---
