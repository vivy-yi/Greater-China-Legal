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

## 数据源与判断框架引用

本 skill 引用以下 plugin 根级 references 与 CLAUDE.md：

- **判断框架**：`../../references/判断框架.md`（4 场景簇路由 + 考试判断节点 + 学习阶段 + IRAC 案例分析）
- **数据源清单**：`../../references/数据源清单.md`（[YD]/[WKL]/[GOV]/[BD]/[model] + 学习场景适用）
- **查询路径**：`../../references/查询路径.md`（法条/案例/真题/教材/英美判例检索入口）
- **CLAUDE.md**：`../../CLAUDE.md`（CN 法学体系 + 考试类型基础信息）
- **B 重构规范**：`../../../scene-design/README.md`（场景簇定义 + 数据源锚定规范）
- **货币触发主题**：`../../../references/currency-watch.md`（高频更新主题清单）

来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）详见 `../../references/数据源清单.md` §七。

本 skill 所属场景簇：`law-student`（参见 `../../references/判断框架.md` §一）

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
