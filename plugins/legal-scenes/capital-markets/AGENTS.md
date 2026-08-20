# capital-markets — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:资本市场 — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `abs-asset-segregation-advisor` — 资本市场 / IPO / 发债 / asset segregation
- `bond-coupon-calculator` — 资本市场 / IPO / 发债 / bond coupon
- `corporate-bond-eligibility-checker` — 资本市场 / IPO / 发债 / bond eligibility
- `hk-ipo-compliance-advisor` — 资本市场 / IPO / 发债 / compliance
- `compliance-assessor` — 资本市场 / IPO / 发债 / compliance
- `a-share-ipo-disclosure-reviewer` — 资本市场 / IPO / 发债 / disclosure
- `hk-ipo-eligibility-checker` — 资本市场 / IPO / 发债 / eligibility
- `corporate-bond-disclosure-monitor` — 资本市场 / IPO / 发债 / information disclosure
- `corporate-bond-procedure-advisor` — 资本市场 / IPO / 发债 / issuance procedure
- `a-share-ipo-issue-eligibility-checker` — 资本市场 / IPO / 发债 / issue eligibility
- `abs-product-eligibility-checker` — 资本市场 / IPO / 发债 / product eligibility
- `a-share-ipo-prospectus-drafter` — 资本市场 / IPO / 发债 / prospectus
- `hk-ipo-prospectus-reviewer` — 资本市场 / IPO / 发债 / prospectus
- `a-share-ipo-regulatory-tracker` — 资本市场 / IPO / 发债 / regulatory tracker
- `abs-transaction-structure-advisor` — 资本市场 / IPO / 发债 / transaction structure

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
