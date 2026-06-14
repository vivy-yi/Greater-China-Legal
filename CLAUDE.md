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
