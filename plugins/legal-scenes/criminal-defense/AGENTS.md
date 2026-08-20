# criminal-defense — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Criminal Defense — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `bail-and-detention` — 取保候审 / 监视居住 / 解除羁押 / 强制措施变更
- `case-file-review` — 阅卷 / 证据梳理 / 非法证据排除 / 证据三性
- `defense-drafting` — 辩护词 / 上诉状 / 不起诉意见 / 法律意见书
- `defense-strategy` — 辩护策略 / 无罪辩护 / 罪轻辩护 / 认罪认罚
- `engagement-and-meeting` — 刑事辩护 / 接受委托 / 首次会见 / 会见笔录
- `trial-defense` — 庭审 / 质证 / 法庭辩论 / 最后陈述

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
