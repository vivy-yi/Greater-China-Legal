# 完整路由表 — litigation-support 35 skill × 用户意图

> 来源:scene-claudemd-curator `learn-patterns.md` § 0.1(主入口结构)
> 适用:agent 根据用户意图路由到具体 skill
> **CLAUDE.md § 2 路由表是速查版,本文件是完整版**

---

## 0. 路由原则

1. **先问用户"想做什么"和"哪一案件"** —— 不知道就不路由
2. **主入口优先** —— 4 段时序各 1 个主入口,非主入口 skill 不直接路由
3. **关键串接检查** —— 起诉前必先 demand-draft / 立案前必先 matter-intake / 举证前必先 evidence-gathering-advisor / 判决前必先 strategy-designer
4. **应急任务特殊处理** —— 收到传票/律师函/监管处罚 → matter-intake 立即,跳过 demand-draft

---

## 1. 按 4 段时序分组(主入口已标 🔷)

### 1.1 立案阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **matter-intake** | 收到诉状/应诉/立案/对方律师函 | 后接 cause-action-analysis |
| | matter-briefing | 案件简报(律师内部沟通) | 需先 matter-intake |
| | matter-update | 案件状态更新(庭后/调解后) | 需先 matter-intake |
| | cause-action-analysis | 请求权基础分析(案由) | 需先 matter-intake |
| | claim-chart | 证据链归集(要件 → 证据) | 需先 cause-action-analysis |
| | demand-draft | 诉前催告(合同纠纷起诉前) | 起诉前的强制前置 |
| | demand-intake | 收到催告函的应对 | 调解/反驳 |
| | demand-received | 收到对方催告函的应对 | 评估/调解/反诉 |

### 1.2 举证阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **evidence-gathering-advisor** | 证据收集策略 | 后接 evidence-organizer |
| | evidence-organizer | 证据整理(分类/编号) | 需先 evidence-gathering-advisor |
| | chronology | 时间线制作 | 需先 evidence-organizer |
| | deposition-prep | 证人庭前准备 | 需先 evidence-organizer |
| | privilege-log-review | 特权证据审查 | 需先 evidence-organizer |
| | legal-hold | 证据保全(紧急) | 立案后立即可调 |

### 1.3 判决阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **strategy-designer** | 诉讼策略设计 | 后接 brief-section-drafter |
| | brief-section-drafter | 法律文书起草(诉状/答辩/上诉) | 需先 strategy-designer |
| | fee-calculator | 律师费计算 | 独立工具 |
| | litigation-cost-estimator | 诉讼成本估算 | 独立工具 |
| | lawsuit-doc-generator | 起诉状/答辩状生成器 | 需先 strategy-designer |
| | procedure-timeline | 程序时间线查询 | 辅助工具 |

### 1.4 执行阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **execution-obstacle-removal** | 排除执行障碍 | 后接 asset-search-strategy |
| | foreclosure-auction-advisor | 司法拍卖评估 | 需先 execution-obstacle-removal |
| | asset-search-strategy | 财产线索调查 | 需先 execution-obstacle-removal |
| | coercive-measure-assessment | 强制措施评估(拘留/罚款) | 应急使用 |

---

## 2. 按"特殊场景"分组(应急/特殊程序)

| skill | 用户意图 | 严重度 |
|-------|---------|------|
| **admin-penalty-review** | 行政处罚复核(60 天内) | 🔴 紧急 |
| **regulatory-filing-advisor** | 监管备案(反垄断申报等) | 🟡 重要 |
| **appeal-path-checker** | 上诉/再审路径检查 | 🟡 重要 |
| **crime-element-analysis** | 罪状构成分析(刑事) | 🔴 重大 |
| **subpoena-triage** | 收到传票的应急处理 | 🔴 紧急 |
| **government-contract-dispute** | 政府/国资合同纠纷 | 🟡 重要 |
| **penalty-range-calculation** | 量刑/罚款范围计算 | 🟡 重要 |
| **statute-of-limitations** | 诉讼时效核查 | 🔴 关键 |

---

## 3. 按"案件组合管理"分组

| skill | 用户意图 | 备注 |
|-------|---------|------|
| **portfolio-status** | 案件组合状态报告(法务总监视角) | 多个 matter 汇总 |
| **oc-status** | 对方/客户信息状态 | 单方信息汇总 |
| **matter-close** | 案件结案归档 | 完结时使用 |

---

## 4. 关键串接(强制前置)

> agent 路由时**必须检查**这些串接——违反会导致程序瑕疵或败诉风险。

| 强制串接 | 跳过后果 | 例外 |
|--------|--------|------|
| 合同纠纷起诉前 → demand-draft | 调解优先义务未履行 | 紧急案件/对方已失联 |
| 立案前 → matter-intake | 无案件登记/无法追踪 | 应急案件可并行 |
| 举证前 → evidence-gathering-advisor | 证据策略缺失 | 简单案件(标的<10 万) |
| 判决前 → strategy-designer | 诉状缺乏策略 | 缺席判决等程序案件 |
| 涉外诉讼 → 海牙送达公约核查 | 送达无效 | 互惠协议/双边条约 |
| 涉港/澳/台 → 司法协助安排核查 | 判决互认失败 | 仲裁案件 |

---

## 5. 路由决策树(用户意图 → skill)

