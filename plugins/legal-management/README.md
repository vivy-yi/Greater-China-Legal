# legal-management/ — 法律流程管理层

**7 个**案件/财务/排期/风险等流程类 skill。

## 职责

提供**业务流程管理**——案件生命周期、预算、排期、风险识别、纠纷履约等。这些是**业务管理能力**，不是法律推理。

## 包含

| Skill | 作用 |
|---|---|
| `case-lifecycle-planning` | 案件生命周期规划（受理→审理→结案→归档） |
| `case-retrieval` | 案件检索（按案号/客户/标的/律师多维度） |
| `billing-and-litigation-budget` | 诉讼预算与计费 |
| `trial-scheduling-and-deadline-monitoring` | 庭审排期与截止日监控 |
| `strategic-risk-prioritization` | 战略风险优先级 |
| `internal-compliance-risk-identification` | 内部合规风险识别 |
| `dispute-and-performance-risk` | 争议与履约风险 |

## 命名规范

- **kebab-case**
- 包含具体业务名词（`case-` / `billing-` / `trial-` / `risk-` 等）

## 与其他层关系

```
scenes/  ──→  legal-management/  ←─── 主动调用
             │
             └→ shared/matter-workspace/ (存储案件)
```

- **下游**：调用 matter-workspace 存案件数据
- **上游**：场景 § B16 推理原子能力调用流程 + 直接调用

## frontmatter 要求

```yaml
---
name: <kebab-case>
description: >
  流程管理...
legal_frame: cn-mainland
last_reviewed: YYYY-MM
version: X.Y.Z
risk_level: medium
trigger_phrases:  # 至少 1 个
  - 触发词
---
```

## 新增 skill 流程

1. 判断是否真的"业务流程"——法律推理应放 atomic，文书输出放 documents
2. 创建目录 + SKILL.md
3. 写明业务规则（受理条件、结案标准等）
4. 校验

## 详见

- `plugins/README.md`