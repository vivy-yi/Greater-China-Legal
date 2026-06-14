# Commercial Arbitration

商事仲裁场景 — 覆盖ICC/SIAC/HKIAC/贸仲/深仲等主流仲裁机构规则，
处理跨境商事争议、股权投资争议、贸易金融争议等。

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
| P0 | 仲裁机构官网（ICC/SIAC/HKIAC/CIETAC） | 仲裁规则与案件管理 |
| P0 | 裁判文书网 / 无讼 | 仲裁裁决司法审查案例 |
| P1 | 北达检索 / Westlaw | 国际仲裁案例与评论 |

## 风险等级
| 风险等级 | 条件 | 处理方式 |
|----------|------|----------|
| 🔴 高 | 仲裁协议无效 / 裁决可能被撤销或不予执行 | 立即移交外部律师，评估替代争议解决路径 |
| 🟠 中 | 仲裁程序违规 / 管辖权争议 | 内部律师深入分析，联系仲裁庭 |
| 🟡 低 | 仲裁费用估算 / 程序性咨询 | 内部处理，输出参考意见 |

## 输出格式
所有分析输出须包含：
1. **工作成果头部标记**（根据角色选择对应标记）
2. **来源标注**：引用仲裁规则标注来源（仲裁机构官网 `[GOV]`、案例库 `[WKL]`、Westlaw `[BD]`、模型知识 `[model]`）
3. **升级提示**：涉及裁决执行或刑事风险须标注升级路径

## 升级决策门
涉及以下情形须移交专业律师并明确标注：
- 仲裁协议效力存在重大争议
- 裁决面临撤销或不予执行风险（含跨境执行）
- 涉及国家主权豁免或公共政策例外
- 涉及刑事犯罪线索（如伪造证据、仲裁欺诈）

## 核心能力

- 仲裁协议效力审查
- 仲裁程序管理（保全/临时措施）
- 证据规则适用
- 裁决承认与执行（中国境内/境外）

## 参考文件

- `references/判断框架.md` — 仲裁协议效力/程序/裁决执行判断框架
- `references/查询路径.md` — 仲裁规则检索路径
- `references/数据源清单.md` — 仲裁机构/案例数据库

## Skill 调用顺序

1. `arbitration-clause-reviewer` — 仲裁条款效力审查
2. `arbitral-procedure-advisor` — 仲裁程序与保全
3. `evidence-rule-guide` — 证据规则指引
4. `award-enforcement-checker` — 裁决执行核查
5. `jurisdiction-dispute-advisor` — 管辖权异议咨询
6. `arbitration-cost-estimator` — 仲裁费用估算

## 推理原子能力

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
