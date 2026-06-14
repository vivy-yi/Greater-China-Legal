---
name: plain-language-letters
description: >
  通俗版信件——给当事人的非法律语言沟通（C3（婚姻家事））。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: legal-clinic
last_reviewed: 2026-06
version: 2.0.0
risk_level: medium
---

## 数据源与判断框架引用

本 skill 引用以下 plugin 根级 references 与 CLAUDE.md：

- **判断框架**：`../../references/判断框架.md`（4 场景簇路由 + 各场景判断树 + 督导审核 + 升级决策门）
- **数据源清单**：`../../references/数据源清单.md`（[YD]/[WKL]/[GOV]/[BD]/[model] + 法援场景适用 + 隐私保护）
- **查询路径**：`../../references/查询路径.md`（法援法规/案例/案件档案/争议程序/应急检索）
- **CLAUDE.md**：`../../CLAUDE.md`（CN 法律援助体系 + 申请流程）
- **B 重构规范**：`../../../scene-design/README.md`（场景簇定义 + 数据源锚定）
- **货币触发主题**：`../../../references/currency-watch.md`

本 skill 所属场景簇：`legal-clinic`（参见 `../../references/判断框架.md` §一）

⚠️ **法援场景特别提示**：
- 本 skill 输出**必须经督导复核**（除 client-comms-log / ramp 等元数据 skill）
- 当事人陈述标注 `[user]`，事实陈述与法律评价须明确区分
- 案件档案脱敏处理，遵循 `../../references/数据源清单.md` §九
- 关键结论须 2-3 个数据源交叉验证（详见 `../../references/数据源清单.md` §六）

升级条件详见 `../../references/判断框架.md` §六。

# /plain-language-letters — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 通俗版信件——给当事人的非法律语言沟通

**所属场景：** C3（婚姻家事）

## 二、判断树

**Node 1：** 当事人文化水平？
  - 初中/高中/大学

**Node 2：** 情感状态？
  - 冷静/激动/悲伤

**Node 3：** 是否涉及未成年人？
  - 需特别保护表述
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 离婚案件 | 避免归责性语言 |
| 继承案件 | 避免刺激性、聚焦事实 |
| 抚养纠纷 | 保护子女利益 |

## 四、数据源锚定

- **主要数据源：** [model] 通俗化模板
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
legal-clinic/plain-language-letters/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic plain-language-letters B-phase v2.0.0（场景优先重构）*
