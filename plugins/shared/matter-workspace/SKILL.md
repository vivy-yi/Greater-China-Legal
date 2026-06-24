---
name: matter-workspace
description: >
  管理案件工作区——新建、列出、切换、关闭案件工作区。
  适用于多客户/多项目法务场景，确保一个客户的上下文不会泄露到另一个。
  适用情形：用户说"新建案件"、"切换案件"、"列出我的案件"。
argument-hint: "<new | list | switch | close | none> [slug]"
trigger_phrases:
  - 案件
  - 工作区
  - 案件管理
  - 新建案件
  - 案件切换
last_reviewed: 2026-06
legal_frame: cn-mainland
version: 1.0.0
risk_level: low
---

# /matter-workspace — 通用案件工作区管理

## 原理

matter-workspace 为每个案件创建一个隔离的工作目录，确保一个案件的上下文不会泄漏到另一个。每个场景独立维护自己场景的案件工作区。

## 存储路径

案件文件存储在调用场景的 `matters/` 目录下：

```
plugins/legal-scenes/<scene>/
├── CLAUDE.md
├── matters/
│   ├── <slug>/
│   │   ├── matter.md         # 案件基本信息
│   │   ├── history.md        # 事件时间线
│   │   └── notes.md          # 自由格式笔记
│   └── _archived/
│       └── <slug>/           # 已归档案件
```

路径由调用时的场景上下文自动确定，无需硬编码。

## Subcommands

- `matter-workspace new <slug>` — 创建新案件工作区，运行简短问询，写入 `matter.md`
- `matter-workspace list` — 列出所有活跃案件，显示状态和摘要
- `matter-workspace switch <slug>` — 切换当前活跃案件
- `matter-workspace close <slug>` — 归档案件（移至 `_archived/`）
- `matter-workspace none` — 退出案件级上下文，使用场景级配置

## 工作流程

### new — 新建案件

1. 确认场景上下文中 `matters/` 目录是否存在，不存在则创建
2. 检查 slug 是否已存在：如已存在，提示 "案件 [slug] 已存在。使用 switch 切换或 close 归档后再新建。"
3. 询问以下信息填写 `matter.md`：

```
系统：请提供案件基本信息：

案件名称：_______
案件类型：[合同审查 / 诉讼 / 仲裁 / 合规/ 咨询 / 其他]
对方当事人（如有）：_______
案件状态：[进行中 / 待处理 / 已结案]
关键日期（如有）：_______
简要描述：_______

是否需要本场景特有的额外字段？(Y/N)
如 Y，请说明需要记录的信息：
```

如用户指定了场景特有字段，追加到 matter.md 的 `## 场景特定信息` 节。

4. 生成 `matter.md`：

```markdown
# 案件：[案件名称]

## 基本信息

**案件名称：** [名称]
**案件类型：** [类型]
**对方当事人：** [名称]
**案件状态：** [状态]
**创建日期：** [YYYY-MM-DD]
**最后更新：** [YYYY-MM-DD]

## 关键事实

[简要描述]

## 关键日期

- [日期]：[事件]

## 场景特定信息

[如有场景特有针对他，填写在此]
```

5. 创建空的 `history.md` 和 `notes.md`
6. 输出：`✅ 案件 [slug] 已创建`

### list — 列出案件

```
📋 案件列表 — [场景名]

活跃案件：
- [slug1] — [案件名称] — [状态] ← 当前
- [slug2] — [案件名称] — [状态]

已归档：
- [slug3] — [案件名称]
```

### switch — 切换案件

1. 检查 slug 是否存在
2. 将当前活跃标记切换为新 slug
3. 输出：`✅ 已切换至案件 [slug]`

### close — 归档案件

1. 检查 slug 是否存在
2. 将 `matters/<slug>/` 移至 `matters/_archived/<slug>/`
3. 更新 history.md 添加归档记录
4. 输出：`✅ 案件 [slug] 已归档`

## 自动检索

当用户直接提问（未指定 slug）时，尝试自动检索：

1. 检查 `matters/_archived/` 下是否有匹配的案件
2. 如找到一个，询问是否要恢复
3. 如找到多个，列出供用户选择

## 本技能不做什么

- 不提供法律策略建议。只管理案件上下文。
- 不跨案件读取信息（除非明确切换）。
- 不保证案件信息的完整性。

---

*Greater China Legal — shared matter-workspace v1.0.0*
