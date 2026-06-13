---
title: Greater China Legal — 大中华区法律 AI Agent Skill 体系
description: >
  Greater China Legal 是基于 Anthropic claude-for-legal 适配的大中华区法律 AI Agent 技能库。
  覆盖中国大陆、香港、澳门、台湾、新加坡五大法域，30 个法律场景，478 个原子 Skills。
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

> **大中华区法律 AI Agent Skill 体系** — 基于 Anthropic `claude-for-legal` 深度适配，支持中国大陆 / 香港 / 澳门 / 台湾 / 新加坡，覆盖 **30 个法律场景 · 478 个原子 Skills**。开箱即用于 Claude Code、Codex 及各类 Agent 平台。

---

## 项目概览

| 指标 | 数值 |
|------|------|
| **法域覆盖** | CN · HK · MO · TW · SG（5个） |
| **法律场景** | 30 个（15 核心场景 + 15 精细化场景） |
| **原子 Skills** | 478 个 |
| **精细化子场景** | 72 个 |
| **适配来源** | Anthropic `claude-for-legal`（⭐ 8,195） |

**2026-06 完成精细化**：web3-virtual-assets、government-investigation、special-opportunity-investment、real-estate-construction、financing-business、litigation-support、contract-review、corporate-governance、ip-infringement、employment-legal、internet-finance 共 11 个场景完成深度精细化（子场景 × 3~4，每个子场景 3 个原子 Skills + 3 篇法条参考）。

---

## 核心场景目录

### 金融与资本市场

| 场景 | Skills | 说明 |
|------|--------|------|
| **capital-markets** 资本市场 | 19 | A股IPO、港股上市、上市公司合规、增发配股 |
| **pe-vc-funds** 私募股权与创投 | 18 | 基金设立、LP尽调、投资协议、退出路径 |
| **bankruptcy-restructuring** 破产与重整 | 15 | 破产清算、重整程序、债权人保护、不良资产 |
| **financing-business** 融资业务 | 9 | 保理、融资租赁、供应链金融、资产证券化 |
| **special-opportunity-investment** 特殊机会投资 | 10 | 不良资产收购、困境企业并购、诉讼投资 |

### 企业与合规

| 场景 | Skills | 说明 |
|------|--------|------|
| **corporate-governance** 公司治理 | 28 | 股权架构、股东权利、董事会运作、高管激励 |
| **m-and-a** 股权与并购 | 19 | 收购兼并、私有化、拆分子公司、阻力评估 |
| **regulatory-compliance** 监管合规 | 18 | 行业监管（医药/金融/能源）、牌照咨询、合规审计 |
| **cross-border-trade** 跨境贸易 | 15 | 国际贸易救济、出口管制、海关合规、跨境电商 |
| **cross-border-ma** 跨境并购 | 6 | 境外投资备案（ODI）、红筹架构、VIE合规 |

### 知识产权

| 场景 | Skills | 说明 |
|------|--------|------|
| **ip-infringement** 知识产权侵权 | 27 | 专利侵权、商标争议、著作权维权、商业秘密 |
| **data-compliance** 数据合规 | 26 | 个人信息保护、数据跨境传输、数据分类分级 |
| **web3-virtual-assets** Web3 与虚拟资产 | 9 | 虚拟货币合规、NFT平台运营、DeFi协议合规 |

### 争议解决

| 场景 | Skills | 说明 |
|------|--------|------|
| **litigation-support** 诉讼支持 | 35 | 民事诉讼、刑事辩护、行政诉讼、判决执行 |
| **commercial-arbitration** 商事仲裁 | 18 | CIETAC/ICC/SICC仲裁、临时仲裁、调解 |
| **white-collar-crime** 白领犯罪 | 15 | 刑事合规、反腐调查、证券犯罪辩护 |

### 劳动与雇佣

| 场景 | Skills | 说明 |
|------|--------|------|
| **employment-legal** 劳动法 | 26 | 招聘入职、薪酬福利、解除终止、职场纠纷 |
| **labor-arbitration** 劳动仲裁 | 9 | 仲裁程序、赔偿计算、证据准备、代理策略 |

### 传统与新兴领域

| 场景 | Skills | 说明 |
|------|--------|------|
| **tax-compliance** 税务合规 | 24 | 企业所得税、转让定价、跨境税务、税务筹划 |
| **government-investigation** 政府监管调查 | 9 | 反垄断调查、证监会调查、商业反腐合规 |
| **real-estate-construction** 房地产与建筑工程 | 9 | 土地获取开发、建设工程纠纷、商业租赁 |
| **internet-finance** 互联网金融 | 22 | 第三方支付、网络借贷、互联网保险、数字资产 |
| **wealth-succession** 财富传承 | 15 | 遗嘱信托、遗产规划、家族治理、婚前协议 |

### 通用与工具层

