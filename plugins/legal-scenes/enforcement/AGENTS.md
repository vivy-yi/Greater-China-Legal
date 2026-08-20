# enforcement — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Enforcement — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `application-and-filing` — 执行立案 / 申请执行 / 执行期限 / 强制执行
- `execution-measures` — 查封 / 划拨 / 拍卖 / 失信被执行人
- `objection-and-dispute` — 执行异议 / 案外人异议 / 异议之诉
- `preservation-measures` — 财产保全 / 诉前保全 / 行为保全
- `property-investigation` — 财产调查 / 调查令 / 财产线索
- `settlement-and-distribution` — 执行和解 / 财产分配 / 多债权人

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
