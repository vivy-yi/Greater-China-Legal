---
name: supervisor-review-queue
description: >
  提交督导复核的案件队列管理（C1+C4（需督导审核））。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: legal-clinic
last_reviewed: 2026-06
version: 2.0.0
risk_level: medium
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /supervisor-review-queue — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 提交督导复核的案件队列管理

**所属场景：** C1+C4（需督导审核）

## 二、判断树

**Node 1：** 案件复杂程度？
  - 简单：自查；中等：1审；复杂：2审+

**Node 2：** 风险等级？
  - 低/中/高

**Node 3：** 时效紧迫？
  - 普通/紧急/特急
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 劳动案件 | 经济补偿金计算、违法解除认定须复核 |
| 行政案件 | 被告主体、复议前置要件须复核 |
| 刑事援助 | 会见、阅卷、辩护意见须复核 |

## 四、数据源锚定

- **主要数据源：** [BD] 督导审核记录
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
legal-clinic/supervisor-review-queue/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic supervisor-review-queue B-phase v2.0.0（场景优先重构）*
