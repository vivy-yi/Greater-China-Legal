---
name: matter-workspace
description: >
  管理监管合规案件工作区——新建、列出、切换、关闭监管合规案件。
  适用情形：用户说"新建监管案件"、"切换案件"、"列出合规案件"。
argument-hint: "<new | list | switch | close | none> [slug]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: low
---

# /matter-workspace — China Mainland

## Subcommands

- `/regulatory-legal:matter-workspace new <slug>` — 创建新案件工作区
- `/regulatory-legal:matter-workspace list` — 列出案件
- `/regulatory-legal:matter-workspace switch <slug>` — 切换活跃案件
- `/regulatory-legal:matter-workspace close <slug>` — 归档案件
- `/regulatory-legal:matter-workspace none` — 退出案件级上下文

## CN监管合规案件字段

matter.md 应包含：

```markdown
# 监管合规案件：[案件名称]

**案件类型：**
□ 监管政策变化跟进
□ 合规差距评估
□ 内部政策修订
□ 监管问询/调查应对
□ 行政处罚应对
□ 其他

**涉及监管领域：** [列表]
**涉及业务线：** [列表]
**管辖机关：** [机关名称]

---

## CN案件特殊信息

- 法规依据：[具体法规条文]
- 整改要求：[描述]
- 报告截止日期：[日期]
- 是否须向监管机关提交材料：[是/否]

## 合规整改时间线

| 事项 | 截止日期 | 状态 |
|---|---|---|
| [事项] | [日期] | [待处理/已完成] |

## 升级事项

- 当前阶段：[阶段]
- 下一步行动：[事项]
- 截止日期：[日期]
```

---

*Greater China Legal — regulatory-legal matter-workspace CN adapter v1.0.0*