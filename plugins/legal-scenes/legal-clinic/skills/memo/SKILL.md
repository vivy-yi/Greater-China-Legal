---
name: memo
description: >
  案件备忘录——事实/法律/策略三层（C1+C3+C4（备忘录））。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: legal-clinic
last_reviewed: 2026-06
version: 2.0.0
risk_level: medium
trigger_phrases:
  - 法律诊所
  - 法援
  - memo
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /memo — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 案件备忘录——事实/法律/策略三层

**所属场景：** C1+C3+C4（备忘录）

## 二、判断树

**Node 1：** 案件阶段？
  - 受理/研究/调解/起诉/审理

**Node 2：** 对象？
  - 内部督导/当事人/法院

**Node 3：** 详细程度？
  - 1页简报/3页标准/10页详尽
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 给督导 | 结构化、问题清单、风险标注 |
| 给当事人 | 通俗易懂、避免法律术语 |
| 给法院 | 规范格式、引用法条 |

## 四、数据源锚定

- **主要数据源：** [BD] 内部备忘录 / [WKL] 同类胜诉案例
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
legal-clinic/memo/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic memo B-phase v2.0.0（场景优先重构）*
