# legal-clinic — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:法律援助 / 公益法律诊所 — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `build-guide` — 法律诊所 / 法援 / build
- `client-comms-log` — 法律诊所 / 法援 / client comms log
- `client-intake` — 法律诊所 / 法援 / client
- `client-letter` — 法律诊所 / 法援 / client letter
- `cold-start-interview` — 法律诊所 / 法援 / cold start interview
- `customize` — 法律诊所 / 法援 / customize
- `deadlines` — 法律诊所 / 法援 / deadlines
- `draft` — 法律诊所 / 法援 / draft
- `form-generation` — 法律诊所 / 法援 / form generation
- `memo` — 法律诊所 / 法援 / memo
- `plain-language-letters` — 法律诊所 / 法援 / plain language letters
- `ramp` — 法律诊所 / 法援 / ramp
- `research-start` — 法律诊所 / 法援 / research start
- `semester-handoff` — 法律诊所 / 法援 / semester handoff
- `status` — 法律诊所 / 法援 / status
- `supervisor-review-queue` — 法律诊所 / 法援 / supervisor review queue

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
