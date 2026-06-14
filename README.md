---
title: Greater China Legal — 大中华区法律 AI Agent Skill 体系
description: >
  Greater China Legal 是基于 Anthropic claude-for-legal 适配的大中华区法律 AI Agent 技能库。
  覆盖中国大陆、香港、澳门、台湾、新加坡五大法域，31 个法律场景，475 个原子 Skills。
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

> **大中华区法律 AI Agent Skill 体系** — 基于 Anthropic `claude-for-legal` 深度适配，支持中国大陆 / 香港 / 澳门 / 台湾 / 新加坡，覆盖 **31 个法律场景 · 475 个原子 Skills**。开箱即用于 Claude Code、Codex 及各类 Agent 平台。

---

## 项目概览

| 指标 | 数值 |
|------|------|
| **法域覆盖** | CN · HK · MO · TW · SG（5个） |
| **法律场景** | 31 个（全部扁平化） |
| **原子 Skills** | 475 个 |
| **Skill 平均长度** | ~180 行（原 36 行骨架已全部填充） |
| **场景级 Agent** | 8 个场景共 8 个监控 Agent |
| **事件钩子** | 8 个场景共 27 个事件触发器 |
| **适配来源** | Anthropic `claude-for-legal`（⭐ 8,195） |

**2026-06 重大重构：**
- 🏗 **架构扁平化**：16 个场景从 `sub-scenes/` 嵌套结构全部平铺至 `skills/`
- 📋 **CLAUDE.md 统一**：31 个场景统一添加 `## Who's using this`（角色定义+特权标记），根 CLAUDE.md 改为 AI Agent 上下文
- 🚀 **Skill 内容填充**：183 个空心 Skill（骨架仅 36 行）全部填充至 100-420 行实质性法律内容
- 🔗 **路径修复**：415 处错误相对路径 `../../../references/` 修复为 `../../../../references/`
- 🧹 **硬编码清理**：192 个 SKILL.md 移除逐文件路径声明，统一引用场景级 CLAUDE.md
- 👤 **角色感知**：每个场景输出根据 Role（律师/法务/业务方）自动切换 privilege 标记

---

## 核心场景目录

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
| **cross-border-ma** 跨境并购 | 6 | ODI备案、红筹架构、外资准入 |
| **m-and-a** 并购重组 | 19 | 尽职调查、交易结构、审批流程、信息披露 |
| **regulatory-compliance** 行业监管合规 | 18 | 金融/医药/电信/环保等行业准入与合规 |
| **tax-compliance** 税务合规 | 24 | 企业所得税、增值税、转让定价、跨境税务 |
| **product-legal** 产品法务 | 7 | 产品发布审查、营销合规、风险分级 |
| **real-estate-construction** 房地产与建设工程 | 9 | 开发合规、工程纠纷、租赁管理 |

### 合同与商事

| 场景 | Skills | 说明 |
|------|--------|------|
| **contract-review** 合同审查 | 28 | 供应商/客户/NDA/SaaS/MSA全类型审查 |
| **commercial-arbitration** 商事仲裁 | 18 | CIETAC/HKIAC/SIAC/ICC/ICSID程序 |
| **cross-border-trade** 跨境贸易 | 15 | 进出口管制、关税优化、贸易金融合规 |
| **internet-finance** 互联网金融 | 22 | 网络小贷/消费金融/第三方支付合规 |
| **employment-legal** 劳动法务 | 27 | 合同/解除/社保/竞业/调查全流程 |
| **labor-arbitration** 劳动争议 | 9 | 仲裁程序、证据组织、赔偿计算 |
| **cross-border-ma** 跨境并购 | 6 | 外资准入、ODI、VIE架构 |

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
| **commercial-arbitration** 商事仲裁 | 18 | 仲裁条款/程序/裁决执行 |
| **government-investigation** 政府调查应对 | 9 | 反垄断/证券/反腐败调查应对 |
| **white-collar-crime** 白领犯罪 | 15 | 商业贿赂/职务侵占/涉税犯罪/合规体系 |
| **bankruptcy-restructuring** 破产重整 | 15 | 清算/重整/和解/债权人保护 |

### 法律教育与公益

| 场景 | Skills | 说明 |
|------|--------|------|
| **law-student** 法学学习 | 13 | 法考备考、案例分析、法律写作、IRAC训练 |
| **legal-clinic** 法律诊所 | 16 | 劳动法援/消费者维权/婚姻家事/行政诉讼 |

### 基础平台

| 场景 | Skills | 说明 |
|------|--------|------|
| **legal-builder-hub** Skill构建中心 | 10 | Skill安装/更新/注册表/QA/冷启动 |
| **legal-atomic** 原子能力（已合并） | — | 原 law-firm-research 已合并至此 |

---

## 场景架构

每个 scene 由四层构成：

```
CLAUDE.md         ← 场景级配置：角色定义 + 数据源 + 风险等级 + 输出特权标记
  └─ skills/*/SKILL.md  ← 原子 Skill：流程式工作指引 + 分析框架 + 升级决策门
  └─ agents/*.md        ← 定时调度 Agent（监控/复盘/提醒）
  └─ hooks/hooks.json   ← 事件驱动钩子（完成后自动触发其他 skill）
```

### 角色感知

每个场景的 CLAUDE.md 有 `## Who's using this` 节，定义了输出特权标记：

| Role | 特权标记 |
|------|---------|
| 律师/法务人员 | `Privileged & Confidential — Attorney Work Product` |
| 非法务（有律师支持） | `Research Notes — Not Legal Advice — Review With Attorney Before Acting` |
| 非法务（无律师支持） | `General Information — Not Legal Advice — Consult A Licensed Attorney` |

### 数据源标注

所有输出标注来源：`[YD]` 元典 / `[WKL]` 裁判文书网 / `[BD]` 北达 / `[GOV]` 政府平台 / `[web]` 网络搜索 / `[model]` 模型推理

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

## 授权

Apache 2.0 — 详见 [LICENSE](LICENSE)。

---

*Greater China Legal — 2026-06 重构版*
