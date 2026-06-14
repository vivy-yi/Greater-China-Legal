---
name: customize
description: >
  根据学生偏好调整输出（通用）。
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
  - customize
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /customize — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 根据学生偏好调整输出

**所属场景：** 通用

## 二、判断树

**Node 1：** 输出语言？
  - 中文/中英对照

**Node 2：** 详细程度？
  - 极简/标准/详细

**Node 3：** 案例偏好？
  - 真实案例/虚构案例/混合
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 法考主观题 | 必须中文案例分析 |
| JD | 需要英文案例对照 |

## 四、数据源锚定

- **主要数据源：** [BD] 学生偏好
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/customize/[session-id]/output.md
```

---

*Greater China Legal — law-student customize B-phase v2.0.0（场景优先重构）*
