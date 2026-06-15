> 企业画像速览 SKILL · 企查查 MCP V2.0 增强版。
> PE / VC / FA 在 LP 推介前、项目初步筛选、内部立项汇报等场景的轻量尽调工具。3 分钟生成一页纸企业画像，整合工商登记、核心风险信号、知识产权资产、V2.0 主体延续性、核心管理层概要五大板块，以结构化方式呈现企业基本面。
>
> 核心能力：
> - 基础工商核验 + 主体延续性（V2.0 新能力，qcc-history 治理稳定性回溯）
> - 核心风险标签：1 页内呈现失信 / 限高 / 被执行 / 股权冻结等关键风险信号
> - 知识产权资产概览 + 知产出质（V2.0 新工具）
> - 核心管理层概要：实控人 + 法代 + 核心高管姓名与简要画像
> - 融资与经营活跃度：融资记录 + 招聘活跃度 + 荣誉信息
>
> 适用场景：LP 推介前 5 分钟了解目标公司全貌 / 项目初步筛选 / 内部立项汇报 / 投资分析师快速背调 / 投资经理每日浏览池。
>
> 使用方式：/strip-profile-qcc 企业名称 [--depth quick|standard] [--format md|docx|pptx]
>
> **风险核查采用「先扫后钻」**：先通过企业风险全量扫描一次性分诊 35 项风险维度、快速定位命中项，再对命中维度深入取证——既不漏维度，也避免逐项无效查询。

**命令**：`/strip-profile-qcc` · **MCP 工具集**：`qcc-company, qcc-risk, qcc-ipr, qcc-history, qcc-executive, qcc-operation`

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

# 企业画像速览 · 企查查 MCP V2.0 增强版

## SKILL 定位

本 SKILL 服务于投资类场景的"快速筛查"——在 IC Memo 之前、DD 之前，投资团队常常需要对大量项目做"5 分钟扫一眼"式筛查。企业画像速览就是这种场景的标准工具：输入公司名，5 分钟内输出一张结构化的"公司身份卡"，让投资经理快速判断"这家公司是否值得进入 DD 阶段"。

V2.0 相对 V1.0 的升级在两个方面：
- **主体延续性维度**（qcc-history）—— 画像表上增加"治理稳定性"一行，识别"频繁变更"的高风险企业
- **核心管理层概要**（qcc-executive）—— 画像表上增加"创始人速览"一行，3 秒内判断实控人是否清洁

## MCP 依赖与配置

必选：
- `qcc-company`（企业基座）—— 工商基础 + 股东 + 实控人
- `qcc-risk`（风控大脑）—— 核心风险标签

强烈建议：
- `qcc-history`（历史存档）—— 主体延续性
- `qcc-executive`（人员画像）—— 核心管理层快扫

可选：
- `qcc-ipr`（知产引擎）—— IP 资产概览
- `qcc-operation`（经营罗盘）—— 融资、荣誉、招聘活跃度

## 通用执行原则

**第一，轻量快速是第一目标。** 画像速览不是 IC Memo。要在 1-2 页（500-800 字）内让读者快速抓到"主体真实性 + 核心风险 + 关键人物 + IP 数量 + 融资轮次"五项核心信息，**不做深度推演**。

**第二，信息密度优先于文字包装。** 推荐用表格而非段落。每个指标一行，最多一句话解读。

**第三，主体延续性是新加入的结构化维度。** 治理稳定 / 不稳定 / 高度不稳定三档标签，不做深入分析——如读者想深入，进入下一层的 IC Memo / KYB。

**第四，创始人画像做"轻扫"而非"深扫"。** 只看 4 项核心红线（失信 / 限高 / 被执行 / 限出境）是否触发，不做完整 18 维扫描。

**第五，明确告知"可用于初步筛查不可用于投资决策"。** 画像速览定位决定了其深度——如进入正式投资决策阶段，必须升级到 IC Memo + KYB + 专项 DD 工作。

## 工作流

### 维度一：基础工商 × 主体延续性（V2.0 加强）

工具链：
- `mcp__qcc-company__get_company_registration_info`
- `mcp__qcc-company__get_shareholder_info`
- `mcp__qcc-company__get_actual_controller`
- `mcp__qcc-history__get_historical_legal_rep` / `get_historical_registration`

**速览输出**：
- 全称 + USCC
- 成立日期 + 注册资本（实缴）
- 登记状态
- 所属地区 + 行业
- 实控人 + 持股比例
- **治理稳定性标签**（V2.0 新）：稳定 / 不稳定 / 高度不稳定

### 维度二：核心风险标签

工具链：
- `mcp__qcc-risk__get_dishonest_info` / `get_judgment_debtor_info` / `get_high_consumption_restriction` / `get_equity_freeze` / `get_business_exception` / `get_tax_arrears_notice` / `get_administrative_penalty`

**速览输出 6 色标签**：
- 🟢 失信 0
- 🟢 被执行 0
- 🟢 限高 0
- 🟢 股权冻结 0
- 🟢 经营异常 0
- 🟡 行政处罚 N（有则列数量）

### 维度三：知识产权资产概览

工具链：
- `mcp__qcc-ipr__get_patent_info`（总数）
- `mcp__qcc-ipr__get_trademark_info`（总数）
- `mcp__qcc-ipr__get_software_copyright_info`（总数）
- `mcp__qcc-ipr__get_ipr_pledge`（V2.0 新工具，是否有知产出质）

