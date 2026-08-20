# contract-review — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Contract Review — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `amendment-history` — 合同变更 / 补充协议
- `civil-code-checker` — 民法典 / 合同合规
- `commercial-lease-drafter` — 商业租赁合同起草 / 商铺租赁 / 厂房租赁 / lease-real-estate / contract-review / commercial-lease-drafter
- `confidentiality-nda-reviewer` — 保密协议审查 / NDA审查 / confidentiality-nda-reviewer / contract-review / 竞业限制
- `contract-classifier` — 合同分类 / 类型识别
- `debt-collection-letter` — 催款函起草 / debt-collection-letter / contract-review / 律师函 / 货款催收
- `dispute-handler` — 合同纠纷 / 争议解决
- `ecommerce-sales-contract` — 电商平台交易合同审查 / ecommerce-sales-contract / contract-review / 平台入驻 / 电商合同
- `escalation-flagger` — 合同升级 / 风险标记
- `housing-lease-reviewer` — 房屋租赁合同审查 / housing-lease-reviewer / contract-review / 租房合同 / 住宅租赁
- `international-sales-advisor` — 国际贸易合同咨询 / international-sales-advisor / contract-review / 进出口合同 / 外贸合同 / INCOTERMS / 信用证
- `labor-contract-audit` — 劳动合同审计 / labor-contract-audit / contract-review / 劳动合同 / 雇佣合同 / offer审查
- `land-lease-agreement` — 土地租赁合同审查 / land-lease-agreement / contract-review / 土地租赁 / 农用地租赁 / 建设用地租赁
- `loan-agreement-checker` — 借贷合同审查 / loan-agreement-checker / contract-review / 借款合同 / 民间借贷 / 利率 / 担保合同
- `mutual-fund-bylaws` — 私募基金合同审查 / mutual-fund-bylaws / contract-review / 基金合同 / 私募基金 / 合伙协议
- `nda-review` — 保密协议 / NDA审查 / 保密合同 / nda-review / 非公开协议
- `negotiation-redlines` — 合同谈判 / 条款协商
- `renewal-tracker` — 合同续期 / 续约
- `review` — 合同审查 / 审核
- `review-proposals` — 合同提案 / 审查建议
- `risk-clause-database` — 风险条款 / 合同条款库 / 风险条款数据库 / 合同风险 / 条款风险
- `risk-triage` — 合同风险 / 风险评估
- `saas-msa-review` — SaaS协议 / 服务协议 / 订阅协议 / MSA审查 / saas-msa-review
- `service-contract-reviewer` — 服务合同审查 / service-contract-reviewer / contract-review / 咨询合同 / IT服务合同 / 设计合同 / 代理合同
- `stakeholder-summary` — 合同概要 / 利益相关方 / 业务摘要 / 非法律摘要 / stakeholder-summary
- `standard-sales-reviewer` — 商品买卖合同（通用） / 买卖合同审查 / sales-contract-review / contract-review / standard-sales-reviewer
- `term-analyzer` — 合同条款 / 术语分析
- `vendor-agreement-review` — 供应商合同 / 采购合同 / 服务协议 / 供应商MSA / 供应商协议

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
