---
target: skills/privacy-policy-update/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["个人信息", "PIPL", "风险"]
  - no_placeholder: true
  - starts_with_header: true
expected:
  - section: "风险等级"
    type: must
  - section: "合规差距"
    type: should
trigger_phrases:
  - 自测
  - 功能测试
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---

# 隐私政策更新自测

**测试场景：** 用户提交某电商 APP 的现有隐私政策文本，要求 AI 对照 PIPL 最新要求进行合规性审查。验证 skill 是否正确识别隐私政策中缺失的告知事项（如数据存储地点、共享第三方清单、撤回同意途径等），标记不合规条款并给出修改建议。重点检查 PIPL 法条引用的准确性。
