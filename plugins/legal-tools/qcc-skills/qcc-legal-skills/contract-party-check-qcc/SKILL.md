---
name: contract-party-check-qcc
description: >
  TODO: 待补充 description（YAML 安全的描述）
legal_frame: cn-mainland
last_reviewed: 2026-06-24
version: 1.0.0
risk_level: low
trigger_phrases:
  - contract-party-check-qcc
---

> 合同相对方主体核验 SKILL · 企查查 MCP V2.0 增强版。
> 合同签署前的主体快速核验工具，输出"A/B/C/D"四档评级，D 级直接拒绝签约。
>
> 核心能力：
> - **工商登记二要素一致性核验**（`mcp__qcc-company__verify_company_accuracy` + `get_company_registration_info`）—— 企业名称 + 统一社会信用代码一致性核验，登记状态（吊销 / 注销 / 异常）一票否决
> - **V2.0 历史工商变更追溯**（`mcp__qcc-history__get_historical_registration` + `get_historical_legal_rep`）—— 识别频繁变更注册地址 / 频繁更换法代的壳公司
> - **司法风险快扫**（失信 `get_dishonest_info` / 限高 `get_high_consumption_restriction` / 被执行 `get_judgment_debtor_info` / 股权冻结 `get_equity_freeze` / 经营异常 `get_business_exception`）—— 5 项核心红线
> - **V2.0 法代个人风险（先扫后钻）**：先调 `mcp__qcc-executive__get_executive_risk_scan`（searchKey+personName 双锚）一次分诊法代 18 项个人风险 → 命中再下钻（失信 `get_executive_dishonest` / 限高 `get_executive_high_consumption_ban` / 限出境 `get_executive_exit_restriction` 等）—— 法代当前失信 / 限高 / 限出境直接触发签约风险
> - **经营活跃度辅助判定**（参保人数 + 招投标 + 招聘）—— 区分"形式存续 vs 实质经营"
> - 关联企业网络扫描（`mcp__qcc-executive__get_executive_controlled_companies`）—— 识别合同方背后真实集团关系
>
> 适用场景：合同签署前主体快速核验 / 法务 / 合规 / 律师 / 商务签约前风控、新合作方准入审批。
>
> 使用方式：/contract-party-check 企业名称 [--format md|docx|pptx]
>
> **风险核查采用「先扫后钻」**：先通过企业风险全量扫描一次性分诊 35 项风险维度、快速定位命中项，再对命中维度深入取证——既不漏维度，也避免逐项无效查询。

**命令**：`/contract-party-check` · **MCP 工具集**：`qcc-company, qcc-risk, qcc-history, qcc-executive, qcc-operation, qcc-ipr`

---

## 🔍 风险维度扫描 · 先扫后钻（统一规范 · 2026-06-08 · 对齐 A 层铁律 5-A）