**速览输出**：
- 专利 N 件 / 商标 N 件 / 软著 N 件 / 域名 N 个
- 知产出质：有 / 无（V2.0 新指标）

### 维度四：核心管理层速览（V2.0 新能力）

**【个人风险先扫后钻 · 2026-06-08 · 对齐 A 层铁律 5 个人维度】** 对每位目标人（法代/实控人/董监高），**先调 `mcp__qcc-executive__get_executive_risk_scan`（searchKey=企业完整名/USCC + personName=姓名，双锚定）一次返回其 18 项个人风险维度命中计数 → 仅对 count>0 维度下钻下列对应 `get_executive_*` 原子工具取明细**；count=0 跳过。❌ 禁止不先扫、逐个散弹枪调个人风险原子。单人工具：多人则逐人各扫一次，不对全体董监高自动循环。
对实控人 + 法代做 4 项红线快扫：
- `mcp__qcc-executive__get_executive_dishonest`
- `mcp__qcc-executive__get_executive_high_consumption_ban`
- `mcp__qcc-executive__get_executive_judgment_debtor`
- `mcp__qcc-executive__get_executive_exit_restriction`

**速览输出**：
- 实控人姓名 + 4 项红线扫描结果（全绿 / 有红）
- 法代姓名 + 红线扫描结果
- 如两人非同一人，各扫一遍

### 维度五：融资与经营活跃度

工具链：
- `mcp__qcc-operation__get_financing_records`（融资历史）
- `mcp__qcc-operation__get_recruitment_info`（招聘活跃度）
- `mcp__qcc-operation__get_honor_info`（荣誉）

**速览输出**：
- 最近融资轮次 + 金额 + 时间 + 投资方
- 招聘活跃度（近 3 月职位数）
- 荣誉：高新技术企业 / 专精特新 / 国家级 / 省级 等关键标签

## 画像速览标准模板（一页纸格式）

```
┌─────────────────────────────────────────────────────┐
│  【企业画像速览】目标公司名称                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ▎基础信息                                           │
│    USCC：___  成立：___  注册资本：___               │
│    行业：___  地区：___  登记状态：___               │
│    实控人：___（持股 __%）                           │
│    治理稳定性（V2.0）：🟢 稳定 / 🟡 不稳定 / 🔴 高度不稳定 │
│                                                     │
│  ▎核心风险标签                                       │
│    🟢 失信 0  🟢 被执行 0  🟢 限高 0                │
│    🟢 股权冻结 0  🟢 经营异常 0  🟡 行政处罚 N      │
│                                                     │
│  ▎知识产权（V2.0 + 知产出质）                        │
│    专利 N 件  商标 N 件  软著 N 件                   │
│    知产出质：🟢 无 / 🔴 有                          │
│                                                     │
│  ▎核心管理层速览（V2.0 新）                         │
│    实控人 ___（4 项红线）：🟢 / 🔴                   │
│    法代 ___（4 项红线）：🟢 / 🔴                    │
│                                                     │
│  ▎融资与活跃度                                       │
│    最近融资：__ 轮（__ 万 __ 年 __ 月）             │
│    投资方：___                                       │
│    招聘活跃度：近 3 月 N 个职位                      │
│    荣誉：__                                          │
│                                                     │
│  ▎一句话结论（由 AI 基于上述数据生成）               │
│    "___"                                            │
└─────────────────────────────────────────────────────┘

## 参数

- `--depth <quick|standard>`：quick（默认）仅 4 红线 + 基础工商；standard 涵盖所有维度
- `--format md|docx|pptx`：输出格式，默认 md；pptx 为一页 PPT 速览模板

## 边界与免责

画像速览仅供"初步筛查 / 立项前浏览 / LP 推介前准备"场景。**不得**作为投资决策依据——任何投资决策应基于 IC Memo + KYB + 专项 DD 的完整尽调流程。

---

**SKILL 版本**：v2.0（MCP V2.0 升级版）
**适配 MCP 版本**：146 工具 / 6 Server 全量版
**所需 Server**：qcc-company（必选）、qcc-risk（必选）、qcc-history（建议）、qcc-executive（建议）、qcc-ipr（可选）、qcc-operation（可选）

---

## 报告输出纪律（内部规则 · 严禁出现在最终报告中）

1. **一律业务语言**：报告正文、备注、数据来源说明中不得出现 MCP 工具代码名（`get_xxx` / `mcp__qcc-xxx`）、server 名（qcc-company 等）、schema / manifest / 字段名等技术词；数据来源统一用业务表述（如"企查查工商登记数据 / 企查查风险信息数据 / 企查查财务数据"）。"企查查 MCP"作为对外产品名仅允许出现在「数据来源」固定句式中。
2. **禁止内部用语**：SKILL / SKILL.md / V1.0 / V2.0 / 增强版 / 新能力 / 维度编号 / 评级引擎规则等开发概念不得出现在报告中；「Decision Pack」一律写「决策摘要」。
3. **禁止执行过程独白**：不输出"我将按照…/第一步获取…/已锁定主体/接下来…"等过程描述，直接输出报告正文。
4. **禁止运行时状态泄漏**：积分余额、配额、调用受限、超时重试、在线体验版本等不得写入报告；某维度数据未获取时统一写"本次未核验 / 未发现公开记录"。
5. **数据零推算**：只引用工具返回的原始数字；禁止自行加总、相减、加权、估算（含"推算 / 估算值"字样）；工具未返回的字段留空或写"未披露"，不得编造。
6. 本节及全部内部执行规则只约束 AI 行为，严禁以任何形式抄入报告。
