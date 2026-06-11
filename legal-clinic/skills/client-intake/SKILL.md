---
name: client-intake
description: >
  CN法律援助申请接收——审核申请人资格、收集案件信息。
  适用情形：接收新的法律援助申请。
argument-hint: "[申请人信息]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

# /client-intake — China Mainland

## CN法律援助申请接收

### Step 1：资格审核

**经济困难认定：**
- 低收入户证明
- 五保户证明
- 失业证明

**特殊群体：**
- 残疾人
- 老年人（60岁以上）
- 妇女
- 儿童

**刑事案件特殊情形：**
- 可能判处死刑
- 可能判处无期徒刑
- 未成年犯罪

---

### Step 2：案件信息

- 案件类型
- 案件事实
- 法律诉求
- 证据材料

---

### Step 3：申请材料

- 法律援助申请表
- 经济困难证明
- 身份证明
- 案件相关材料

---

## 输出

创建 `clients/[id]/intake.md` 和 `clients/_log.yaml` 条目。

---

*Greater China Legal — legal-clinic client-intake CN adapter v1.0.0*