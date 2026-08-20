# special-opportunity-investment — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:特殊机会投资 — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `judgment-investment-advisor` — 不良资产 / 困境资产 / 债务重组 / 借壳上市 / SPAC / Pre-IPO / 诉讼投资 / 判决债权
- `arbitration-award-investment` — 不良资产 / 困境资产 / 债务重组 / 借壳上市 / SPAC / Pre-IPO / 诉讼投资 / 判决债权
- `backdoor-listing-advisor` — 不良资产 / 困境资产 / 债务重组 / 借壳上市 / SPAC / Pre-IPO / 诉讼投资 / 判决债权
- `collateral-enforcement-advisor` — 不良资产 / 困境资产 / 债务重组 / 借壳上市 / SPAC / Pre-IPO / 诉讼投资 / 判决债权
- `debt-restructuring-advisor` — 不良资产 / 困境资产 / 债务重组 / 借壳上市 / SPAC / Pre-IPO / 诉讼投资 / 判决债权
- `ipo-anchor-investor-advisor` — 不良资产 / 困境资产 / 债务重组 / 借壳上市 / SPAC / Pre-IPO / 诉讼投资 / 判决债权
- `judgment-investment-advisor` — 不良资产 / 困境资产 / 债务重组 / 借壳上市 / SPAC / Pre-IPO / 诉讼投资 / 判决债权
- `litigation-funding-advisor` — 不良资产 / 困境资产 / 债务重组 / 借壳上市 / SPAC / Pre-IPO / 诉讼投资 / 判决债权
- `npl-acquisition-advisor` — 不良资产 / 困境资产 / 债务重组 / 借壳上市 / SPAC / Pre-IPO / 诉讼投资 / 判决债权
- `special-purpose-acquisition` — 不良资产 / 困境资产 / 债务重组 / 借壳上市 / SPAC / Pre-IPO / 诉讼投资 / 判决债权

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
