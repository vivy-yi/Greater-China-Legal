# litigation-support — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Litigation Support — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `admin-penalty-review` — admin-penalty-review / litigation_support / 行政处罚 / 复议 / 行政诉讼 / 处罚决定书
- `appeal-path-checker` — 上诉 / 申诉
- `asset-search-strategy` — asset-search-strategy / litigation_support / 财产线索 / 强制执行 / 查封财产 / 执行
- `brief-section-drafter` — brief-section-drafter / litigation_support / 起诉状 / 答辩状 / 上诉状 / 事实陈述 / 法律分析 / 诉讼文书
- `cause-action-analysis` — cause-action-analysis / litigation_support / 诉因分析 / 案由 / 诉讼时效 / 管辖法院
- `chronology` — 时间线 / 事实梳理
- `claim-chart` — 诉请 / 请求权
- `coercive-measure-assessment` — coercive-measure-assessment / litigation_support / 行为保全 / 财产保全 / 证据保全 / 禁令 / 诉讼禁令
- `crime-element-analysis` — crime-element-analysis / litigation_support / 刑事罪名 / 犯罪构成 / 诈骗罪 / 合同诈骗 / 职务侵占
- `demand-draft` — 律师函起草 / 催款函
- `demand-intake` — demand-intake / litigation_support
- `demand-received` — demand-received / litigation_support / 律师函 / 催告函 / 收到函件 / 法律函件
- `deposition-prep` — 取证 / 询问 / 质证
- `evidence-gathering-advisor` — evidence-gathering-advisor / litigation_support / 证据收集 / 证据保全 / 公证 / 电子取证 / 时间戳
- `evidence-organizer` — 证据整理 / 举证
- `execution-obstacle-removal` — execution-obstacle-removal / litigation_support
- `fee-calculator` — 律师费 / 诉讼费用
- `foreclosure-auction-advisor` — foreclosure-auction-advisor / litigation_support
- `government-contract-dispute` — government-contract-dispute / litigation_support
- `lawsuit-doc-generator` — 起诉状 / 答辩状 / 诉讼文书
- `legal-hold` — 证据保全 / 诉讼保全
- `litigation-cost-estimator` — litigation-cost-estimator / litigation_support / 诉讼费 / 律师费 / 仲裁费 / 诉讼成本 / 诉讼周期
- `matter-briefing` — matter-briefing / litigation_support
- `matter-close` — matter-close / litigation_support
- `matter-intake` — 案件受理 / 咨询
- `matter-update` — matter-update / litigation_support
- `oc-status` — oc-status / litigation_support
- `penalty-range-calculation` — penalty-range-calculation / litigation_support / 行政处罚 / 罚款幅度 / 听证 / 行政复议
- `portfolio-status` — 案件状态 / 诉讼组合 / 风险汇总 / 组合总览 / 所有案件 / 组合透视
- `privilege-log-review` — privilege-log-review / litigation_support
- `procedure-timeline` — 诉讼时效 / 程序期限
- `regulatory-filing-advisor` — regulatory-filing-advisor / litigation_support
- `statute-of-limitations` — 时效 / 诉讼时效 / 仲裁时效 / 上诉期限 / 执行期限 / 举证期限 / 保全期限 / 时效计算 / statute-of-limitations
- `strategy-designer` — 诉讼策略 / 法律策略
- `subpoena-triage` — subpoena-triage / litigation-support / 传票 / 调查令 / 文件调令 / 法院调令

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
