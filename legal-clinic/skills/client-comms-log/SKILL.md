---
name: client-comms-log
description: >
  当事人沟通日志——避免责任风险（通用（沟通记录））。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: legal-clinic
last_reviewed: 2026-06
version: 2.0.0
risk_level: medium
---

# /client-comms-log — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 当事人沟通日志——避免责任风险

**所属场景：** 通用（沟通记录）

## 二、判断树

**Node 1：** 沟通方式？
  - 当面/电话/微信/邮件

**Node 2：** 沟通内容？
  - 案件事实/法律意见/承诺/价格

**Node 3：** 是否需要当事人确认？
  - 重要事项须书面回执
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 口头沟通 | 当日补记 |
| 书面沟通 | 保留原始文件 |
| 敏感内容 | 避免承诺胜诉、避免评价其他律师 |

## 四、数据源锚定

- **主要数据源：** [BD] 沟通档案
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
legal-clinic/client-comms-log/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic client-comms-log B-phase v2.0.0（场景优先重构）*
