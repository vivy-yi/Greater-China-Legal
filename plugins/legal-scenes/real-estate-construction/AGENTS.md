# real-estate-construction — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Real Estate Construction — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `commercial-lease-reviewer` — 房地产开发 / 建设工程 / 物业租赁 / 工程款 / REITs / 土地出让 / 预售
- `construction-contract-reviewer` — 房地产开发 / 建设工程 / 物业租赁 / 工程款 / REITs / 土地出让 / 预售
- `construction-defect-advisor` — 房地产开发 / 建设工程 / 物业租赁 / 工程款 / REITs / 土地出让 / 预售
- `engineering-quantity-dispute` — 房地产开发 / 建设工程 / 物业租赁 / 工程款 / REITs / 土地出让 / 预售
- `land-acquisition-checker` — 房地产开发 / 建设工程 / 物业租赁 / 工程款 / REITs / 土地出让 / 预售
- `long-term-lease-advisor` — 房地产开发 / 建设工程 / 物业租赁 / 工程款 / REITs / 土地出让 / 预售
- `pre-sale-compliance-advisor` — 房地产开发 / 建设工程 / 物业租赁 / 工程款 / REITs / 土地出让 / 预售
- `property-management-dispute` — 房地产开发 / 建设工程 / 物业租赁 / 工程款 / REITs / 土地出让 / 预售
- `reit-structure-advisor` — 房地产开发 / 建设工程 / 物业租赁 / 工程款 / REITs / 土地出让 / 预售

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
