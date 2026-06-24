> 授信尽调报告 SKILL · 企查查 MCP V2.0 增强版。
> 信贷审批放款前的全维度企业尽调工具。输入目标企业全称后，自动完成工商核验、真实财务底盘、司法风险扫描、信用修复追溯、实控人个人风险五位一体的授信风险画像，输出可直接归档的授信决策底稿。
>
> 核心能力：
> - 真实财务底盘：`get_financial_data` 首次引入授信场景，直接返回 3 年完整财报（资产负债率 / 速动比率 / 所有者权益 / 经营现金流），告别旧版仅靠事件信号推断偿债
> - 信用修复追溯：qcc-history 14 个历史风险工具识别"修复型主体 vs 连年失信型"，对评级起决定性作用
> - 实控人 × 法代个人兜底能力评估：qcc-executive 核心工具快扫，识别"企业清洁、实控人出险"的隐性风险
> - 授信评级 × 建议授信额度 × 风险缓释条款：输出可直接进入信贷审批委员会的决策材料
>
> 适用场景：银行对公贷款审批 / 供应链金融授信 / 融资租赁风控 / 保理业务准入 / 流贷 × 项目贷 × 并购贷预审。
>
> 使用方式：/credit-due-diligence 企业名称 [--amount 授信金额] [--tenor 授信期限] [--type 流贷|项目贷|并购贷] [--format md|docx|pptx]
>
> **风险核查采用「先扫后钻」**：先通过企业风险全量扫描一次性分诊 35 项风险维度、快速定位命中项，再对命中维度深入取证——既不漏维度，也避免逐项无效查询。

**命令**：`/credit-due-diligence` · **MCP 工具集**：`qcc-company, qcc-risk, qcc-history, qcc-executive`

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

# 授信尽调报告 · 企查查 MCP V2.0 增强版

## SKILL 定位

本 SKILL 服务于银行对公贷款审批、供应链金融授信、融资租赁风控、保理业务准入等场景的放款前企业尽调需求。输入目标企业全称或统一社会信用代码后，SKILL 自动串联 qcc-company / qcc-risk / qcc-history / qcc-executive 四大 MCP Server，执行"工商核验 × 真实财务底盘 × 司法风险扫描 × 信用修复追溯 × 实控人个人风险"五位一体的授信画像，最终输出可直接归档的标准化授信尽调底稿。

相对 V1.0 版本的最大跃迁在于两点：第一，`get_financial_data` 让授信评估第一次能拿到真实的资产负债率 / 速动比率 / 所有者权益等硬指标，从"靠事件信号推断"升级为"有数据可算"；第二，qcc-history 的 14 个历史风险工具让 SKILL 能够识别"曾经出险但已履行"的修复型主体与"连年失信"的高危主体，这对评级阈值的设定具有决定性意义。

## MCP 依赖与配置

必选：
- `qcc-company`（企业基座）—— 工商登记、股东、实控人、对外投资、**get_financial_data**
- `qcc-risk`（风控大脑）—— 失信、被执行、限高、终本、股权冻结、股权质押、动产抵押

强烈建议：
- `qcc-history`（历史存档）—— 识别信用修复模式，影响评级阈值
- `qcc-executive`（人员画像）—— 法代 + 实控人个人画像，识别"企业清洁 × 个人出险"的隐性风险

## 通用执行原则

**第一，财务硬指标先行，事件信号为辅。** V2.0 有了真实财报数据后，偿债能力评估的主路径是"资产负债率 / 流动比率 / 速动比率 / 有息负债 / EBITDA"五项核心比率，司法事件仅作为交叉验证。如果 `get_financial_data` 返回空（非上市小微），SKILL 需明示"无直接财务数据"并在评级上下调一级做保守处理。

**第二，历史修复必须加权评估。** 5 年内的历史失信或被执行即便已履行，仍须在评级中起保守作用（相对无历史记录的主体下调半级）；10 年以上的历史事件可归入"历史标注"层，不触发评级调整。

**第三，实控人个人兜底单独评估。** 企业授信的最后一条防线是实控人个人偿债能力与其他关联企业的资产池。凡原告债权金额超过企业近 3 年累计净利润的情境，均须对实控人做完整个人画像扫描，不得省略。

**第四，授信金额与风险敞口必须对比注册资本。** 拟授信金额占注册资本比例超过 20% 即需引发内部授信委员会特别审议；超过 50% 原则上不建议普通流贷，改走项目贷或增加担保。

**第五，数据时效明示。** 所有 MCP 数据均须附采集时间戳。授信决策前 48 小时内须复核一次企业主体侧的重要负面信号（新增失信 / 限高 / 被执行 / 经营异常等）。

## 工作流

### 维度一：主体工商核验与实控人穿透

