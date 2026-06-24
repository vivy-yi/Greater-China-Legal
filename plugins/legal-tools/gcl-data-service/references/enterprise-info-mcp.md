---
title: 企业信息 MCP — 天眼查 / 企查查
description: >
  天眼查与企查查的 MCP / API / CLI 接入参考。
  gcl CLI 的 paid-tier 企业信息数据源（公司核查、股东穿透、司法风险、知识产权）。
  27 个 SKILL + 182 个工具，覆盖尽调/投资/法务/采购四大场景。
---

# 企业信息 MCP — 天眼查 / 企查查

## 核心结论

| 平台 | 推荐度 | 接入方式 |
|------|--------|---------|
| **企查查 agent.qcc.com** | ⭐⭐⭐⭐⭐ | MCP + CLI 双接入，182 工具 |
| 天眼查 mcp.tianyancha.com | ⭐⭐⭐⭐ | 接入中，访问受限 |

**首选企查查**——已有完整的"智能体数据平台"，专为 AI Agent 设计。

---

## 一、企查查智能体数据平台（agent.qcc.com）

### 平台定位

> 让 AI 智能体读懂中国企业

不是普通 API 网关，是**面向 AI Agent 的企业数据基座**：

- 实体强锚定（强制验证 18 位统一社会信用代码）
- 强语义负向防御（"查无" vs "没有"）
- 数据脱水（按需返回 AI 决策结论，非原始 JSON）
- 可审计决策链路

### 数据规模

| 数据维度 | 规模 |
|---------|------|
| 市场主体 | 3.65 亿+ |
| 司法诉讼 | 2.5 亿+ |
| 知识产权 | 2.1 亿+ |
| 新闻舆情 | 4300 万+ |
| 招投标 | 1.7 亿+ |
| 投融资 | 106 万+ |

数据截至 2026-05，持续更新。

### 接入方式 1：MCP（推荐）

6 个 Server / **181 个工具**（完整列表见 references/qcc-tools-list.md）/ 27 个 SKILL：

```json
{
  "mcpServers": {
    "qcc-company": {
      "url": "https://agent.qcc.com/mcp/company/stream",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    },
    "qcc-risk": {
      "url": "https://agent.qcc.com/mcp/risk/stream",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    },
    "qcc-ipr": {
      "url": "https://agent.qcc.com/mcp/ipr/stream",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    },
    "qcc-operation": {
      "url": "https://agent.qcc.com/mcp/operation/stream",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    },
    "qcc-executive": {
      "url": "https://agent.qcc.com/mcp/executive/stream",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    },
    "qcc-history": {
      "url": "https://agent.qcc.com/mcp/history/stream",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

### 接入方式 2：CLI（自动化用）

```bash
npm install -g qcc-agent-cli
qcc init --authorization "Bearer YOUR_API_KEY"

# 直接查询
qcc company get_shareholder_info "小米科技有限责任公司"
```

特点：零 Token 消耗、确定性执行、返回原始 JSON。

### 6 个 Server 职责

| Server | 工具数 | 覆盖 |
|--------|--------|------|
| company | 16 | 工商登记维度 |
| risk | ~30 | 司法风险/失信/经营异常 |
| ipr | ~25 | 知识产权 |
| operation | ~25 | 经营状况/招投标 |
| executive | ~30 | 股东/高管/关联方 |
| history | ~56 | 历史变更/沿革 |

### 典型工具

| 工具名 | 用途 |
|--------|------|
| `get_company_base_info` | 工商基本信息 |
| `get_shareholder_info` | 股东结构 |
| `get_legal_representative` | 法定代表人 |
| `get_case_filing_info` | 立案信息（含时间窗口） |
| `get_serious_violation` | 严重违法记录 |
| `get_trademark_info` | 商标信息 |
| `get_patent_info` | 专利信息 |

### 4 大业务场景

| 场景 | 客户 | 解决 |
|------|------|------|
| 银行/金融机构 | KYB 企业核验 | 人工尽调 2 小时 → 分钟级 |
| 投资人/FA | IC Memo 投资备忘录 | 一次对话完成 DD |
| 法务/律师 | 合同相对方主体核验 | 防已注销/失信/异常 |
| 采购/供应链 | 新供应商快速筛选 | 3 分钟批量出筛查结论 |

### 兼容客户端

WorkBuddy ★ / QoderWork ★ / QClaw ★ / Trae / Cursor / OpenClaw / 阿里云百炼 / 扣子 Coze / CherryStudio / Claude Code / Windsurf

---

## 二、天眼查开放平台（mcp.tianyancha.com）

### 现状

- 主站 https://open.tianyancha.com/ 仍以传统 API 为主
- https://mcp.tianyancha.com/ 已上线 MCP 服务
- 公开信息少，需登录控制台查看

### 接入方式

- API 端点：mcp.tianyancha.com 提供
- 详细工具列表需登录控制台核实
- 不公开 agent 平台，等同于早期企查查

---

## 三、与 GCL 的集成

```json
~/.gcl/config.json:
{
  "data_sources": {
    "qcc_mcp": {
      "enabled": true,
      "api_key": "YOUR_API_KEY",
      "endpoint": "https://agent.qcc.com/mcp"
    }
  }
}
```

调用链路：

```
gcl company <企业名>
  → 检查配置: qcc_mcp.enabled
  → POST https://agent.qcc.com/mcp/company/stream
     Header: Authorization: Bearer xxx
     Body: {"tool": "get_company_base_info", "params": {"name": "..."}}
  → 解析返回（已 AI-friendly 脱水）
  → 标注 [QCC]
```

**AI 调用示例**：

```
用户：查询小米科技的基本工商信息
AI：
  → 调用 get_company_base_info
  → 返回：{
      "企业名称": "小米科技有限责任公司",
      "法定代表人": "...",
      "成立日期": "...",
      "统一社会信用代码": "91110108551385082Q",
      "摘要": "..."
    }
  → 标注 [QCC: qcc-company, get_company_base_info]
```

---

## 四、场景匹配

| GCL 场景 | 使用 Server | 解决什么 |
|---------|-------------|---------|
| `m-and-a` 尽调 | qcc-company / qcc-risk / qcc-ipr | 标的方背景穿透 |
| `corporate-governance` | qcc-company / qcc-executive | 关联方核查 |
| `data-compliance` | qcc-risk | 数据合规风险 |
| `contract-review` | qcc-company | 对方主体核验 |
| `litigation-support` | qcc-risk | 对方涉诉情况 |
| `investment-DD` | qcc-ipr / qcc-operation | 知识产权/经营状况 |

---

## 五、定价/限制

- 6 个 Server × 182 个工具 = 完整能力
- 27 个 SKILL 已上线，复制示例提问即可使用
- 具体定价：登录 agent.qcc.com 后查看
- 客服：400-088-8275

---

## 六、安全规则

- API Key 只存在本地 `~/.gcl/config.json`，不提交到仓库
- 实体强锚定：调用前先用 get_company_base_info 锁定 18 位统一社会信用代码
- 强语义负向防御："经企查查全量核查未发现失信" ≠ "绝对无失信"
- 最终判断由执业人员承担

---

*Greater China Legal — gcl-data-service reference: 企业信息 MCP*
*来源：https://agent.qcc.com/ 实际验证 2026-06-15*
