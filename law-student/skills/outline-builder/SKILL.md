---
name: outline-builder
description: >
  学科大纲/知识树构建（S2）。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: law-student
last_reviewed: 2026-06
version: 2.0.0
risk_level: low
---

# /outline-builder — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 学科大纲/知识树构建

**所属场景：** S2

## 二、判断树

**Node 1：** 学科？
  - 8 大部门法任选

**Node 2：** 深度？
  - 概念级/制度级/理论级

**Node 3：** 目标考试？
  - 考研/法考/学术研究
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 学硕 | 侧重理论深度 |
| 法考 | 侧重实务应用 |

## 四、数据源锚定

- **主要数据源：** [YD] 大纲资料 / [model] 框架构建
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/outline-builder/[session-id]/output.md
```

---

*Greater China Legal — law-student outline-builder B-phase v2.0.0（场景优先重构）*
