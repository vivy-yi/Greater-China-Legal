# white-collar-crime — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:白领犯罪 — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `bribery-crime-advisor` — 贿赂 / 犯罪 / 顾问 / 白领犯罪 / 商业贿赂
- `bribery-risk-assessor` — 贿赂 / 评估 / 白领犯罪 / 商业贿赂 / 舞弊
- `compliance-program-designer` — 合规 / 设计 / 白领犯罪 / 商业贿赂 / 舞弊
- `corruption-compliance-advisor` — 腐败 / 合规 / 顾问 / 白领犯罪 / 商业贿赂
- `criminal-procedure-guide` — 指南 / 白领犯罪 / 商业贿赂 / 舞弊 / 调查
- `criminal-procedure-navigation` — 白领犯罪 / 商业贿赂 / 舞弊 / 调查
- `embezzlement-charge-checker` — 挪用 / 检查 / 白领犯罪 / 商业贿赂 / 舞弊
- `employee-misconduct-investigator` — 员工 / 不当行为 / 白领犯罪 / 商业贿赂 / 舞弊
- `fraud-crime-checker` — 欺诈 / 犯罪 / 检查 / 白领犯罪 / 商业贿赂
- `investigation-response-advisor` — 调查 / 顾问 / 白领犯罪 / 商业贿赂 / 舞弊
- `money-laundering-advisor` — 洗钱 / 顾问 / 白领犯罪 / 商业贿赂 / 舞弊
- `recovery-procedure-advisor` — 顾问 / 白领犯罪 / 商业贿赂 / 舞弊 / 调查
- `tax-crime-dispatcher` — 税务 / 犯罪 / 白领犯罪 / 商业贿赂 / 舞弊
- `tax-crime-risk-checker` — 税务 / 犯罪 / 检查 / 白领犯罪 / 商业贿赂
- `voluntary-disclosure-advisor` — 披露 / 顾问 / 白领犯罪 / 商业贿赂 / 舞弊

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
