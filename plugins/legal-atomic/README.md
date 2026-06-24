# legal-atomic/ — 法律推理原子能力

**25 个** 跨场景复用的**纯法律推理方法论** skill。

> **变更说明**：2026-06 拆出 14 个混入 skill（输出型 / 操作型 / 管理型），本目录现仅保留纯方法论 skill。详见 `plugins/legal-documents/` `plugins/legal-operations/` `plugins/legal-management/` 三个新层。

## 职责

提供**纯方法论、零副作用**的法律推理能力，可被任意场景按需组合。每个 skill 单独负责一种推理方法（演绎、归纳、溯因、类比、解释、论证等）。

## 命名规范

- **kebab-case**（如 `deductive-reasoning` `legal-element-extraction`）
- 前缀 `legal-` 表示法律领域
- 后缀表示能力类型（`-reasoning` / `-retrieval` / `-assessment` / `-prediction` 等）

## 包含类型（25 个纯推理方法论）

| 类别 | 数量 | skill 示例 |
|---|---|---|
| 推理方法论 | 8 | deductive / inductive / abductive / counterfactual / analogical reasoning / systematic / teleological interpretation / normative-meaning argumentation |
| 法律解释/论证 | 3 | legal-interpretation-argument / argument-strength-evaluation / evidence-argument-chain |
| 检索 | 3 | legal-article-retrieval / other-legal-retrieval / cn-judicial-rules |
| 理解/要素 | 4 | legal-concept-comprehension / legal-element-extraction / structured-element-extraction / legal-terminology |
| 法条效力 | 1 | legal-norm-validity-check |
| 风险/预测/价值 | 6 | legal-risk-assessment / legal-judgment-prediction / judicial-value-judgment / administrative-value-judgment / conflict-resolution / formal-legal-consequence |

## 已拆出（不再属于本层）

| 类别 | 数量 | 新位置 |
|---|---|---|
| 输出/生成型 | 5 | `plugins/legal-documents/` |
| 操作型（有副作用） | 2 | `plugins/legal-operations/` |
| 管理/流程型 | 7 | `plugins/legal-management/` |

> 拆分原则参见 [[skill-atomic-design]] memory。

## frontmatter 要求

```yaml
---
name: <kebab-case>
description: >  # 必须用折叠形式（避免中文冒号 YAML 不合法）
  描述...
legal_frame: cn-mainland  # 或 hk/tw/sg/mo/eu
last_reviewed: YYYY-MM
version: X.Y.Z
risk_level: low|medium|high
trigger_phrases:  # 至少 1 个
  - 触发词
---
```

## 新增 skill 流程

1. 判断是否**真正属于"纯推理方法论"**（不是输出/操作/管理类）
2. 创建目录：`plugins/legal-atomic/<skill-name>/SKILL.md`
3. 写 frontmatter（见上）
4. 行数控制在 290-400 行（红线 500）
5. 校验：`python3 scripts/validate-skills.py`

## 调用方式

场景 CLAUDE.md § B16 "推理原子能力调用流程" 应按业务节奏**显式列出**本目录下的调用顺序。

## 详见

- `plugins/README.md`
- `memory/skill-atomic-design.md`
- `memory/cn-adaptation-rules.md`

## frontmatter 要求

```yaml
---
name: <kebab-case>
description: >  # 必须用折叠形式（避免中文冒号 YAML 不合法）
  描述...
legal_frame: cn-mainland  # 或 hk/tw/sg/mo/eu
last_reviewed: YYYY-MM
version: X.Y.Z
risk_level: low|medium|high
trigger_phrases:  # 至少 1 个
  - 触发词
---
```

## 新增 skill 流程

1. 判断是否**真正属于"纯推理方法论"**（不是输出/操作/管理类）
2. 创建目录：`plugins/legal-atomic/<skill-name>/SKILL.md`
3. 写 frontmatter（见上）
4. 行数控制在 290-400 行（红线 500）
5. 校验：`python3 scripts/validate-skills.py`

## 调用方式

场景 CLAUDE.md § B16 "推理原子能力调用流程" 应按业务节奏**显式列出**本目录下的调用顺序。

## 详见

- `plugins/README.md`
- `memory/skill-atomic-design.md`
- `memory/cn-adaptation-rules.md`