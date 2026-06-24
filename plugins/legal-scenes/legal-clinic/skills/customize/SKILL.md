---
name: customize
description: >
  根据诊所偏好调整输出（通用（个性化））。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: legal-clinic
last_reviewed: 2026-06
version: 2.0.0
risk_level: medium
trigger_phrases:
  - 法律诊所
  - 法援
  - customize
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /customize — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 根据诊所偏好调整输出

**所属场景：** 通用（个性化）

## 二、判断树

**Node 1：** 输出语言？
  - 中文/中英对照

**Node 2：** 详细程度？
  - 极简/标准/详细

**Node 3：** 模板偏好？
  - 标准化/个性化
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 当事人对外 | 通俗语言、避免法言法语 |
| 督导对内 | 专业术语、问题清单 |
| 法院对外 | 规范格式、引用法条 |

## 四、数据源锚定

- **主要数据源：** [BD] 律所/诊所偏好
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
legal-clinic/customize/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic customize B-phase v2.0.0（场景优先重构）*
