---
name: cold-start-interview
description: >
  识别学生目标与起点（通用）。
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

# /cold-start-interview — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 识别学生目标与起点

**所属场景：** 通用

## 二、判断树

**Node 1：** 你是哪类学生？
  - 本科/学硕/JD/法考备考

**Node 2：** 当前学期？
  - 开学/期中/期末/假期

**Node 3：** 主攻方向？
  - 法考/考研/JD/课程
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 法考 | 9月+10月两个考试节点 |
| 学硕 | 12月统考 |
| JD | 各校自主，时间不统一 |

## 四、数据源锚定

- **主要数据源：** [BD] 学生画像 / [model] 推理
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/cold-start-interview/[session-id]/output.md
```

---

*Greater China Legal — law-student cold-start-interview B-phase v2.0.0（场景优先重构）*
