# cross-border-trade — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:跨境贸易 — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `sanctioned-entity-checker` — 跨境 / 进出口 / 海关 / sanctioned entity
- `customs-compliance-assessor` — 跨境 / 进出口 / 海关 / customs compliance
- `customs-valuation-checker` — 跨境 / 进出口 / 海关 / customs valuation
- `dual-use-goods-classifier` — 跨境 / 进出口 / 海关 / dual use goods
- `export-control-reviewer` — 跨境 / 进出口 / 海关 / export control
- `export-license-assessment` — 跨境 / 进出口 / 海关 / export license
- `forfaiting-compliance-advisor` — 跨境 / 进出口 / 海关 / forfaiting compliance
- `fta-origin-certifier` — 跨境 / 进出口 / 海关 / fta origin certifier
- `import-tariff-adviser` — 跨境 / 进出口 / 海关 / import tariff
- `incoterms-guide` — 跨境 / 进出口 / 海关 / incoterms
- `letter-of-credit-reviewer` — 跨境 / 进出口 / 海关 / letter of credit
- `tariff-classification-advisor` — 跨境 / 进出口 / 海关 / tariff classification
- `trade-dispute-advisor` — 跨境 / 进出口 / 海关 / trade dispute
- `trade-finance-sanctions-checker` — 跨境 / 进出口 / 海关 / trade finance sanctions
- `trade-sanctions-checker` — 跨境 / 进出口 / 海关 / trade sanctions

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
