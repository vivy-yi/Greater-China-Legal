# antitrust — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Antitrust — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `abuse-of-dominance` — 市场支配 / 滥用支配地位 / 平台垄断 / 数据垄断
- `antitrust-investigation` — 反垄断调查 / 调查应对 / 反垄断局 / 处罚决定
- `leniency-application` — 宽大制度 / 主动报告 / 宽大申请 / 卡特尔减免
- `merger-filing` — 经营者集中 / 反垄断申报 / 并购申报 / 集中审查
- `monopoly-agreement-review` — 垄断协议 / 卡特尔 / 反垄断协议 / 价格协调
- `private-antitrust-litigation` — 反垄断诉讼 / 私人诉讼 / 民事赔偿 / 反垄断民事

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
