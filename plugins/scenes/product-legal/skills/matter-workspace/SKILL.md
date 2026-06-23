---
name: matter-workspace
description: >
  Manage matter workspaces — new, list, switch, close, or detach (practice-level).
  Use when working across multiple clients, subsidiaries, or matters and you
  need to create, list, switch, close, or detach the active matter so context
  from one engagement doesn't leak into another.
legal_frame: cn-mainland
last_reviewed: 2026-06-23
version: 2.0.0
argument-hint: "<new | list | switch | close | none> [slug]"
trigger_phrases:
  - '产品发布'
  - '营销'
  - '合规'
  - '风险'
  - 'matter-workspace'
  - '案件管理'
---

# /matter-workspace — cn-mainland 适配版

> ⚠️ **本 skill 已从 Anthropic 原版 claude-for-legal US 版本（v1.0）适配为 GCL cn-mainland 版本（v2.0）。**
>
> **核心变更**：
> 1. 配置路径从 `~/.claude/plugins/config/claude-for-legal/...` 改为 `plugins/scenes/product-legal/CLAUDE.md` § B9
> 2. 案件类型从 US 合同（vendor MSA / NDA / SaaS subscription）改为 CN 合同（保理 / 担保 / 资产证券化 / 互联网贷款 / 建设工程 / 跨境贸易 / 商业租赁）
> 3. 适用法从 Delaware / English law 改为中国法 / 香港法 / 国际条约
> 4. 保密级别从 clean-team / heightened 改为 涉密 / 商业秘密 / 一般
> 5. 跨事项上下文开关适配 GCL 多插件体系

---

# /matter-workspace

> 律师 / 法务跨多个客户、子公司或事项工作。一个事项工作区保持一个客户 / 业务线的上下文与其他所有分开。此 skill 管理这些工作区。

## Subcommands

- `/product-legal:matter-workspace new <slug>` — 创建一个新事项工作区，运行简短访谈，写入 `matter.md`
- `/product-legal:matter-workspace list` — 列出事项及状态和活动标记
- `/product-legal:matter-workspace switch <slug>` — 设置活动事项
- `/product-legal:matter-workspace close <slug>` — 归档事项（移动到 `_archived/`，绝不删除）
- `/product-legal:matter-workspace none` — 脱离任何活动事项，仅在 practice-level 工作

## Instructions

1. **读取配置。** 读 `plugins/scenes/product-legal/CLAUDE.md`（特别是 § B9 用户配置 + `## Matter workspaces` 部分）。如果 `Enabled` 是 `✗`，告诉用户："事项工作区已关闭——你配置为内部律师且只有一家公司，所以插件自动在 practice-level 上下文工作。如果你实际跨多个客户，重新运行 `/cold-start-interview --redo` 并选择私人执业设置。否则，你根本不需要 `/matter-workspace`。" 不要报错——对内部用户来说禁用状态是预期的。

2. 应用下面的存储布局和子命令逻辑。

3. 对 `$ARGUMENTS` 的第一个 token 分派：
   - `new` → 运行访谈，写入 `plugins/scenes/product-legal/matters/<slug>/matter.md`，seed `history.md` 和 `notes.md`。
   - `list` → 枚举 `plugins/scenes/product-legal/matters/*/matter.md`，打印表，标记活动事项。
   - `switch` → 更新 practice-level CLAUDE.md 中的 `Active matter:` 行。
   - `close` → 移动 `plugins/scenes/product-legal/matters/<slug>/` → `plugins/scenes/product-legal/matters/_archived/<slug>/`，在 `history.md` 中记录关闭日期。
   - `none` → 设置 `Active matter:` 为 `none — practice-level context only`。

4. 显示用户变化的内容并在写入前确认。

## Notes

- 此 skill 永远不会跨事项读取，除非 practice-level CLAUDE.md 中 `Cross-matter context` 为 `on`。
- 归档不是删除——关闭的事项仍可读取用于保留 / 冲突检查目的。
- Slugs 使用小写连字符。如果 slug 在归档和活动之间重复使用，归档的保留在 `_archived/<slug>/` 下。

---

# Matter Workspace

