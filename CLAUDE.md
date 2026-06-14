# Greater China Legal — AI Agent Context

本项目是 **大中华区法律 AI Agent Skill 体系**，基于 Anthropic `claude-for-legal` 深度适配中国大陆/香港/澳门/台湾/新加坡五大法域，覆盖 31 个法律场景、475 个原子 Skills。

---

## 项目架构

```
Greater-China-Legal/
├── CLAUDE.md                     ← 本文件：AI Agent 运行时上下文
├── plugins/
│   ├── scenes/<scene>/           ← 31 个法律场景
│   │   ├── CLAUDE.md             ← 场景级实践画像 + 角色 + 数据源 + 推理原子能力
│   │   ├── skills/<skill>/SKILL.md ← 原子 Skill（可独立执行）
│   │   ├── agents/<agent>.md     ← 定时调度 Agent（可选）
│   │   ├── hooks/hooks.json      ← 事件驱动钩子（可选）
│   │   └── references/           ← 场景内参考文件
│   ├── legal-atomic/             ← 37 个推理原子能力（跨场景复用）
│   │   ├── deductive-reasoning/  ← P-F-C三段论
│   │   ├── legal-element-extraction/ ← 法律要素提取
│   │   ├── legal-norm-validity-check/ ← 法条效力核查
│   │   └── ...（共37个）
│   └── shared/                   ← 跨场景共享 skill
│       ├── cold-start-interview/ ← 场景冷启动配置
│       ├── customize/            ← 自定义配置
│       └── matter-workspace/     ← 案件工作区管理
├── LEGAL_FRAMES/                 ← 五法域法律框架基线
├── references/                   ← 全局共享模板
├── managed-agent-cookbooks/      ← CMA 部署模板
├── scripts/                      ← 验证/部署工具
└── scene-design/                 ← B 阶段设计规范
```

---

## 场景结构

每个 scene 由四层构成：

```
┌─────────────────────────────────┐
│  CLAUDE.md — 场景级配置          │ ← 公司基本信息 + 数据源 + 角色 + 输出格式
│  (AI 每次进入该场景先读这个)       │
├─────────────────────────────────┤
│  skills/<skill>/SKILL.md        │ ← 原子 Skill，200-500行，判断树结构
│  (每一条独立法律能力)             │
├─────────────────────────────────┤
│  agents/<name>.md               │ ← 定时调度 Agent（可选）
│  (续约监控、盘后复盘等)           │
├─────────────────────────────────┤
│  hooks/hooks.json               │ ← 事件驱动钩子（可选）
│  (完成后自动触发其他 skill)       │
└─────────────────────────────────┘
```

协作链路示例：
```
用户审查合同 → review SKILL.md
  → hooks: on_contract_review_complete → 更新续约注册簿
  → agents/deal-debrief.md (每周) → 复盘偏差
```

---

## 使用规范

### 场景选择

用户的问题对应哪个 scene，通过 SKILL.md 的 `trigger_phrases` 匹配。skill 名 = kebab-case。

### 角色感知

每个场景的 CLAUDE.md 有 `## Who's using this` 节，定义了当前 AI 的输出角色：

| Role | 特权标记 |
|------|---------|
| 律师/法务人员 | `Privileged & Confidential — Attorney Work Product` |
| 非法务（有律师支持） | `Research Notes — Not Legal Advice — Review With Attorney Before Acting` |
| 非法务（无律师支持） | `General Information — Not Legal Advice — Consult A Licensed Attorney` |

执行 skill 前必须先检查 Role 字段。如 Role 含 `[填空]`，要求用户先设置或选择适用角色。

### 数据源标注

所有输出必须标注来源：

| 标注 | 含义 |
|------|------|
| `[YD]` | 元典 MCP 实际返回 |
| `[WKL]` | 裁判文书网/无讼 |
| `[BD]` | 北达检索 |
| `[GOV]` | 政府平台 |
| `[web]` | 网络搜索 |
| `[model]` | 模型推理（须核实）|

