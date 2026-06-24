---
name: competitor-analysis-qcc
description: >
  TODO: 待补充 description（YAML 安全的描述）
legal_frame: cn-mainland
last_reviewed: 2026-06-24
version: 1.0.0
risk_level: low
trigger_phrases:
  - competitor-analysis-qcc
---

> 竞品对比分析 SKILL · 企查查 MCP V2.0 增强版。
> 两家或多家竞争企业的横向对比分析工具，输出"领先者 / 追赶者 / 掉队者"三档评级。
>
> 核心能力：
> - **基础规模对比**：注册资本、参保人数、成立年数、登记状态等工商基础维度（`mcp__qcc-company__get_company_registration_info`）
> - **V2.0 真实财报对比**（`mcp__qcc-company__get_financial_data`）—— 营收、毛利率、资产负债率三年同比，告别仅靠注册资本推断
> - **融资历史对比**（`mcp__qcc-operation__get_financing_records` + `mcp__qcc-history__get_historical_shareholders`）—— 还原融资节奏与估值锚
> - **V2.0 历史专利 / 商标轨迹**（`mcp__qcc-history__get_historical_patent` / `get_historical_trademark`）—— 技术积累曲线对比
> - 司法风险对比（失信 / 限高 / 经营异常 / 行政处罚等多维风险信号）
> - 核心团队稳定性对比（创始团队任职稳定性、关键人员流失轨迹）
>
> 适用场景：投前竞品分析 / 投资团队市场调研 / 行业护城河量化 / 战略研究 / 同业 benchmark。
>
> 使用方式：/competitor-analysis 企业名称 1, 企业名称 2, ... [--format md|docx|pptx]

**命令**：`/competitor-analysis` · **MCP 工具集**：`qcc-company, qcc-risk, qcc-history, qcc-executive, qcc-operation`

---

# 竞品对比分析 · 企查查 MCP V2.0 增强版

## SKILL 定位

两家或多家竞争企业的横向对比分析。V2.0 新增双方真实财报 + 历史专利商标两层能力。

## 工作流维度

1. 基础规模对比（注册资本 / 参保 / 成立年数）
2. **V2.0 新能力：双方财报对比**（get_financial_data —— 营收 / 毛利率 / 资产负债率对比）
3. 融资历史对比（get_financing_records + get_historical_shareholders）
4. **V2.0 新能力：历史专利 / 商标**（qcc-history —— 技术积累曲线对比）
5. 司法风险对比
6. 核心团队对比（创始团队稳定性）

## 评级

领先者 / 追赶者 / 掉队者



## MCP 依赖

- 必选：qcc-company / qcc-risk
- V2.0 强烈建议：qcc-history / qcc-executive / qcc-operation / qcc-ipr（视场景）

## 输出模板

- 章节 1：决策摘要（评级 + 关键判断 + 推荐 Action）
- 章节 2：数据来源
- 章节 3-7：各维度扫描结果
- 章节 8：V2.0 能力增量说明
- 章节 9：综合评级 × 处置建议

## 参数

- `--format md|docx|pptx`：输出格式，默认 md

## 边界与免责

本 SKILL 基于企查查 MCP V2.0 公开数据生成，不替代专业财务审计 / 律师尽调 / 技术评估。


**SKILL 版本**：v2.0 | **适配 MCP 版本**：146 工具 / 6 Server 全量

---

## 报告输出纪律（内部规则 · 严禁出现在最终报告中）

1. **一律业务语言**：报告正文、备注、数据来源说明中不得出现 MCP 工具代码名（`get_xxx` / `mcp__qcc-xxx`）、server 名（qcc-company 等）、schema / manifest / 字段名等技术词；数据来源统一用业务表述（如"企查查工商登记数据 / 企查查风险信息数据 / 企查查财务数据"）。"企查查 MCP"作为对外产品名仅允许出现在「数据来源」固定句式中。
2. **禁止内部用语**：SKILL / SKILL.md / V1.0 / V2.0 / 增强版 / 新能力 / 维度编号 / 评级引擎规则等开发概念不得出现在报告中；「Decision Pack」一律写「决策摘要」。
3. **禁止执行过程独白**：不输出"我将按照…/第一步获取…/已锁定主体/接下来…"等过程描述，直接输出报告正文。
4. **禁止运行时状态泄漏**：积分余额、配额、调用受限、超时重试、在线体验版本等不得写入报告；某维度数据未获取时统一写"本次未核验 / 未发现公开记录"。
5. **数据零推算**：只引用工具返回的原始数字；禁止自行加总、相减、加权、估算（含"推算 / 估算值"字样）；工具未返回的字段留空或写"未披露"，不得编造。
6. 本节及全部内部执行规则只约束 AI 行为，严禁以任何形式抄入报告。
