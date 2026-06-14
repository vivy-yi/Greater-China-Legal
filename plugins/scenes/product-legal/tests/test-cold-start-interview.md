---
target: skills/cold-start-interview/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["产品发布", "合规", "风险", "集成", "配置"]
  - no_placeholder: true
expected:
  - section: "输出格式"
    type: must
  - section: "升级决策门"
    type: must
trigger_phrases:
  - 产品发布
  - 营销
  - 合规
  - 风险
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---
