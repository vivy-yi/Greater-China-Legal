# Greater China Legal — 项目上下文 (context.md)

> 本文件是这套「大中华区法律 AI Agent Skill 体系」的**项目上下文**。任何 agentic tool(Claude Code / OpenCode / Codex / WorkBuddy / OpenClaw / Hermes 等)进入本仓库后,应首先阅读本文件,了解「这是什么、有哪些能力、怎么用」。Agent 的行为契约见 [agent.md](agent.md)。

---

## 这是什么

一套给 AI Agent 使用的**法律技能体系**:不是模型、不是 API,而是一组「指令文档」——**SKILL.md 集合**。装进 agentic tool 后,用户用自然语言提问,agent 读取对应 skill、按流程执行,输出带来源标注的分析结果。

- **覆盖法域**:中国大陆 CN · 香港 HK · 澳门 MO · 台湾 TW · 新加坡 SG(5 个)
- **法律场景**:36 个(并购、合同、诉讼、劳动、知产、数据、刑事、家事…)
- **原子 Skills**:574 个 SKILL.md(每个场景下若干条,可独立触发)
- **推理原子能力**:25 个(`plugins/legal-atomic/`,跨场景复用)
- **适配来源**:基于 Anthropic `claude-for-legal` 深度本土化

---

## 目录结构(关键路径)

```
Greater-China-Legal/
├── CLAUDE.md            ← Claude Code 的运行时上下文(项目级)
├── context.md           ← 本文件:项目上下文(给所有 agentic tool)
├── agent.md             ← Agent 行为契约(怎么响应用户需求)
├── AGENTS.md            ← 跨工具入口(OpenCode/Codex 读它,内部 @import 上面两个)
├── README.md            ← 面向人类的展示页
└── plugins/
    ├── legal-scenes/<scene>/
    │   ├── CLAUDE.md        ← 场景级配置(Part A 通用 + Part B 场景画像)
    │   ├── skills/<skill>/SKILL.md  ← 原子 Skill(单条法律能力)
    │   ├── agents/<agent>.md        ← 定时调度 Agent(可选)
    │   └── hooks/hooks.json         ← 事件钩子(可选)
    ├── legal-atomic/           ← 25 个推理原子能力(跨场景复用)
    ├── legal-tools/            ← 数据源/API 封装
    └── shared/                 ← 跨场景共享 skill
```

---

## 36 个场景路由表

用户提问命中「触发关键词」→ 加载对应场景。涉及多领域的,先跑核心场景,再并行跑辅助场景。

| 类别 | 场景 | 触发关键词 |
|------|------|-----------|
| 金融与资本市场 | **capital-markets** 资本市场 | IPO / 上市 / 增发 / 发债 |
| | **pe-vc-funds** 私募创投 | 基金 / 私募 / 对赌 / LP尽调 |
| | **bankruptcy-restructuring** 破产重整 | 破产 / 重整 / 清算 / 不良资产 |
| | **financing-business** 融资业务 | 保理 / 融资租赁 / 供应链金融 |
| | **special-opportunity-investment** 特殊机会投资 | 不良资产收购 / 困境企业 |
| 企业与合规 | **corporate-governance** 公司治理 | 董事会 / 股东会 / 股权激励 |
| | **m-and-a** 并购重组 | 并购 / 股权收购 / 尽调 |
| | **cross-border-ma** 跨境并购 | ODI / 红筹 / VIE / 外资准入 |
| | **regulatory-compliance** 行业监管合规 | 牌照 / 准入 / 金融 / 医药 / 电信 |
| | **tax-compliance** 税务合规 | 税务 / 发票 / 转让定价 |
| | **product-legal** 产品法务 | 产品发布 / 营销合规 |
| | **real-estate-construction** 房地产建设 | 房地产 / 建设工程 / 租赁 |
| | **antitrust** 反垄断 | 经营者集中 / 垄断协议 / 宽大 |
| | **enforcement** 行政执法 | 行政处罚 / 听证 / 行政复议 |
| 合同与商事 | **contract-review** 合同审查 | 合同 / 供应商 / NDA / 采购 |
| | **commercial-arbitration** 商事仲裁 | 仲裁 / CIETAC / HKIAC / SIAC |
| | **cross-border-trade** 跨境贸易 | 进出口 / 关税 / 贸易合规 |
| | **internet-finance** 互联网金融 | 网络小贷 / 消费金融 / 支付 |
| | **employment-legal** 劳动法务 | 劳动 / 员工 / 解除 / 社保 / 竞业 |
| | **labor-arbitration** 劳动争议 | 劳动仲裁 / 赔偿计算 |
| | **maritime** 海事海商 | 船舶 / 海上运输 / 碰撞 |
| 知识产权与数据 | **ip-infringement** 知识产权 | 商标 / 专利 / 著作权 / 商业秘密 |
| | **data-compliance** 数据合规 | PIPL / 个人信息 / 数据出境 |
| | **ai-governance-legal** AI治理 | 算法备案 / 深度合成 / 生成式AI |
| | **web3-virtual-assets** Web3与虚拟资产 | 加密资产 / NFT / DeFi / DAO |
| 诉讼与争议解决 | **litigation-support** 诉讼支持 | 诉讼 / 证据 / 年表 / 论证链 |
| | **government-investigation** 政府调查应对 | 反垄断 / 证券 / 反腐败调查 |
| | **white-collar-crime** 白领犯罪 | 商业贿赂 / 职务侵占 / 涉税犯罪 |
| | **administrative-litigation** 行政诉讼 | 行政诉讼 / 国家赔偿 |
| | **criminal-defense** 刑事辩护 | 刑事 / 侦查 / 起诉 / 会见 |
| | **family-law** 婚姻家事 | 离婚 / 继承 / 抚养 / 家暴 |
| 财富与传承 | **wealth-succession** 财富传承 | 遗嘱 / 信托 / 保险 / 遗产税 |
| 环境与社会责任 | **environmental** 环境法 | 排污 / 环保处罚 / ESG |
| 教育与公益 | **law-student** 法学学习 | 法考 / 案例分析 / IRAC |
| | **legal-clinic** 法律诊所 | 法援 / 消费者维权 |
| | **cocounsel-legal** 协同法律服务 | 多律所协同 / 案件分配 |

