---
name: vendor-ai-review
description: >
  审查第三方AI供应商——供应商AI系统的监管合规状态和风险评估。
  适用情形：采购AI供应商或使用第三方AI API时须评估合规风险。
argument-hint: "[供应商名称或AI产品描述]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# /vendor-ai-review — China Mainland

## CN AI供应商合规审查

### 审查要点

1. **供应商资质**
   - 是否在中国境内注册
   - 是否有ICP许可证（如适用）
   - 是否通过安全评估/备案

2. **数据处理合规**
   - 数据是否出境
   - 个人信息保护措施
   - 数据存储地点

3. **合同条款**
   - 数据处理协议（DPA）
   - 知识产权条款
   - 违约责任

4. **服务稳定性**
   - 服务中断的应急方案
   - 数据备份和恢复

---

## CN AI供应商审查清单

| 检查项 | 说明 | 状态 |
|---|---|---|
| 算法备案 | 供应商AI系统是否已备案 | □ |
| 安全评估 | 供应商是否已完成安全评估 | □ |
| PIPL合规 | 个人信息处理是否符合PIPL | □ |
| 数据出境 | 数据是否出境，须评估安全 | □ |
| DPA | 是否签署数据处理协议 | □ |

---

## 输出格式

```
## AI供应商审查报告 — [供应商名称]

### 基本信息
[供应商信息]

### 合规状态
[上述清单]

### 风险评估
🔴 不可接受 / 🟠 可接受（须改进） / 🟢 可接受

### 建议
[采购建议]
```

---

*Greater China Legal — ai-governance-legal vendor-ai-review CN adapter v1.0.0*