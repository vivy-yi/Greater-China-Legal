# ai-governance-legal — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:AI Governance Legal — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `policy-monitor` — AI政策有哪些更新 / 互联网法规变化 / 深度合成规定 / 生成式AI监管 / 算法备案 / AI合规监控
- `reg-gap-analysis` — AI监管差距 / 生成式AI合规 / 算法备案差距 / AI安全评估 / 深度合成合规 / 互联网法规对照
- `use-case-triage` — AI应用场景合规 / 这个功能需要ICP许可吗 / AI产品需要哪些牌照 / 业务场景合规审查 / 互联网金融业务资质

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