---

## Skill 是什么、怎么触发

**SKILL.md** 是「单条法律能力的指令文档」,内含 `trigger_phrases`、流程式指引、判断树、升级决策门。触发方式:

1. **自然语言命中**:用户提问命中某条 skill 的 `trigger_phrases`
2. **显式点名**:用户直接指定 `/skill-name`
3. **跨场景路由**:用 `legal-element-extraction` 提取法律要素 → 映射场景 → 加载场景 `CLAUDE.md` → 按其「推理原子能力调用流程」执行 skill

---

## 角色与输出

每个场景 CLAUDE.md 的 `## Who's using this` 节定义输出特权标记:

| 角色 | 输出标记 |
|------|---------|
| 律师 / 法务人员 | `Privileged & Confidential — Attorney Work Product` |
| 非法务(有律师支持) | `Research Notes — Not Legal Advice — Review With Attorney Before Acting` |
| 非法务(无律师支持) | `General Information — Not Legal Advice — Consult A Licensed Attorney` |

### 数据源标注

所有输出必须标注来源:`[YD]` 元典 / `[WKL]` 裁判文书网 / `[BD]` 北达 / `[GOV]` 政府平台 / `[web]` 网络搜索 / `[model]` 模型推理。标注必须诚实——不得把 `[model]` 冒充 `[YD]`。

### 升级决策门

涉及**刑事风险、重大金额、跨境执法**等情形,必须标注「须专业律师处理」,不得自行给出终局结论。

---

## 装进各 agentic tool

| Tool | 入口文档 | Skills 怎么装 | 触发 |
|------|---------|--------------|------|
| Claude Code | `CLAUDE.md`(已有) | `cp -r plugins/* ~/.claude/skills/` 或 `/plugin` | 自然语言 / 斜杠命令 |
| OpenCode | `AGENTS.md`(本入口链) | 按 OpenCode 的 skills / plugins 机制 | 自然语言 |
| Codex(OpenAI) | `AGENTS.md` | 按 Codex 的 AGENTS.md / skills 机制 | 自然语言 |
| Gemini CLI | `GEMINI.md`(可 `@import`) | 按 Gemini CLI 的 skill 机制 | 自然语言 |
| WorkBuddy | 待平台文档确认 | 待确认 | 待确认 |
| OpenClaw | 待平台文档确认 | 待确认 | 待确认 |
| Hermes | 待平台文档确认 | 待确认 | 待确认 |

> 未标注「待确认」的工具,以各自平台官方文档为准;如这些平台支持 AGENTS.md 标准,则本仓库的 `agent.md` + `context.md` 已可直接复用。

---

## 免责

本体系输出**非法律意见**,所有结论须经执业律师复核后方可采信。引用法条/判例以官方来源为准。
