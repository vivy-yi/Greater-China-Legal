---
name: cold-start-interview
description: >
  诉讼争议解决实践冷启动向导——了解案件类型、合规状态和程序管理规则。
  适用情形：首次使用、配置缺失 [--redo]、或 [--check-integrations]。
argument-hint: "[--redo | --check-integrations]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: low
---

# /cold-start-interview — China Mainland

## CN诉讼争议解决实践询问

### Part 1：案件类型

> 你处理哪些类型的诉讼/争议？

**CN常见争议类型：**
- 合同纠纷（买卖/租赁/服务/借款）
- 劳动争议（仲裁前置）
- 知识产权纠纷（专利/商标/著作权侵权）
- 公司治理纠纷（股东/董事争议）
- 侵权纠纷（人身/财产）
- 行政争议（行政复议/诉讼）

---

### Part 2：案件管理现状

> 你的案件管理现状？

**CN案件管理成熟度：**
- □ 系统化：使用案件管理系统，完整记录所有案件
- □ 基本跟踪：有案件清单但更新不及时
- □ 手动管理：依赖Excel/纸质记录
- □ 无系统：临时查找

---

### Part 3：CN程序关键节点

**CN诉讼时效（重要！）：**
| 纠纷类型 | 时效 |
|---|---|
| 合同纠纷 | 3年 |
| 侵权纠纷 | 3年（身体伤害1年）|
| 劳动争议 | 60日（仲裁时效）|
| 产品质量 | 2年 |
| 租赁纠纷 | 1年 |

**CN举证责任：**
- 民事诉讼：谁主张谁举证
- 劳动争议：用人单位负主要举证责任（考勤/解除理由等）

---

## Write to CLAUDE.md

```markdown
## 争议类型

**主要类型：** [列表]
**次要类型：** [列表]

## 案件管理成熟度

[系统化/基本跟踪/手动管理/无系统]

## 常用法院/仲裁机构

[列表]

## 程序偏好

- 倾向仲裁还是诉讼：[理由]
- 是否接受调解：[是/否]
```

---

*Greater China Legal — litigation-legal cold-start-interview CN adapter v1.0.0*