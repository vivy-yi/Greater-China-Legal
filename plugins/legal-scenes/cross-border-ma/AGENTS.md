# cross-border-ma — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Cross-Border M&A — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `closing-checklist` — 跨境并购 / ODI / 外资 / closing checklist
- `dd-checker` — 跨境并购 / ODI / 外资 / dd
- `fdi-odi-filing` — 跨境并购 / ODI / 外资 / fdi odi filing
- `regulatory-approval` — 跨境并购 / ODI / 外资 / regulatory approval
- `structure-designer` — 跨境并购 / ODI / 外资 / structure
- `transaction-doc-review` — 跨境并购 / ODI / 外资 / transaction doc

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
