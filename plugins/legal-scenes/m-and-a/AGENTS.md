# m-and-a — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:M&A — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `domestic-ma-approval-checker` — 并购 / 股权收购 / 资产收购 / 退市
- `deal-structurer` — 并购 / 股权收购 / 资产收购 / 退市
- `domestic-ma-disclosure-checker` — 披露 / 并购 / 股权收购 / 资产收购 / 退市
- `domestic-ma-due-diligence` — 尽调 / 并购 / 股权收购 / 资产收购 / 退市
- `due-diligence-checker` — 尽调 / 检查 / 并购 / 股权收购 / 资产收购
- `cross-border-ma-fem-procedures` — 并购 / 股权收购 / 资产收购 / 退市
- `going-private-approval-advisor` — 顾问 / 并购 / 股权收购 / 资产收购 / 退市
- `going-private-price-advisor` — 顾问 / 并购 / 股权收购 / 资产收购 / 退市
- `going-private-scheme-design-checker` — 私有化方案 / 上市公司私有化 / 私有化合规 / 私有化审查 / going-private / 要约收购 / 吸收合并
- `cross-border-ma-odi-filing` — 备案 / 并购 / 股权收购 / 资产收购 / 退市
- `post-closing-integration` — 并购 / 股权收购 / 资产收购 / 退市
- `cross-border-ma-red-chip-advisor` — 并购 / 股权收购 / 资产收购 / 退市
- `regulatory-approval-tracker` — 监管 / 追踪 / 并购 / 股权收购 / 资产收购
- `sha-negotiator` — 并购 / 股权收购 / 资产收购 / 退市
- `signing-closing-checklist` — 并购 / 股权收购 / 资产收购 / 退市
- `tender-offer-approval-advisor` — 顾问 / 并购 / 股权收购 / 资产收购 / 退市
- `tender-offer-price-advisor` — 顾问 / 并购 / 股权收购 / 资产收购 / 退市
- `tender-offer-scheme-checker` — 检查 / 并购 / 股权收购 / 资产收购 / 退市
- `domestic-ma-valuation-advisor` — 估值 / 并购 / 股权收购 / 资产收购 / 退市

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