标注必须诚实——不能因"引用看起来是对的"就把 `[model]` 标为 `[YD]`。关键结论须多源交叉验证。

### 升级决策门

所有 skill 在输出前必须检查场景 CLAUDE.md 中的升级条件。涉及刑事风险、重大金额、跨境执法等情形，必须移交专业律师并在输出中明确标注。

---

## 跨场景路由

当用户查询涉及多个法律领域时，按以下流程执行：

### Step 1：调用 legal-element-extraction

读取 `plugins/legal-atomic/legal-element-extraction/SKILL.md`，提取用户输入中的法律事实。从提取结果中推断涉及的法律领域。

### Step 2：映射到场景

根据法律领域确定需要加载的场景：

| 法律领域关键词 | 对应场景 |
|--------------|---------|
| 并购/股权/资产收购/尽职调查 | `m-and-a`、`corporate-governance`、`tax-compliance` |
| 合同/供应商/采购/NDA | `contract-review` |
| 诉讼/仲裁/争议解决 | `litigation-support`、`commercial-arbitration` |
| 数据/隐私/PIPL/个人信息 | `data-compliance`、`ai-governance-legal` |
| 知识产权/商标/专利/著作权 | `ip-infringement` |
| 劳动/员工/解除/社保 | `employment-legal`、`labor-arbitration` |
| 税务/发票/转让定价 | `tax-compliance` |
| 破产/重整/清算 | `bankruptcy-restructuring` |
| 监管/牌照/合规 | `regulatory-compliance` |
| 虚拟资产/NFT/Web3 | `web3-virtual-assets` |
| 白领犯罪/反舞弊/调查 | `white-collar-crime`、`government-investigation` |
| 投资/基金/私募/对赌 | `pe-vc-funds`、`financing-business` |
| 资本市场/IPO/发债 | `capital-markets` |
| 跨境贸易/进出口 | `cross-border-trade` |
| 房地产/建设工程 | `real-estate-construction` |
| 财富传承/信托/遗嘱 | `wealth-succession` |

### Step 3：逐场景加载执行

对于每个涉及场景：

1. 读取 `plugins/scenes/<scene>/CLAUDE.md`（含 Role、数据源、推理原子能力调用流程）
2. 按该场景 CLAUDE.md 的「推理原子能力调用流程」执行
3. 调用 `legal-atomic` 中的对应原子 skill
4. 输出该场景的分析结论

场景间顺序：按「核心场景→辅助场景」执行。如并购尽调：先跑 `m-and-a`，再并行跑 `ip-infringement`、`data-compliance`、`employment-legal`、`tax-compliance`。

### Step 4：汇总输出

1. 合并各场景结论
2. 如某结论在不同场景间矛盾（如税务场景认为重组方案可行，劳动场景认为存在障碍），标注矛盾点
3. 整体论证强度评估（调用 `argument-strength-evaluation`）
4. 输出最终跨场景报告

场景隔离：每个场景在独立的上下文中执行。场景 A 的中间结论不泄漏到场景 B。

---

## 法域支持

`LEGAL_FRAMES/` 定义了 5 个法域的法律框架基线：

| 法域 | 标识 | 说明 |
|------|------|------|
| 中国大陆 | `cn-mainland` | 默认法域 |
| 香港 | `hk` | 普通法系 |
| 澳门 | `mo` | 大陆法系 |
| 台湾 | `tw` | 大陆法系 |
| 新加坡 | `sg` | 普通法系 |

SKILL.md 通过 YAML frontmatter 的 `legal_frame` 字段锚定。

---

## 开发者规范（供参考）

- CI 验证规则见 `scripts/validate-skills.py`
- 数据结构见 `SKILL_MD_SCHEMA.md`
- 贡献指南见 `CONTRIBUTING.md`
- 上游追踪见 `UPSTREAM_TRACKING.md`

---

*此文件为 AI Agent 运行时上下文，非开发者 CI 文档。*