工具链：
- `mcp__qcc-company__get_company_registration_info` — 工商登记信息（全称、USCC、法代、成立日期、注册资本、登记状态）
- `mcp__qcc-company__verify_company_accuracy` — 企业名称 + 统一社会信用代码二要素一致性核验
- `mcp__qcc-company__get_shareholder_info` — 股东结构
- `mcp__qcc-company__get_actual_controller` — 实际控制人穿透链路
- `mcp__qcc-company__get_key_personnel` — 主要人员名单（为维度五铺垫）

产出：《主体身份档案》——企业全称、USCC、法代、成立年限、登记状态、注册资本与实缴率、股权结构简图、实控人识别。

### 维度二：真实财务底盘（V2.0 核心新能力）

工具链：
- `mcp__qcc-company__get_financial_data` —— **V2.0 新工具**，返回 3 年完整财报（利润表 + 资产负债表 + 现金流量表 + 盈利/偿还/营运/成长能力四类比率）
- `mcp__qcc-company__get_annual_reports` —— 企业年报（作为 `get_financial_data` 的补充）
- `mcp__qcc-company__get_tax_invoice_info` —— 税号信息（为税务合规性铺垫）

核心偿债比率矩阵：

| 指标 | 行业正常值 | 警戒线 | 致命线 |
|------|-----------|-------|-------|
| 资产负债率 | < 70% | 70-90% | > 100%（资不抵债） |
| 流动比率 | > 1.5 | 1.0-1.5 | < 1.0 |
| 速动比率 | > 1.0 | 0.5-1.0 | < 0.3 |
| 有息负债 / EBITDA | < 3 倍 | 3-5 倍 | > 5 倍 |
| 经营现金流 | 正 | 微正或微负 | 持续负 |

分析要点：任何一项触及致命线即直接触发 D 级评级。三项以上触及警戒线则下调至少一级。成长能力指标（营收同比 / 总资产同比）若连续两年为负，授信额度建议不超过其近 3 年平均净利润的 50%。

### 维度三：司法风险扫描

工具链（当前层）：
- `mcp__qcc-risk__get_dishonest_info` — 失信被执行人
- `mcp__qcc-risk__get_judgment_debtor_info` — 被执行人
- `mcp__qcc-risk__get_high_consumption_restriction` — 限制高消费
- `mcp__qcc-risk__get_terminated_cases` — 终本案件
- `mcp__qcc-risk__get_equity_freeze` — 股权冻结
- `mcp__qcc-risk__get_equity_pledge_info` — 股权出质
- `mcp__qcc-risk__get_chattel_mortgage_info` — 动产抵押
- `mcp__qcc-risk__get_land_mortgage_info` — 土地抵押
- `mcp__qcc-risk__get_tax_arrears_notice` — 欠税公告
- `mcp__qcc-risk__get_business_exception` — 经营异常

分析要点：

- 当前失信 1 条即触发 D 级；当前限高生效直接触发 C 级
- 股权出质 + 股权冻结是"融资已枯竭"信号，需在授信额度中相应扣减
- 欠税公告是"税务合规瑕疵"信号，影响税收优惠资格判定
- 对外担保余额（`get_guarantee_info`）须作为表外负债纳入总负债计算

### 维度四：信用修复追溯（V2.0 新能力）

工具链（历史层）：
- `mcp__qcc-history__get_historical_dishonest` — 历史失信（已移出）
- `mcp__qcc-history__get_historical_judgment_debtor` — 历史被执行
- `mcp__qcc-history__get_historical_high_consumption_ban` — 历史限高
- `mcp__qcc-history__get_historical_terminated_cases` — 历史终本
- `mcp__qcc-history__get_historical_equity_freeze` — 历史股权冻结
- `mcp__qcc-history__get_historical_tax_arrears` — 历史欠税
- `mcp__qcc-history__get_historical_business_exception` — 历史经营异常
- `mcp__qcc-history__get_historical_admin_penalty` — 历史行政处罚

分析要点（5 种偿债模式识别）：

- **模式 A · 始终清洁型**（10 年零失信零被执行）：授信评级上浮半级
- **模式 B · 修复型**（5-10 年前曾出险但已修复 + 近 3 年清洁）：维持标准评级
- **模式 C · 间歇失信型**（每 2-3 年一轮）：评级下调一级
- **模式 D · 连年失信型**（近 5 年每年都有新增失信）：直接触发 D 级
- **模式 E · 集中爆发型**（近 12-24 月突发）：进入增强监测 + 评级至少 C 级

### 维度五：实控人 × 法代个人风险

