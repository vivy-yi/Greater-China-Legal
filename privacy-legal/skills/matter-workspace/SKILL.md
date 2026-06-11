---
name: matter-workspace
description: >
  管理数据保护案件工作区——新建、列出、切换、关闭隐私合规案件。
  适用情形：用户说"新建隐私案件"、"切换案件"、"列出数据合规案件"。
argument-hint: "<new | list | switch | close | none> [slug]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: low
---

# /matter-workspace — China Mainland

## Subcommands

- `/privacy-legal:matter-workspace new <slug>` — 创建新案件工作区
- `/privacy-legal:matter-workspace list` — 列出案件
- `/privacy-legal:matter-workspace switch <slug>` — 切换活跃案件
- `/privacy-legal:matter-workspace close <slug>` — 归档案件
- `/privacy-legal:matter-workspace none` — 退出案件级上下文

## CN数据保护案件字段

matter.md 应包含：

```markdown
# 隐私合规案件：[案件名称]

**案件类型：**
□ 数据泄露/安全事件
□ 个人信息主体权利请求（DSAR）
□ PII合规差距评估
□ 隐私政策审查/更新
□ 个人信息保护影响评估（PIIA）
□ 合同审查（数据处理协议）
□ 监管问询/调查
□ 其他

**涉及数据类型：**
[列表]

**涉及数据主体数量：**
[估计人数]

**管辖机关（如有）：**
[网信办/工信部/其他]

---

## CN案件特殊信息

- PIPL依据条款：[条款]
- 是否须向网信办报告：[是/否/待确认]
- 是否须通知受影响个人：[是/否]
- 报告截止日期：[日期]（数据泄露72小时内）
- PIIA完成日期：[日期]（如适用）

## 升级事项

- 当前阶段：[阶段]
- 下一步行动：[事项]
- 截止日期：[日期]
```

## CN数据泄露时间线

| 时间 | 行动 |
|---|---|
| 发现后立即 | 评估泄露范围和严重程度 |
| 72小时内 | 向网信办报告（如达到报告标准）|
| 立即或合理时间内 | 通知受影响个人（采取必要措施）|

---

*Greater China Legal — privacy-legal matter-workspace CN adapter v1.0.0*