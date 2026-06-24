# legal-tools/ — 外部数据/API 工具封装

**4 项**外部数据源、API、MCP 服务的封装层。**所有内容都依赖外部资源**。

## 职责

把项目外部的**法律数据 API、查询服务、MCP 工具**封装成可被场景调用的 skill。这是 GCL 项目**唯一直接与外部世界交互**的层。

## 包含

| 工具 | 类别 | 数据源 | 触发词 |
|---|---|---|---|
| `gcl-data-service` | 数据查询服务 | 元典 / 北大法宝 / 政府公开数据 | 法条查询 / 案例检索 / 效力验证 |
| `law-firm-research` | 律所检索 | 胡润 TOP100 律所 | 找律所 / 推荐律师 |
| `qcc-skills/` | 企业信息 MCP | 企查查 agent.qcc.com | 企业工商 / 资质 / 投资 / 供应链 |
| `qcc-tools-list.md` | 工具索引（参考文档） | — | — |

## 命名规范

- **kebab-case**
- 描述清楚数据源（如 "gcl-data-service" 明确指 GCL 项目数据服务）
- 若是 MCP 服务，目录内套用子目录分类（如 `qcc-skills/qcc-legal-skills/`）

## 与其他层关系

```
scenes/ ──→ atomic/ ──→ legal-tools/  ← 调用
```

- **下游**：所有 `[YD]/[WKL]/[BD]/[GOV]` 标注实际通过 `gcl-data-service` 实现
- **上游**：场景可以直接调用，也可以让 atomic 调用后再返回

## frontmatter 要求

```yaml
---
name: <tool-name>
description: >
  外部数据/API 封装...
legal_frame: cn-mainland  # 工具的默认法域
last_reviewed: YYYY-MM
version: X.Y.Z
data_source: <来源说明>
data_scope: <数据范围>
---
```

## 新增工具流程

1. 确认是否**真的需要新增外部依赖**（优先考虑用现有工具组合）
2. 选择合适的封装策略（直接调用 / MCP / CLI 包装）
3. 创建目录 + SKILL.md
4. 在数据源标注体系（[YD]/[WKL] 等）中注册新来源
5. 校验

## 详见

- `plugins/README.md`
- `CLAUDE.md` § "数据源标注"