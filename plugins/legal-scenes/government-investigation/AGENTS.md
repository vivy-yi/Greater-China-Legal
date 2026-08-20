# government-investigation — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:政府监管与调查应对 — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `monopoly-investigation-response` — 反垄断 / 经营者集中 / 内幕交易 / 信披违规 / 证监会调查 / 商业贿赂 / 反腐合规 / 反商业贿赂合规
- `competition-compliance-advisor` — 反垄断 / 经营者集中 / 内幕交易 / 信披违规 / 证监会调查 / 商业贿赂 / 反腐合规 / 反商业贿赂合规
- `corruption-risk-assessment` — 反垄断 / 经营者集中 / 内幕交易 / 信披违规 / 证监会调查 / 商业贿赂 / 反腐合规 / 反商业贿赂合规
- `fcpa-bribery-act-advisor` — 反垄断 / 经营者集中 / 内幕交易 / 信披违规 / 证监会调查 / 商业贿赂 / 反腐合规 / 反商业贿赂合规
- `information-disclosure-violation` — 反垄断 / 经营者集中 / 内幕交易 / 信披违规 / 证监会调查 / 商业贿赂 / 反腐合规 / 反商业贿赂合规
- `insider-trading-investigation` — 反垄断 / 经营者集中 / 内幕交易 / 信披违规 / 证监会调查 / 商业贿赂 / 反腐合规 / 反商业贿赂合规
- `internal-investigation-advisor` — 反垄断 / 经营者集中 / 内幕交易 / 信披违规 / 证监会调查 / 商业贿赂 / 反腐合规 / 反商业贿赂合规
- `merger-filing-checker` — 反垄断 / 经营者集中 / 内幕交易 / 信披违规 / 证监会调查 / 商业贿赂 / 反腐合规 / 反商业贿赂合规
- `securities-enforcement-response` — 反垄断 / 经营者集中 / 内幕交易 / 信披违规 / 证监会调查 / 商业贿赂 / 反腐合规 / 反商业贿赂合规

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
