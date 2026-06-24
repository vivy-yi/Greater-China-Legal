---
name: new-supplier-screening-qcc
description: >
  TODO: 待补充 description（YAML 安全的描述）
legal_frame: cn-mainland
last_reviewed: 2026-06-24
version: 1.0.0
risk_level: low
trigger_phrases:
  - new-supplier-screening-qcc
---

> 新供应商快速筛选 SKILL · 企查查 MCP V2.0 增强版。
> 招投标或采购寻源阶段对候选供应商的批量快速筛选工具。与"供应商准入评估"的深度核验不同，本 SKILL 聚焦"快速筛选 + 去伪存真"——一次扫描多家候选供应商，输出排序后的短名单。V2.0 新增双随机抽查作为合规筛选利器。
>
> 核心能力：
> - 批量扫描候选供应商（每次可处理 5-20 家）
> - 9 项核心红线快筛（失信 / 限高 / 被执行 / 经营异常 / 破产 / 资不抵债 / 重大处罚 / 股权冻结 / 吊销）
> - **V2.0 新能力**：`get_random_check` 双随机抽查合规评分——经得起政府抽查 = 合规性强信号
> - 输出短名单（排除红线 + 按综合评分排序）
>
> 适用场景：招标寻源阶段候选供应商排查 / 集中采购前的候选池筛选 / 新业务领域供应商批量扫描。
>
> 使用方式：/new-supplier-screening 供应商 1 / 供应商 2 / ... [--top N 返回前 N 名] [--format md|docx|pptx]
>
> **风险核查采用「先扫后钻」**：先通过企业风险全量扫描一次性分诊 35 项风险维度、快速定位命中项，再对命中维度深入取证——既不漏维度，也避免逐项无效查询。

**命令**：`/new-supplier-screening` · **MCP 工具集**：`qcc-company, qcc-risk, qcc-operation`

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

# 新供应商快速筛选 · 企查查 MCP V2.0 增强版

## SKILL 定位

本 SKILL 是采购寻源的"筛子"——在进入正式"准入评估"或"IC Memo 级"深度尽调前，快速从候选池中排除"显然不合格"的主体。V2.0 `get_random_check` 是本场景的神器：**一家长期经得起政府双随机抽查、零违规记录的供应商，合规性上基本可信**——这比看资质证书更实在。

## MCP 依赖

- 必选：`qcc-company` / `qcc-risk`
- 强烈建议：`qcc-operation`（含 `get_random_check`）

## 工作流

### 维度一：9 项核心红线快筛

对每家候选供应商并行执行：

| 序号 | 工具 | 红线判定 |
|------|------|---------|
| 1 | `get_dishonest_info` | 当前失信 > 0 → 🔴 直接出局 |
| 2 | `get_high_consumption_restriction` | 当前限高 > 0 → 🔴 出局 |
| 3 | `get_judgment_debtor_info` | 当前被执行 > 0 → 🔴 出局 |
| 4 | `get_business_exception` | 当前经营异常 > 0 → 🔴 出局 |
| 5 | `get_bankruptcy_reorganization` | 已进入破产程序 → 🔴 出局 |
| 6 | `get_equity_freeze` | 股权冻结 > 0 → 🔴 出局 |
| 7 | `get_company_registration_info` | 登记状态吊销 / 注销 → 🔴 出局 |
| 8 | `get_tax_arrears_notice` | 欠税 > 0 → 🔴 出局 |
| 9 | `get_serious_violation` | 严重违法失信名单 → 🔴 出局 |

### 维度二：综合合规评分（未被红线排除的）

对通过红线的候选者计算综合评分：

| 指标 | 权重 | 评分逻辑 |
|------|------|---------|
| 纳税信用等级 | 25% | A=100 / B=70 / C=40 / D=0 |
| 海关信用等级 | 15% | 高级 AEO=100 / 一般认证=80 / 备案=50 |
| **双随机抽查记录**（V2.0）| 20% | 无违规=100 / 有违规已整改=70 / 有违规未整改=0 |
| 参保人数 | 10% | 100+=100 / 50-100=80 / 10-50=60 / <10=30 |
| 资质证书数量 | 10% | >10=100 / 5-10=80 / 1-5=50 / 0=0 |
| 招投标活跃度 | 10% | 高=100 / 中=70 / 低=30 |
| 荣誉信息 | 10% | 国家级=100 / 省级=70 / 市级=40 / 无=20 |

**综合评分 = Σ(指标得分 × 权重)**

### 维度三：短名单生成

1. 排除所有 🔴 红线触发者
2. 对剩余候选按综合评分降序排列
3. 返回 Top N（默认 Top 5）

## 输出模板

- 章节 1：筛选结果 决策摘要（进入短名单的候选清单）
- 章节 2：筛选方法说明
- 章节 3：9 项红线排查结果（每家供应商一行）
- 章节 4：综合合规评分明细
- 章节 5：**短名单**（按排序） + 理由 + 下一步建议（IC Memo / 准入评估）

## 参数

- `--top N`：返回前 N 名，默认 5
- `--threshold <score>`：综合评分阈值，低于此值不入短名单
- `--format md|docx|pptx`：输出格式

---

**SKILL 版本**：v2.0 | **所需 Server**：qcc-company / qcc-risk（必选）、qcc-operation（强烈建议）


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
