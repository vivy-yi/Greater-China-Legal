---
name: cold-call-prep
description: >
  Socratic 课堂 cold call 准备（S3+S4）。
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

# /cold-call-prep — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** Socratic 课堂 cold call 准备

**所属场景：** S3+S4

## 二、判断树

**Node 1：** 案例篇幅？
  - 短案（5页内）/长案（10页+）

**Node 2：** 涉及学科？
  - 宪法/民法/刑法/行政

**Node 3：** 学生水平？
  - 本科一年级/高年级/JD
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| JD 试点院校 | 案例教学为主，类似美国法学院 |
| 传统法学本科 | 以讲授为主，cold call 较少 |

## 四、数据源锚定

- **主要数据源：** [model] 案例推理 / [WKL] 真实案例
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/cold-call-prep/[session-id]/output.md
```

---

*Greater China Legal — law-student cold-call-prep B-phase v2.0.0（场景优先重构）*