> 本 SKILL 凡涉及“一次性排查 ≥ 2 个企业风险维度”（司法风险 / 失信 / 被执行 / 限高 / 经营异常 / 行政处罚 / 破产 / 担保 / 税务 等 qcc-risk 维度），**一律按“先扫后钻”执行，禁止逐个原子风险工具散弹枪式调用**（慢 / 贵 / 多为无效调用）：
>
> 1. **第 1 步 · 分诊（先扫）**：先调 `mcp__qcc-risk__get_company_risk_scan`（企业风险扫描）一次返回企业**自身** 35 项风险维度的命中计数（脱水版：有 / 无 + 条数，不含明细）。
> 2. **第 2 步 · 下钻（后钻）**：仅对 `count > 0` 的维度，调对应原子风险工具取明细（具体工具见本 SKILL 工作流 / 术语对照表）。示例：scan 显示「失信 2、被执行 1、其余 0」→ 只下钻 `mcp__qcc-risk__get_dishonest_info` + `mcp__qcc-risk__get_judgment_debtor_info`。
> 3. **`count = 0` 的维度**：直接判定“无记录”，不再调用该维度原子工具。
> 4. **明确单一维度问句**（仅查某一项，如“有没有失信”）→ 直接调对应原子工具，无需先扫（对应 A 层铁律 5-A 路由 3）。
> 5. scan 只分诊、不出明细；要明细必须下钻原子工具。风险结论只陈述“命中维度 + 计数 / 明细”客观事实，**不替客户判定“能不能合作 / 可不可开户”**。
> 6. 先扫后钻发生在**实体锚定确定唯一主体之后**；简称 / 品牌名仍须先 `mcp__qcc-company__get_company_by_query` 锁定主体，再 scan。
> 7. 本轮**仅**引用已上线的 `get_company_risk_scan`（企业**自身**风险扫描）；企业“自身风险”之外的聚合扫描能力尚未上线（Phase 2），本 SKILL **不得引用任何未上线的聚合风险扫描工具**。
>
> 8. **【定性必须有下钻证据】** 对任一风险维度给出**定性判断**（如“多为原告身份 / 属正常维权”“轻微合规瑕疵”“诉讼活跃度正常”等）之前，必须已下钻该维度的明细工具、拿到支撑数据；未下钻则**只陈述 scan 计数并标注“（未取明细）”**，禁止凭 scan 计数或印象给定性。例：scan 显示「裁判文书 77」但未下钻 `mcp__qcc-risk__get_judicial_documents` → 只能写“裁判文书 77 条（未取明细）”，**不得**写“多为原告身份、属正常维权”；如需该定性，必须先下钻 `get_judicial_documents`（可按 `role` 取原告 / 被告分布）再下结论。

---


## 📖 QCC MCP 术语对照表（强制工具映射）

> **使用约定**：本表列出 SKILL 内业务简写与企查查 MCP 工具的精确映射。AI 执行本 SKILL 时遇到下表"业务简写"列的词汇，**必须调用对应"MCP 工具"列**，禁止使用 web search 或自由文本推测替代。完整规范见 [QCC-MCP-TERMINOLOGY.md](../../QCC-MCP-TERMINOLOGY.md)。

| 业务简写 | 规范全名 | 企查查 MCP 工具 |
| --- | --- | --- |
| 失信 | 失信被执行人 | `mcp__qcc-risk__get_dishonest_info` |
| 被执行 | 被执行人 / 判决债务人 | `mcp__qcc-risk__get_judgment_debtor_info` |
| 限高 | 限制高消费 | `mcp__qcc-risk__get_high_consumption_restriction` |
| 限出境 / 限境 | 限制出境 | `mcp__qcc-risk__get_exit_restriction` |
| 终本 | 终结本次执行案件 | `mcp__qcc-risk__get_terminated_cases` |
| 破产 / 重整 | 破产重整 | `mcp__qcc-risk__get_bankruptcy_reorganization` |
| 经营异常 | 经营异常 | `mcp__qcc-risk__get_business_exception` |
| 严重违法 | 严重违法失信 | `mcp__qcc-risk__get_serious_violation` |
| 行政处罚 / 重大处罚 | 行政处罚 | `mcp__qcc-risk__get_administrative_penalty` |
| 股权冻结 | 股权冻结 | `mcp__qcc-risk__get_equity_freeze` |
| 股权出质 | 股权出质 | `mcp__qcc-risk__get_equity_pledge_info` |
| 欠税 | 欠税公告 | `mcp__qcc-risk__get_tax_arrears_notice` |
| 税务异常 / 税务违法 | 税务异常 / 税收违法 | `mcp__qcc-risk__get_tax_abnormal` / `mcp__qcc-risk__get_tax_violation` |
| 受益所有人 / UBO | 受益所有人 | `mcp__qcc-company__get_beneficial_owners` |
| 实控人 / 实际控制人 | 实际控制人 | `mcp__qcc-company__get_actual_controller` |
| 主要人员 / 董监高 | 主要人员 | `mcp__qcc-company__get_key_personnel` |
| 抽查检查 / 双随机 | 双随机抽查 | `mcp__qcc-operation__get_random_check` |
| 吊销 | （登记状态字段判断）| 调 `mcp__qcc-company__get_company_registration_info` 取"登记状态" |
| 资不抵债 | （资产负债率字段判断）| 调 `mcp__qcc-company__get_financial_data` 判断负债率 > 100% |

---

