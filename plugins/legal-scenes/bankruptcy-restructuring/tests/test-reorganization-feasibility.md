---
target: skills/reorganization-feasibility-checker/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["重整", "清算价值", "营运价值", "破产法", "债权人"]
  - no_placeholder: true
expected:
  - section: "输出格式"
    type: must
  - section: "升级决策门"
    type: must
trigger_phrases:
  - 破产
  - 清算
  - 重整
  - reorganization feasibility
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---
