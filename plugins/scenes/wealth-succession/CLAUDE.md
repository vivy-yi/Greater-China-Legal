# Wealth Succession

财富传承场景 — 覆盖遗嘱审查、家族信托、遗产税规划、继承公证、家族治理与婚姻财产协议。

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
| P0 | 最高人民法院裁判文书网 | 继承纠纷与信托纠纷案例 |
| P0 | 各地公证处官网 | 继承公证程序指引 |
| P1 | 北达检索 / 威科先行 | 家族信托与税务法规 |
| P1 | 国家税务总局官网 | 遗产税/赠与税政策动态 |

## 风险等级
| 风险等级 | 条件 | 处理方式 |
|----------|------|----------|
| 🔴 高 | 遗嘱效力存疑 / 信托架构合规瑕疵 | 立即移交外部律师，暂缓方案执行 |
| 🟠 中 | 跨境遗产税规划复杂 / 婚姻财产争议 | 内部律师深入分析，联合税务顾问 |
| 🟡 低 | 常规继承公证咨询 / 遗嘱起草建议 | 内部处理，输出参考意见 |

## 输出格式
所有分析输出须包含：
1. **工作成果头部标记**（根据角色选择对应标记）
2. **来源标注**：引用法规标注来源（裁判文书网 `[WKL]`、政府官网 `[GOV]`、北达检索 `[BD]`、模型知识 `[model]`）
3. **升级提示**：涉及跨境资产或重大财产争议须标注升级路径

## 升级决策门
涉及以下情形须移交专业律师并明确标注：
- 遗嘱形式要件存在瑕疵或效力争议
- 家族信托架构涉及跨境法域
- 存在继承权纠纷或潜在诉讼
- 涉及大额跨境资产转移或税务筹划
- 婚姻财产协议涉及重大利益分配

## 核心能力

- 遗嘱效力审查与形式要求
- 家族信托架构设计与税务筹划
- 跨境遗产税规划（内地暂无遗产税）
- 继承公证程序与材料准备
- 家族治理结构与传承方案
- 婚前/婚内财产协议效力审查

## Skill 调用顺序

1. `testament-drafting-checker` — 遗嘱效力审查
2. `trust-structure-advisor` — 家族信托架构
3. `estate-tax-planner` — 跨境遗产税规划
4. `probate-procedure-guide` — 继承公证程序
5. `family-governance-advisor` — 家族治理规划
6. `prenuptial-agreement-checker` — 婚姻财产协议审查

## 推理原子能力

本场景在执行 legal analysis 时，按需调用以下 `legal-atomic` 原子 skill：

| 原子 Skill | 用途 | 调用时机 |
|-----------|------|---------|
| `legal-element-extraction` | 法律要素提取 | 所有输入预处理——将非结构化叙述转化为法律事实 |
| `legal-norm-validity-check` | 法条效力核查 | 引用法条前验证是否现行有效 |
| `deductive-reasoning` | P-F-C三段论推理 | 构建法律推理链时 |
| `legal-risk-assessment` | 法律风险评估 | 涉及风险分级判断时 |
| `conflict-resolution` | 法条竞合/冲突解决 | 多个法条或请求权竞合时 |
| `case-retrieval` | 类案检索方法论 | 需要检索类案时 |
| `trial-scheduling-and-deadline-monitoring` | 期限管理 | 涉及诉讼/仲裁期限时 |
