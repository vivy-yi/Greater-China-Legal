# commercial-arbitration — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:商事仲裁 — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `arbitral-procedure-advisor` — 仲裁 / 商事争议 / CIETAC / arbitral procedure
- `arbitration-clause-drafter` — 仲裁 / 商事争议 / CIETAC / arbitration clause
- `arbitration-clause-reviewer` — 仲裁 / 商事争议 / CIETAC / arbitration clause
- `arbitration-cost-estimator` — 仲裁 / 商事争议 / CIETAC / arbitration cost estimator
- `asian-arbitration-comparison` — 仲裁 / 商事争议 / CIETAC / asian arbitration comparison
- `asset-preservation-advisor` — 仲裁 / 商事争议 / CIETAC / asset preservation
- `award-enforcement-checker` — 仲裁 / 商事争议 / CIETAC / award enforcement
- `bilateral-investment-advisor` — 仲裁 / 商事争议 / CIETAC / bilateral investment
- `cietac-procedure-advisor` — 仲裁 / 商事争议 / CIETAC / cietac procedure
- `emergency-arbitrator-advisor` — 仲裁 / 商事争议 / CIETAC / emergency arbitrator
- `evidence-rule-guide` — 仲裁 / 商事争议 / CIETAC / evidence rule
- `hkiac-procedure-advisor` — 仲裁 / 商事争议 / CIETAC / hkiac procedure
- `icc-procedure-advisor` — 仲裁 / 商事争议 / CIETAC / icc procedure
- `icsid-procedure-advisor` — 仲裁 / 商事争议 / CIETAC / icsid procedure
- `interim-measures-application` — 仲裁 / 商事争议 / CIETAC / interim measures application
- `investment-treaty-checker` — 仲裁 / 商事争议 / CIETAC / investment treaty
- `jurisdiction-dispute-advisor` — 仲裁 / 商事争议 / CIETAC / jurisdiction dispute
- `siac-procedure-advisor` — 仲裁 / 商事争议 / CIETAC / siac procedure

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
