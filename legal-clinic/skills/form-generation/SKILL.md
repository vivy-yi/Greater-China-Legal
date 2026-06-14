---
name: form-generation
description: >
  标准化表单生成——申请书/告知书/委托书（C2+C4（表单生成））。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: legal-clinic
last_reviewed: 2026-06
version: 2.0.0
risk_level: medium
---

# /form-generation — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 标准化表单生成——申请书/告知书/委托书

**所属场景：** C2+C4（表单生成）

## 二、判断树

**Node 1：** 表单类型？
  - 法援申请表/授权委托书/风险告知书

**Node 2：** 对象？
  - 法院/当事人/行政机关

**Node 3：** 详细程度？
  - 填空式/手写式/电子签
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| C2 消保 | 小额诉讼申请书 |
| C4 行政 | 复议申请书/起诉状 |
| 通用 | 授权委托书 |

## 四、数据源锚定

- **主要数据源：** [GOV] 司法部标准表单 / [BD] 律所表单库
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
legal-clinic/form-generation/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic form-generation B-phase v2.0.0（场景优先重构）*
