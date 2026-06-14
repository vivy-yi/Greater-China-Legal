<!--
Greater China Legal — Regulatory Compliance Scene Configuration
===============================================================

本文件为 regulatory-compliance 场景的运行时配置。
Skill执行时会读取此文件获取场景级上下文，用于定制化输出。
-->

# Regulatory Compliance Scene — Practice Profile

*Written for: [公司名称] · 场景：行业监管合规*
*Last updated: 2026-06*

---

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
**主营业务/行业：** [填空：金融/医药/电信/互联网/环保/制造/其他]
**监管机构：** [填空：主管监管机构名称]
**牌照/许可证清单：** [填空：已持有的行业准入许可]
**合规负责人：** [填空：姓名/联系方式]
**外部合规律师：** [填空：联系方式]

---

## 覆盖的行业监管领域

| 领域 | 场景 | 主管机关 |
|---|---|---|
| 金融监管 | 银行/证券/保险 | 金融监管总局/央行/证监会 |
| 医药医疗 | 药品/医疗器械/GMP | 药监局(NMPA)/卫健委 |
| 电信互联网 | ICP/IDC/增值电信 | 工信部(MIIT)/网信办(CAC) |
| 环保安全 | 环评/危化品/安全生产 | 生态环境部/应急管理部 |
| 反洗钱(AML/KYC) | 客户尽职调查/可疑交易 | 央行/金融监管总局 |

---

## 数据源配置

| 优先级 | 数据源 | 用途 |
|---|---|---|
| 1 | yuandian MCP | 行业法规/监管规定/处罚案例 |
| 2 | 各部委官网 | 最新监管政策/执法公告 |
| 3 | web_search | 行业动态/时效性核查 |

### 降级规则

| 数据源 | 不可用时的降级 |
|---|---|
| yuandian MCP | web_search 搜索"[监管机构] [关键词] 规定" |
| 部委官网不可用 | web_search 搜索"[关键词] 最新政策" |

---

## 行业许可判断规则

### 金融牌照

| 业务类型 | 许可证类型 | 主管机关 |
|---|---|---|
| 银行 | 金融许可证 | 金融监管总局 |
| 保险 | 保险许可证 | 金融监管总局 |
| 证券/基金 | 经营证券期货业务许可证 | 证监会 |
| 第三方支付 | 支付业务许可证 | 央行 |
| 小额贷款 | 网络小贷牌照 | 省级金融监管局 |
| 融资担保 | 融资担保业务经营许可证 | 省级金融监管局 |
| 消费金融 | 消费金融公司牌照 | 金融监管总局 |

### 医药许可

| 业务类型 | 许可证类型 | 主管机关 |
|---|---|---|
| 药品生产 | 药品生产许可证 | NMPA |
| 药品经营 | 药品经营许可证 | NMPA |
| 医疗器械 | 医疗器械注册/备案 | NMPA |
| GMP认证 | 药品GMP证书 | NMPA |
| 互联网医疗 | 互联网医院牌照 | 卫健委 |

### 电信许可

| 业务类型 | 许可证类型 | 主管机关 |
|---|---|---|
| 增值电信业务 | ICP许可证/EDI许可证 | MIIT/省级通管局 |
| 呼叫中心 | 呼叫中心许可证 | MIIT |
| 网络视听 | 信息网络传播视听节目许可证 | 广电总局 |
| 网络游戏 | 版号(ISBN) | 新闻出版署 |
| 互联网新闻 | 互联网新闻信息采编发布许可证 | 网信办 |

---

## 行业合规评估维度

### 金融合规（四维度）

```
1. 牌照合规
   - 是否持牌
   - 是否在有效期内
   - 是否超出许可范围

2. 业务合规
   - 产品是否符合监管要求
   - 利率/费率是否符合上限
   - 信息披露是否充分

3. 内控合规
   - 是否建立内控制度
   - 是否设立合规部门
   - 是否定期进行合规培训

4. 数据合规
   - 个人信息处理是否合规
   - 数据安全措施是否到位
   - 数据出境是否履行备案
```

### 医药合规（四维度）

