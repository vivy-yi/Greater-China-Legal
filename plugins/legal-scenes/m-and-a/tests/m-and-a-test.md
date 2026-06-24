---
target: skills/post-closing-integration/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["股权", "并购", "风险"]
  - no_placeholder: true
  - starts_with_header: true
expected:
  - section: "风险等级"
    type: must
  - section: "交割清单"
    type: should
trigger_phrases:
  - 自测
  - 功能测试
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---

# 并购交割后整合自测

**测试场景：** 用户完成了一笔目标公司100%股权收购交易（已完成交割），要求 AI 输出交割后整合法律工作清单。验证 skill 是否正确列出股权变更工商登记、公章证照交接、劳动合同承继、知识产权转让登记、供应商客户通知等关键整合事项，并评估未完成事项的法律风险。重点检查公司法及外商投资相关法规引用。
