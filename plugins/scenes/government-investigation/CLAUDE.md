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

## 推理原子能力
## 推理原子能力调用流程

本场景的工作流程中，按以下顺序调用 `legal-atomic` 原子能力：

| 顺序 | 原子 Skill | 调用时机 |
|------|-----------|---------|
| 0 | `legal-element-extraction` | 收到用户输入后立即调用，将非结构化叙述转化为结构化法律事实 |
| 1 | `legal-norm-validity-check` | 在任何法条引用前调用，验证法条是否现行有效 |
| 2 | `deductive-reasoning` | 在分析阶段，将待判断的问题转化为 P-F-C 三段论格式 |
| 3 | `conflict-resolution` | 发现多个法条或请求权可能竞合时调用 |
| 4 | `evidence-argument-chain` | 需要组织证据与主张对应关系时调用 |
| 5 | `argument-strength-evaluation` | 输出结论前，标注论证强度（强/中/弱/存疑） |
| 6 | `legal-risk-assessment` | 在风险分级判断时调用 |
| 7 | `case-retrieval` | 需要检索类案时调用 |

每个 scene skill 的工作流程第一步应为「法律要素提取」，最后一步前应为「论证强度评估」。


本场景在执行 legal analysis 时，按需调用以下 `legal-atomic` 原子 skill：

| 原子 Skill | 用途 | 调用时机 |
|-----------|------|---------|
| `legal-element-extraction` | 法律要素提取 | 所有输入预处理——将非结构化叙述转化为法律事实 |
| `legal-norm-validity-check` | 法条效力核查 | 引用法条前验证是否现行有效 |
| `deductive-reasoning` | P-F-C三段论推理 | 构建法律推理链时 |
| `conflict-resolution` | 法条竞合/冲突解决 | 多个法条或请求权竞合时 |
| `evidence-argument-chain` | 证据论证链 | 组织证据与主张对应关系时 |
| `argument-strength-evaluation` | 论证强度评估 | 输出结论时标注强/中/弱/存疑 |
| `legal-risk-assessment` | 法律风险评估 | 涉及风险分级判断时 |
| `case-retrieval` | 类案检索方法论 | 需要检索类案时 |