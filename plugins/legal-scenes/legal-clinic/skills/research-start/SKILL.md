---
name: research-start
description: >
  案件法律研究启动——管辖法院、时效、依据（C1+C4（劳动/行政））。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: legal-clinic
last_reviewed: 2026-06
version: 2.0.0
risk_level: medium
trigger_phrases:
  - 法律诊所
  - 法援
  - research start
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /research-start — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 案件法律研究启动——管辖法院、时效、依据

**所属场景：** C1+C4（劳动/行政）

## 二、判断树

**Node 1：** 案件类型？
  - 民事/刑事/行政

**Node 2：** 时效是否紧迫？
  - 60日/3个月/1年/3年/20年

**Node 3：** 管辖法院？
  - 被告住所地/合同履行地/侵权行为地
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 劳动争议 | 仲裁前置，时效 60 日，特殊 1 年 |
| 行政诉讼 | 复议前置 60 日，起诉 6 个月 |
| 民事普通 | 3 年一般时效 |

## 四、数据源锚定

- **主要数据源：** [YD] 法规检索 / [WKL] 同类案例
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
legal-clinic/research-start/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic research-start B-phase v2.0.0（场景优先重构）*
