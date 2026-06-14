---
target: skills/review-proposals/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["合同", "违约责任", "风险"]
  - no_placeholder: true
  - starts_with_header: true
expected:
  - section: "风险等级"
    type: must
  - section: "修改建议"
    type: should
trigger_phrases:
  - 自测
  - 功能测试
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---

# 合同审查方案自测

**测试场景：** 用户提交一份供应商框架合作协议，要求 AI 基于 review-proposals 技能输出审查方案。验证 skill 是否正确识别合同类型、提取关键条款风险、按风险等级分类并给出修改建议。重点检查是否包含"工作流程"章节、风险等级评定逻辑、以及合同违约责任的条文引用。
