---
name: ic-memo-qcc
description: >
  TODO: 待补充 description（YAML 安全的描述）
legal_frame: cn-mainland
last_reviewed: 2026-06-24
version: 1.0.0
risk_level: low
trigger_phrases:
  - ic-memo-qcc
---

> IC Memo 投资备忘录 SKILL · 企查查 MCP V2.0 增强版。
> PE / VC 投资决策的核心尽调工具。一次调用并行完成目标公司工商登记、多层股权穿透、真实财务底盘、司法风险、知识产权、核心高管全景六维度扫描，直接输出符合投委会要求的标准格式备忘录。
>
> 核心能力：
> - 多层股权穿透 + UBO 识别：`get_beneficial_owners` + `get_executive_beneficial_owner` 双向锁定
> - **V2.0 新能力：真实财务底盘**（`get_financial_data` 3 年完整财报，首次用于投资类场景）
> - 知识产权资产清单：专利 / 商标 / 软件著作权 + 知产出质（V2.0 新工具）
> - 司法风险全景：当前 + 历史双层
> - 核心高管画像：法代 / 董事长 / 实控人 / CEO / CFO 的个人司法轨迹、任职履历、控制企业
> - 融资历史追踪：融资记录 × 历史股东变迁（qcc-history）
>
> 适用场景：PE / VC 项目 DD、投资银行并购尽调、企业战投立项、Pre-IPO 投前核查、Term Sheet 前的快速筛查。
>
> 使用方式：/ic-memo-qcc 目标公司名称 [--stage pre-a|a|b|c|pre-ipo] [--thesis 投资主题] [--format md|docx|pptx]
>
> **风险核查采用「先扫后钻」**：先通过企业风险全量扫描一次性分诊 35 项风险维度、快速定位命中项，再对命中维度深入取证——既不漏维度，也避免逐项无效查询。

**命令**：`/ic-memo-qcc` · **MCP 工具集**：`qcc-company, qcc-risk, qcc-ipr, qcc-history, qcc-executive, qcc-operation`

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

# IC Memo 投资备忘录 · 企查查 MCP V2.0 增强版

## SKILL 定位

本 SKILL 服务于 PE / VC 机构、投资银行、企业战投部门在投资决策前的项目尽调场景。IC Memo 是投委会决策的核心输入材料——传统分析师需要 2-3 小时人工拼接工商登记、股权穿透、司法风险、知识产权等多源数据，本 SKILL 一次调用 30 秒内完成所有数据收集 + 深度推演 + 标准格式输出。

V2.0 相对 V1.0 最具颠覆性的升级是 `get_financial_data` 首次让 IC Memo 能拿到真实财务数据——投资决策从"靠路演 PPT 宣称"升级为"靠 MCP 实时财务数据核验"。叠加 qcc-executive 对核心创始团队的个人画像扫描，IC Memo 的两个核心决策点（财务可信度 × 创始团队可靠性）从此具备了硬数据支撑。

## MCP 依赖与配置

必选：
- `qcc-company`（企业基座）—— 工商核验 + 股东 + 实控人 + UBO + 主要人员 + **`get_financial_data`**
- `qcc-risk`（风控大脑）—— 司法风险全维
- `qcc-ipr`（知产引擎）—— 专利 / 商标 / 软件著作权 / **`get_ipr_pledge`**（V2.0 新工具）

强烈建议：
- `qcc-history`（历史存档）—— 历史融资记录 / 历史股东变迁
- `qcc-executive`（人员画像）—— 创始团队个人画像

可选：
- `qcc-operation`（经营罗盘）—— 融资记录、招聘活跃度、荣誉信息

## 通用执行原则

**第一，IC Memo 的第一决策点是"财务数据真实性"。** 创业公司向投资人讲述的增长故事常常存在"经调整后的收入 / 非 GAAP 利润 / 管理口径"等包装。V2.0 `get_financial_data` 返回的是年报披露的审计口径数据，是判断路演 PPT 是否"水份过高"的基准。如 `get_financial_data` 返回与路演口径偏差 > 30%，IC Memo 必须显式标注"路演 vs 审计口径差异"。

**第二，创始团队是第二决策点。** 投资看人的本质是看"创始人 / 核心 CEO / CTO / CFO"过往商业记录。V2.0 qcc-executive 对这些自然人做多维扫描——个人失信 / 限高 / 限出境 / 其他控制企业是否存在过暴雷 / 历史任职记录中是否有职业稳定性问题。

**第三，股权结构的清晰性决定投资可行性。** 复杂代持 / VIE 架构 / 多层离岸 SPV 等均提高尽调难度。SKILL 须标注股权结构复杂度（简单 / 中等 / 复杂）+ VIE 风险（无 / 轻度 / 重度）+ UBO 清晰度（单一 / 多元 / 模糊）。

**第四，知识产权是科技项目的核心资产评估维度。** 专利数 + 软件著作权数 + 知产出质情况（V2.0 新工具）构成科技项目估值的重要基础，若知产已被大量质押融资，净资产中的"无形资产"水分极大。

