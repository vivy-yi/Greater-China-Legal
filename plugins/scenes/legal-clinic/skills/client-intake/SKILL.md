---
name: client-intake
description: >
  CN 法律援助申请接收——资格审核、案件分流（C1+C2+C3+C4（通用接待））。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: legal-clinic
last_reviewed: 2026-06
version: 2.0.0
risk_level: medium
trigger_phrases:
  - 法律诊所
  - 法援
  - client
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /client-intake — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** CN 法律援助申请接收——资格审核、案件分流

**所属场景：** C1+C2+C3+C4（通用接待）

## 二、判断树

**Node 1：** 申请人是否符合法援条件？
  - 经济困难标准：按各省市最低生活保障 1.5-2 倍认定

**Node 2：** 案件类型？
  - 劳动争议/消费者维权/婚姻家事/行政诉讼 → 分流到对应场景

**Node 3：** 是否涉及特殊群体？
  - 残疾人/老年人/妇女/儿童/农民工/死刑/未成年被告
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 刑事案件 | 可能判处死刑/无期/未成年犯罪，公设辩护全覆盖 |
| 民事/行政 | 经济困难+案件类型匹配 |
| 特殊群体 | 免审查经济困难（盲聋哑/未成年人等） |

## 四、数据源锚定

- **主要数据源：** [GOV] 司法部法援规定 / [WKL] 各地法援实施办法
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
legal-clinic/client-intake/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic client-intake B-phase v2.0.0（场景优先重构）*
