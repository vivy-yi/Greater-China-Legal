# legal-operations/ — 法律文件操作层

**2 个**有副作用的法律文件操作 skill（脱敏 + 还原）。

## 职责

提供**有副作用的法律文件操作**——会创建/修改文件、产生 sidecar 输出。**与 legal-atomic/ 的关键区别**：atomic 是纯方法论（无副作用），本层会真实改文件系统。

## 包含

| Skill | 作用 | 副作用 |
|---|---|---|
| `legal-document-redaction` | 文件脱敏（识别 16 类敏感实体 + 替换） | 写入 sidecar JSON + 比对文件 |
| `legal-document-restoration` | 脱敏稿还原（runs 级精确替换 + round-trip 校验） | 写入还原稿 docx |

## 命名规范

- **kebab-case**
- 前缀 `legal-` 表示法律领域
- 包含 `-redaction` / `-restoration` 等动词

## 与其他层关系

```
scenes/  ──→  legal-operations/  ←─── 主动调用
             │
             ├→ legal-atomic/ (识别阶段调用)
             └→ shared/matter-workspace/ (存储)
```

- **下游**：调用 atomic 做实体识别，调用 matter-workspace 存 sidecar
- **上游**：场景 § B17 跨场景协作钩子调用

## 配套 references

`legal-document-redaction/references/config.md` 包含：
- 白/黑名单 + 优先级机制
- 自定义脱敏类型
- 冲突检测

调用脱敏前必须先 Read 该文件。

## frontmatter 要求

```yaml
---
name: <kebab-case>
description: >
  文件操作...
legal_frame: cn-mainland
last_reviewed: YYYY-MM
version: X.Y.Z
risk_level: high  # 操作类通常 risk 较高
trigger_phrases:  # 至少 1 个
  - 触发词
---
```

## 新增 skill 流程

1. 判断是否真的"有副作用"——纯方法论应放 atomic
2. 创建目录 + SKILL.md
3. 写明副作用类型（文件创建/修改/删除）
4. 写明可逆性（是否可撤销）
5. 校验

## 详见

- `plugins/README.md`
- `plugins/legal-document-redaction/references/config.md`