**第五，融资历史连贯性预判估值合理性。** 通过 qcc-history 追溯历史股东变迁和融资记录，识别上轮估值与本轮估值的跃升合理性，警惕"估值倒挂"型项目。

## 工作流

### 维度一：目标公司工商与股权核验

工具链：
- `mcp__qcc-company__get_company_registration_info`
- `mcp__qcc-company__verify_company_accuracy`
- `mcp__qcc-company__get_shareholder_info`
- `mcp__qcc-company__get_actual_controller`
- `mcp__qcc-company__get_beneficial_owners`
- `mcp__qcc-company__get_external_investments`

产出：主体基本信息表、股权结构图（多层穿透）、UBO 清单、对外投资清单。

### 维度二：真实财务底盘（V2.0 核心新能力）

工具链：
- `mcp__qcc-company__get_financial_data` —— 3 年完整财报
- `mcp__qcc-company__get_annual_reports` —— 年报文本数据

核心评估指标：

| 类别 | 指标 | 投资评估意义 |
|------|------|------------|
| 规模 | 营业总收入、总资产 | 业务规模 |
| 盈利 | 净利润、毛利率、净利率 | 商业模型可持续性 |
| 成长 | 营收同比、总资产同比 | 成长速度 |
| 健康 | 资产负债率、流动比率、速动比率 | 财务稳健性 |
| 现金 | 经营现金流 | 自造血能力 |

**IC Memo 财务决策逻辑**：
- 连续 3 年营收高速增长（>50%）+ 毛利率 > 30% + 经营现金流趋正 → **高成长可投** A 类
- 营收增长但毛利率薄 + 现金流持续负 → **烧钱扩张** B 类，需评估估值与轮次匹配
- 营收停滞或下降 + 现金流负 → **早期风险或已过拐点** C 类，慎投

### 维度三：核心高管画像（V2.0 新能力）

对创始人 + CEO + CFO + CTO 做 qcc-executive 画像：

**【个人风险先扫后钻 · 2026-06-08 · 对齐 A 层铁律 5 个人维度】** 对每位目标人（法代/实控人/董监高），**先调 `mcp__qcc-executive__get_executive_risk_scan`（searchKey=企业完整名/USCC + personName=姓名，双锚定）一次返回其 18 项个人风险维度命中计数 → 仅对 count>0 维度下钻下列对应 `get_executive_*` 原子工具取明细**；count=0 跳过。❌ 禁止不先扫、逐个散弹枪调个人风险原子。单人工具：多人则逐人各扫一次，不对全体董监高自动循环。
- `mcp__qcc-executive__get_executive_dishonest` / `get_executive_high_consumption_ban` / `get_executive_judgment_debtor` / `get_executive_exit_restriction` / `get_executive_tax_violation`
- `mcp__qcc-executive__get_executive_controlled_companies` / `get_executive_investments` / `get_executive_positions` / `get_executive_historical_positions`

**投资视角重点**：
- 创始人其他控制企业是否存在失信 / 破产 → 道德风险信号
- 创始人 CFO 其他任职企业是否存在财务丑闻 → 重大审计风险
- CTO 是否同时在多家公司任技术负责人 → 精力分散 / 关联技术纠纷风险
- 历史任职企业是否集中在特定行业 → 创始团队的行业经验深度

### 维度四：司法风险扫描

工具链：
- `mcp__qcc-risk__*`（与其他 SKILL 类似的 10+ 工具）
- `mcp__qcc-history__get_historical_judicial_docs` / `get_historical_dishonest` / `get_historical_judgment_debtor`

**投资视角解读**：
- 当前诉讼为被告且大额 → 负面，需评估或有负债
- 当前诉讼为原告且追讨应收 → 中性，但反映客户违约风险
- 历史失信已修复 → 有风险承担能力但需标注
- 完全零诉讼 → 可能是"太年轻尚未经历纠纷"或"真正合规"，需结合成立年数判断

### 维度五：知识产权资产（含 V2.0 `get_ipr_pledge`）

工具链：
- `mcp__qcc-ipr__get_patent_info` —— 专利
- `mcp__qcc-ipr__get_trademark_info` —— 商标
- `mcp__qcc-ipr__get_software_copyright_info` —— 软著
- `mcp__qcc-ipr__get_copyright_work_info` —— 作品著作权
- `mcp__qcc-ipr__get_internet_service_info` —— 网络服务备案
- `mcp__qcc-ipr__get_ipr_pledge` —— **V2.0 新工具**，知产出质
- `mcp__qcc-history__get_historical_patent` / `get_historical_trademark` / `get_historical_ipr_pledge`

**估值关键判定**：
- 核心专利数 × 发明专利占比 → 技术壁垒深度
- 软件著作权数 → 软件资产规模
- **知产出质 > 50%** → 无形资产已大量抵押融资，净资产水分大
- 商标注册 + 域名备案 → 品牌护城河

### 维度六：融资历史与经营活跃度

