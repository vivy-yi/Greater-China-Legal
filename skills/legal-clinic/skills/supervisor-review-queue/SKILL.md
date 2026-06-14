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

本 skill 引用以下 plugin 根级 references 与 CLAUDE.md：

- **判断框架**：`../../references/判断框架.md`（4 场景簇路由 + 各场景判断树 + 督导审核 + 升级决策门）
- **数据源清单**：`../../references/数据源清单.md`（[YD]/[WKL]/[GOV]/[BD]/[model] + 法援场景适用 + 隐私保护）
- **查询路径**：`../../references/查询路径.md`（法援法规/案例/案件档案/争议程序/应急检索）
- **CLAUDE.md**：`../../CLAUDE.md`（CN 法律援助体系 + 申请流程）
- **B 重构规范**：`../../../scene-design/README.md`（场景簇定义 + 数据源锚定）
- **货币触发主题**：`../../../references/currency-watch.md`

本 skill 所属场景簇：`legal-clinic`（参见 `../../references/判断框架.md` §一）

⚠️ **法援场景特别提示**：
- 本 skill 输出**必须经督导复核**（除 client-comms-log / ramp 等元数据 skill）
- 当事人陈述标注 `[user]`，事实陈述与法律评价须明确区分
- 案件档案脱敏处理，遵循 `../../references/数据源清单.md` §九
- 关键结论须 2-3 个数据源交叉验证（详见 `../../references/数据源清单.md` §六）

- **时效合理性校验**：`../../references/plausibility-bands/cn-mainland.md`（deadlines skill 录入时自动触发）

升级条件详见 `../../references/判断框架.md` §六。

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
