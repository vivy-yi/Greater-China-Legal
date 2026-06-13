---
name: portfolio-status
description: '组合状态总览——所有活跃案件的汇总视图，包括风险敞口、即将到来的截止日期。 适用情形：用户要求"查看所有案件状态"或"组合总览"。

  '
argument-hint: '[--all | --filter]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
trigger_phrases:
- 案件状态
- 诉讼组合
legal_sources:
- name: 中华人民共和国民法典
  effective_date: '2021-01-01'
---

# /portfolio-status — China Mainland

## CN案件组合总览格式

### 🔴 高风险案件

| 案件 | 风险等级 | 敞口 | 下一截止 |
|---|---|---|---|
| [slug] | 🔴 | [金额] | [日期] |

### 🟠 中风险案件

| 案件 | 风险等级 | 敞口 | 下一截止 |
|---|---|---|---|
| [slug] | 🟠 | [金额] | [日期] |

### 🟡 低风险案件

| 案件 | 风险等级 | 敞口 | 下一截止 |
|---|---|---|---|
| [slug] | 🟡 | [金额] | [日期] |

### 📅 本周截止

| 日期 | 案件 | 事项 |
|---|---|---|
| [日期] | [slug] | [事项] |

---

## 汇总指标

- **总案件数：**
- **总敞口：**
- **本月预计费用：**

---

*Greater China Legal — litigation-legal portfolio-status CN adapter v1.0.0*