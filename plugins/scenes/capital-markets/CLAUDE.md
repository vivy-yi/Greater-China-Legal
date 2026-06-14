# Capital Markets

资本市场场景 — 覆盖A股IPO、再融资（增发/配股）、公司债与企业债、资产支持证券（ABS）、优先股等证券发行与监管合规业务。

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
| P0 | 证监会官网 / 交易所公告 | 监管政策与发行审核动态 |
| P0 | 巨潮资讯网 | 上市公司信息披露 |
| P1 | Wind / 彭博 | 市场数据与行业对标 |

## 风险等级
| 风险等级 | 条件 | 处理方式 |
|----------|------|----------|
| 🔴 高 | 发行条件不满足 / 重大信息披露遗漏 | 立即移交外部律师，暂停项目推进 |
| 🟠 中 | 监管政策重大变化 / 合规瑕疵 | 内部律师深入评估，制定补救方案 |
| 🟡 低 | 规范性瑕疵 / 文件格式问题 | 内部整改，无需外部介入 |

## 输出格式
所有分析输出须包含：
1. **工作成果头部标记**（根据角色选择对应标记）
2. **来源标注**：引用监管法规标注来源（证监会官网 `[GOV]`、巨潮 `[WKL]`、Wind `[BD]`、模型知识 `[model]`）
3. **升级提示**：涉及刑事风险或重大金额事项须标注升级路径

## 升级决策门
涉及以下情形须移交专业律师并明确标注：
- 发行条件存在重大不确定性
- 涉嫌信息披露违法违规（刑事/行政处罚风险）
- 跨法域证券发行（境外上市/互联互通）
- 涉及重大未决诉讼或监管调查

## 核心能力

- 招股说明书（IPO/再融资）合规审查
- 公司债/企业债/ABS发行核查
- 监管政策追踪与合规评估
- 证券信息披露审核

## 数据源

- 证监会官网 / 交易所公告
- 巨潮资讯网
- Wind / 彭博

## 参考文件

- `references/判断框架.md` — 发行条件核查框架
- `references/查询路径.md` — 法规检索路径
- `references/数据源清单.md` — 数据源列表

## Skill 调用顺序

1. `issue-eligibility-checker` — 发行主体资格核查
2. `prospectus-drafter` — 招股书/债券募集说明书起草
3. `disclosure-reviewer` — 信息披露完整性审核
4. `regulatory-tracker` — 监管政策动态追踪
5. `compliance-assessor` — 发行合规评估

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