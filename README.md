---
title: Greater China Legal — 大中华区法律 AI Agent Skill 体系
description: >
  Greater China Legal 是基于 Anthropic claude-for-legal 适配的大中华区法律 AI Agent 技能库。
  覆盖中国大陆、香港、澳门、台湾、新加坡五大法域，36 个法律场景，501 个原子 Skills。
  适用于 Claude Code、Codex 及各类 Agent 平台的法律咨询、合同审查、诉讼支持、合规管理等场景。
keywords:
  - Greater China Legal
  - 大中华区法律 AI
  - 中国法律 Agent
  - 法律 Skill 系统
  - Hong Kong legal AI
  - Taiwan legal AI
  - claude-for-legal 中文适配
  - 法律人工智能助手
  - 劳动仲裁 AI
  - 合同审查 AI
  - 知识产权 AI
  - 公司治理 AI
  - 数据合规 AI
  - 诉讼支持 AI
  - 税务合规 AI
  - AI legal skill system
  - Chinese law AI agent
  - legal workflow automation
---

# Greater China Legal

> **大中华区法律 AI Agent Skill 体系** — 基于 Anthropic `claude-for-legal` 深度适配，支持中国大陆 / 香港 / 澳门 / 台湾 / 新加坡，覆盖 **36 个法律场景 · 501 个原子 Skills**。开箱即用于 Claude Code、Codex 及各类 Agent 平台。

---

## 项目概览

| 指标 | 数值 |
|------|------|
| **法域覆盖** | CN · HK · MO · TW · SG（5个） |
| **法律场景** | 36 个（v2.0 双层结构 + § A8.1 场景特化块） |
| **原子 Skills** | 501 个 |
| **场景 CLAUDE.md** | 230-500 行一体化（v3 红线控制） |
| **场景级 Agent** | 8 个场景共 8 个监控 Agent |
| **事件钩子** | 8 个场景共 27 个事件触发器 |
| **推理原子能力** | 37 个（legal-atomic 跨场景复用） |
| **适配来源** | Anthropic `claude-for-legal`（⭐ 8,195） |

**2026-06 v2.0 架构升级：**
- 🏗 **双层结构落地**：所有 scene CLAUDE.md 采用 Part A(16 universal)+ Part B(16-18 pattern adaptive)双层
- 📋 **§ A8.1 场景特化块**：10 个核心场景新增 4-6 大块特别说明(法条 + 量刑 + blocks/work but ships + 6 类主动问)
- 🚀 **行数压缩控制**：v1→v2 迁移平均压缩 30%(689→481 行 / 621→498 行等),全部场景 < 500 行
- 🗑 **冗余清理**：删除 legal-builder-hub 整个 plugin + 12 个错误创建的 references/ 拆分文件
- 🔗 **路径修复**：415 处错误相对路径修复为 `../../../../references/`
- 🧹 **硬编码清理**：192 个 SKILL.md 移除逐文件路径声明,统一引用场景级 CLAUDE.md
- 👤 **角色感知**：每个场景输出根据 Role(律师/法务/业务方)自动切换 privilege 标记
- 🇨🇳 **CN 全面适配**：product-legal 从 Anthropic US 模板完整本土化(广告法/个保法/未保法/电商法)

---

## 36 个法律场景

### 金融与资本市场

| 场景 | Skills | 说明 |
|------|--------|------|
| **capital-markets** 资本市场 | 15 | A股IPO、港股上市、上市公司合规、增发配股 |
| **pe-vc-funds** 私募股权与创投 | 18 | 基金设立、LP尽调、投资协议、退出路径 |
| **bankruptcy-restructuring** 破产与重整 | 15 | 破产清算、重整程序、债权人保护、不良资产 |
| **financing-business** 融资业务 | 9 | 保理、融资租赁、供应链金融、资产证券化 |
| **special-opportunity-investment** 特殊机会投资 | 10 | 不良资产收购、困境企业并购、诉讼投资 |

### 企业与合规

| 场景 | Skills | 说明 |
|------|--------|------|
| **corporate-governance** 公司治理 | 28 | 董事会、股东会、股权激励、合规管理 |
| **m-and-a** 并购重组 | 19 | 尽职调查、交易结构、审批流程、信息披露 |
| **cross-border-ma** 跨境并购 | 6 | ODI备案、红筹架构、外资准入、VIE |
| **regulatory-compliance** 行业监管合规 | 18 | 金融/医药/电信/环保等行业准入与合规 |
| **tax-compliance** 税务合规 | 24 | 企业所得税、增值税、转让定价、跨境税务 |
| **product-legal** 产品法务 | 7 | 产品发布审查、营销合规、风险分级 |
| **real-estate-construction** 房地产与建设工程 | 9 | 开发合规、工程纠纷、租赁管理 |
| **antitrust** 反垄断 | 6 | 经营者集中、反垄断协议、宽大制度、行政调查 |
| **enforcement** 行政执法 | 6 | 行政处罚、听证、行政复议、国家赔偿 |

