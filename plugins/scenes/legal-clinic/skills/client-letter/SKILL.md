---
name: client-letter
description: >
  给当事人的信件——进度更新/法律意见（C2+C3+C4（当事人信函））。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: legal-clinic
last_reviewed: 2026-06
version: 2.0.0
risk_level: medium
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /client-letter — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 给当事人的信件——进度更新/法律意见

**所属场景：** C2+C3+C4（当事人信函）

## 二、判断树

**Node 1：** 信件类型？
  - 受理通知/进度更新/法律意见/结案报告

**Node 2：** 当事人理解力？
  - 需要通俗化

**Node 3：** 敏感度？
  - 避免诱导、避免承诺
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| C2 消保 | 小额诉讼、调解优先 |
| C3 家事 | 避免刺激性语言、保护未成年人 |
| C4 行政 | 不评价政府行为、聚焦事实 |

## 四、数据源锚定

- **主要数据源：** [model] 信函模板
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，必须升级至督导/专业律师：
- 涉及具体案件的法律意见
- 案件复杂程度超过学生能力（须督导介入）
- 时效紧迫或金额重大
- 刑事案件会见/阅卷/辩护意见
- 行政诉讼复议前置/被告主体认定
- 跨学科/跨法域问题

## 六、输出路径

```
legal-clinic/client-letter/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic client-letter B-phase v2.0.0（场景优先重构）*
