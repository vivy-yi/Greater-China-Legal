# Greater China Legal

> **大中华区法律 Agent Skill 体系** — 基于 Anthropic `claude-for-legal` 适配，支持中国大陆/香港/澳门/台湾/新加坡，覆盖 9 个核心法律场景 × 100+ 个原子 Skill。

---

## 背景

Anthropic 官方 [`claude-for-legal`](https://github.com/anthropics/claude-for-legal)（⭐ 8,195）覆盖美国/普通法系。本项目 fork 自官方仓库，持续同步上游，**专注于大中华区法律体系的完整适配**，供各种 Agent 工具（Claude Code / Codex / 自研 Agent 平台）使用。

---

## 目录结构

```
Greater-China-Legal/
├── legal-atomic/                 ← 35个通用原子能力（跨场景可调用）
│   └── {35个通用推理skill}
├── shared/agent-ops/             ← 通用工作台初始化skills
│   ├── cold-start-interview/     # 新建事项时了解背景
│   ├── customize/                 # 按客户/法域定制
│   └── matter-workspace/          # 工作台初始化
│
├── {9个核心场景}/                 ← 各场景含 CLAUDE.md + skills/ + references/
│   ├── labor-arbitration/        # 劳动仲裁（9 skills）
│   ├── contract-review/           # 合同审查（15 skills）
│   ├── data-compliance/          # 数据合规（14 skills）
│   ├── corporate-governance/     # 公司治理（16 skills）
│   ├── ip-infringement/          # 知识产权侵权（15 skills）
│   ├── litigation-support/       # 诉讼支持（22 skills）
│   ├── tax-compliance/           # 税务合规（12 skills）
│   ├── cross-border-ma/          # 跨境并购（6 skills）
│   └── internet-finance/         # 互联网金融（10 skills）
│
├── {独立保留域}/                  ← 无对应9场景，按原结构保留
│   ├── employment-legal/         # HR专用操作（14 skills）
│   ├── legal-clinic/            # 法律诊所（16 skills）
│   ├── law-student/             # 法学教育（13 skills）
│   ├── product-legal/            # 产品合规（7 skills）
│   ├── legal-builder-hub/        # Skill管理（10 skills）
│   └── ai-governance-legal/      # AI治理通用（3 skills）
│
├── LEGAL_FRAMES/                 ← 5个法域基准文档
│   ├── cn-mainland.md
│   ├── hk.md
│   ├── mo.md
│   ├── tw.md
│   └── sg.md
├── references/                   ← 共享方法论（独立维护）
├── scripts/
│   ├── sync-upstream.py         # 同步上游
│   └── validate-skills.py        # 格式检查
├── .github/workflows/
│   └── sync-upstream.yml        # 月度同步自动化
├── SKILL_MD_SCHEMA.md            ← Skill YAML规范
├── UPSTREAM_TRACKING.md          ← 上游追踪
└── README.md
```

---

## 架构说明

### 三层结构

| 层级 | 定位 | 内容 |
|---|---|---|
| **legal-atomic** | 通用原子能力 | 35个跨场景可调用的通用推理能力 |
| **shared/agent-ops** | 工作台初始化 | 通用工作台操作，所有场景可调用 |
| **{9场景}** | 场景专属能力 | 各场景独立的原子skills，依赖 legal-atomic |

### 9 核心场景

```
labor-arbitration    劳动仲裁    ← employment-legal 合并
contract-review      合同审查    ← commercial-legal 合并
data-compliance     数据合规    ← privacy-legal 合并
corporate-governance 公司治理    ← corporate-legal 合并
ip-infringement     知识产权侵权 ← ip-legal 合并
litigation-support  诉讼支持    ← litigation-legal 合并
tax-compliance      税务合规    ← regulatory-legal 合并
cross-border-ma     跨境并购    （独立场景）
internet-finance    互联网金融  ← ai-governance-legal 部分合并
```

---

## 快速开始

### 安装 Skill（Claude Code）

```bash
claude skills install https://github.com/vivy-yi/Greater-China-Legal
```

### 触发 Skill

```
大陆劳动仲裁：  /labor-arbitration:dispute-classifier
香港合同审查：    /contract-review:term-analyzer --frame hk
台湾数据合规：    /data-compliance:pipl-assessment --frame tw
新加坡税务：      /tax-compliance:tax-type-classifier --frame sg
```

---

## 法域覆盖

### 第一阶段：大中华区

| 法域 | 法律体系 | 核心法规 |
|---|---|---|
| **CN** 中国大陆 | 社会主义法系/民法系 | 民法典、劳动合同法、个保法、公司法 |
| **HK** 香港 | 普通法系 | Employment Ordinance (Cap.57)、Companies Ordinance (Cap.622) |
| **MO** 澳门 | 大陆法系 | 澳门民法典（葡萄牙民法典延续）、劳动关系法 |
| **TW** 台湾 | 大陆法系 | 台湾民法、劳动基准法、公司法 |
| **SG** 新加坡 | 普通法系 | Employment Act (Cap.91)、PDPA、Companies Act |

### 第二阶段：亚洲（计划中）

- 东亚：日本、韩国、朝鲜、蒙古
- 东南亚：越南、泰国、马来西亚、印度尼西亚、菲律宾等
- 中亚：哈萨克斯坦、乌兹别克斯坦等

---

## 上游同步

本仓库每月自动同步 [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) 的更新。详见 [UPSTREAM_TRACKING.md](UPSTREAM_TRACKING.md)。

---

## License

继承上游 Anthropic 仓库 License
