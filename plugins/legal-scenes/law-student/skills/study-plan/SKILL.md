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
trigger_phrases:
  - 法考
  - 学习
  - 案例
  - study plan
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

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
