---
name: matter-workspace
description: >
  管理商业合同案件工作区——新建、列出、切换、关闭案件工作区。
  适用情形：用户说"新建合同案件"、"切换案件"、"列出我的合同案件"。
argument-hint: "<new | list | switch | close | none> [slug]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: low
---

# /matter-workspace — China Mainland

## Subcommands

- `/commercial-legal:matter-workspace new <slug>` — 创建新案件工作区
- `/commercial-legal:matter-workspace list` — 列出案件
- `/commercial-legal:matter-workspace switch <slug>` — 切换活跃案件
- `/commercial-legal:matter-workspace close <slug>` — 归档案件
- `/commercial-legal:matter-workspace none` — 退出案件级上下文

## Storage layout

```
commercial-legal/
├── CLAUDE.md
└── matters/
    ├── <slug>/
    │   ├── matter.md
    │   ├── history.md
    │   └── notes.md
    └── _archived/
```

## CN合同案件字段

matter.md 应包含：

```markdown
# 合同案件：[案件名称]

**合同类型：** [NDA/采购合同/销售合同/SaaS协议/租赁合同/其他]
**我方角色：** □ 销售端（我方卖）  □ 采购端（我方买）
**对手方：** [公司名称]
**签约主体：** [我方公司全称]
**合同金额（如有）：** ¥[金额]
**合同语言：** □ 中文  □ 英文  □ 中英文

---

## 关键事实

[合同背景、特殊条款]

## CN特殊信息

- 适用法律：中国法律
- 争议解决：[仲裁/诉讼] — [机构名称]
- 合同签署地：[城市]
- 涉及监管审批：[是/否] — [审批类型]

## 升级事项

- 当前阶段：[谈判/审查中/待签署/已签署]
- 关键条款争议：[条款描述]
- 下一步行动：[事项]
```

## CN争议解决机构参考

| 机构 | 适用场景 |
|---|---|
| 上海国际经济贸易仲裁委员会（SIETAC）| 涉外合同 |
| 中国国际经济贸易仲裁委员会（CIETAC）| 重大商事争议 |
| 北京仲裁委员会（BAC/BIAC）| 一般商事合同 |
| 上海仲裁委员会（SHAC）| 一般合同 |
| 各省市中级人民法院 | 诉讼 |

---

*Greater China Legal — commercial-legal matter-workspace CN adapter v1.0.0*