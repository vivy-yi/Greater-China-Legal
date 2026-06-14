---
target: skills/export-license-assessment/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["出口管制", "许可证", "ECCN", "最终用户", "制裁"]
  - no_placeholder: true
expected:
  - section: "输出格式"
    type: must
  - section: "升级决策门"
    type: must
trigger_phrases:
  - 跨境
  - 进出口
  - 海关
  - export license
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---
