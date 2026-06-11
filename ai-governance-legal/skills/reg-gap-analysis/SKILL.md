---
name: reg-gap-analysis
description: >
  分析AI系统与CN监管要求之间的差距——识别合规缺口和补救建议。
  适用情形：算法备案前或安全评估前的自查。
argument-hint: "[AI系统名称或描述]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# /reg-gap-analysis — China Mainland

## CN AI合规差距分析框架

### Step 1：确认系统类型和监管要求

**算法推荐系统须满足：**
- 算法备案（省级网信办）
- 算法透明度说明
- 用户权利保障机制

**生成式AI服务须满足：**
- 安全评估（国家级）
- 算法备案（按模型规模）
- 数据标注合规

---

### Step 2：对照内部现状

- 备案状态
- 安全评估状态
- 政策文件是否齐全
- 技术措施是否到位

---

### Step 3：输出差距分析

```
## AI合规差距分析 — [系统名称]

### 🔴 重大缺口（影响备案/安全评估）
[GAP-ID] [要求] — [现状] — [补救建议]

### 🟠 中等缺口（须改进）
[GAP-ID] [要求] — [现状] — [补救建议]

### ✅ 已满足
[要求] — [现状]
```

---

*Greater China Legal — ai-governance-legal reg-gap-analysis CN adapter v1.0.0*