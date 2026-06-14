---
name: case-brief
description: >
  CN 案例分析报告——要素拆解、判决依据、案例价值（S1+S4）。
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
  - case brief
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /case-brief — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** CN 案例分析报告——要素拆解、判决依据、案例价值

**所属场景：** S1+S4

## 二、判断树

**Node 1：** 案例来源？
  - 最高法指导案例/公报案例/普通案例/地方法院案例

**Node 2：** 效力级别？
  - 指导性 > 公报 > 普通

**Node 3：** 案件类型？
  - 民事/刑事/行政/执行
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 指导案例 | 各级法院应当参照（最高法规定） |
| 公报案例 | 最高法公报，参考价值高 |
| 普通案例 | 事实认定参考，不具备普遍约束力 |

## 四、数据源锚定

- **主要数据源：** [WKL] 中国裁判文书网 / [GOV] 最高法案例库
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/case-brief/[session-id]/output.md
```

---

*Greater China Legal — law-student case-brief B-phase v2.0.0（场景优先重构）*
