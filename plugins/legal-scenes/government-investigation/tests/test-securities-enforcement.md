---
target: skills/securities-enforcement-response/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["证监会", "调查", "处罚", "证券法", "合规"]
  - no_placeholder: true
expected:
  - section: "输出格式"
    type: must
  - section: "升级决策门"
    type: must
trigger_phrases:
  - 反垄断
  - 内幕交易
  - 信披违规
  - 证监会调查
  - 商业贿赂
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---