**【个人风险先扫后钻 · 2026-06-08 · 对齐 A 层铁律 5 个人维度】** 对每位目标人（法代/实控人/董监高），**先调 `mcp__qcc-executive__get_executive_risk_scan`（searchKey=企业完整名/USCC + personName=姓名，双锚定）一次返回其 18 项个人风险维度命中计数 → 仅对 count>0 维度下钻下列对应 `get_executive_*` 原子工具取明细**；count=0 跳过。❌ 禁止不先扫、逐个散弹枪调个人风险原子。单人工具：多人则逐人各扫一次，不对全体董监高自动循环。
工具链（对法代和实控人分别扫描）：
- `mcp__qcc-executive__get_executive_dishonest` — 个人失信
- `mcp__qcc-executive__get_executive_high_consumption_ban` — 个人限高
- `mcp__qcc-executive__get_executive_judgment_debtor` — 个人被执行
- `mcp__qcc-executive__get_executive_exit_restriction` — 个人限制出境
- `mcp__qcc-executive__get_executive_controlled_companies` — 个人其他控制企业
- `mcp__qcc-executive__get_executive_investments` — 个人对外投资
- `mcp__qcc-executive__get_executive_historical_dishonest` — 个人历史失信

分析要点：

- 实控人 / 法代任何一人当前失信直接触发 D 级
- 实控人限制出境是"跑路风险"最强信号——直接 D 级 + 拒绝授信
- 实控人控制的其他企业如有 3 家以上处于失信 / 被执行状态，整个授信建议重新评估：该实控人存在"连环担保、互保"风险
- 如法代与实控人为不同自然人，法代若为"职业清算人型"（MCP 零负面 + 任职时间短），说明企业可能处于清算或壳化阶段，评级至少下调两级

## 综合授信评级 × 建议授信额度 × 风险缓释

### 评级体系（A/B/C/D 四级）

| 评级 | 核心标准 | 授信建议 |
|------|---------|---------|
| **A 级** | 财务五项比率全部达标 + 无任何当前司法风险 + 实控人清洁 + 历史清洁或已修复 10 年以上 | 可正常授信，额度上限为近 3 年平均净利润 × 3 |
| **B 级** | 财务一项达警戒线（非致命）+ 近 3 年清洁 + 历史有已修复事件 + 实控人清洁 | 可授信但加强监测，额度为 A 级的 60-80%，增加一道风险缓释 |
| **C 级** | 财务两项以上警戒线 或 历史间歇失信 或 实控人历史已修复事件 | 谨慎授信，要求强担保（土地抵押 / 保证金 / 应收账款质押），额度为 A 级的 30-50% |
| **D 级** | 任何致命线触发 或 当前失信 / 限高 / 资不抵债 或 实控人出险 | **不建议授信**，或仅做担保类短期业务 |

### 授信额度建议公式

```
基础额度 = MIN(
  近 3 年平均净利润 × 3,
  净资产 × 30%,
  年营收 × 10%
)

调整后额度 = 基础额度 × 评级系数
  评级系数：A = 1.0 / B = 0.7 / C = 0.4 / D = 0 或担保类
```

### 风险缓释条款建议

A 级：可信用贷款，仅需基础财务承诺条款
B 级：要求实控人个人连带责任保证 + 关键财务承诺（资产负债率上限、对外担保余额上限）
C 级：要求土地抵押 / 应收账款质押 + 实控人连带责任 + 交叉违约条款 + 财务季报
D 级：放弃信用类授信，仅做全额保证金业务或不开展

## 输出模板

- 章节 1：**执行摘要 · 决策摘要**（评级 + 建议授信额度 + 关键风险信号 + T+0/T+3/T+7 Action）
- 章节 2：数据来源与互证方法
- 章节 3：主体身份档案
- 章节 4：**真实财务底盘**（`get_financial_data` 3 年对比 + 核心比率矩阵）
- 章节 5：司法风险扫描（当前层 × 历史层双层）
- 章节 6：信用修复追溯与偿债模式识别
- 章节 7：实控人与法代个人风险
- 章节 8：综合评级 × 授信额度 × 风险缓释条款
- 章节 9：数据来源、采集时间戳、免责声明

## 参数

- `--amount <金额>`：拟授信金额（必填）—— 用于授信敞口 / 注册资本比率测算
- `--tenor <期限>`：授信期限（1 年 / 3 年 / 5 年）—— 长期限授信对资产负债率警戒线更严格
- `--type <类型>`：授信类型（流贷 / 项目贷 / 并购贷 / 供应链金融）
- `--format md|docx|pptx`：输出格式，默认 md

## 边界与免责

本 SKILL 基于企查查 MCP 公开工商 + 财务 + 司法数据生成。`get_financial_data` 返回的财务数据来源于企业年报披露，对非上市小微企业可能返回空，此时 SKILL 会明示并保守处理。

授信决策涉及宏观经济、行业周期、政策导向等多维度因素，本 SKILL 仅提供基于单企业主体侧的尽调材料，不构成对市场风险、利率风险、汇率风险等宏观维度的判断。

最终授信决策应由所在机构的信贷审批委员会 / 风险管理委员会综合评审，本 SKILL 输出仅为决策支持材料。

---

**SKILL 版本**：v2.0（MCP V2.0 升级版）
**适配 MCP 版本**：146 工具 / 6 Server 全量版
**所需 Server**：qcc-company（必选）、qcc-risk（必选）、qcc-history（强烈建议）、qcc-executive（强烈建议）


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
