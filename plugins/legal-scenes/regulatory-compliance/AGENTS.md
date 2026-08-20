# regulatory-compliance — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Regulatory Compliance — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `aml-kyc-checker` — 检查 / 监管 / 牌照 / 安全 / 合规
- `bank-supervision-advisor` — 顾问 / 监管 / 牌照 / 安全 / 合规
- `compliance-gap-assessor` — 合规 / 评估 / 监管 / 牌照 / 安全
- `data-localization-checker` — 数据 / 检查 / 监管 / 牌照 / 安全
- `drug-approval-checker` — 检查 / 监管 / 牌照 / 安全 / 合规
- `enforcement-response-advisor` — 执行 / 顾问 / 监管 / 牌照 / 安全
- `environmental-impact-assessor` — 评估 / 监管 / 牌照 / 安全 / 合规
- `gmp-compliance-advisor` — 合规 / 顾问 / 监管 / 牌照 / 安全
- `hazardous-chemical-compliance` — 合规 / 监管 / 牌照 / 安全
- `industry-specific-compliance` — 合规 / 监管 / 牌照 / 安全
- `insurance-regulatory-advisor` — 保险 / 监管 / 顾问 / 牌照 / 安全
- `internet-content-compliance` — 互联网 / 合规 / 监管 / 牌照 / 安全
- `license-eligibility-checker` — 牌照 / 检查 / 监管 / 安全 / 合规
- `medical-device-registration` — 登记 / 监管 / 牌照 / 安全 / 合规
- `regulatory-change-tracker` — 监管 / 追踪 / 牌照 / 安全 / 合规
- `safety-production-advisor` — 顾问 / 监管 / 牌照 / 安全 / 合规
- `securities-compliance-checker` — 合规 / 检查 / 监管 / 牌照 / 安全
- `telecom-license-advisor` — 牌照 / 顾问 / 监管 / 安全 / 合规

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
