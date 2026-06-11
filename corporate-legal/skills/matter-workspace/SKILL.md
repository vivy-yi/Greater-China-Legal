---
name: matter-workspace
description: >
  管理公司法务案件工作区——新建、列出、切换、关闭公司治理案件。
  适用情形：用户说"新建公司案件"、"切换案件"、"列出治理案件"。
argument-hint: "<new | list | switch | close | none> [slug]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: low
---

# /matter-workspace — China Mainland

## Subcommands

- `/corporate-legal:matter-workspace new <slug>` — 创建新案件工作区
- `/corporate-legal:matter-workspace list` — 列出案件
- `/corporate-legal:matter-workspace switch <slug>` — 切换活跃案件
- `/corporate-legal:matter-workspace close <slug>` — 归档案件
- `/corporate-legal:matter-workspace none` — 退出案件级上下文

## CN公司治理案件字段

matter.md 应包含：

```markdown
# 公司治理案件：[案件名称]

**案件类型：**
□ 股权转让/并购
□ 注册资本变更
□ 董事会/监事会改选
□ 章程修改
□ 对外担保
□ 合并、分立、解散
□ 合规整改
□ 工商变更登记
□ 其他

**涉及公司：** [公司全称]
**统一社会信用代码：** [代码]

---

## CN案件特殊信息

- 须股东会决议：[是/否] — [决议类型]
- 须董事会决议：[是/否]
- 须工商变更登记：[是/否]
- 须政府审批（如有）：[审批机关]
- 涉及国有资产：[是/否]
- 涉及外商投资：[是/否]

## 合规时间线

| 事项 | 截止日期 | 状态 |
|---|---|---|
| [事项] | [日期] | 待处理/已完成 |

## 升级事项

- 当前阶段：[阶段]
- 下一步行动：[事项]
- 截止日期：[日期]
```

---

*Greater China Legal — corporate-legal matter-workspace CN adapter v1.0.0*