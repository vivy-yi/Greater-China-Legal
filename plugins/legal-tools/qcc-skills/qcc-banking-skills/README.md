---
title: 企查查银行客群 SKILL 集（12 个）
description: >
  企查查银行 · 合规风控客群的 12 个 SKILL 完整本地副本。
  涵盖 KYB 开户合规 / 授信尽调 / 反洗钱穿透 / 贸易融资合规 / 贷后风险监控。
  完整 SKILL.md 已下载到本目录，可作为 GCL 企业尽调类场景的补充知识。
last_reviewed: 2026-06
source: https://agent.qcc.com/skill/v1/banking/README.md
---

# 企查查银行客群 SKILL 集（12 个）

> 数据源：https://agent.qcc.com/skill/v1/banking/README.md
> 客群定位：🏦 银行 · 合规风控（KYB / 授信 / 反洗钱 / 贷后）

## 12 个 SKILL 完整列表

| # | 技能 | 命令 | 核心场景 | 工具集 |
|---|------|------|---------|--------|
| 1 | KYB 企业核验 | `/kyb-verification-qcc` | 贷款申请后 AI 自动执行主体核验 + 关联风险扫描，约 3 分钟出报告 | qcc-company, qcc-risk, qcc-history, qcc-executive, qcc-operation |
| 2 | 诉讼风险评估 | `/litigation-analysis-qcc` | 诉讼前评估对手方 10 年诉讼轨迹 + 核心人员个人司法画像 | qcc-company, qcc-risk, qcc-executive |
| 3 | 授信尽调报告 | `/credit-due-diligence-qcc` | 信贷审批流程中的企业全维度尽调 | 全部 6 个 server |
| 4 | 交易对手风险评估 | `/counterparty-risk-qcc` | 贸易融资业务中对交易对手的多维风险评估 | qcc-company, qcc-risk, qcc-operation |
| 5 | 受益所有人识别 | `/ubo-screening-qcc` | 对公开户、高净值客户尽调与反洗钱日常筛查 | qcc-company, qcc-executive, qcc-history |
| 6 | 贸易融资合规核查 | `/trade-finance-compliance-qcc` | 跨境贸易与国际结算场景下的合规准入 | qcc-company, qcc-operation, qcc-risk |
| 7 | 信贷风险定期监控 | `/credit-monitoring-qcc` | 贷后管理中对存量借款客户的持续风险监控 | qcc-company, qcc-risk, qcc-history |
| 8 | 股权结构穿透分析 | `/equity-structure-qcc` | 投资决策前的控制权核查 | qcc-company, qcc-executive, qcc-history |
| 9 | 高管背景核查 | `/executive-background-qcc` | 投前对法代/实控人/董事长做 30+ 维度个人司法画像 | qcc-executive, qcc-risk, qcc-company |
| 10 | 经营健康度扫描 | `/business-health-scan-qcc` | 企业经营状态的动态追踪 | qcc-company, qcc-operation, qcc-ipr |
| 11 | 担保方资信核查 | `/guarantor-check-qcc` | 贷款担保审批前的资信核查 | qcc-company, qcc-risk, qcc-executive |
| 12 | 企业破产预警监控 | `/bankruptcy-monitor-qcc` | 债权管理中的破产风险持续监控 | qcc-company, qcc-risk, qcc-history |

## 与 GCL 场景的映射

| QCC SKILL | GCL 对应场景 | 替代/补充 |
|-----------|-------------|-----------|
| KYB 企业核验 | `contract-review`, `m-and-a` | 替代/补充尽职调查 |
| 诉讼风险评估 | `litigation-support`, `commercial-arbitration` | 案件对手方分析 |
| 授信尽调报告 | `m-and-a`, `financing-business` | 完整尽调报告 |
| 交易对手风险评估 | `contract-review` | 合同签约前主体核验 |
| 受益所有人识别 | `corporate-governance` | UBO 穿透 |
| 贸易融资合规 | `cross-border-trade` | 跨境贸易尽调 |
| 信贷风险定期监控 | `financing-business` | 贷后监控 |
| 股权结构穿透 | `m-and-a`, `corporate-governance` | 股权图谱 |
| 高管背景核查 | `m-and-a`, `corporate-governance` | 高管风险 |
| 经营健康度扫描 | `m-and-a` | 经营状态 |
| 担保方资信核查 | `financing-business` | 担保审查 |
| 企业破产预警 | `bankruptcy-restructuring` | 破产预警 |

## 关键技术模式：先扫后钻

QCC SKILL 普遍采用的 5-A 铁律：

```
1. 第 1 步 · 分诊（先扫）
   → 调 mcp__qcc-risk__get_company_risk_scan
   → 一次性分诊 35 项风险维度（脱水版：有/无 + 条数）
   
2. 第 2 步 · 下钻（后钻）
   → 仅对 count > 0 的维度调对应原子工具取明细
   
3. count = 0 的维度
   → 直接判定"无记录"，不再调用该维度原子工具
   
4. 明确单一维度问句
   → 直接调对应原子工具，无需先扫
   
5. scan 只分诊、不出明细
   → 要明细必须下钻原子工具
   → 风险结论只陈述"命中维度 + 计数/明细"客观事实
   → 不替客户判定"能不能合作/可不可开户"
```

## 文件结构

```
qcc-banking-skills/
├── README.md                              ← 本文件
├── kyb-verification-qcc.md
├── litigation-analysis-qcc.md
├── credit-due-diligence-qcc.md
├── counterparty-risk-qcc.md
├── ubo-screening-qcc.md
├── trade-finance-compliance-qcc.md
├── credit-monitoring-qcc.md
├── equity-structure-qcc.md
├── executive-background-qcc.md
├── business-health-scan-qcc.md
├── guarantor-check-qcc.md
└── bankruptcy-monitor-qcc.md
```

## 使用建议

GCL 集成时：

1. **直接复用**——12 个 SKILL.md 已经是完整的 AI 可执行规则
2. **引用方式**——在 GCL 场景的 SKILL.md 中用 `data_source: qcc-banking-skills` 引用
3. **优先级**——付费 QCC MCP 启用时，AI 自动按 SKILL 流程执行；未启用时，AI 按通用兜底执行

---

*Greater China Legal — gcl-data-service reference: 企查查银行客群 SKILL*
*源文档：https://agent.qcc.com/skill/v1/banking/README.md*
*下载时间：2026-06-15*
