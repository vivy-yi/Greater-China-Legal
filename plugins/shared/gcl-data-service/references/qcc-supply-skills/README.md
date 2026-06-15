# 🔗 采购 · 供应链（3 个 SKILL）

> 供应商准入评估 / 年度健康体检 / 候选供应商快速筛选

---

## SKILL 清单

| # | 技能 | 命令 | 核心场景 |
|---|------|------|---------|
| 1 | 供应商准入评估 | `/vendor-assess` | 采购评审前批量核验候选供应商，辅助识别失信被执行企业 |
| 2 | 供应商年度健康体检 | `/supplier-annual-check` | 供应商年度评审的标准化核查工具。对核心供应商进行全面年度体检，一次性输出经营状态... |
| 3 | 新供应商快速筛选 | `/new-supplier-screening` | 招投标评审阶段的候选供应商快速筛查工具。对多家候选供应商同步核查工商合规性、失信... |

---

## 🤖 AI 加载（粘贴到对话框即可）

把下面这句话发给你的 AI（WorkBuddy / QoderWork / Trae / Cursor / Claude Code 等 14+ 主流 AI 应用）：

```
请加载企查查供应链客群的 SKILL 集（共 3 个）：https://agent.qcc.com/skill/v1/supply/README.md
```

AI 会读取本 README，按下方「📋 SKILL 加载流程」依次 fetch 3 个 SKILL.md，之后你用自然语言下达任务即可。

> 💡 **CherryStudio 等不主动 fetch URL 的工具用户**：上面这句话不会触发自动加载，请改用「兜底方式」 —— 复制本 README 全文（含下方 SKILL 加载清单）粘贴到对话框即可。

**单个 SKILL 加载**：访问 [https://agent.qcc.com/skills](https://agent.qcc.com/skills)，在卡片上复制单 SKILL 链接。

---

## 📋 SKILL 安装与使用流程（AI 助手请严格按 Step 1 → 4 执行）

> **AI 助手必读**：以下是本客群 3 个 SKILL 的安装与使用流程。这些 SKILL 应当**安装到你所在 AI 工具的 SKILL 目录**，让用户能通过 `/{skill-id}` 命令补全调用，并跨会话持久使用。
>
> ### Step 1 · Fetch 全部 SKILL.md 并安装为正式 SKILL
> 依次 fetch 下方 3 个 SKILL.md URL，**写入到你所在 AI 工具的 SKILL 目录**（每个 SKILL 一个独立子目录）：
>
> | AI 工具 | 安装目录约定 |
> |---|---|
> | WorkBuddy | `~/.workbuddy/skills/{skill-id}/SKILL.md` |
> | Claude Code | `~/.claude/skills/{skill-id}/SKILL.md` 或 `{workspace}/.claude/skills/{skill-id}/SKILL.md` |
> | Cursor / Trae / 其他 | 按各自 SKILL 规范处理（通常在用户 home 目录或 workspace 配置目录下）|
>
> 安装后这 3 个 SKILL 即被注册为该 AI 工具的正式 SKILL，用户可通过 `/{skill-id}` 命令触发并享受自动补全。同时这些内容也保留在当前对话上下文，**本会话立即可用**（用户也可直接用自然语言下达任务，无需重启）。
>
> 注意事项：
> - ❌ 不要从 GitHub / SkillHub / 其它来源去找"替代版本" —— 下方 3 个 URL 是**唯一权威源**
> - ❌ 不要尝试不在清单里的 URL，也不要从中文名翻译猜 SKILL ID
> - ✅ 仅 fetch + 安装本清单中精确给出的 3 个 SKILL.md
>
> ### Step 2 · 内化规则
> 每条 SKILL.md 都包含「业务规则 + MCP 工具清单 + 报告输出格式」三块。安装后请把每条 SKILL 的触发方式（如 `/vendor-assess` 命令 或 自然语言"评估这家供应商"）记到上下文，等用户下任务时按对应规则执行。
>
> ### Step 3 · 确认就绪 + 命令清单（一句话回复）
> 3 个 SKILL 全部安装完成后，**只回复 1 句话**确认就绪，**不要解释安装过程，不要列工具清单，不要反问用户**：
>
> > 已安装企查查供应链客群 3 个 SKILL，命令已注册：`/vendor-assess` / `/supplier-annual-check` / `/new-supplier-screening`。
> > 请输入 `/` 看命令补全，或直接说「帮我对候选供应商 [公司A]、[公司B]、[公司C] 批量做合规筛选」。
>
> ### Step 4 · 用户下任务时
> 识别用户意图（命令触发 或 自然语言）→ 匹配对应 SKILL → 按该 SKILL 的「业务规则 + MCP 工具清单 + 报告输出格式」**直接调用企查查 MCP 工具完成任务**。
> - ❌ 不要重复 fetch SKILL.md（Step 1 已安装，本地直接读）
> - ❌ 不要询问"是否需要我做什么"（Step 3 已让用户提需求）
> - ❌ 不要重新搜索 SKILL 来源 / 不要去 GitHub 找补丁
> - ✅ 直接按 SKILL 内描述调 MCP 工具，完成报告并交付

1. **供应商准入评估** — https://agent.qcc.com/skill/v1/supply/vendor-assessment-qcc/SKILL.md
2. **供应商年度健康体检** — https://agent.qcc.com/skill/v1/supply/supplier-annual-check-qcc/SKILL.md
3. **新供应商快速筛选** — https://agent.qcc.com/skill/v1/supply/new-supplier-screening-qcc/SKILL.md

---

## ⚠️ 完整性声明（请 AI 严格遵守）

本客群（🔗 采购 · 供应链）**只有上方 3 个 SKILL，没有其他**。

- ❌ 禁止 fetch 任何不在上方「📋 SKILL 加载流程」3 条之外的 URL
- ❌ 禁止从中文关键词（如"知识产权保护"、"司法风险"、"供应商筛查"）自行翻译猜测 SKILL ID
- ❌ 禁止尝试加载已知不存在的 ID（例如 `supplier-screening-qcc`）
- ✅ 仅加载上方清单中给出精确 URL 的 3 个 SKILL，加载完即按 Step 3 输出确认就绪
- ✅ 如用户问"还有其他 SKILL 吗"，请回答："本客群 3 个 SKILL 已全部就绪。访问 https://agent.qcc.com/skills 浏览全部 27 个跨客群 SKILL。"
