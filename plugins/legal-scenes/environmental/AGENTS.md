# environmental — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Environmental — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `carbon-trading` — 碳交易 / 碳排放权 / CCER
- `environmental-administrative` — 环境行政 / 行政处罚 / 听证
- `environmental-impact-assessment` — 环评 / 环境影响评价 / 公众参与
- `environmental-public-interest` — 公益诉讼 / 环保组织 / 检察机关
- `environmental-tort` — 环境侵权 / 污染损害 / 生态损害
- `esg-compliance` — ESG / 披露 / greenwashing

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
