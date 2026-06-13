---
name: brief-section-drafter
description: '按内部风格起草法律文书章节——每个事实须有引用，每个案例须核实。 适用情形：用户要求起草"事实陈述"、"论证第二节"等文书章节。

  '
argument-hint: '[章节名称 — 如''statement of facts''/''argument II'']'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
- 法律文书
- 代理词
legal_sources:
- name: 中华人民共和国民法典
  effective_date: '2021-01-01'
---

# /brief-section-drafter — China Mainland

## CN法律文书格式

### 民事起诉书格式

**须包含：**
1. 标题（法院名称+案件类型）
2. 当事人信息（原告/被告）
3. 诉讼请求
4. 事实与理由
5. 证据和证据来源
6. 尾部（起诉人签名/盖章+日期）

---

### CN答辩状格式

**须包含：**
1. 标题（法院名称+案号）
2. 当事人信息
3. 答辩请求和事实理由
4. 证据
5. 尾部

---

## CN法律文书写作要点

**事实陈述：**
- 每个事实须有证据支持（合同/邮件/付款记录/证人）
- 按时间顺序组织
- 区分已证实事实与推测

**法律论证：**
- 每项法律主张须有法条支持（《民法典》条款）
- 引用权威案例（指导性案例/公报案例）
- 预判对方反驳并回应

**引用格式（CN）：**
- 法律：《民法典》第XXX条
- 司法解释：《最高人民法院关于适用〈民法典〉合同编的解释（一）》第X条
- 案例：（2021）最高法民终XXX号

---

## 输出格式

```
## [文书章节] — [案件名称]

### 章节内容
[完整章节内容]

### 须核实项
⚠️ [事实/引用] — 须核实 — [建议核实方式]
```

---

*Greater China Legal — litigation-legal brief-section-drafter CN adapter v1.0.0*