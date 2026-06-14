---
name: build-guide
description: >
  行政诉讼入门指引——复议前置/被告主体（C4（行政诉讼））。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: legal-clinic
last_reviewed: 2026-06
version: 2.0.0
risk_level: medium
---

# /build-guide — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 行政诉讼入门指引——复议前置/被告主体

**所属场景：** C4（行政诉讼）

## 二、判断树

**Node 1：** 是否复议前置？
  - 自然资源权属/纳税/工伤认定等须先复议

**Node 2：** 被告主体？
  - 作出具体行政行为的行政机关

**Node 3：** 诉讼请求？
  - 撤销/确认违法/变更/赔偿
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 复议前置 | 复议机关逾期不决定 → 起诉复议机关 |
| 自由选择 | 可复议可诉讼 |
| 诉讼时效 | 知道作出行为之日起 6 个月 |

## 四、数据源锚定

- **主要数据源：** [GOV] 行政诉讼法 / [WKL] 行政诉讼案例
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，必须升级至督导/专业律师：
- 涉及具体案件的法律意见
- 案件复杂程度超过学生能力（须督导介入）
- 时效紧迫或金额重大
- 刑事案件会见/阅卷/辩护意见
- 行政诉讼复议前置/被告主体认定
- 跨学科/跨法域问题

## 六、输出路径

```
legal-clinic/build-guide/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic build-guide B-phase v2.0.0（场景优先重构）*
