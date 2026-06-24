# shared/ — 跨场景共享机制

**8 项**横切层 skill，分 3 类。

## 职责

提供**跨场景共享**的机制，**不依赖外部**。所有场景可按需调用。

## 3 大类

### 业务机制（4 项）—— 法律专属

| Skill | 作用 |
|---|---|
| `matter-workspace` | 案件工作区管理（new/list/switch/close）—— 确保多客户上下文隔离 |
| `cold-start-interview` | 场景冷启动向导——自动扫描 [填空] 标记生成访谈 |
| `customize` | 配置调整——无需重新冷启动 |
| `legal-builder-hub` ⚠️ | legal skill 构造中心（**当前为空壳，仅 README**——待补全） |

### 演化机制（2 项）

| Skill | 作用 |
|---|---|
| `evolution` | skill 自主学习闭环（反思归因 → patch 提案 → gate → 回归验证） |
| `evolution-meta` | evolution 元学习视图——patterns.md 的 agent-side 视图 |

### 质量机制（2 项）

| Skill | 作用 |
|---|---|
| `auto-test` | 自测——对每个场景 SKILL.md 执行模拟查询、评估输出 |
| `self-audit` | 自动 QA 循环——遍历全部场景和 skill 检查完整性、路径、frontmatter |

## 与其他层关系

- **依赖**：不依赖任何其他层
- **被依赖**：所有场景 + 项目元管理 (.claude/skills) 可调用

## 命名规范

- **kebab-case**
- 业务类用业务术语（`matter-workspace` / `cold-start-interview`）
- 质量类用 `-audit` / `-test` 后缀
- 演化类用 `-meta` / `evolution-` 前缀

## frontmatter 要求

```yaml
---
name: <kebab-case>
description: >
  横切机制说明...
legal_frame: cn-mainland  # 或 hk/tw/sg/mo/eu
last_reviewed: YYYY-MM
version: X.Y.Z
risk_level: low|medium|high
trigger_phrases:  # 至少 1 个
  - 触发词
---
```

## 新增横切机制流程

1. 判断是否真的"跨场景共享"——非共享则不放这里
2. 选 3 类之一：业务 / 演化 / 质量
3. 创建目录 + SKILL.md
4. 校验

## 详见

- `plugins/README.md`