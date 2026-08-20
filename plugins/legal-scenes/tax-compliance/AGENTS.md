# tax-compliance — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Tax Compliance — Greater China Legal Practice Profile

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `beps-compliance-advisor` — 合规 / 顾问 / 税务 / 所得税 / 增值税
- `comments` — 税务 / 所得税 / 增值税 / 转让定价
- `consumption-tax-compliance` — 税务 / 合规 / 所得税 / 增值税 / 转让定价
- `cross-border-tax-checker` — 跨境 / 税务 / 检查 / 所得税 / 增值税
- `deduction-compliance-checker` — 合规 / 检查 / 税务 / 所得税 / 增值税
- `eit-return-reviewer` — 审查 / 税务 / 所得税 / 增值税 / 转让定价
- `equity-incentive-tax-advisor` — 股权 / 税务 / 顾问 / 所得税 / 增值税
- `gap-surfacer` — 税务 / 所得税 / 增值税 / 转让定价
- `gaps` — 税务 / 所得税 / 增值税 / 转让定价
- `high-net-worth-tax-optimization` — 税务 / 优化 / 所得税 / 增值税 / 转让定价
- `individual-income-tax-planner` — 税务 / 规划 / 所得税 / 增值税 / 转让定价
- `input-tax-credit-checker` — 税务 / 检查 / 所得税 / 增值税 / 转让定价
- `invoice-compliance-checker` — 合规 / 检查 / 税务 / 所得税 / 增值税
- `policy-diff` — 税务 / 所得税 / 增值税 / 转让定价
- `policy-redraft` — 税务 / 所得税 / 增值税 / 转让定价
- `reg-feed-watcher` — 税务 / 所得税 / 增值税 / 转让定价
- `tax-dispute-handler` — 税务 / 争议 / 所得税 / 增值税 / 转让定价
- `tax-preference-application-advisor` — 税务 / 顾问 / 所得税 / 增值税 / 转让定价
- `tax-treaty-application-advisor` — 税务 / 顾问 / 所得税 / 增值税 / 转让定价
- `tax-type-classifier` — 税务 / 所得税 / 增值税 / 转让定价
- `transfer-pricing-checker` — 转让 / 定价 / 检查 / 税务 / 所得税
- `transfer-pricing-risk` — 转让 / 定价 / 税务 / 所得税 / 增值税
- `vat-credit-calculator` — 增值税 / 计算 / 税务 / 所得税 / 转让定价
- `vat-rate-classification-advisor` — 增值税 / 顾问 / 税务 / 所得税 / 转让定价

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
