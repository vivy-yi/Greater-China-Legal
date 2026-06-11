---
name: cold-start-interview
description: >
  监管合规实践冷启动向导——了解监管领域范围、合规状态和差距监控规则。
  适用情形：首次使用、配置缺失 [--redo]、或 [--check-integrations]。
argument-hint: "[--redo | --check-integrations]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: low
---

# /cold-start-interview — China Mainland

## CN监管合规实践询问

### Part 1：业务领域与监管范围

> 你的公司受哪些监管领域管辖？

**CN主要监管领域：**
- 互联网/数据（网信办、工信部）
- 电子商务（市场监管总局）
- 反垄断/竞争（市场监管总局）
- 金融（央行/银保监/证监会）
- 医疗健康（卫健委/药监局）
- 教育（教育部）
- 消费品（市场监管总局）
- 广告（市场监管总局）
- 其他：[行业特定监管]

---

### Part 2：当前合规状态

> 你们目前的合规状态？

**CN合规成熟度评估：**
- □ 成熟：已有完整的合规体系，定期审计
- □ 基本合规：有基本政策，正在完善
- □ 初步建立：有框架但执行不足
- □ 空白：刚意识到合规需求

---

### Part 3：重点监管关注

> 哪些监管领域你最担心？

**CN高频执法领域（2023-2025）：**
- App个人信息保护（网信办专项整治）
- 数据安全（CNIPA安全评估）
- 反垄断（市场监管总局罚款案例）
- 消费者权益保护（大数据杀熟、虚假宣传）
- 平台经济（二选一、算法推荐）

---

## Write to CLAUDE.md

```markdown
## 监管领域

**主要领域：** [列表]
**次要领域：** [列表]

## 合规成熟度

[成熟/基本合规/初步建立/空白]

## 重点关注领域

[列表]

## 监控频率

- 高优先级领域：[每月/每周]
- 中优先级领域：[每季度]
- 低优先级领域：[每半年]
```

---

*Greater China Legal — regulatory-legal cold-start-interview CN adapter v1.0.0*