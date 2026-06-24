---
target: skills/siac-procedure-advisor/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["仲裁", "SIAC", "风险"]
  - no_placeholder: true
  - starts_with_header: true
expected:
  - section: "风险等级"
    type: must
  - section: "仲裁程序"
    type: should
trigger_phrases:
  - 自测
  - 功能测试
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---

# SIAC 仲裁程序指引自测

**测试场景：** 用户公司与新加坡客户之间的国际货物买卖合同约定争议由 SIAC（新加坡国际仲裁中心）按其现行仲裁规则仲裁，现发生合同履行纠纷，要求 AI 输出 SIAC 仲裁程序指引。验证 skill 是否正确说明仲裁申请流程、仲裁庭组成方式、临时措施申请路径、证据开示规则及裁决执行（含中国境内承认与执行）。重点检查 SIAC 仲裁规则引用与纽约公约衔接分析。
