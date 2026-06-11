---
name: is-this-a-problem
description: >
  快速识别产品功能是否构成法律风险——CN消费者保护/个人信息/广告合规。
  适用情形：产品团队问"这个功能有没有法律问题"。
argument-hint: "[功能描述或问题]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

# /is-this-a-problem — China Mainland

## CN产品法律风险快速识别

### 快速判断流程

```
1. 是否收集个人信息？
   → 是：须符合PIPL（告知/同意/最小化）
   → 否：继续下一步

2. 是否涉及消费者权益？
   → 是：须符合消费者权益保护法
   → 否：继续下一步

3. 是否涉及广告宣传？
   → 是：须符合广告法（虚假宣传/绝对化用语）
   → 否：继续下一步

4. 是否涉及合同条款？
   → 是：须符合民法典合同编
   → 否：低风险
```

---

## 快速评估输出

```
## 快速法律风险识别 — [功能]

### 风险判断
🔴 明确违法 / 🟠 可能有风险 / 🟡 须进一步评估 / 🟢 无明显风险

### 涉及法规
[相关法规]

### 建议
[是否须launch review或feature risk assessment]
```

---

*Greater China Legal — product-legal is-this-a-problem CN adapter v1.0.0*