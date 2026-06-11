---
name: policy-monitor
description: >
  监控CN AI监管动态——CAC/SAMR/MIIT新规、执法案例、备案要求变化。
  适用情形：用户说"检查AI监管动态"、"有什么新规"、"AI合规更新"。
argument-hint: "[--since DATE]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

# /policy-monitor — China Mainland

## CN AI监管动态监控

### 高优先级来源

| 监管机关 | 关注内容 |
|---|---|
| 国家网信办（CAC）| 算法推荐/深度合成/生成式AI执法 |
| 工业和信息化部（MIIT）| AI产品准入、数据安全 |
| 市场监管总局（SAMR）| AI产品合规、消费者保护 |

### 监控频率

- 高风险系统：每月检查
- 中风险系统：每季度检查
- 低风险系统：每半年检查

---

## 输出格式

```
## AI监管动态报告 — [日期范围]

### 🔴 重大变化
[法规名称] — [发布机关] — [日期]
[简要内容] — [影响]

### 🟠 执法案例
[案例名称] — [机关] — [日期]
[处罚内容] — [教训]

### 🟡 备案更新
[系统名称] — [须做的备案]
```

---

*Greater China Legal — ai-governance-legal policy-monitor CN adapter v1.0.0*