```
用户输入
  │
  ├─ 关键词:立案/起诉/应诉/对方起诉/收到诉状
  │   └─→ matter-intake 🔷(主入口)
  │
  ├─ 关键词:催告/律师函/通知
  │   ├─ 我方发出 → demand-draft
  │   └─ 收到对方 → demand-received
  │
  ├─ 关键词:证据/取证/举证/收集
  │   └─→ evidence-gathering-advisor 🔷(主入口)
  │
  ├─ 关键词:策略/诉状/起诉状/答辩状/上诉
  │   └─→ strategy-designer 🔷(主入口)
  │
  ├─ 关键词:执行/拍卖/财产/查封
  │   └─→ execution-obstacle-removal 🔷(主入口)
  │
  ├─ 关键词:上诉/再审/时效
  │   ├─ 上诉/再审 → appeal-path-checker
  │   └─ 时效 → statute-of-limitations
  │
  ├─ 关键词:行政处罚/复议/监管
  │   └─→ admin-penalty-review
  │
  ├─ 关键词:刑事/犯罪/逮捕
  │   └─→ crime-element-analysis
  │
  ├─ 关键词:收到传票/对方起诉(应急)
  │   └─→ matter-intake 🔷(主入口,跳过 demand-draft)
  │      路由规则:用户说"收到传票/被起诉/法院通知"
  │      → 直接 matter-intake(不走 demand-draft 催告)
  │      → 应急检查:诉讼时效 + 管辖 + 证据
  │      → 14 天时效压力优先
  │
  ├─ 关键词:仲裁(SIAC/HKIAC/ICC 等)
  │   └─→ matter-intake 🔷(主入口,识别涉外维度)
  │      路由规则:用户说"申请仲裁/约定 SIAC/HKIAC"
  │      → matter-intake(识别涉外)
  │      → 触发 § 5.3 主动问"是否涉外/跨境/涉制裁"
  │      → 升级到跨境律师 + 当地律师
  │      → 仲裁地 + 纽约公约执行双路径
  │
  ├─ 关键词:涉外数据(SaaS/跨境电商)
  │   └─→ matter-intake 🔷(主入口) + PIPL 38-40 路径
  │      路由规则:SaaS/跨境电商/数据处理
  │      → PIPL 38-40 三选一(安全评估/标准合同/认证)
  │      → § 5.3 主动问"数据是否跨境"
  │
  ├─ 关键词:政府/国资/采购
  │   └─→ government-contract-dispute
  │
  ├─ 关键词:案件组合/汇总
  │   └─→ portfolio-status
  │
  ├─ 关键词:结案/归档
  │   └─→ matter-close
  │
  └─ 不确定
      └─→ 主动问用户(5 类主动问见 CLAUDE.md § 5.3)
          - "想做什么?"
          - "涉及哪一案件?"
          - "对方是否已发函/起诉?"
          - "是否涉外?"
          - "标的多少?"
```

---

## 6. 35 skill 总目录(按字母序)

| # | skill | 严重度 | 阶段 |
|---|------|------|------|
| 1 | admin-penalty-review | 🔴 | 特殊(行政) |
| 2 | appeal-path-checker | 🟡 | 特殊(救济) |
| 3 | asset-search-strategy | 🟡 | 执行 |
| 4 | brief-section-drafter | 🟡 | 判决 |
| 5 | cause-action-analysis | 🟡 | 立案 |
| 6 | chronology | 🟢 | 举证 |
| 7 | claim-chart | 🟡 | 立案 |
| 8 | coercive-measure-assessment | 🟡 | 特殊(强制) |
| 9 | crime-element-analysis | 🔴 | 特殊(刑事) |
| 10 | demand-draft | 🟡 | 立案(前置) |
| 11 | demand-intake | 🟢 | 立案(前置) |
| 12 | demand-received | 🟡 | 立案(前置) |
| 13 | deposition-prep | 🟡 | 举证 |
| 14 | evidence-gathering-advisor | 🟡 | 举证(主入口) |
| 15 | evidence-organizer | 🟢 | 举证 |
| 16 | execution-obstacle-removal | 🟡 | 执行(主入口) |
| 17 | fee-calculator | 🟢 | 判决 |
| 18 | foreclosure-auction-advisor | 🟢 | 执行 |
| 19 | government-contract-dispute | 🟡 | 特殊(政府) |
| 20 | lawsuit-doc-generator | 🟡 | 判决 |
| 21 | legal-hold | 🟡 | 举证(应急) |
| 22 | litigation-cost-estimator | 🟢 | 判决 |
| 23 | matter-briefing | 🟢 | 立案 |
| 24 | matter-close | 🟢 | 组合 |
| 25 | matter-intake | 🟡 | 立案(主入口) |
| 26 | matter-update | 🟢 | 立案 |
| 27 | oc-status | 🟢 | 组合 |
| 28 | penalty-range-calculation | 🟡 | 特殊(量刑) |
| 29 | portfolio-status | 🟢 | 组合 |
| 30 | privilege-log-review | 🟡 | 举证 |
| 31 | procedure-timeline | 🟢 | 判决(辅助) |
| 32 | regulatory-filing-advisor | 🟡 | 特殊(监管) |
| 33 | statute-of-limitations | 🔴 | 特殊(时效) |
| 34 | strategy-designer | 🟡 | 判决(主入口) |
| 35 | subpoena-triage | 🔴 | 特殊(仲裁/传票) |

---

## 7. 与 CLAUDE.md § 2 的关系

- **§ 2 路由表**:速查版(15 个高频意图)
- **本文件**:完整版(35 skill + 决策树 + 串接检查)
- **更新**:新增 skill → 加到本文件 + § 2

---

*Greater China Legal — litigation-support 完整路由表 v1.0.0*
*scene-claudemd-curator § 0.1 主入口结构 适配*
*最后更新:2026-06*
