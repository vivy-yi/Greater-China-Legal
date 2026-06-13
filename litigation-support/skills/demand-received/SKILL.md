---
name: demand-received
description: >
  分类收到的律师函——提取字段、检查案件组合、评估价值、提出应对建议。
  适用情形：用户说"收到律师函"、"评估这个demand"。
argument-hint: "[path-to-incoming] [--slug=custom-slug]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# /demand-received — China Mainland

## CN收到的律师函处理流程

### Step 1：提取律师函内容

- 发送方信息
- 核心诉求（金额/行为要求）
- 事实陈述
- 法律依据
- 截止日期

### Step 2：交叉检查案件组合

检查 `_log.yaml` 中是否已有相关案件。

### Step 3：评估价值

| 风险等级 | 标准 |
|---|---|
| 🔴 高风险 | 金额大、涉及核心业务、有诉讼威胁 |
| 🟠 中风险 | 中等金额、法律问题复杂 |
| 🟡 低风险 | 小额、事实清楚、法律问题简单 |

### Step 4：提出选项

**选项A：** 创建案件（→matter-intake预填充）
**选项B：** 发送反律师函（→demand-intake预填充）
**选项C：** 关联到现有案件
**选项D：** 单独处理

---

## CN律师函应对建议框架

**须评估：**
1. 律师函中的事实是否准确？
2. 法律依据是否正确？
3. 诉求是否合理？
4. 时效是否对我方有利？
5. 是否有反诉机会？

---

## 输出

写入 `inbound/[slug]/triage.md`，包含：
- 律师函摘要
- 风险评估
- 应对选项及建议
- 下一步行动

---

*Greater China Legal — litigation-legal demand-received CN adapter v1.0.0*