工具链：
- `mcp__qcc-operation__get_financing_records` —— 融资记录
- `mcp__qcc-history__get_historical_shareholders` —— 历史股东变迁
- `mcp__qcc-history__get_historical_investments` —— 企业历史对外投资
- `mcp__qcc-operation__get_recruitment_info` —— 招聘活跃度（经营扩张信号）

**IC Memo 视角**：
- 历轮估值递进合理（每轮 2-3 倍）→ 健康
- 历轮估值倒挂 / 退出股东多 → 警惕
- 招聘活跃度 × 岗位层级 → 扩张真实性

## IC Memo 标准结构（投委会格式）

- **章节 1：交易摘要 · 决策摘要** —— 项目评级 A/B/C + 估值合理性 + 核心投资逻辑 + 核心风险点
- **章节 2：目标公司速览** —— 基本信息、所处赛道、核心产品、营收规模、团队规模
- **章节 3：股权穿透 × UBO 识别**（V2.0 加强）
- **章节 4：真实财务底盘**（V2.0 新能力）—— 3 年财报 + 关键比率 + 增长曲线
- **章节 5：核心高管画像**（V2.0 新能力）—— 创始人 + CEO + CFO + CTO 个人司法 + 任职履历
- **章节 6：司法风险全景** —— 当前 + 历史
- **章节 7：知识产权资产** —— 专利 + 商标 + 软著 + 知产出质（V2.0）
- **章节 8：融资历史与估值合理性**
- **章节 9：核心风险清单 × 缓释条款建议**（如反稀释 / 优先清算 / 对赌条款等）
- **章节 10：投委会建议与 Term Sheet 要点**

## 投委会评级

- **A 级（强烈推荐）**：财务 + 团队 + 股权 + 知产 + 融资历史五维度全部达标 → 建议 Lead / Co-lead
- **B 级（可投但有保留）**：四维度达标，一项有瑕疵 → 建议参投 + 加强对赌条款
- **C 级（暂缓）**：三维度以下达标 → 建议暂缓 + 要求补充材料
- **D 级（不投）**：任一致命风险（财务造假嫌疑 / 创始人出险 / 股权代持 / 当前重大诉讼）→ 不投

## 参数

- `--stage <轮次>`：投资轮次（Pre-A / A / B / C / Pre-IPO），影响评估重点
- `--thesis <投资主题>`：本机构对该项目的投资逻辑
- `--format md|docx|pptx`：输出格式，默认 md；pptx 为投委会一页摘要

## 边界与免责

本 SKILL 是基于主体侧公开数据的投资尽调，不涉及以下内容（需配合其他工作）：
- 创始人访谈与团队动态评估
- 市场规模与竞争格局分析
- 商业模式创新性判定
- 客户访谈与复购数据
- 供应链真实性验证（线下走访）

`get_financial_data` 覆盖上市公司、Pre-IPO 申报披露企业、部分有主动披露意愿的非上市公司。对早期 Pre-A / A 轮项目，大概率返回空——此时 IC Memo 的财务维度需依赖创业公司主动提供的审计 / VAT 报表 + 公司业务数据脱敏版。

最终投资决策由投委会综合评审，本 SKILL 输出仅为决策支持材料。

---

**SKILL 版本**：v2.0（MCP V2.0 升级版）
**适配 MCP 版本**：146 工具 / 6 Server 全量版
**所需 Server**：qcc-company（必选，含 get_financial_data）、qcc-risk（必选）、qcc-ipr（必选，含 get_ipr_pledge）、qcc-history（强烈建议）、qcc-executive（强烈建议）、qcc-operation（建议）

---

## 报告输出纪律（内部规则 · 严禁出现在最终报告中）

1. **一律业务语言**：报告正文、备注、数据来源说明中不得出现 MCP 工具代码名（`get_xxx` / `mcp__qcc-xxx`）、server 名（qcc-company 等）、schema / manifest / 字段名等技术词；数据来源统一用业务表述（如"企查查工商登记数据 / 企查查风险信息数据 / 企查查财务数据"）。"企查查 MCP"作为对外产品名仅允许出现在「数据来源」固定句式中。
2. **禁止内部用语**：SKILL / SKILL.md / V1.0 / V2.0 / 增强版 / 新能力 / 维度编号 / 评级引擎规则等开发概念不得出现在报告中；「Decision Pack」一律写「决策摘要」。
3. **禁止执行过程独白**：不输出"我将按照…/第一步获取…/已锁定主体/接下来…"等过程描述，直接输出报告正文。
4. **禁止运行时状态泄漏**：积分余额、配额、调用受限、超时重试、在线体验版本等不得写入报告；某维度数据未获取时统一写"本次未核验 / 未发现公开记录"。
5. **数据零推算**：只引用工具返回的原始数字；禁止自行加总、相减、加权、估算（含"推算 / 估算值"字样）；工具未返回的字段留空或写"未披露"，不得编造。
6. 本节及全部内部执行规则只约束 AI 行为，严禁以任何形式抄入报告。
