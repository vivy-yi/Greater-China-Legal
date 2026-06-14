---
name: irac-practice
description: >
  IRAC 法律分析训练（S1+S4）。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: law-student
last_reviewed: 2026-06
version: 2.0.0
risk_level: low
trigger_phrases:
  - 法考
  - 学习
  - 案例
  - irac practice
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /irac-practice — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** IRAC 法律分析训练

**所属场景：** S1+S4

## 二、判断树

**Node 1：** 案例类型？
  - 民事/刑事/行政

**Node 2：** 争议焦点数量？
  - 单焦点/多焦点

**Node 3：** 是否给出参考答？
  - 先练后看/对照练习
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 法考主观题 | 必须 IRAC 结构 |
| 学硕论述题 | 可以更开放 |

## 四、数据源锚定

- **主要数据源：** [WKL] 案例库 / [model] 推理
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/irac-practice/[session-id]/output.md
```

---

*Greater China Legal — law-student irac-practice B-phase v2.0.0（场景优先重构）*