> 跨多个客户 / 子公司 / 事项的执业（律所 — 独立 / 小所 / 大所；企业内部 — 集团多子公司）跨许多事项工作。一个事项的上下文绝不能泄漏到另一个。此 skill 是使这成为现实的薄薄的文件管理层。

**默认状态为关闭。** 内部用户永远看不到这个——他们仅在 practice-level 运行。事项工作区在冷启动时为私人执业用户打开，或通过编辑 practice-level CLAUDE.md 中的 `## Matter workspaces` 打开。如果 `Enabled` 是 `✗`，此 skill 不运行；`/matter-workspace` 命令解释禁用状态并为实际需要事项隔离的用户建议 `/cold-start-interview --redo`。

## 存储布局

所有事项数据位于：

```
plugins/scenes/product-legal/
├── CLAUDE.md                       # practice-level practice profile (含 Matter workspaces 部分)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # 客户 / 对手方 / 事项类型 / 关键事实 / 覆盖
    │   ├── history.md              # 带日期的事件日志 / 决定 / 草稿 / 审查
    │   ├── notes.md                # 自由格式工作笔记
    │   └── outputs/                # 此事项的 skill 输出（可选子文件夹）
    └── _archived/
        └── <slug>/                 # 关闭的事项 — 可读但不活动
```

Slugs 使用小写连字符。示例：`acme-保理-2026`、`zenith-担保-续约`、`vendor-xyz-nda`。

## 活动事项在 practice CLAUDE.md 中

practice-level CLAUDE.md 中 `## Matter workspaces` 下的 `Active matter:` 行是单一真相源。切换事项会编辑该行。没有单独的状态文件。

## Subcommand logic

### `new <slug>`

1. 确认 slug 在 `matters/<slug>/` 或 `matters/_archived/<slug>/` 中不存在。如果重用，要求用户选择不同的 slug。
2. 运行访谈：

   - **客户**（我们代表的方，或内部业务单位如果是企业内部）
   - **对手方**（另一方 — 可能有多个）
   - **事项类型**（读插件的 practice profile 获取典型类别；product-legal：launch / feature review / marketing claim review / risk deep dive / product area（常设）/ other）
   - **CN 事项类型扩展**（如果是企业 / 律所常见）：保理合同 / 担保合同 / 资产证券化 / 互联网贷款 / 建设工程 / 跨境贸易 / 商业租赁 / 反垄断 / 证券监管 / 网络安全审查 / 反腐败调查
   - **保密级别**（一般 / 商业秘密 / 涉密 / 上市公司未公开信息）
   - **关键事实**（2-5 句：事项内容、利益相关者、利益所在、与默认剧本的不同）
   - **事项特定覆盖**（例如："客户要求 24 个月 Lol 上限而非 12"，"对手方是战略合作伙伴 — 关系维护语气"）
   - **相关事项**（相关事项的 slugs）
   - **适用法**（中国法 / 香港法 / 纽约公约 / 国际条约）

3. 用下面的模板写入 `matters/<slug>/matter.md`。
4. Seed `matters/<slug>/history.md` 包含一个 "Opened" 条目。
5. 创建空的 `matters/<slug>/notes.md`。
6. **不要**自动切换到新事项。询问："现在切换到 `<slug>` 吗？（`/matter-workspace switch <slug>`）"

### `list`

枚举 `matters/*/matter.md`。读每个文件的前置数据或前几行提取状态。打印表：

| Slug | 客户 | 事项类型 | 状态 | 开启 | 活动 |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

用 `*` 标记当前活动的事项。如果有 `_archived/*`，将其包含在单独的 "Archived" 标题下。

### `switch <slug>`

1. 确认 `matters/<slug>/matter.md` 存在。如果不存在，提供 `/matter-workspace new <slug>`。
2. 编辑 practice-level CLAUDE.md 中的 `Active matter:` 行为 `Active matter: <slug>`。
3. 向用户显示 matter.md 摘要以便确认他们在正确的事项上。

### `close <slug>`

1. 确认 `matters/<slug>/` 存在。
2. 在 `matters/<slug>/history.md` 中附加一个 "Closed" 条目，写明今天的日期。
3. 移动 `matters/<slug>/` → `matters/_archived/<slug>/`。
4. 如果关闭的事项是活动事项，设置 `Active matter:` 为 `none — practice-level context only`。

