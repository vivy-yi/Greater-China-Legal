---
name: subpoena-triage
description: >
  传票/调查令triage——评估文件披露要求、豁免权和响应策略。
  适用情形：用户收到法院调查令/传票要求提供文件。
argument-hint: "[path-to-subpoena] [--respond | --challenge]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# /subpoena-triage — China Mainland

## CN司法调查令处理流程

**CN法院调查令：**
- 法院可要求当事人或第三方提供证据
- 须在法定期限内响应
- 拒绝可能构成妨碍诉讼

---

## 评估框架

### 1. 调查令内容
- 要求提供的文件/信息
- 时间范围
- 响应期限

### 2. 豁免权检查
- 是否涉及特权信息
- 是否有保密义务
- 是否有其他豁免理由

### 3. 响应策略

| 选项 | 适用情形 |
|---|---|
| 完全配合 | 无豁免理由 |
| 部分配合 | 部分文件涉及特权 |
| 提出异议 | 有合法豁免理由 |

---

## 输出格式

```
## 调查令评估 — [案件名称]

### 要求
[描述]

### 豁免权评估
- [豁免理由] — [是否适用]

### 建议响应策略
[策略]

### 时间节点
- 响应截止：[日期]（距今N天）
```

---

*Greater China Legal — litigation-legal subpoena-triage CN adapter v1.0.0*