---
name: exam-forecast
description: >
  法考重难点预测（S1）。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: law-student
last_reviewed: 2026-06
version: 2.0.0
risk_level: low
---

# /exam-forecast — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 法考重难点预测

**所属场景：** S1

## 二、判断树

**Node 1：** 距考试时间？
  - 6月/3月/1月/2周

**Node 2：** 学科范围？
  - 民法/刑法/民诉等 8 科

**Node 3：** 学生基础？
  - 零基础/有基础/强化阶段
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 客观题 | 覆盖广，重点在高频考点 |
| 主观题 | 重点在民法/刑法/民诉/刑诉 |

## 四、数据源锚定

- **主要数据源：** [YD] 历年考点统计 / [model] 趋势推理
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/exam-forecast/[session-id]/output.md
```

---

*Greater China Legal — law-student exam-forecast B-phase v2.0.0（场景优先重构）*
