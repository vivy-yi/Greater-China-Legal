---
name: matter-workspace
description: >
  管理案件工作区——新建、列出、切换、关闭案件工作区。
  适用于多客户/多项目法务场景，确保一个客户的上下文不会泄露到另一个。
  适用情形：用户说"新建案件"、"切换案件"、"列出我的案件"。
argument-hint: "<new | list | switch | close | none> [slug]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: low
---

# /matter-workspace — China Mainland

## Subcommands

- `/employment-legal:matter-workspace new <slug>` — 创建新案件工作区，运行简短问询，写入 `matter.md`
- `/employment-legal:matter-workspace list` — 列出案件，显示状态和活跃标记
- `/employment-legal:matter-workspace switch <slug>` — 设置活跃案件
- `/employment-legal:matter-workspace close <slug>` — 归档案件（移至 `_archived/`）
- `/employment-legal:matter-workspace none` — 退出案件级上下文，使用实践级配置

## Storage layout

```
employment-legal/
├── CLAUDE.md                       # 实践级配置
└── matters/
    ├── <slug>/
    │   ├── matter.md               # 客户、对手方、案件类型、关键事实
    │   ├── history.md             # 事件、决定、草稿、审查的日期记录
    │   └── notes.md               # 自由格式笔记
    └── _archived/
        └── <slug>/                # 已归档案件
```

## CN案件工作区字段

matter.md 应包含：

```markdown
# 案件：[案件名称]

**客户/公司名称：** [名称]
**对手方（如有）：** [名称]
**案件类型：** [劳动仲裁/合同审查/咨询/其他]
**管辖区域：** [省份/直辖市]
**劳动关系类型：** [解除/招聘/社保/加班费/其他]
**涉及人数：** [N人]
**案件状态：** [进行中/已结案/待处理]

---

## 关键事实

[简要描述案件背景]

## CN特定信息

- 对方当事人：[个人/企业]
- 劳动仲裁委：[城市区劳动人事争议仲裁委员会]
- 涉及金额（如有）：¥[金额]
- 代理律师（如有）：[律所/律师]

## 升级事项

- 当前阶段：[阶段]
- 下一步行动：[事项]
- 截止日期：[日期]
```

## CN仲裁管辖

劳动争议仲裁管辖的一般规则：
- 用人单位注册地或劳动合同履行地的仲裁委
- 涉及多个仲裁委：合同履行地优先

---

## 本技能不做什么

- 不提供法律策略建议。只管理案件上下文。
- 不跨案件读取信息（除非 `Cross-matter context` 开启）。
- 不保证案件信息的完整性。

---

*Greater China Legal — employment-legal matter-workspace CN adapter v1.0.0*