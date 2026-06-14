# CLAUDE.md — Cross-Border Trade Compliance Workspace

## Workspace Overview
This workspace provides AI-powered guidance for cross-border trade compliance operations, including export controls, import tariffs, sanctions screening, Incoterms, customs compliance, and trade dispute resolution.

## Who's using this
**Role:** [律师 / 法务人员 / 业务部门（非法律背景，有律师支持）/ 业务部门（无律师支持）]
**Attorney contact:** [填空]
**工作成果头部标记：**
- 律师/法务人员 → `Privileged & Confidential — Attorney Work Product`
- 非法务（有律师支持）→ `Research Notes — Not Legal Advice — Review With Attorney Before Acting`
- 非法务（无律师支持）→ `General Information — Not Legal Advice — Consult A Licensed Attorney`

## 公司基本信息
**公司名称：** [填空]
**业务类型：** [填空]
**外部律师：** [填空]

## 数据源配置
| 优先级 | 数据源 | 用途 |
|--------|---------|------|
| P0 | 美国政府官网（BIS/DDTC/OFAC） | EAR/ITAR/Sanctions 法规 |
| P0 | 欧盟官方公报（EUR-Lex） | EU Dual-Use Regulation |
| P1 | 海关总署官网 | 中国进出口管制法规 |
| P1 | WTO争端解决数据库 | 贸易争端案例 |

## 风险等级
| 风险等级 | 条件 | 处理方式 |
|----------|------|----------|
| 🔴 高 | 涉及制裁清单 / 出口管制违规风险 >$100K | 立即移交外部律师，暂停交易 |
| 🟠 中 | 海关分类存疑 / FTA适用不确定 | 内部律师深入分析，联系专业报关行 |
| 🟡 低 | Incoterms选择咨询 / 常规关税咨询 | 内部处理，输出参考意见 |

## 输出格式
所有分析输出须包含：
1. **工作成果头部标记**（根据角色选择对应标记）
2. **来源标注**：引用法规标注来源（政府官网 `[GOV]`、案例库 `[WKL]`、Westlaw `[BD]`、模型知识 `[model]`）
3. **升级提示**：涉及刑事制裁风险或重大金额须标注升级路径

## 升级决策门
涉及以下情形须移交专业律师并明确标注：
- 涉及OFAC/UN/EU制裁清单主体
- 出口管制物项分类存在争议
- 面临刑事调查或重大处罚风险（>$100K）
- 跨境贸易涉及反倾销/反补贴调查

## Available Skills

### Core Skills
| Skill | Purpose |
|-------|---------|
| `export-control-reviewer` | EAR/ITAR/Commerce Control List compliance review |
| `import-tariff-adviser` | HTS classification and duty rate advisory |
| `trade-sanctions-checker` | OFAC, UN, EU sanctions list screening |
| `incoterms-guide` | Incoterms 2020 rules interpretation and selection |
| `customs-compliance-assessor` | Customs bonds, bonded warehouses, FTA utilization |
| `trade-dispute-advisor` | WTO, anti-dumping, countervailing duty disputes |

## Directory Structure
```
/tmp/gl-work/cross-border-trade/
├── CLAUDE.md
├── export-control-reviewer/
│   └── skill.md
├── import-tariff-adviser/
│   └── skill.md
├── trade-sanctions-checker/
│   └── skill.md
├── incoterms-guide/
│   └── skill.md
├── customs-compliance-assessor/
│   └── skill.md
├── trade-dispute-advisor/
│   └── skill.md
└── references/
    ├── 判断框架.md
    ├── 查询路径.md
    └── 数据源清单.md
```

## Usage Guidelines
1. Always identify the specific trade compliance question before invoking a skill
2. When in doubt about jurisdiction, check multiple relevant skills (e.g., US + EU for transatlantic trade)
3. Escalate complex cases involving penalties >$100K or criminal exposure to human legal counsel
4. Document all compliance determinations with supporting regulatory citations

## Key Regulatory Frameworks
- **US**: EAR (15 CFR 730-774), ITAR (22 CFR 120-130), Customs Regulations (19 CFR)
- **EU**: Dual-Use Regulation (EC 428/2009), EU Sanctions Framework
- **International**: Incoterms® 2020, WTO Agreements, UN Sanctions Resolutions

## Quality Assurance
- All tariff/HTS classifications should be verified against official government databases
- Sanctions screening requires real-time database checks, not historical knowledge
- Legal determinations involving penalty exposure require human attorney review

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

### 追问规则（关键）

legal-element-extraction 的输出包含 `## 待补充事实` 节。如果该节非空：

1. **暂停当前分析流程**
2. 向用户逐一提问待补充事实，例如：
   > "请问合同中关于[知识产权归属/数据存储位置/价格调整机制]的条款是什么？这会影响后续判断。"
3. 用户补充后，**回到 Step 0 重新执行 legal-element-extraction**，将新信息并入结构化事实
4. 当待补充事实清空后，继续后续分析

**不得在待补充事实未清空的情况下输出最终结论。** 缺失关键事实的结论标注为「推定结论，须在事实补全后复核」。

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
| `deductive-reasoning` | P-F-C三段论推理 | 构建法律推理链时 |
| `conflict-resolution` | 法条竞合/冲突解决 | 多个法条或请求权竞合时 |
| `evidence-argument-chain` | 证据论证链 | 组织证据与主张对应关系时 |
| `argument-strength-evaluation` | 论证强度评估 | 输出结论时标注强/中/弱/存疑 |
| `legal-risk-assessment` | 法律风险评估 | 涉及风险分级判断时 |
| `case-retrieval` | 类案检索方法论 | 需要检索类案时 |