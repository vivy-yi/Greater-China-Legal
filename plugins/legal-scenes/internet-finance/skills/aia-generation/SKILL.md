---
name: aia-generation
description: 'AI影响评估——结构化分析、CN监管分类、政策一致性diff和建议。 适用情形：用户说"AI影响评估"、"评估这个AI用例"、"生成AIA"。

  '
argument-hint: '[描述AI用例或系统]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
- AI合规
- 评估生成
legal_sources:
- name: 中华人民共和国民法典
  effective_date: '2021-01-01'
---

# /aia-generation — China Mainland

## CN AI影响评估框架

### 1. 基本信息

- **系统名称：**
- **系统功能：**
- **用户类型：**
- **数据输入：**
- **决策影响：**

---

### 2. CN监管分类

**CAC算法推荐规定：**
- 是否属于算法推荐服务？
- 是否须备案？

**生成式AI管理办法：**
- 是否提供生成式AI服务？
- 是否须安全评估？

**个人信息保护法：**
- 是否处理个人信息？
- 是否须做个人信息保护影响评估（PIA）？

---

### 3. 风险评估

| 风险类型 | 等级 | 说明 |
|---|---|---|
| 歧视性算法 | 🔴 | 可能导致不公平对待 |
| 隐私侵犯 | 🟠 | 处理敏感个人信息 |
| 虚假信息 | 🟠 | 生成内容可能被滥用 |
| 安全威胁 | 🟠 | 可能被用于犯罪 |

---

### 4. 建议行动

**立即行动：**
- [ ] 算法备案（如适用）
- [ ] 安全评估（如适用）
- [ ] PIA（如处理个人信息）

**持续监控：**
- CAC执法动态
- 监管政策变化

---

## 输出格式

```
## AI影响评估 — [系统名称]

### 基本信息
[以上信息]

### CN监管分类
- CAC算法推荐：须备案 / 不适用
- 生成式AI：须安全评估 / 不适用
- PIPL：须PIA / 不适用

### 风险评估
[以上表格]

### 建议行动
[以上列表]
```

---

*Greater China Legal — ai-governance-legal aia-generation CN adapter v1.0.0*