---
name: status
description: >
  案件当前状态更新（通用（案件状态））。
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

# /status — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 案件当前状态更新

**所属场景：** 通用（案件状态）

## 二、判断树

**Node 1：** 案件阶段？
  - 受理/研究/调解/立案/审理/执行

**Node 2：** 下一步？
  - 等待/主动/待审核

**Node 3：** 时间节点？
  - 立案前/审限中/上诉期/执行期
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 民事 | 6个月/9个月审限 |
| 劳动仲裁 | 45 日+15 日 |
| 行政 | 3 个月/6 个月 |

## 四、数据源锚定

- **主要数据源：** [BD] 案件状态日志
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
legal-clinic/status/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic status B-phase v2.0.0（场景优先重构）*
