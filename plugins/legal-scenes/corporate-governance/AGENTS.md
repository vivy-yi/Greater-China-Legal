# corporate-governance — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Corporate Governance — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `ai-tool-handoff` — AI工具 / 交接
- `board-minutes` — 董事会决议 / 会议记录
- `board-resolution-reviewer` — board-resolution-reviewer / corporate_governance / 董事会决议 / 股东会决议 / 股东大会决议 / 公司决议
- `capital-change` — 注册资本 / 股权变更
- `closing-checklist` — 交割清单 / checklist
- `deal-team-summary` — 交易团队 / 项目组
- `diligence-issue-extraction` — 尽调 / 尽职调查
- `director-liability-insurance` — director-liability-insurance / corporate_governance / 董责险 / 董事责任险 / 高管责任险 / D&O保险 / 董事高管责任
- `duality-reduction-advisor` — duality-reduction-advisor / corporate_governance / 两权分离 / 两职合一 / 董事长兼总经理 / 实际控制人 / 独立董事 / 公司治理结构 / ESG治理
- `entity-compliance` — 公司合规 / 合规管理
- `entity-setup` — 公司设立 / 注册
- `equity-split-design` — equity-split-design / 股权结构设计 / 股权分配 / 股权比例 / 创始股东 / 合伙人股权 / 控制权 / 股权调整 / 动态股权
- `esop-incentive-plan` — esop / esop-incentive-plan / 股权激励 / 员工期权 / 期权授予 / 限制性股票 / RSU / 员工持股 / 股份期权 / stock-option / restricted-stock / vesting / corporate_governance
- `family-holding-structure` — family-holding-structure / corporate_governance / 家族持股 / 家族企业 / 股权传承 / 家族信托 / 股权代持 / 家族办公室 / 企业传承
- `financing-cycle` — 融资 / 资金周期
- `governance-design` — 治理结构 / 设计
- `integration-management` — 整合管理 / 并购
- `material-contract-schedule` — 重大合同 / 合同清单
- `minority-rights-protection` — minority-rights-protection / 中小股东权益保护 / 少数股东权 / 异议股东回购请求权 / 股东代表诉讼 / 派生诉讼
- `odi-compliance` — ODI备案 / 境外投资
- `performance-appraisal-legal` — performance-appraisal-legal / corporate_governance / 绩效考核 / 不胜任退出 / 绩效考核违法 / 末位淘汰 / 绩效改进 / 劳动法绩效考核
- `profit-sharing-plan` — profit-sharing-plan / 利润分配 / 分红方案 / 分红条件 / 股东分红 / 滚存利润 / 分红决议 / 分红比例 / 分红程序 / 分红限制
- `related-party-transaction` — related-party-transaction / 关联交易 / 关联方认定 / 关联交易的审批 / 关联交易披露 / 关联企业 / 控股股东 / 实际控制人 / 上市公司关联交易 / corporate_governance
- `shareholder-meeting-advisor` — shareholder-meeting-advisor / 召集程序 / 股东会召集 / 股东大会召集 / 会议通知 / 临时提案 / 股东会效力 / 股东大会效力
- `tabular-review` — 表格审查 / 合规表
- `transfer-restriction-advisor` — transfer-restriction-advisor / corporate_governance / 股权转让 / 优先购买权 / 股权转让限制 / 股东退出 / 股权转让合同 / 章程限制 / 股权转让程序
- `vie-red-flag` — VIE风险 / 红筹
- `written-consent` — written-consent / corporate_governance / 书面决定 / 书面决议 / 股东书面决定 / 董事书面决议 / 签字有效 / 股东会书面方式 / 董事会书面方式 / 豁免开会

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
