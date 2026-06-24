# legal-documents/ — 法律文书输出层

**5 个**法律文书生成、格式化、摘要、分类的输出类 skill。

## 职责

提供**纯输出能力**——从已有事实生成符合规范的法律文书（判决书、备忘录、摘要等）。**与 legal-atomic/ 的关键区别**：atomic 输出的是"分析结论"（中间产物），本层输出的是"对外交付物"（终产物）。

## 包含

| Skill | 作用 | 输出物 |
|---|---|---|
| `legal-document-formatting` | 法律文书格式适用——民事/刑事判决书七段式 | 判决书 |
| `legal-document-summarization` | 法律文书摘要——六要素框架 | 摘要 |
| `judgment-document-generation` | 判决书生成——8 步流程（刑事案件） | 刑事判决书 |
| `multi-document-summarization` | 多文书摘要 | 多份文档综合摘要 |
| `legal-domain-taxonomy` | 法律域分类法 | 分类参考 |

## 命名规范

- **kebab-case**
- 前缀 `legal-` 表示法律领域
- 包含 `-generation` / `-formatting` / `-summarization` / `-taxonomy` 表示输出类型

## 与其他层关系

```
scenes/ ──→  legal-atomic/ ──→  legal-tools/
   │              │                （外部数据）
   │              ↓                （推理结论）
   │         legal-documents/ ←─── 输出终产物
   ↓
  shared/
```

- **下游**：消费 atomic 的推理结论
- **上游**：场景直接调用生成文书
- **不调用 atomic**：本层是输出层，不重复推理

## frontmatter 要求

```yaml
---
name: <kebab-case>
description: >
  文书生成/格式化...
legal_frame: cn-mainland  # 或 hk/tw/sg/mo/eu
last_reviewed: YYYY-MM
version: X.Y.Z
risk_level: medium|high  # 输出正式文书通常 risk 较高
trigger_phrases:  # 至少 1 个
  - 触发词
---
```

## 新增 skill 流程

1. 判断是否真的"输出对外文书"——中间分析产物应放 atomic
2. 创建目录 + SKILL.md
3. 写明输出格式模板（markdown / docx / html）
4. 校验

## 详见

- `plugins/README.md`
- `plugins/legal-atomic/README.md`（atomic 输出 vs 本层输出的区别）