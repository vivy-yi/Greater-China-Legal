---
name: ai-inventory
description: 'CN AI系统清单管理——跟踪算法推荐/深度合成/生成式AI系统的备案状态和风险等级。 适用情形：用户说"ai清单"、"添加AI系统"、"我的系统有哪些"、"CAC备案"。

  '
argument-hint: '[list | add | edit <id> | classify <id> | show <id>]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
- AI清单
- 人工智能
legal_sources:
- name: 中华人民共和国民法典
  effective_date: '2021-01-01'
---

# /ai-inventory — China Mainland

## CN AI System Inventory

### Inventory文件

文件路径：`ai-systems.yaml`

```yaml
systems:
  - id: AI-001
    name: "[系统名称]"
    type: "算法推荐 | 深度合成 | 生成式AI | 自动驾驶 | 人脸识别"
    provider_role: "provider | deployer | importer"
    risk_tier: "prohibited | high-risk | limited | minimal"
    registration_status: "pending | filed | approved | not-required"
    registration_id: ""  # CAC备案号
    security_assessment: "pending | completed | expired"
    last_assessment: YYYY-MM-DD
    last_updated: YYYY-MM-DD
```

---

## CN AI System分类

### 算法推荐系统

**风险等级：** Limited-risk
**须履行义务：**
- 算法备案（省级网信办）
- 算法透明度说明
- 用户权利保障

### 深度合成系统

**风险等级：** High-risk
**须履行义务：**
- 算法备案
- 安全评估
- 标识要求（水印/元数据）

### 生成式AI服务

**风险等级：** High-risk
**须履行义务：**
- 安全评估（国家级）
- 算法备案
- 数据合规（PIPL/DSL）

---

## 输出格式

```
## AI系统清单

| 系统 | 类型 | 风险等级 | 备案状态 | 安全评估 |
|---|---|---|---|---|
| [名称] | [类型] | 🟠高风险 | 已备案 | 有效 |
```

---

*Greater China Legal — ai-governance-legal ai-inventory CN adapter v1.0.0*