---
name: web3-virtual-assets
description: |
  Web3与虚拟资产法律服务场景——覆盖加密资产合规、NFT、数字藏品、DeFi协议法律风险。
  适用情形：虚拟货币交易/OTC合规、DeFi协议风险评估、NFT IP纠纷、DAO架构设计、稳定币发行咨询。
last_reviewed: 2026-06
version: 1.0.0
gcl_scope: 中国大陆（虚拟货币禁令边界）+ 香港SFC牌照路径 + 海外DeFi合规
upgrade_threshold: 涉及刑事风险（非法集资/传销/洗钱）立即移交专业律师
---


> 🚀 **首次使用？** 运行 `cold-start-interview`（位于 `plugins/shared/cold-start-interview`）完成场景配置。如 CLAUDE.md 中存在 `[填空]` 标记，先配置再使用 skill。

# Web3与虚拟资产

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
**所属行业：** [Web3 / 区块链 / 金融科技 / 数字藏品 / 其他]
**上市状态：** [未上市 / 港股 / 美股 / 其他]
**法域：** cn-mainland / hk
**营业执照经营范围包含：** [虚拟资产相关业务描述]

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

- 虚拟货币监管合规（境内禁令边界 + 香港牌照路径）
- NFT铸造/交易合规 + IP纠纷处理
- DeFi协议法律风险评估
- DAO离岸架构设计

## 精细化子场景

| 子场景 | 核心问题 |
|--------|---------|
| crypto-asset-compliance | 虚拟货币/稳定币/资产代币化合规 |
| nft-digital-collectibles | NFT智能合约+平台运营+IP纠纷 |
| defi-protocol-advisor | DeFi Token性质认定+DAO架构 |

## 关键法规

- 中国人民银行等《关于进一步防范代币发行融资风险的公告》（2017年9月4日）
- 中国人民银行等《关于进一步防范虚拟货币交易炒作风险的公告》（2021年9月）
- 香港证监会《虚拟资产交易平台指引》
- FATF Travel Rule

## 输出格式

所有正式输出须在文档开头标注特权头部标记（参见 ## Who's using this），并遵守以下格式要求：

- 法律分析结论须标注数据来源标记
- 涉及虚拟货币定性须引用监管文件具体条款
- 涉及刑事风险评估须明确标注升级建议
- 涉及金额、代币数量等数字须注明信息来源

## 升级决策门

出现以下情形，立即升级至专业律师：
- 涉及非法集资罪、刑法第176条
- 涉及组织、领导传销活动罪
- 涉及洗钱罪的刑事风险
- 平台涉及涉众型犯罪（被害人众多）

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

### 追问规则（关键）

legal-element-extraction 的输出包含 `## 待补充事实` 节。如果该节非空：

1. **暂停当前分析流程**
2. 向用户逐一提问待补充事实，例如：
   > "请问合同中关于[知识产权归属/数据存储位置/价格调整机制]的条款是什么？这会影响后续判断。"
3. 用户补充后，**回到 Step 0 重新执行 legal-element-extraction**，将新信息并入结构化事实
4. 当待补充事实清空后，继续后续分析

**不得在待补充事实未清空的情况下输出最终结论。** 缺失关键事实的结论标注为「推定结论，须在事实补全后复核」。

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
| `legal-risk-assessment` | 法律风险评估 | 涉及风险分级判断时 |
| `conflict-resolution` | 法条竞合/冲突解决 | 多个法条或请求权竞合时 |
| `case-retrieval` | 类案检索方法论 | 需要检索类案时 |
| `trial-scheduling-and-deadline-monitoring` | 期限管理 | 涉及诉讼/仲裁期限时 |