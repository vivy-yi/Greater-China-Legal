---
name: matter-workspace
description: >
  管理知识产权案件工作区——新建、列出、切换、关闭IP争议案件。
  适用情形：用户说"新建IP案件"、"切换案件"、"列出知识产权案件"。
argument-hint: "<new | list | switch | close | none> [slug]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: low
---

# /matter-workspace — China Mainland

## Subcommands

- `/ip-legal:matter-workspace new <slug>` — 创建新案件工作区
- `/ip-legal:matter-workspace list` — 列出案件
- `/ip-legal:matter-workspace switch <slug>` — 切换活跃案件
- `/ip-legal:matter-workspace close <slug>` — 归档案件
- `/ip-legal:matter-workspace none` — 退出案件级上下文

## CN IP案件字段

matter.md 应包含：

```markdown
# IP案件：[案件名称]

**IP类型：** □ 商标  □ 专利  □ 著作权  □ 商业秘密  □ 域名  □ 其他
**案件性质：** □ 侵权 □ 抢注 □ 合同纠纷 □ 无效/撤销 □ 其他
**对方当事人：** [公司/个人]
**涉案IP：** [注册号/名称]
**涉案金额（如有）：** ¥[金额]

---

## CN案件特殊信息

- 管辖机关：[机关名称]
- 程序类型：[行政执法/民事诉讼/刑事报案/仲裁]
- 证据保全方式：[公证/时间戳/诉前保全/其他]
- 是否涉及平台：[是/否] — [平台名称]

## 合规时间线

| 事项 | 截止日期 | 状态 |
|---|---|---|
| [事项] | [日期] | [待处理/已完成] |

## 升级事项

- 当前阶段：[阶段]
- 下一步行动：[事项]
```

---

*Greater China Legal — ip-legal matter-workspace CN adapter v1.0.0*