### `none`

将 practice-level CLAUDE.md 中的 `Active matter:` 设置为 `none — practice-level context only`。与用户确认。

## `matter.md` template

```markdown
[WORK-PRODUCT HEADER — 按插件配置 ## Outputs — 角色不同；参见 practice-level CLAUDE.md 中 `## Who's using this`]

# Matter: [客户] — [简短描述]

**Slug:** [slug]
**开启：** [YYYY-MM-DD]
**状态：** active
**保密级别：** [一般 / 商业秘密 / 涉密 / 上市公司未公开信息]

---

## 当事方

**客户：** [名称]
**对手方：** [名称(s)]

## 事项类型

[保理合同 / 担保合同 / 资产证券化 / 互联网贷款 / 建设工程 / 跨境贸易 / 商业租赁 / 反垄断 / 证券监管 / 网络安全审查 / 反腐败调查 / 商业租赁 / SaaS 订阅 / 修订 / 续约 / 合作 / 其他 — 附一行说明]

## 关键事实

[2-5 句。事项内容。利益相关者。利益所在。使其与默认剧本不同的方面。]

## 事项特定覆盖

*与 practice-level 剧本的任何偏差，仅适用于此事项。*

- [例如："Lol 上限：客户要求 24 个月，非 house 标准 12。"]
- [例如："语气：关系维护 — 对手方是战略合作伙伴。"]
- [例如："适用法：必须为中国法，非香港法。"]
- [例如："上市合规：信披敏感期，决议需董事会批准。"]

## 适用法

[中国法 / 香港法 / 国际条约 / 纽约公约 / UNCITRAL]

## 相关事项

- [slug — 一行说明为什么相关]

## 保密注意

[如果保密级别高或涉密，描述原因。谁可以查看事项文件。即使全局开启，跨事项上下文是否允许。]
```

## `history.md` seed

```markdown
# History: [客户] — [简短描述]

Append-only event log. Most recent at top.

---

## [YYYY-MM-DD] — Matter opened

Intake completed. Slug: `[slug]`. Status: active.
[Any initial context worth preserving beyond matter.md — e.g., "Opened in response to inbound 担保 contract draft from [counterparty]."]
```

## Cross-matter context

practice-level CLAUDE.md 有一个 `Cross-matter context:` 标志。当它是 `off`（默认），在事项 A 工作的 skill **绝不读取** `matters/B/` 中任何其他 `B` 的文件。期间。这是设置存在的保密保证。

当它是 `on`，skill 仅在用户明确要求时可能读取跨事项文件夹的文件（例如，"比较我们过去五个供应商事项的责任上限立场"）。即使在 `on`，默认仅加载活动事项，除非用户要求跨事项视图。

## What this skill does not do

- **运行利益冲突检查。** 利益冲突是执业者 / 律所的工作；访谈捕获用户声明的内容。
- **执行保留。** 关闭归档事项；它不删除。保留政策超出范围。
- **自动路由输出。** 实质性 skill 决定写在哪里；此 skill 告诉它*哪个文件夹*是活动的，不是放什么。
- **决定跨事项是否合适。** 它读取标志并遵守。

---

## CN 特别注意事项

- **中国法 vs 香港法 vs 国际条约**：跨境事项需要明确适用法（参见 `jurisdictional-footprint.md` 和 `cn-adaptation.md`）。
- **上市公司未公开信息**：根据《证券法》第 52 条，内幕信息知情人在信息公开前不得买卖证券。涉及上市公司事项需标记 `[上市公司未公开信息]` 级别。
- **涉密 / 商业秘密**：根据《反不正当竞争法》第 9 条，商业秘密保护。涉及技术 / 经营信息的事项标记 `[商业秘密]` 级别。
- **境外数据出境**：涉及 1 万用户+ / 100 万用户+ 的数据出境事项触发网信办安全评估（参见产品法律 § B12 块 2）。
- **跨境破产 / 重整**：集团破产 / 重整涉及多事项协同。

---

*Greater China Legal — product-legal:matter-workspace v2.0.0*
*从 Anthropic 原版 claude-for-legal 适配为 GCL cn-mainland*
*最后更新:2026-06-23*