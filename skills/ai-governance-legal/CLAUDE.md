---
name: ai-governance-legal
description: >
  AI governance and compliance legal practice — AI inventory management,
  impact assessments, regulatory compliance for AI systems under CAC regulations
  and Mainland China AI governance framework.
  Covers AI推荐算法/生成合成内容/深度合成/自动驾驶等场景。
synopsis: >
  CN AI governance framework: CAC 算法推荐/深度合成/生成式AI管理办法,
 个人信息保护法, 数据安全法, 网络安全法.
  Obligations: 算法备案, 安全评估, 个人信息保护, 数据本地化.
advisory_scale: medium
client_types: [in-house-legal, compliance-team]
internal_stakeholders: [compliance, product, engineering, privacy]
external_interfaces: [cac, mit, samr]
risks: [regulatory-enforcement, enforcement-risk-high, privacy-penalty]
---

# AI Governance Legal Practice — China Mainland

## Who's using this

**Role:** [律师 / 法务人员 / 业务部门（非法律背景，有律师支持）/ 业务部门（无律师支持）]
**Attorney contact:** [填空]

**工作成果头部标记：**
- 律师/法务人员 → `Privileged & Confidential — Attorney Work Product`
- 非法务（有律师支持）→ `Research Notes — Not Legal Advice — Review With Attorney Before Acting`
- 非法务（无律师支持）→ `General Information — Not Legal Advice — Consult A Licensed Attorney`

在产出工作成果前，必须先检查 Role 字段。如果 Role 为 `[填空]`，要求用户先设置角色。

## 公司基本信息

**公司名称：** [填空]
**统一社会信用代码：** [填空]
**注册资本：** [填空]
**所属行业：** [填空]
**上市状态：** [未上市 / 新三板 / 科创板 / 创业板 / 主板 / 港股 / 美股]
**法域：** cn-mainland

## 数据源配置

**数据源标注规则：**
- `[YD]` = 元典 MCP 实际返回
- `[WKL]` = 裁判文书网/无讼
- `[BD]` = 北达检索
- `[GOV]` = 政府平台
- `[web]` = 网络搜索
- `[model]` = 模型推理（须核实）

标注必须诚实——不能因"引用看起来是对的"就把 `[model]` 标为 `[YD]`。关键结论须多源交叉验证。

## CN AI Regulatory Framework

### Core Regulations

| 法规 | 生效日期 | 适用范围 |
|---|---|---|
| 《互联网信息服务算法推荐管理规定》| 2022-03-01 | 算法推荐服务 |
| 《互联网信息服务深度合成管理规定》| 2023-01-10 | 深度合成 |
| 《生成式人工智能服务管理暂行办法》| 2023-08-15 | 生成式AI服务 |
| 《汽车数据安全管理若干规定》| 2021-10-01 | 自动驾驶/车联网 |
| 《个人信息保护法》| 2021-11-01 | 个人信息处理 |
| 《数据安全法》| 2021-09-01 | 数据处理 |

---

## CN AI Governance Obligations

### 算法推荐服务（CAC规定）

**须履行的义务：**
1. 算法备案（省级网信办）
2. 安全评估（每年）
3. 个人信息保护评估（变更时）
4. 算法透明度和可解释性
5. 用户权利保障（选择权/退出权/删除权）

---

### 生成式AI服务

**须履行的义务：**
1. 安全评估（国家级）
2. 算法备案（按模型规模）
3. 数据标注合规（不得侵犯个人信息）
4. 个人信息保护（尤其用于训练的数据）
5. 色情/虚假信息防控

---

## CN AI Inventory Management

### CN AI System Categories

| 类型 | 说明 | 备案要求 |
|---|---|---|
| 算法推荐 | 推荐/排序/过滤 | 须备案 |
| 深度合成 | 换脸/语音合成/AI生成内容 | 须备案 |
| 生成式AI | LLM/图像生成/视频生成 | 须安全评估 |
| 自动驾驶 | L2+/L3/L4 | 须安全评估 |
| 人脸识别 | 生物识别 | 须安全评估 |

---

## Risk Tiers

| 风险等级 | 说明 |
|---|---|
| 🔴 Prohibited | 深度伪造用于犯罪、歧视性算法 |
| 🟠 High-risk | 生成式AI大规模服务、自动驾驶 |
| 🟡 Limited-risk | 算法推荐（须透明度） |
| ⚪ Minimal-risk | 信息检索类 |

---

## Data Sources

- [GOV] CAC官网算法推荐备案公示
- [GOV] 全国互联网安全管理服务平台
- [YD] 法律精灵执法案例
- [WKL] 各大律所AI合规指南

---

## 输出格式

所有正式输出须在文档开头标注特权头部标记（参见 ## Who's using this），并遵守以下格式要求：

- 法律分析结论须标注数据来源标记
- 涉及法条引用须标明具体条款及生效版本
- 涉及金额、日期等数字须注明信息来源

## 升级决策门

以下情形必须升级给执业律师：
1. 涉及算法备案被驳回或处罚的应对策略
2. 涉及生成式AI安全评估未通过的后续方案
3. 涉及个人信息泄露事件的应急与通知义务
4. 涉及跨境数据传输的合规路径设计
5. 涉及刑事风险（如深度合成用于犯罪）的案件

---

*Greater China Legal — ai-governance-legal CN adapter v1.0.0*