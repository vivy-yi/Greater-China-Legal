# legal-research-templates/ — 法律研究编排模板

面向 **agent** 的研究流程编排模板。律师不必读，**agent 必读**。

## 职责

定义"律师问 X 类问题时，agent 按什么顺序调哪些 atomic"。避免每个场景 CLAUDE.md 重复写流程。

## 与 SKILL_INDEX 的关系

| 文件 | 受众 | 内容 |
|---|---|---|
| `SKILL_INDEX.md` | 律师 | "你能问什么 + 怎么问" |
| `plugins/legal-research-templates/` | agent | "用户问 X 时怎么跑" |

## 5 个模板

| template_id | 适用场景 | 主要 atomic 链 |
|---|---|---|
| `contract-dispute-analysis` | 合同纠纷分析 | legal-element-extraction → legal-article-retrieval → case-retrieval → deductive-reasoning → argument-strength-evaluation |
| `litigation-strategy` | 诉讼策略 | legal-element-extraction → case-retrieval → legal-judgment-prediction → strategic-risk-prioritization |
| `compliance-audit` | 合规审查 | legal-element-extraction → legal-norm-validity-check → legal-risk-assessment → conflict-resolution |
| `employment-dispute` | 劳动争议 | legal-element-extraction → legal-article-retrieval → case-retrieval → counterfactual-reasoning |
| `cross-border-transaction` | 跨境交易 | legal-element-extraction → cn-judicial-rules → legal-interpretation-argument → conflict-resolution |

## 模板结构（统一）

每个模板的 frontmatter 含：
- `template_id`：唯一标识
- `trigger_keywords`：触发关键词列表（律师说这些词时 agent 自动匹配）
- `legal_frame`：默认法域
- `risk_level`：风险等级

正文含 5 段：
1. **触发条件** — 什么场景用
2. **工作流** — 按顺序调哪些 atomic + 每个的输入输出契约
3. **输入契约** — 律师需要提供什么
4. **输出契约** — 最终给律师什么
5. **失败 fallback** — skill 失败时怎么办

## 调用方式

律师说：
```
"用合同纠纷分析模板研究这份材料"
```

或：
```
"研究这份合同纠纷"  （关键词触发）
```

agent 根据 `trigger_keywords` 自动匹配模板，按模板工作流跑。

## 新增模板流程

1. 创建 `<template-id>.md`（按统一结构）
2. 在 `SKILL_INDEX.md` 添加条目
3. 提交

## 详见

- `../../SKILL_INDEX.md`（律师视角）
- `../legal-atomic/`（被调用的 25 个 atomic skill）