# internet-finance — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Internet Finance Compliance — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `ai-inventory` — AI清单 / 人工智能
- `aia-generation` — AI合规 / 评估生成
- `claims-dispute-advisor` — claims-dispute-advisor / internet_finance
- `compliance-doc-generator` — 合规文档 / 生成
- `consumer-lending-reviewer` — consumer-lending-reviewer / internet_finance
- `consumer-protection-checker` — 消费者保护 / 合规
- `cross-border-payment-advisor` — cross-border-payment-advisor / internet_finance
- `crypto-exchange-compliance` — crypto-exchange-compliance / internet_finance
- `data-security-assessment` — 数据安全 / 评估
- `ico-token-offering-advisor` — ico-token-offering-advisor / internet_finance
- `insurance-license-advisor` — insurance-license-advisor / internet_finance
- `insurance-product-compliance` — insurance-product-compliance / internet_finance
- `license-type-checker` — 牌照类型 / 资质
- `nft-platform-compliance` — nft-platform-compliance / internet_finance
- `ongoing-compliance-monitor` — 合规监控 / 持续
- `online-loan-compliance` — online-loan-compliance / internet_finance
- `p2p-registration-filing` — p2p-registration-filing / internet_finance / P2P / 网贷 / 非法集资 / 平台清退
- `payment-license-compliance` — 支付牌照申请 / 第三方支付 / 支付业务许可证 / 互联网支付资质 / 银行卡收单资质 / 预付卡资质 / 支付牌照合规
- `payment-service-agreement` — payment-service-agreement / internet_finance
- `policy-starter` — 政策起草 / 合规咨询 / 互联网金融合规 / 金融政策
- `qualification-gap-assessment` — 资质差距 / 评估
- `vendor-ai-review` — 供应商AI / 审查

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