| 场景 | Skills | 说明 |
|------|--------|------|
| **legal-atomic** 通用原子能力 | 35 | 跨场景可复用的通用推理能力 |
| **contract-review** 合同审查 | 28 | 买卖合同、借贷租赁、服务劳务、保密协议 |
| **legal-clinic** 法律诊所 | 16 | 通用法律咨询、案例检索、法律援助 |
| **law-student** 法学教育 | 13 | 法学考试备考、法律写作、案例研习 |
| **product-legal** 产品合规 | 7 | 产品说明书合规、广告法合规、消费者保护 |
| **legal-builder-hub** Skill 管理 | 10 | Skill 创作、验证、发布管理工具 |
| **ai-governance-legal** AI 治理 | 3 | AI 系统合规评估、算法备案、数据安全 |
| **employment-legal / hiring** | — | （归入 employment-legal 统一管理） |

---

## 目录结构

```
Greater-China-Legal/
├── legal-atomic/                  # 35个通用原子能力（跨场景可调用）
├── shared/agent-ops/              # 通用工作台初始化Skills
│   ├── cold-start-interview/      # 新建事项时了解背景
│   ├── customize/                 # 按客户/法域定制
│   └── matter-workspace/          # 工作台初始化
│
├── {30个法律场景}/                 # 各场景含 CLAUDE.md + skills/ + refs/
│   ├── skills/                   # 顶层原子 Skills
│   └── sub-scenes/               # 精细化子场景（场景名/子场景名/Skills）
│       └── {子场景名}/
│           ├── skills/           # 3个原子 Skills
│           └── refs/             # 3篇法条参考
│
├── LEGAL_FRAMES/                  # 5个法域基准文档
│   ├── cn-mainland.md            # 中国大陆
│   ├── hk.md                     # 香港
│   ├── mo.md                     # 澳门
│   ├── tw.md                     # 台湾
│   └── sg.md                     # 新加坡
│
├── references/                   # 共享方法论
├── scripts/
│   ├── validate-skills.py        # Skill 格式校验
│   └── sync-upstream.py          # 同步上游
└── README.md
```

---

## 架构说明

### 三层结构

| 层级 | 定位 | 内容 |
|------|------|------|
| **legal-atomic** | 通用原子能力 | 35 个跨场景可调用的通用推理能力 |
| **shared/agent-ops** | 工作台初始化 | 通用工作台操作，所有场景可调用 |
| **{30场景}** | 场景专属能力 | 各场景独立的原子 Skills，依赖 legal-atomic |

### Skill 精细化结构（子场景 × 3 Skills + 3 Refs）

每个精细化子场景包含：

```
{sub-scene}/
├── skills/
│   ├── {skill-01}/SKILL.md   # 原子 Skill（如 cause-action-analysis）
│   ├── {skill-02}/SKILL.md
│   └── {skill-03}/SKILL.md
└── refs/
    ├── 01-{法条名称}.md       # 相关法规全文/要点
    ├── 02-{司法解释}.md
    └── 03-{操作指引}.md
```

---

## 快速开始

### 安装

```bash
# Claude Code
claude skills install https://github.com/vivy-yi/Greater-China-Legal

# 其他 Agent 平台：直接克隆到本地 skills 目录
git clone https://github.com/vivy-yi/Greater-China-Legal.git /path/to/skills
```

### 触发示例

```
大陆劳动仲裁：  /labor-arbitration:dispute-classifier
香港合同审查：    /contract-review:term-analyzer --frame hk
台湾数据合规：    /data-compliance:pipl-assessment --frame tw
新加坡税务：      /tax-compliance:tax-type-classifier --frame sg
A股IPO咨询：      /capital-markets:a-share-ipo:ipo-process-advisor
Web3合规：       /web3-virtual-assets:crypto-asset-compliance
反垄断调查：      /government-investigation:anti-monopoly-investigation
```

---

## 法域覆盖

| 法域 | 法律体系 | 核心法规 |
|------|---------|---------|
| **CN 中国大陆** | 民法典/大陆法系 | 民法典、劳动合同法、个人信息保护法、公司法、证券法 |
| **HK 香港** | 普通法系 | Employment Ordinance (Cap.57)、Companies Ordinance (Cap.622)、SFO |
| **MO 澳门** | 大陆法系 | 澳门民法典（葡萄牙民法典延续）、劳动关系法 |
| **TW 台湾** | 大陆法系 | 台湾民法、劳动基准法、公司法、个人信息保护法 |
| **SG 新加坡** | 普通法系 | Employment Act (Cap.91)、PDPA、Companies Act、Securities and Futures Act |

---

## 上游同步

本仓库持续同步 [Anthropic `claude-for-legal`](https://github.com/anthropics/claude-for-legal)（⭐ 8,195），保留原版 Skill 作为参考，中国本地化适配新增 `cn-mainland` 标记。

---

## License

继承上游 Anthropic 仓库 License
