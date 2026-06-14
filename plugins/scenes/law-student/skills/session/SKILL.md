---
name: session
description: >
  单次学习时间管理（S2+S4）。
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

# /session — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 单次学习时间管理

**所属场景：** S2+S4

## 二、判断树

**Node 1：** 学习时长？
  - 30分/1小时/2小时/半日

**Node 2：** 学习目标？
  - 新学/复习/刷题/模拟

**Node 3：** 干扰程度？
  - 高/中/低
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 番茄工作法 | 25+5 节奏 |
| 深度学习 | 90 分钟一个 cycle |

## 四、数据源锚定

- **主要数据源：** [BD] 学生学习日志
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/session/[session-id]/output.md
```

---

*Greater China Legal — law-student session B-phase v2.0.0（场景优先重构）*
