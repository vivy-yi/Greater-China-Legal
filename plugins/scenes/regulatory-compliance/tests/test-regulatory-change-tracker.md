---
target: skills/regulatory-change-tracker/SKILL.md
type: functional
priority: medium
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["监管", "法规", "合规", "追踪", "政策"]
  - no_placeholder: true
expected:
  - section: "输出格式"
    type: must
  - section: "升级决策门"
    type: must
trigger_phrases:
  - 监管
  - 追踪
  - 牌照
  - 安全
  - 合规
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---
