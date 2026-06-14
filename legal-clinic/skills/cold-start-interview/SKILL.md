---
name: cold-start-interview
description: >
  识别诊所/案件类型（通用（首次使用））。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: legal-clinic
last_reviewed: 2026-06
version: 2.0.0
risk_level: medium
---

# /cold-start-interview — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 识别诊所/案件类型

**所属场景：** 通用（首次使用）

## 二、判断树

**Node 1：** 诊所类型？
  - 高校法律援助中心/律所公益/独立机构

**Node 2：** 主要案件类型？
  - 劳动/消保/家事/行政

**Node 3：** 督导模式？
  - 驻场/定期/随叫随到
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 高校诊所 | 学生办案+督导审核 |
| 律所公益 | 律师主导+学生协助 |
| 独立机构 | 专业团队 |

## 四、数据源锚定

- **主要数据源：** [BD] 诊所档案 / [model] 推理
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
legal-clinic/cold-start-interview/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic cold-start-interview B-phase v2.0.0（场景优先重构）*
