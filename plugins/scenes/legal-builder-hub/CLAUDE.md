---
name: legal-builder-hub
description: >
  Skill builder hub — build, test, and publish CN legal skills.
  Manages skill registry, installation, and lifecycle.
synopsis: >
  CN legal skill building for Greater China Legal ecosystem.
  Supports skill creation, testing, and publishing workflow.
advisory_scale: medium
client_types: [skill-builder, developer]
internal_stakeholders: [engineering]
---

# Legal Builder Hub — China Mainland

## Who's using this

**Role:** [律师 / 法务人员 / 业务部门（非法律背景，有律师支持）/ 业务部门（无律师支持）]
**Attorney contact:** [填空]

**工作成果头部标记：**
- 律师/法务人员 → `Privileged & Confidential — Attorney Work Product`
- 非法务（有律师支持）→ `Research Notes — Not Legal Advice — Review With Attorney Before Acting`
- 非法务（无律师支持）→ `General Information — Not Legal Advice — Consult A Licensed Attorney`

在产出工作成果前，必须先检查 Role 字段。如果 Role 为 `[填空]`，要求用户先设置角色。

## 公司基本信息

**场景说明：** 本场景面向 Skill 构建者与开发者，不涉及具体的法律实务客户。

**开发团队/组织：** [填空]
**Skill 注册商：** [更大的中国法律生态系统 / 自托管 / 其他]
**开发用途：** [内部使用 / 公开发布 / 法律场景定制]

## 数据源配置

**数据源标注规则：**
- `[YD]` = 元典 MCP 实际返回
- `[WKL]` = 裁判文书网/无讼
- `[BD]` = 北达检索
- `[GOV]` = 政府平台
- `[web]` = 网络搜索
- `[model]` = 模型推理（须核实）

标注必须诚实——不能因"引用看起来是对的"就把 `[model]` 标为 `[YD]`。关键结论须多源交叉验证。

## CN Legal Skill Builder

### Skill构建流程
1. 需求分析（场景/触发词/功能）
2. 编写SKILL.md（frontmatter + body）
3. 本地测试
4. 发布到skill registry

### Skill规范
- frontmatter: name/description/legal_frame/version/risk_level
- body: 清晰的步骤和判断逻辑
- 触发词: 自然的用户表达

---

---

## 输出格式

所有正式输出须在文档开头标注特权头部标记（参见 ## Who's using this），并遵守以下格式要求：

- Skill 设计文档须标注版本号和最后更新日期
- 涉及法律知识的 Skill 须注明所引用的法规来源
- 测试用例须包含预期输出与实际输出对比

## 升级决策门

本场景面向 Skill 开发与构建。如果构建的 Skill 涉及以下内容，必须由执业律师审核后方可发布：

1. 涉及刑事法律判断的 Skill
2. 涉及正式法律意见生成的 Skill
3. 涉及跨境法律适用场景的 Skill
4. 涉及重大经济利益判断的 Skill

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
| `deductive-reasoning` | P-F-C三段论推理 | 构建法律推理链时 |
| `legal-risk-assessment` | 法律风险评估 | 涉及风险分级判断时 |
| `conflict-resolution` | 法条竞合/冲突解决 | 多个法条或请求权竞合时 |
| `case-retrieval` | 类案检索方法论 | 需要检索类案时 |
| `trial-scheduling-and-deadline-monitoring` | 期限管理 | 涉及诉讼/仲裁期限时 |

---

*Greater China Legal — legal-builder-hub CN adapter v1.0.0*