---
name: feature-risk-assessment
description: >
  单一功能或产品领域的深度风险评估——当launch review发现须深入分析的问题时使用。
  适用情形：用户说"深入评估这个风险"、"风险评估[功能]"。
argument-hint: "[功能名称或描述]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
  - '评估'
  - '产品发布'
  - '营销'
  - '合规'
  - '风险'
---

# /feature-risk-assessment — China Mainland

## CN产品功能风险评估框架

### 1. 功能概述

- 功能名称：
- 功能描述：
- 新特点：
- 为什么被escalate：

---

### 2. 风险分析

**可能出错的地方：**
- 功能设计缺陷
- 用户误用
- 数据泄露
- 违反法规

**可能性评估：**
- 高 / 中 / 低

**影响程度：**
- 严重 / 中等 / 轻微

---

### 3. CN法规对照

| 法规 | 相关条款 | 是否适用 |
|---|---|---|
| 个人信息保护法 | 第XX条 | 是/否 |
| 消费者权益保护法 | 第XX条 | 是/否 |
| 广告法 | 第XX条 | 是/否 |
| 电子商务法 | 第XX条 | 是/否 |

---

### 4. 缓解措施

- 技术缓解
- 产品缓解
- 法律缓解

---

### 5. 建议行动

- [ ] 立即停止（风险不可接受）
- [ ] 修改后上线（须满足条件）
- [ ] 继续监控（可接受风险）

---

## 输出格式

```
## 产品功能风险评估 — [功能名称]

### 风险摘要
[高/中/低风险]

### 风险矩阵
[可能性 vs 影响]

### 建议行动
[上述行动]
```

---

*Greater China Legal — product-legal feature-risk-assessment CN adapter v1.0.0*