### 合同与商事

| 场景 | Skills | 说明 |
|------|--------|------|
| **contract-review** 合同审查 | 28 | 供应商/客户/NDA/SaaS/MSA全类型审查 |
| **commercial-arbitration** 商事仲裁 | 18 | CIETAC/HKIAC/SIAC/ICC/ICSID程序 |
| **cross-border-trade** 跨境贸易 | 9 | 进出口管制、关税优化、贸易金融合规 |
| **internet-finance** 互联网金融 | 22 | 网络小贷/消费金融/第三方支付合规 |
| **employment-legal** 劳动法务 | 27 | 合同/解除/社保/竞业/调查全流程 |
| **labor-arbitration** 劳动争议 | 9 | 仲裁程序、证据组织、赔偿计算 |
| **maritime** 海事海商 | 6 | 船舶物权、海上货物运输、船舶碰撞、海难救助 |

### 知识产权与数据

| 场景 | Skills | 说明 |
|------|--------|------|
| **ip-infringement** 知识产权 | 27 | 商标/专利/著作权/商业秘密侵权全链路 |
| **data-compliance** 数据合规 | 26 | PIPL/DSL/CSL合规、跨境传输、PIA评估 |
| **ai-governance-legal** AI治理 | 3 | 算法备案、深度合成、生成式AI合规 |
| **web3-virtual-assets** Web3与虚拟资产 | 9 | 加密资产合规、NFT纠纷、DeFi风险、DAO架构 |

### 诉讼与争议解决

| 场景 | Skills | 说明 |
|------|--------|------|
| **litigation-support** 诉讼支持 | 35 | 案件接收、年表构建、证据组织、论证链、法律研究 |
| **government-investigation** 政府调查应对 | 9 | 反垄断/证券/反腐败调查应对 |
| **white-collar-crime** 白领犯罪 | 15 | 商业贿赂/职务侵占/涉税犯罪/合规体系 |
| **administrative-litigation** 行政诉讼 | 6 | 行政诉讼、行政复议、国家赔偿 |
| **criminal-defense** 刑事辩护 | 6 | 侦查/起诉/审判辩护、会见、阅卷、上诉 |
| **family-law** 婚姻家事 | 6 | 离婚、继承、抚养、家暴、人身安全保护令 |

### 财富与传承

| 场景 | Skills | 说明 |
|------|--------|------|
| **wealth-succession** 财富传承 | 14 | 遗嘱、信托、保险、跨境资产配置、遗产税 |

### 环境与社会责任

| 场景 | Skills | 说明 |
|------|--------|------|
| **environmental** 环境法 | 6 | 排污许可、环保行政处罚、ESG、气候披露 |

### 法律教育与公益

| 场景 | Skills | 说明 |
|------|--------|------|
| **law-student** 法学学习 | 13 | 法考备考、案例分析、法律写作、IRAC训练 |
| **legal-clinic** 法律诊所 | 16 | 劳动法援/消费者维权/婚姻家事/行政诉讼 |
| **cocounsel-legal** 协同法律服务 | 1 | 多律所协同、案件分配、协作流程 |

---

## 场景架构

每个 scene 由四层构成(均为 v2.0 双层结构):

```
CLAUDE.md          ← 场景级配置:Part A (16 universal) + Part B (16-18 pattern adaptive)
                    § A8.1 场景特化块(4-6 大块):blocks/work but ships + 6 类主动问
  ├─ skills/*/SKILL.md  ← 原子 Skill:流程式工作指引 + 分析框架 + 升级决策门
  ├─ agents/*.md        ← 定时调度 Agent(监控/复盘/提醒)
  └─ hooks/hooks.json   ← 事件驱动钩子(完成后自动触发其他 skill)
```

### 双层结构(Part A + Part B)

**Part A — Operating System(16 universal sections)**
所有 scene 共享:A1 配置位置 / A2 角色(5 档)/ A3 Quiet mode / A4 集成 / A5 Outputs / A6 决策姿势 / A7 9+3+N guardrails / A8 Scaffolding / **§ A8.1 场景特化块**(本场景独有法律细节) / A9-A16 通用规范。

