# bankruptcy-restructuring — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Bankruptcy Restructuring — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `asset-disposal-advisor` — 破产 / 清算 / 重整 / asset disposal
- `asset-liquidation-advisor` — 破产 / 清算 / 重整 / asset liquidation
- `bankruptcy-eligibility-checker` — 破产 / 清算 / 重整 / bankruptcy eligibility
- `bankruptcy-petition-filer` — 破产 / 清算 / 重整 / bankruptcy petition
- `core-asset-preservation-advisor` — 破产 / 清算 / 重整 / core asset preservation
- `creditor-claims-calculator` — 破产 / 清算 / 重整 / creditor claims
- `creditor-claims-manager` — 破产 / 清算 / 重整 / creditor claims
- `cross-border-insolvency-advisor` — 破产 / 清算 / 重整 / cross border insolvency
- `debt-restructuring-planner` — 破产 / 清算 / 重整 / debt restructuring
- `director-liability-checker` — 破产 / 清算 / 重整 / director liability
- `employee-handling-advisor` — 破产 / 清算 / 重整 / employee handling
- `non-core-asset-disposal-advisor` — 破产 / 清算 / 重整 / non core asset disposal
- `reorganization-feasibility-checker` — 破产 / 清算 / 重整 / reorganization feasibility
- `restructuring-plan-reviewer` — 破产 / 清算 / 重整 / restructuring plan
- `stakeholder-negotiation-advisor` — 破产 / 清算 / 重整 / stakeholder negotiation

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
