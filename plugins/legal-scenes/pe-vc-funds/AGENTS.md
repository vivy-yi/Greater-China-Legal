# pe-vc-funds — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:PE/VC Funds — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `afl-compliance-assessor` — 合规 / 评估 / 私募 / 基金 / 投资
- `anti-dilution-checker` — 检查 / 私募 / 基金 / 投资 / 对赌
- `capital-call-calculator` — capital-call-calculator
- `drag-along-tag-along-advisor` — 顾问 / 私募 / 基金 / 投资 / 对赌
- `exit-strategy-advisor` — exit-strategy-advisor
- `fund-disclosure-reviewer` — 基金 / 披露 / 审查 / 私募 / 投资
- `fund-formation-checker` — 基金 / 检查 / 私募 / 投资 / 对赌
- `fund-performance-reporter` — fund-performance-reporter
- `fund-structuring-advisor` — 基金 / 架构 / 顾问 / 私募 / 投资
- `gp-background-checker` — 检查 / 私募 / 基金 / 投资 / 对赌
- `gp-lp-agreement-drafter` — 起草 / 私募 / 基金 / 投资 / 对赌
- `investment-agreement-checker` — 投资 / 检查 / 私募 / 基金 / 对赌
- `investment-agreement-reviewer` — investment-agreement-reviewer
- `lp-due-diligence` — lp-due-diligence
- `registration-filing-advisor` — 登记 / 备案 / 顾问 / 私募 / 基金
- `term-sheet-reviewer` — 审查 / 私募 / 基金 / 投资 / 对赌
- `tt-clause-reviewer` — 审查 / 私募 / 基金 / 投资 / 对赌
- `valuation-adjustment-advisor` — 估值 / 顾问 / 私募 / 基金 / 投资

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