**Part B — Scene-Adaptive Practice Profile(16-18 sections)**
本场景业务画像:B1 工作流 / B2 路由表 / B3 三色风险 / B4 风险等级 / B5 升级触发 / B6 输出模板 / B7 决策树 / B8 主动问 / B9 用户配置(24 字段 YAML) / B10 数据源标注 / B11 注册表复用 / B12 Per-matter Side / B13 Enforcement posture / B14 Risk calibration 3 段 / B15 7 条设计哲学 / B16 推理原子能力调用流程。

### § A8.1 场景特化块(三段式)

每个核心场景在 Part A 内部包含 § A8.1,统一使用三段式:

| 标记 | 含义 | Agent 动作 |
|------|------|-----------|
| **blocks** | 绝对禁止 — 命中即停止 | 直接停止 + 告知 + 不绕过 |
| **work but ships** | 可补救 — 但有整改时限 | 提示律师 + 给时间表 |
| **FYI** | 记录不主动告知 | 写入工作底稿 |

已落地 10 个场景的 § A8.1:
- **regulatory-compliance**: 行政处罚 + 听证 + 信用 + 重大违法
- **corporate-governance**: 公司法 2023 + 上市公司治理 + 股东权益 + 董监高义务
- **employment-legal**: 劳动合同 + 解除 39/40/41 + 经济补偿 N + 竞业限制 + 11 升 6 禁
- **contract-review**: 民法典 4 编 + 格式条款 + 合同效力 + 涉外
- **cross-border-ma**: 外资准入 + 数据出境 + 反垄断 + VIE/红筹
- **m-and-a**: 尽职调查 + 股权收购 + 资产收购 + 反垄断 + 对赌回购
- **ip-infringement**: 商标 + 专利 + 著作权 + 不正当竞争 + 商业秘密
- **labor-arbitration**: 仲裁前置 + 时效 + 裁决执行 + 一裁终局
- **white-collar-crime**: 监察留置 + 贪贿罪 + 自首立功 + 单位犯罪 + 涉案财物
- **ai-governance-legal**: 算法治理 + 个保法 + 数据安全 + 生成式 AI + 跨境

### 角色感知

每个场景的 CLAUDE.md 有 `## Who's using this` 节,定义了输出特权标记:

| Role | 特权标记 |
|------|---------|
| 律师/法务人员 | `Privileged & Confidential — Attorney Work Product` |
| 非法务(有律师支持) | `Research Notes — Not Legal Advice — Review With Attorney Before Acting` |
| 非法务(无律师支持) | `General Information — Not Legal Advice — Consult A Licensed Attorney` |

### 数据源标注

所有输出标注来源:`[YD]` 元典 / `[WKL]` 裁判文书网 / `[BD]` 北达 / `[GOV]` 政府平台 / `[web]` 网络搜索 / `[model]` 模型推理 / `[域外]` 域外法律

### 跨场景路由

涉及多个法律领域时,按 `legal-element-extraction` → 推断领域 → 加载对应场景 → 跨场景汇总的 4 步流程执行。详见 `CLAUDE.md` § 跨场景路由。

---

## 快速开始

```bash
# Claude Code
/plugin marketplace add /path/to/Greater-China-Legal
/plugin install contract-review@greater-china-legal

# 或直接加载场景
/contract-review:review vendor-msa.pdf
```

详见 `QUICKSTART.md`。

---

## 项目结构

```
Greater-China-Legal/
├── CLAUDE.md                     ← AI Agent 运行时上下文
├── README.md                     ← 本文件
├── QUICKSTART.md                 ← 快速开始
├── CONNECTORS.md                 ← 数据源连接器
├── SKILL_MD_SCHEMA.md            ← SKILL.md 字段规范
├── CONTRIBUTING.md               ← 贡献指南
├── LEGAL_FRAMES/                 ← 五大法域法律框架基线
├── references/                   ← 全局共享模板
├── managed-agent-cookbooks/      ← CMA 部署模板
├── scene-design/                 ← B 阶段设计规范
├── scripts/                      ← 验证/部署工具
└── plugins/
    ├── scenes/<scene>/           ← 36 个法律场景
    │   ├── CLAUDE.md             ← v2.0 双层结构
    │   ├── skills/<skill>/SKILL.md
    │   ├── agents/<agent>.md     ← 可选
    │   ├── hooks/hooks.json      ← 可选
    │   └── references/           ← 跨 skill 复用资料
    ├── legal-atomic/             ← 37 个推理原子能力
    └── shared/                   ← 跨场景共享 skill
        ├── cold-start-interview/
        ├── customize/
        └── matter-workspace/
```

---

## 授权

Apache 2.0 — 详见 [LICENSE](LICENSE)。

---

*Greater China Legal — 2026-06 v2.0 双层结构版*
*Last updated: 2026-06-23 · 36 scenes · 501 atomic skills · 5 jurisdictions*
