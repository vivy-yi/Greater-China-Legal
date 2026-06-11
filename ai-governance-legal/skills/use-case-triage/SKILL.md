---
name: use-case-triage
description: >
  AI用例triage——快速评估新AI功能的监管分类和风险等级。
  适用情形：产品团队询问"这个AI功能要不要做合规评估"。
argument-hint: "[描述AI用例]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

# /use-case-triage — China Mainland

## CN AI用例快速评估

### 判断流程

```
1. 是否处理个人信息？
   → 是：须PIPL评估
   → 否：继续下一步

2. 是否属于算法推荐？
   → 是：须CAC备案
   → 否：继续下一步

3. 是否属于深度合成？
   → 是：须CAC备案 + 安全评估
   → 否：继续下一步

4. 是否属于生成式AI？
   → 是：须安全评估 + 备案
   → 否：低风险，可能不需要
```

---

## 快速评估输出

```
## AI用例Triage — [用例名称]

### 监管分类
- CAC算法推荐：适用 / 不适用
- 深度合成：适用 / 不适用
- 生成式AI：适用 / 不适用
- PIPL：适用 / 不适用

### 风险等级
🔴 高风险 / 🟠 中风险 / 🟡 低风险

### 建议
[须做AIA / 须做备案 / 可直接上线 / 须进一步评估]
```

---

*Greater China Legal — ai-governance-legal use-case-triage CN adapter v1.0.0*