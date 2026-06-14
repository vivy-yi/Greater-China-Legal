---
name: study-plan
description: >
  长期/中期/短期学习计划（S1+S2）。
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

# /study-plan — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 长期/中期/短期学习计划

**所属场景：** S1+S2

## 二、判断树

**Node 1：** 目标考试？
  - 法考/学硕/JD/期末

**Node 2：** 距考试？
  - 12月+/6月/3月/1月

**Node 3：** 每日可用时间？
  - 2h/4h/8h/全职
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 法考客观题 | 6-9月三轮复习 |
| 学硕 | 12月统考前3-6个月冲刺 |
| JD | 各校培养方案不同 |

## 四、数据源锚定

- **主要数据源：** [BD] 学生进度 / [model] 计划生成
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/study-plan/[session-id]/output.md
```

---

*Greater China Legal — law-student study-plan B-phase v2.0.0（场景优先重构）*
