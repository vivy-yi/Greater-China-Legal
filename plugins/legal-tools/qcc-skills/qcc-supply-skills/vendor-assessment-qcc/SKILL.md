---
name: vendor-assessment-qcc
description: >
  TODO: 待补充 description（YAML 安全的描述）
legal_frame: cn-mainland
last_reviewed: 2026-06-24
version: 1.0.0
risk_level: low
trigger_phrases:
  - vendor-assessment-qcc
---

> 供应商准入评估 SKILL · 企查查 MCP V2.0 增强版。
> 采购准入阶段的供应商深度尽调工具。输入供应商名称，AI 完成 9 维度风险评估，覆盖 34 类中国特有风险信号（司法执行 / 经营异常 / 税务违规 / 破产风险等），V2.0 新增双随机抽查 + 历史处罚两层维度，输出结构化准入报告。
>
> 核心能力：
> - 基础工商核验 + 资质证书有效性
> - 司法风险 34 类扫描（当前层）
> - **V2.0 新能力**：历史行政处罚追溯（qcc-history）+ 双随机抽查合规评分（qcc-operation `get_random_check` 新工具）
> - 纳税信用 + 海关信用 + 政府监管评级
> - 法代 × 实控人个人风险快扫
> - 准入评级 A/B/C/D 输出
>
> 适用场景：集中采购评审 / 国有企业供应商准入 / 甲方供应商库入库 / 招投标前资格预审。
>
> 使用方式：/vendor-assess 供应商名称 [--category 类型] [--value 合同金额] [--format md|docx|pptx]
>
> **风险核查采用「先扫后钻」**：先通过企业风险全量扫描一次性分诊 35 项风险维度、快速定位命中项，再对命中维度深入取证——既不漏维度，也避免逐项无效查询。

**命令**：`/vendor-assess` · **MCP 工具集**：`qcc-company, qcc-risk, qcc-operation, qcc-history, qcc-executive`

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


# 供应商准入评估 · 企查查 MCP V2.0 增强版

## SKILL 定位

本 SKILL 服务于采购评审委员会在供应商入库前的资格核查场景。V2.0 相对 V1.0 的升级聚焦两点：

- **`get_random_check`（双随机抽查）** 作为政府对企业的监管抽查合规评分，直接反映"企业在常规经营中是否经得起政府抽查"
- **qcc-history 历史行政处罚** 识别"曾经出险已修复"vs"连年处罚"两类供应商

## MCP 依赖

- 必选：`qcc-company` / `qcc-risk`
- 建议：`qcc-operation`（含 `get_random_check`）/ `qcc-history` / `qcc-executive`

## 工作流（9 维度）

### 维度一：工商基础核验
`get_company_registration_info` / `verify_company_accuracy` / `get_shareholder_info`

### 维度二：资质证书核验
`get_qualifications` / `get_administrative_license`

### 维度三：经营活跃度
`get_bidding_info` / `get_recruitment_info` / `get_honor_info`

### 维度四：政府信用评级
`get_credit_evaluation`（纳税信用）/ `get_import_export_credit`（海关信用）

### 维度五：**双随机抽查合规**（V2.0 新工具）
`mcp__qcc-operation__get_random_check` —— 返回企业被政府抽查的历史记录与结果。**无违规记录** = 经得起抽查的合规企业。

### 维度六：司法风险当前层
`get_dishonest_info` / `get_judgment_debtor_info` / `get_high_consumption_restriction` / `get_equity_freeze` / `get_tax_arrears_notice`

### 维度七：历史处罚追溯（V2.0 新能力）
`mcp__qcc-history__get_historical_admin_penalty` —— 识别 5 年内是否有已处罚但已结清的合规瑕疵，对"长期清洁"和"修复型供应商"差异化评估。

### 维度八：法代 × 实控人个人快扫（先扫后钻）
**先调 `mcp__qcc-executive__get_executive_risk_scan`（searchKey=企业 + personName=姓名，双锚）一次分诊法代/实控人 18 项个人风险维度 → 仅对 count>0 维度下钻对应 `get_executive_*` 原子**（如失信 `get_executive_dishonest`、限出境 `get_executive_exit_restriction`，对跨境供应商特别关键）；count=0 跳过，❌ 禁逐个散弹枪；多人则逐人各扫一次。

### 维度九：破产风险识别
`get_bankruptcy_reorganization` / `get_liquidation_info`

## 评级

| 评级 | 标准 | 准入建议 |
|------|------|---------|
| **A 级** | 工商真实 + 无司法风险 + 纳税 A 级 + 资质齐全 + 无双随机抽查违规 + 历史清洁 | **优先准入** |
| **B 级** | 无当前致命风险 + 历史已修复轻微事件 | **准入 + 加强监测** |
| **C 级** | 当前轻微风险 或 历史有已结清的中等处罚 | **附条件准入** + 担保要求 |
| **D 级** | 任一致命（失信 / 破产 / 资不抵债 / 实控人出险 / 吊销）| **拒绝准入** |

## 输出模板

- 章节 1：准入 决策摘要（评级 + 准入建议）
- 章节 2：工商核验 × 资质 × 经营活跃度
- 章节 3：政府评级 × 双随机抽查（V2.0）
- 章节 4：司法风险 × 历史处罚（V2.0 双层）
- 章节 5：法代 × 实控人画像
- 章节 6：综合评级 × 准入决策

---

**SKILL 版本**：v2.0 | **适配 MCP 版本**：146 工具 / 6 Server 全量
**所需 Server**：qcc-company / qcc-risk（必选）、qcc-operation / qcc-history / qcc-executive（建议）


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
