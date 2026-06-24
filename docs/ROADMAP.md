# ROADMAP — 7 层架构演进路线图

> 基于设计生态 7 层模型（user request → delivered artifact），对比 GCL 当前架构的差距分析。
> 最后更新：2026-06-24

---

## 设计生态 7 层参考

```
L7 · USER INTENT          自然语言 / canvas
L6 · AGENT ORCHESTRATION  Claude Code / Cursor / OpenCode / 22+ agents
L5 · SKILLS / PROMPTS     SKILL.md format · design skills
L4 · DESIGN SYSTEMS       DTCG tokens / design-extract
L3 · BRIDGES              Figma ↔ Agent MCP servers (10+)
L2 · GENERATION + RENDER  screenshot-to-code (73k★)
L1 · INPUT SOURCES         .fig / Figma URL / screenshots / 微信 / web
```

---

## GCL 当前架构（已完成基线）

```
✅ legal-tools        L1 类比（外部数据 API）
✅ legal-atomic       L5 类比（推理方法论，25 个纯推理）
✅ legal-documents    L2 类比（文书输出，5 个）
✅ legal-operations   L2 操作类（脱敏/还原，2 个）
✅ legal-management   L4 类比弱（流程管理，7 个）
✅ legal-scenes       L7 类比（业务入口，36 个）
✅ shared             L6 类比弱（横切机制）
✅ legal-research-templates  L5 增强（5 个编排模板）
✅ SKILL_INDEX.md     L7 律师向索引
```

**v1.3.0 已上线（origin/main @ 4b33908）**——覆盖 L5 + L7 + 部分 L1/L2/L4。

---

## 待办启发（按优先级）

### 🔴 P0-1 · L3 桥梁层（最关键）

**问题**：律师**不在 Claude Code 里工作**——他们在 Word / Outlook / 浏览器。GCL 现在没有"桥梁层"，律师要主动打开 Claude Code 才能用 skill。

**启发**：建 `plugins/legal-bridges/` 层——
- **Word 插件**（Office add-in）：律师在 Word 里勾选段落 → 直接脱敏/审查
- **VS Code 插件**：律师在 IDE 里写合同 → 法律检查
- **浏览器扩展**：在裁判文书网 / 法信 / 北大法宝里直接调用
- **邮件插件**：Outlook 收到邮件自动做合规审查

**参考标杆**：TalkToFigma（6.9k★）用 MCP 把 Figma ↔ Claude Code 桥接——GCL 应该做 Word ↔ Claude Code 桥接（MCP server + Word add-in）。

**工作量**：3-6 个月

**价值**：极高——这是 GCL 从"技术 demo"变成"律师日常工具"的关键动作。

---

### 🔴 P0-2 · L1 多模态输入

**问题**：GCL 现在只支持文本输入 + 文件路径。律师实际材料形态多样：合同 PDF、判决书扫描件、微信聊天记录、网页文章。

**启发**：建 `plugins/legal-input-adapters/` 层——
```
"审查这份 PDF 合同"      → agent 自动 PDF → text → legal-element-extraction
"对比这两个判决书"      → 自动 OCR + 解析 + 比对
"分析这个微信聊天记录"  → OCR + 实体提取
"研究这份 Notion 链接"  → 网页抓取 + 索引
```

**实现**：MCP server + 输入适配器（PDF / EPUB / MD / OCR / 网页）

**工作量**：1-2 个月

**价值**：高——律师文件本就多样，多模态支持直接提升可用性。

---

### 🟡 P1-1 · L4 法律 Token 库

**问题**：GCL 当前只有方法（L5 Skills），没有"资产"。类比设计生态的 **DTCG tokens / design system**——**法律应该有"可复用法律单元库"**。

**启发**：建 `plugins/legal-tokens/` 层——
```
法条 token       常见法条（如《民法典》第 X 条）
条款 token       常见合同条款（保密 / 排他 / 不可抗力 / 争议解决）
请求 token       常见诉讼请求（合同违约 / 撤销权）
术语 token       法律术语定义（格式合同 / 显失公平 / 善意取得）
```

律师"拼装"合同/诉状时直接拖拽 token，而不是从零写。

**对比 L5 Skills**：
- L5 = 怎么做事（方法）
- L4 = 用什么做事（资产）

**工作量**：1-2 个月

**价值**：高——可复用资产层。

---

### 🟡 P1-2 · L6 多 Agent 支持

**问题**：GCL 假设 agent = Claude Code。设计生态支持 22+ agent（Claude Code / Cursor / OpenCode / Qwen Coder / Copilot / Hermes）。

**启发**：SKILL.md frontmatter 加多 agent 元数据——
```yaml
@agent:
  - claude-code
  - cursor
  - opencode
  - qwen-coder
```

不同 agent 的能力差异（如 trigger_phrases 召回机制、frontmatter 解析）做兼容层。

**工作量**：1 周

**价值**：中——扩展受众。

---

### 🟢 P2 · L2 多格式输出

**问题**：GCL 现在只输出 md。律师实际工作需要：
```
md       → 律师自己看
docx     → 给客户看
pdf      → 给法院看
时间线图  → 案件回顾
流程图    → 业务流程
```

**启发**：建 `plugins/legal-output-formats/` 层——多格式渲染器。

**工作量**：2-3 周

**价值**：中——输出便利。

---

## 实施优先级总览

| 优先级 | 启发 | 对应层 | 工作量 | 价值 |
|---|---|---|---|---|
| 🔴 P0-1 | 桥梁层（Word/VSCode/浏览器） | **L3** | 3-6 月 | **极高** |
| 🔴 P0-2 | 多模态输入 | L1 | 1-2 月 | 高 |
| 🟡 P1-1 | 法律 Token 库 | **L4** | 1-2 月 | 高 |
| 🟡 P1-2 | 多 Agent 支持 | L6 | 1 周 | 中 |
| 🟢 P2 | 多格式输出 | L2 | 2-3 周 | 中 |

**推荐执行顺序**：P0-1（L3 桥梁层）→ P1-1（L4 Token 库）→ P0-2（L1 多模态）→ P1-2（L6 多 agent）→ P2（L2 多格式）

---

## 跨层依赖

```
L3 桥梁层（律师真实使用入口）
    ↓ 依赖
L1 多模态输入（律师文件本就多样）
    ↓ 依赖
L5/L4（skill + token 库）
    ↓ 依赖
L6 多 agent（让 skill 跑在不同 runtime）
```

---

## 设计生态参考

### 标杆项目（按层）

| 层 | 标杆项目 | 借鉴点 |
|---|---|---|
| L7 | DESIGN.md（VoltAgent 92k★） | 自然语言触发 |
| L6 | 22+ agent CLIs | 多 runtime 兼容 |
| L5 | design skills（259+） | open-design skill 库 |
| L4 | DTCG tokens / design-extract（3.3k★） | 可复用单元库 |
| L3 | TalkToFigma（6.9k★） | Figma ↔ Agent MCP |
| L2 | screenshot-to-code（73k★） | 截图 → 代码 |
| L1 | onlook（26k★） | 多源适配 |

---

## 维护说明

本文件是**待办路线图**，不是实现计划。每完成一项，更新"已完成基线"。

相关文件：
- `docs/getting-started/SKILL_INDEX.md` —— 律师向索引（L7）
- `plugins/legal-research-templates/` —— L5 编排模板
- `CLAUDE.md` —— AI 运行时上下文

---

*Greater China Legal · ROADMAP v0.1 · 2026-06-24*