# administrative-litigation — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Administrative Litigation — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `compensation-claim` — 国家赔偿 / 行政补偿 / 行政赔偿 / 赔偿义务机关
- `defendant-identification` — 行政诉讼被告 / 被告确定 / 复议维持 / 共同被告
- `evidence-organization` — 行政证据 / 举证倒置 / 证据清单 / 行政诉讼证据
- `judgment-enforcement` — 行政判决执行 / 行政机关履行 / 不履行应对 / 司法拘留
- `litigation-acceptance-and-filing` — 行政诉讼 / 起诉 / 起诉期限 / 立案
- `trial-preparation` — 行政庭审 / 司法变更权 / 不停止执行 / 开庭准备

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
