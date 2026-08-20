# product-legal — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Product Legal — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `cold-start-interview` — 产品发布 / 营销 / 合规 / 风险 / cold-start / cold_start
- `customize` — 产品发布 / 营销 / 合规 / 风险 / customize / 定制
- `feature-risk-assessment` — 评估 / 产品发布 / 营销 / 合规 / 风险
- `is-this-a-problem` — 产品发布 / 营销 / 合规 / 风险
- `launch-review` — 发布 / 审查 / 产品发布 / 营销 / 合规
- `marketing-claims-review` — 营销 / 审查 / 产品发布 / 合规 / 风险
- `matter-workspace` — 产品发布 / 营销 / 合规 / 风险 / matter-workspace / 案件管理

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
