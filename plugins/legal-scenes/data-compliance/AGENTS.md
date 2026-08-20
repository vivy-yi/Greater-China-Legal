# data-compliance — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Data Compliance — Greater China Legal Practice Profile

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `breach-notification` — breach-notification
- `cac-enforcement` — 执行 / 数据合规 / 个人信息 / PIPL / 跨境
- `clinical-data-sharing-advisor` — 数据 / 顾问 / 数据合规 / 个人信息 / PIPL
- `consent-mechanism-checker` — 检查 / 数据合规 / 个人信息 / PIPL / 跨境
- `critical-infrastructure-checker` — 检查 / 数据合规 / 个人信息 / PIPL / 跨境
- `csr-filing-advisor` — 备案 / 顾问 / 数据合规 / 个人信息 / PIPL
- `data-export-assessment` — 数据 / 评估 / 数据合规 / 个人信息 / PIPL
- `data-inventory` — 数据 / 数据合规 / 个人信息 / PIPL / 跨境
- `data-localization` — 数据 / 数据合规 / 个人信息 / PIPL / 跨境
- `dpa-review` — 审查 / 数据合规 / 个人信息 / PIPL / 跨境
- `dsar-response` — dsar-response
- `healthcare-ai-compliance` — 合规 / 数据合规 / 个人信息 / PIPL / 跨境
- `medical-data-classification` — 数据 / 数据合规 / 个人信息 / PIPL / 跨境
- `network-product-security-advisor` — 产品 / 顾问 / 数据合规 / 个人信息 / PIPL
- `pia-assessment-advisor` — 评估 / 顾问 / 数据合规 / 个人信息 / PIPL
- `pia-generation` — 数据合规 / 个人信息 / PIPL / 跨境
- `pipl-assessment` — 个人信息保护 / 评估 / 数据合规 / 个人信息 / PIPL
- `policy-monitor` — 监控 / 数据合规 / 个人信息 / PIPL / 跨境
- `privacy-policy-update` — privacy-policy-update
- `processing-basis` — 数据合规 / 个人信息 / PIPL / 跨境
- `reg-gap-analysis` — reg-gap-analysis
- `rights-exercise-system` — 数据合规 / 个人信息 / PIPL / 跨境
- `scc-implementation-advisor` — 顾问 / 数据合规 / 个人信息 / PIPL / 跨境
- `security-certification-advisor` — 顾问 / 数据合规 / 个人信息 / PIPL / 跨境
- `subject-rights` — 数据合规 / 个人信息 / PIPL / 跨境
- `use-case-triage` — 分类 / 数据合规 / 个人信息 / PIPL / 跨境

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