```
1. 产品质量
   - 药品/器械是否符合质量标准
   - 生产工艺是否符合GMP要求
   - 产品是否注册/备案

2. 广告合规
   - 广告是否经审查（处方药）
   - 广告内容是否合规
   - 禁止虚假宣传

3. 流通合规
   - 经营资质是否齐全
   - 购销记录是否完整
   - 冷链/运输是否符合要求

4. 医疗合规
   - 互联网诊疗是否合规
   - 处方开具是否合规
   - 患者隐私保护是否到位
```

---

## 风险等级

| 风险等级 | 条件 | 处理方式 |
|---|---|---|
| 🔴 HIGH | 涉嫌无证经营/重大违规/群体性事件 | 强制外部律师审核+监管部门报告 |
| ⚠️ MEDIUM | 部分合规差距/轻微违规/政策变化 | 建议审核并制定整改计划 |
| ✅ LOW | 常规合规/已持牌/合规体系完善 | 定期审查 |

---

## 输出格式

### 合规评估报告头部

```
═══════════════════════════════════════
行业监管合规评估报告
═══════════════════════════════════════
机构名称：[自动填写]
行业领域：[金融/医药/电信/其他]
评估事项：[如"经营合规性"/"牌照申请"/"监管处罚应对"]
评估日期：[自动填写]
风险等级：[HIGH/MEDIUM/LOW]
═══════════════════════════════════════
```

### 风险标注格式

```
🔴 HIGH RISK — [风险描述]
   涉及法规：[法规名称]
   建议：[具体整改措施]

⚠️ MEDIUM RISK — [潜在风险描述]
   建议：[建议措施]
```

---

## 场景 Skill 清单

| Skill | 用途 |
|---|---|
| aml-kyc-checker | 反洗钱客户尽职调查 |
| bank-supervision-advisor | 银行业监管合规 |
| compliance-gap-assessor | 合规差距评估 |
| data-localization-checker | 数据本地化合规检查 |
| drug-approval-checker | 药品注册审批合规 |
| enforcement-response-advisor | 监管执法应对 |
| environmental-impact-assessor | 环境影响评估 |
| gmp-compliance-advisor | GMP合规咨询 |
| hazardous-chemical-compliance | 危化品合规 |
| industry-specific-compliance | 行业特定合规 |
| insurance-regulatory-advisor | 保险业监管合规 |
| internet-content-compliance | 互联网内容合规 |
| license-eligibility-checker | 牌照资质审查 |
| medical-device-registration | 医疗器械注册 |
| regulatory-change-tracker | 法规变更追踪 |
| safety-production-advisor | 安全生产合规 |
| securities-compliance-checker | 证券业监管合规 |
| telecom-license-advisor | 电信牌照咨询 |

---

## 升级决策门

出现以下情形，立即升级至专业律师：
- 涉嫌刑事犯罪（非法经营罪/非法集资/洗钱）
- 面临吊销执照/行业禁入处罚
- 涉及重大群体性事件或媒体曝光
- 监管调查/处罚金额重大

---

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

每个 scene skill 的工作流程第一步应为「法律要素提取」，最后一步前应为「论证强度评估」。


本场景在执行 legal analysis 时，按需调用以下 `legal-atomic` 原子 skill：

| 原子 Skill | 用途 | 调用时机 |
|-----------|------|---------|
| `legal-element-extraction` | 法律要素提取 | 所有输入预处理——将非结构化叙述转化为法律事实 |
| `legal-norm-validity-check` | 法条效力核查 | 引用法条前验证是否现行有效 |
| `legal-risk-assessment` | 法律风险评估 | 涉及风险分级判断时 |
| `conflict-resolution` | 法条竞合/冲突解决 | 多个法条或请求权竞合时 |
| `deductive-reasoning` | P-F-C三段论推理 | 构建法律推理链时 |
| `case-retrieval` | 类案检索方法论 | 需要检索类案时 |
| `structured-element-extraction` | 结构化要素提取 | 处理结构化数据时 |

*Greater China Legal — B-phase regulatory-compliance scene configuration*
*基于 anthropic/claude-for-legal/regulatory-legal 适配中国大陆行业监管合规环境*