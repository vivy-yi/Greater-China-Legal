# CoCounsel Legal — Practice Profile (curator v2.0)

<!-- CONFIGURATION LOCATION -->
> 用户配置位置:本文件 § B9。所有 `[填空]` 标记必须由用户填写后才能跑 skill。

*Written for: [律师事务所/公司法务] · 场景:美国法律研究辅助*
*Last updated: 2026-06-22*
*Schema: Part A (16 universal) + Part B (scene-adaptive)*
*目标行数: < 250*

> ⚠️ **场景边界声明**: 本场景是大中华区法律体系的**境外延伸工具**,仅用于美国法律研究辅助。大中华法域问题必须路由到对应 scene(contract-review / m-and-a / cross-border-ma 等)。

---

## Part A — Operating System(精简版,本场景仅路由)

### § A1 Configuration Location

用户配置在 **§ B9**。`[填空]` 字段由 `cold-start-interview` 引导填写。

**本场景特殊性:** 用户配置**必须**包含具体美国法域(联邦 / 州)+ 研究主题。否则视为信息不足,所有 skill 输出自动加注 `[美国法域待补]`。

### § A2 Who's using this

**Role(3 档,精简):**

| 档位 | 角色 | 工作产物头部 |
|------|------|-------------|
| 1 | 主办律师(跨境) | `律师执业秘密 — 美国法律研究工作底稿` |
| 2 | 涉外律师(美国法) | `美国法律研究工作底稿` |
| 3 | 大中华跨境业务法务 | `美国法律研究备忘` |

**绝对禁止:**
- 不得作为大中华法域的主要研究工具
- 不得将 Westlaw 报告直接作为中国法律意见

### § A3 Quiet mode for client-facing deliverables

**对外文档(向客户):**
- 保留 Westlaw 报告引用 + 案例 + 法条
- 注明 "境外法律研究,仅供内部参考"

### § A4 Available integrations

| 集成 | 用途 | 失败回退 |
|------|------|----------|
| `cocounsel-legal MCP` | Westlaw Deep Research | 必须连接,否则停止 |
| Practical Law | 次级权威 | Westlaw fallback |

**前置条件**:`cocounsel-legal` MCP server 必须连接。未连接时停止并告知用户。

### § A5 Outputs

**Reviewer note(3 行,精简):**
1. 美国法域:[联邦 / 州 + 州名]
2. 研究主题:[核心问题]
3. 报告类型:[case law / statute / regulation / secondary]

**Decision tree(3 选项):**
1. ✅ **路由到大中华 scene** — 中国法律问题
2. ⚠️ **运行 Westlaw Deep Research** — 美国法律问题
3. 🔴 **不适用** — 其他法域

### § A6-A14 精简

参见场景 v3 标准 Part A。本场景**仅在美国法律研究场景使用**:
- § A6 Decision posture: 保留 recoverable error
- § A7 Guardrails: 9 + 3 CN 附加 + 2 跨境特化
- § A8 Scaffolding: 路由优先
- § A9 Routing: 大中华 → 对应 scene / 美国 → `deep-research`
- § A10-A14: 简化适用

### § A15 Tag vocabulary

| Tag | 含义 |
|-----|------|
| `[US-federal]` / `[US-state]` | 美国法域 |
| `[Westlaw]` / `[Practical Law]` | 数据源 |
| `[域外]` | 跨境研究 |

---

## Part B — Scene-Adaptive Practice Profile(精简)

### § B1 工作流(主入口 + 路由)

**主入口:** 路由判断 → 美国法律问题才进入 `deep-research`

```
Step 1: 识别法域
  ├─ 大中华法域(中国 / 香港 / 澳门 / 台湾 / 新加坡)
  │   → 路由到对应 scene(contract-review / m-and-a / cross-border-ma / ...)
  └─ 美国法域(联邦 / 州)
      → 进入 Step 2

Step 2: 运行 `deep-research`
  ├─ 验证 cocounsel-legal MCP 已连接
  ├─ 提交研究请求
  ├─ 轮询完成状态
  └─ 返回 Westlaw 报告

Step 3: 报告整理
  → 添加大中华法域对照(如有需要)
  → 输出"美国法律研究 + 大中华法律对照"综合备忘
```

### § B2 路由表(精简)

| 议题 | 路由到 |
|------|--------|
| 中国合同 | `contract-review` scene |
| 中国 M&A | `m-and-a` scene |
| 跨境并购(含美方) | `cross-border-ma` scene |
| **美国法律研究** | **`deep-research`(本场景唯一 skill)** |
| 美国合规 | 路由到 `regulatory-compliance` 涉外分支 + `deep-research` |
| 美国诉讼 | 路由到 `litigation-support` 涉外分支 + `deep-research` |

### § B3 三色风险体系

| 等级 | 案件类型 | 处理 |
|------|----------|------|
| 🔴 HIGH | 美国制裁 / 出口管制 | 主办 + 美国律师 + `deep-research` |
| ⚠️ MEDIUM | 普通美国法律研究 | `deep-research` 即可 |
| ✅ LOW | 概念性查询 | `deep-research` 即可 |

### § B4 路由阻断规则

**绝对禁止触发(即使触发也必须升级):**

| 触发 | 阻断原因 |
|------|---------|
| 中国法律问题 | 不属于本场景 → 路由到对应 scene |
| 美国法律意见 | Westlaw 报告是研究辅助,不是律师意见 |
| 出庭辩护 | 美国执业律师,本场景不涉及 |

### § B5 用户配置(精简 8 字段)

```yaml
us_jurisdiction: [填空:federal/CA/NY/TX/...]
us_state: [填空:具体州名]
research_topic: [填空:研究主题]
mcp_status: [填空:已连接/未连接]
case_type: [填空:caselaw/statute/regulation/secondary/...]
deadline: [填空:YYYY-MM-DD]
attorney_contact: [填空:主办律师]
partner_approval: [填空:是/否]
```

### § B6 余项从略

本场景精简适用,不需要完整 17 节 Part B。详见场景 v3 标准。

---

*Greater China Legal — CoCounsel Legal scene*
*美国法律研究辅助 · 仅作为大中华法域的境外延伸工具*
*行数 < 250 · 最后更新:2026-06-22*