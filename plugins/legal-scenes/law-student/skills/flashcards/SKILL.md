---
name: flashcards
description: >
  Anki/抽认卡生成（S1+S2）。
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
  - flashcards
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /flashcards — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** Anki/抽认卡生成

**所属场景：** S1+S2

## 二、判断树

**Node 1：** 记忆类型？
  - 法条/概念/案例/流程

**Node 2：** 遗忘曲线？
  - 新卡/复习卡/困难卡
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 民法典 | 1260 条，分编记忆 |
| 刑法 | 452 条，重点在分则 |

## 四、数据源锚定

- **主要数据源：** [BD] 学生记忆库 / [YD] 法条原文
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/flashcards/[session-id]/output.md
```

---

*Greater China Legal — law-student flashcards B-phase v2.0.0（场景优先重构）*
