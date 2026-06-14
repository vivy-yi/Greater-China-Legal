---
name: socratic-drill
description: >
  Socratic 连珠炮追问训练（S3+S4）。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: law-student
last_reviewed: 2026-06
version: 2.0.0
risk_level: low
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /socratic-drill — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** Socratic 连珠炮追问训练

**所属场景：** S3+S4

## 二、判断树

**Node 1：** 主题？
  - 民法/刑法/宪法/行政

**Node 2：** 追问深度？
  - 2层/3层/5层

**Node 3：** 学生反应？
  - 能答/卡住/答错
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| JD 课堂 | 教授主导 Socratic，类似 1L 训练 |
| 传统课堂 | 教师提问为主 |

## 四、数据源锚定

- **主要数据源：** [model] 推理
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/socratic-drill/[session-id]/output.md
```

---

*Greater China Legal — law-student socratic-drill B-phase v2.0.0（场景优先重构）*
