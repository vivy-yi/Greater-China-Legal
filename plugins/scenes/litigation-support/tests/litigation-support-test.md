---
target: skills/portfolio-status/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["诉讼", "时效", "风险"]
  - no_placeholder: true
  - starts_with_header: true
expected:
  - section: "风险等级"
    type: must
  - section: "案件状态"
    type: should
trigger_phrases:
  - 自测
  - 功能测试
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---

# 诉讼案件状态自测

**测试场景：** 用户提供公司当前在办的多个诉讼案件清单（含案号、受理法院、标的金额、当前阶段），要求 AI 输出组合状态报告。验证 skill 是否正确汇总各案进度、识别临近诉讼时效的案件、标记高风险案件并按风险等级排序。重点检查时效计算准确性和风险等级评定。
