# wealth-succession — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:财富传承 — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `estate-inventory-assessor` — 遗产 / 评估 / 财富传承 / 信托 / 遗嘱
- `estate-tax-planner` — 遗产 / 税务 / 规划 / 财富传承 / 信托
- `family-charter-drafter` — 起草 / 财富传承 / 信托 / 遗嘱 / 继承
- `family-council-design-advisor` — 顾问 / 财富传承 / 信托 / 遗嘱 / 继承
- `family-governance-advisor` — 顾问 / 财富传承 / 信托 / 遗嘱 / 继承
- `family-trust-structuring-advisor` — 信托 / 架构 / 顾问 / 财富传承 / 遗嘱
- `heir-dispute-advisor` — 继承人 / 争议 / 顾问 / 财富传承 / 信托
- `next-generation-education-advisor` — 顾问 / 财富传承 / 信托 / 遗嘱 / 继承
- `prenuptial-agreement-checker` — 检查 / 财富传承 / 信托 / 遗嘱 / 继承
- `probate-procedure-guide` — 指南 / 财富传承 / 信托 / 遗嘱 / 继承
- `testament-drafting-checker` — 检查 / 财富传承 / 信托 / 遗嘱 / 继承
- `testament-formality-checker` — 检查 / 财富传承 / 信托 / 遗嘱 / 继承
- `trust-structure-advisor` — 信托 / 顾问 / 财富传承 / 遗嘱 / 继承
- `trust-tax-planning-advisor` — 信托 / 税务 / 顾问 / 财富传承 / 遗嘱

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
