---
name: government-investigation
description: |
  政府监管与调查应对场景——覆盖反垄断调查、证券监管调查、证券合规、反腐败反商业贿赂。
  适用情形：监管机构现场检查/调查应对、行政处罚听证、企业内部合规体系建设。
last_reviewed: 2026-06
version: 1.0.0
gcl_scope: 中国大陆 + 香港SFC + 美国SEC/FCPA
upgrade_threshold: 进入刑事程序立即移交专业律师
---

# 政府监管与调查应对

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
**法域：** cn-mainland / hk
**近期是否收到监管调查通知：** [是 / 否]
**是否有在办监管案件：** [是 / 否]

## 数据源配置

**数据源标注规则：**
- `[YD]` = 元典 MCP 实际返回
- `[WKL]` = 裁判文书网/无讼
- `[BD]` = 北达检索
- `[GOV]` = 政府平台
- `[web]` = 网络搜索
- `[model]` = 模型推理（须核实）

标注必须诚实——不能因"引用看起来是对的"就把 `[model]` 标为 `[YD]`。关键结论须多源交叉验证。

## 核心能力

- 反垄断调查应对（市场监管总局/发改委）
- 证券监管调查应对（证监会/香港SFC）
- 反腐败反商业贿赂合规（FCPA/反商业贿赂法）

## 精细化子场景

| 子场景 | 核心问题 |
|--------|---------|
| anti-monopoly-investigation | 经营者集中申报/调查应对 |
| securities-investigation | 内幕交易/信息披露违规/证监会调查 |
| anti-corruption-compliance | FCPA合规/举报人制度/商业贿赂风险 |

## 关键法规

- 《中华人民共和国反垄断法》（2022年修订）
- 《中华人民共和国证券法》（2020年修订）
- 《禁止商业贿赂暂行规定》
- 美国《反海外腐败法》（FCPA）
- FATF Travel Rule

## 输出格式

所有正式输出须在文档开头标注特权头部标记（参见 ## Who's using this），并遵守以下格式要求：

- 法律分析结论须标注数据来源标记
- 涉及监管程序判断须引用具体法规条款
- 涉及调查应对策略须明确区分建议与事实
- 涉及刑事风险须明确标注升级建议

## 升级决策门

出现以下情形，立即升级至专业律师：
- 进入刑事调查程序（公安介入）
- 涉及证券欺诈刑事风险
- 涉及跨国监管执法（美国SEC/FCPA、英国SFO）
- 企业高管被留置/拘留