# 合同相对方主体核验 · 企查查 MCP V2.0 增强版

## SKILL 定位

合同签署前的主体快速核验工具。V2.0 新增历史工商变更追溯 + 法代个人风险扫描两层能力。

## 工作流维度

1. 工商登记状态 + 三项一致性核验
2. **V2.0 新能力：历史工商变更**（qcc-history get_historical_registration/legal_rep —— 识别频繁变更的壳公司）
3. 司法风险快扫（失信 / 限高 / 被执行 / 股权冻结 / 经营异常）
4. **V2.0 新能力：法代个人风险（先扫后钻）**（先调 `get_executive_risk_scan` 双锚一次分诊法代 18 维个人风险 → 命中下钻；法代当前失信 / 限出境直接触发合同签署风险）
5. 经营活跃度辅助判定（参保 / 招投标）

## 评级

A/B/C/D 四级 · D 级拒绝签约



## MCP 依赖

- 必选：qcc-company / qcc-risk
- V2.0 强烈建议：qcc-history（历史追溯）/ qcc-executive（法代画像）/ qcc-operation（经营活跃度）

## 输出模板

- 章节 1：决策摘要（评级 + 关键判断 + 推荐 Action）
- 章节 2：数据来源
- 章节 3-6：各维度扫描结果（详见上文）
- 章节 7：V2.0 能力增量说明
- 章节 8：综合评级 × 处置建议

## 参数

- `--format md|docx|pptx`：输出格式，默认 md

## 边界与免责

本 SKILL 基于企查查 MCP V2.0 公开数据生成。特定法律场景（如商标近似性的最终判定 / 劳动仲裁的实体审查）需配合专业律师做实质审查。


**SKILL 版本**：v2.0 | **适配 MCP 版本**：146 工具 / 6 Server 全量


## 风险维度补充 · 违约事项必查（2026-06-05 · 漏报修复）

> 背景：实测案例中企业存在「票据违约 · 当期逾期」记录（qcc-risk `get_default_info` 违约事项），但本 SKILL 旧版工具清单未包含该维度，导致核验报告漏报重大信用履约风险。

**硬性要求**：执行本 SKILL 的风险扫描时，**必须调用 `mcp__qcc-risk__get_default_info`（违约事项 / 票据违约）**，并在报告的风险核查表中固定输出「违约事项（票据违约）」一行：
- 有记录 → 列明违约类型、违约状态（如当期逾期）、逾期余额、累计逾期发生金额、数据截止日期，并按本 SKILL 评级规则将其计入信用履约风险（"当期逾期"状态应显著影响综合评级与准入建议）；
- 无记录 → 写"未发现违约事项记录"。
报告中该维度使用业务名称「违约事项 / 票据违约」，遵守报告输出纪律。

---

## 报告输出纪律（内部规则 · 严禁出现在最终报告中）

1. **一律业务语言**：报告正文、备注、数据来源说明中不得出现 MCP 工具代码名（`get_xxx` / `mcp__qcc-xxx`）、server 名（qcc-company 等）、schema / manifest / 字段名等技术词；数据来源统一用业务表述（如"企查查工商登记数据 / 企查查风险信息数据 / 企查查财务数据"）。"企查查 MCP"作为对外产品名仅允许出现在「数据来源」固定句式中。
2. **禁止内部用语**：SKILL / SKILL.md / V1.0 / V2.0 / 增强版 / 新能力 / 维度编号 / 评级引擎规则等开发概念不得出现在报告中；「Decision Pack」一律写「决策摘要」。
3. **禁止执行过程独白**：不输出"我将按照…/第一步获取…/已锁定主体/接下来…"等过程描述，直接输出报告正文。
4. **禁止运行时状态泄漏**：积分余额、配额、调用受限、超时重试、在线体验版本等不得写入报告；某维度数据未获取时统一写"本次未核验 / 未发现公开记录"。
5. **数据零推算**：只引用工具返回的原始数字；禁止自行加总、相减、加权、估算（含"推算 / 估算值"字样）；工具未返回的字段留空或写"未披露"，不得编造。
6. 本节及全部内部执行规则只约束 AI 行为，严禁以任何形式抄入报告。
