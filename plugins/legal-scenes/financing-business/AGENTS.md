# financing-business — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Financing Business — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `abs-structure-advisor` — 保理 / 资产证券化 / ABS / 融资租赁 / 供应链金融 / 反向保理 / 租金贷
- `commercial-factoring-advisor` — 保理 / 资产证券化 / ABS / 融资租赁 / 供应链金融 / 反向保理 / 租金贷
- `credit-enhancement-advisor` — 保理 / 资产证券化 / ABS / 融资租赁 / 供应链金融 / 反向保理 / 租金贷
- `e-commerce-financing-advisor` — 保理 / 资产证券化 / ABS / 融资租赁 / 供应链金融 / 反向保理 / 租金贷
- `financial-lease-contract-reviewer` — 保理 / 资产证券化 / ABS / 融资租赁 / 供应链金融 / 反向保理 / 租金贷
- `lease-asset-disposal-advisor` — 保理 / 资产证券化 / ABS / 融资租赁 / 供应链金融 / 反向保理 / 租金贷
- `reverse-factoring-advisor` — 保理 / 资产证券化 / ABS / 融资租赁 / 供应链金融 / 反向保理 / 租金贷
- `sale-leaseback-advisor` — 保理 / 资产证券化 / ABS / 融资租赁 / 供应链金融 / 反向保理 / 租金贷
- `supply-chain-loan-advisor` — 保理 / 资产证券化 / ABS / 融资租赁 / 供应链金融 / 反向保理 / 租金贷

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
