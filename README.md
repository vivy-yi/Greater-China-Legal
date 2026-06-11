# Greater China Legal

> **大中华区法律 Agent Skill 体系** — 基于 Anthropic `claude-for-legal` 适配，支持中国大陆/香港/澳门/台湾/新加坡，覆盖12个业务域 × 117个 Skill。

---

## 背景

Anthropic 官方 [`claude-for-legal`](https://github.com/anthropics/claude-for-legal)（⭐ 8,195）覆盖美国/普通法系。本项目 fork 自官方仓库，持续同步上游，**专注于大中华区法律体系的完整适配**，供各种 Agent 工具（Claude Code / Codex / 自研 Agent 平台）使用。

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

东亚：日本、韩国、朝鲜、蒙古
东南亚：越南、泰国、马来西亚、印度尼西亚、菲律宾等
中亚：哈萨克斯坦、乌兹别克斯坦等

---

## 目录结构

```
Greater-China-Legal/
├── LEGAL_FRAMES/              ← 5个法域基准文档
│   ├── cn-mainland.md
│   ├── hk.md
│   ├── mo.md
│   ├── tw.md
│   └── sg.md
├── {12个业务域}/              ← 每域含大陆+港+澳+台+新 多版本
│   ├── employment-legal/
│   ├── commercial-legal/
│   └── ...
├── references/ ← 共享方法论（独立维护）
├── managed-agent-cookbooks/    ← Agent工作流
├── scripts/ ← 自动化脚本
│   ├── sync-upstream.py ← 同步上游
│   └── validate-skills.py     ← 格式检查
├── .github/workflows/
│   └── sync-upstream.yml ← 月度同步自动化
├── SKILL_MD_SCHEMA.md         ← Skill YAML规范
├── UPSTREAM_TRACKING.md        ← 上游追踪
└── README.md
```

---

## 快速开始

### 安装 Skill（Claude Code）

```bash
claude skills install https://github.com/vivy-yi/Greater-China-Legal
```

### 触发 Skill

```
大陆：/employment-legal:termination-review
香港：  /employment-legal:termination-review --frame hk
台湾：  /employment-legal:termination-review --frame tw
新加坡：/employment-legal:termination-review --frame sg
```

---

## 业务域覆盖

| 域 | Skill数 | 说明 |
|---|---|---|
| employment-legal | 17 | 劳动法 |
| litigation-legal | 16 | 诉讼仲裁 |
| legal-clinic | 14 | 法律诊所 |
| law-student | 11 |法学教育 |
| corporate-legal | 10 | 公司并购 |
| commercial-legal | 9 | 商事合同 |
| ip-legal | 9 | 知识产权 |
| legal-builder-hub | 8 | Skill管理 |
| ai-governance-legal | 7 | AI治理 |
| privacy-legal | 6 | 隐私数据 |
| regulatory-legal | 6 | 监管合规 |
| product-legal | 4 | 产品合规 |

---

## 上游同步

本仓库每月自动同步 [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) 的更新。详见 [UPSTREAM_TRACKING.md](UPSTREAM_TRACKING.md)。

---

## License

继承上游 Anthropic 仓库 License