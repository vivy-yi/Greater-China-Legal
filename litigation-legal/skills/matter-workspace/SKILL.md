---
name: matter-workspace
description: >
  管理诉讼案件工作区——新建、列出、切换、关闭诉讼/仲裁案件。
  适用情形：用户说"新建诉讼案件"、"切换案件"、"列出我的案件"。
argument-hint: "<new | list | switch | close | none> [slug]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: low
---

# /matter-workspace — China Mainland

## Subcommands

- `/litigation-legal:matter-workspace new <slug>` — 创建新案件工作区
- `/litigation-legal:matter-workspace list` — 列出案件
- `/litigation-legal:matter-workspace switch <slug>` — 切换活跃案件
- `/litigation-legal:matter-workspace close <slug>` — 归档案件
- `/litigation-legal:matter-workspace none` — 退出案件级上下文

## CN诉讼案件字段

matter.md 应包含：

```markdown
# 诉讼案件：[案件名称]

**案件类型：** □ 合同纠纷 □ 劳动争议 □ 知识产权 □ 公司治理 □ 侵权 □ 行政
**程序阶段：** □ 协商 □ 仲裁 □ 一审 □ 二审 □ 再审 □ 执行 □ 已结案
**管辖机构：** [法院/仲裁机构名称]
**案号（如有）：** [案号]
**对方当事人：** [公司/个人]
**涉案金额：** ¥[金额]

---

## CN案件特殊信息

- 诉讼时效截止：[日期]（距今N天）
- 代理律师：[律所/律师]
- 是否已保全：[是/否] — [保全类型]
- 关键证据：[描述]

## 程序时间线

| 事项 | 日期 | 状态 |
|---|---|---|
| [事项] | [日期] | [待处理/已完成] |

## 下一步行动

- 当前阶段：[阶段]
- 下一步：[事项]
- 截止日期：[日期]
```

---

*Greater China Legal — litigation-legal matter-workspace CN adapter v1.0.0*