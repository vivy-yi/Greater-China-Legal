---
title: 元典 MCP — 服务与接入参考
description: >
  元典（Yuandian）MCP 接入配置参考。gcl CLI 的 paid-tier 数据源。
  设置 API key 后，gcl law 自动优先走元典 MCP，标注 [YD]。
---

# 元典 MCP · 接入参考

> **⚠️ 信息说明**
> 元典官网（yuandian.com / mcp.yuandian.com）当前无法访问。
> 以下信息基于上游 claude-for-legal 的引用和已知公开文档编写。
> 实际 URL、SERVICE_ID、工具名称请在能访问网站后核实。

---

## 一、核心入口链接

| 用途 | 链接 | 状态 |
|------|------|------|
| 元典官网 | https://www.yuandian.com | ❌ 当前不可达 |
| MCP 平台 | https://mcp.yuandian.com | ❌ 当前不可达 |
| MCP 应用中心 | https://mcp.yuandian.com/apis | ❌ 需确认 |
| 控制台（Token 管理） | https://mcp.yuandian.com/console | ❌ 需确认 |
| 文档中心 | https://mcp.yuandian.com/docs | ❌ 需确认 |
| ModelScope 上的元典 MCP | https://modelscope.cn/mcp/servers/YuanDian/yuandian-law-search | ✅ 可访问 |
| 客服 | 待确认 | ❌ |

---

## 二、数据源覆盖

根据 upstream claude-for-legal 对元典 MCP 的引用，预计覆盖：

| 数据库 | 规模（推测） |
|--------|-------------|
| 法律法规库 | 与北大法宝类似量级 |
| 司法案例库 | 需确认 |
| 裁判文书 | 需确认 |

实际覆盖范围请以元典官网为准。

---

## 三、与 gcl CLI 的集成

```json
~/.gcl/config.json:
{
  "data_sources": {
    "yuandian_mcp": {
      "enabled": true,
      "api_key": "YOUR_TOKEN",
      "service_id": "YOUR_SERVICE_ID"
    }
  }
}
```

接入后，gcl CLI 的调用链路：

```
gcl law 民法典第585条
  → 检查配置: yuandian_mcp.enabled == true
  → 确认 npc_api 和 yuandian 哪个更优先
  → 调用元典 MCP 查法条
  → 标注 [YD]
  → 输出
```

---

## 四、配置方式（推测）

元典 MCP 很可能与北大法宝共用相似的 MCP 协议格式，即：

```json
{
  "mcpServers": {
    "yuandian-law": {
      "url": "https://mcp.yuandian.com/{SERVICE_ID}/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_TOKEN"
      }
    }
  }
}
```

但以下信息待确认：
- MCP gateway URL 格式
- SERVICE_ID 命名规则
- 是否支持 CLI 接入
- Token 获取方式

---

## 五、安全规则

- Token 只存在本地 `~/.gcl/config.json`，不提交到仓库
- 未接入时降级到 NPC 数据库 / web_search
- 本数据源可替换为北大法宝 MCP 或其他等价服务

---

## 六、待确认事项

| # | 事项 | 确认后更新 |
|---|------|-----------|
| 1 | MCP gateway URL 正确格式 | — |
| 2 | SERVICE_ID 获取方式 | — |
| 3 | API key / Token 申请入口 | — |
| 4 | 数据源覆盖范围 | — |
| 5 | 是否提供 CLI 工具 | — |
| 6 | 是否有免费试用额度 | — |
| 7 | 客服联系方式 | — |
| 8 | 定价信息 | — |

---

*Greater China Legal — gcl-data-service reference: 元典 MCP*
*本文件标记为待确认，在官网可访问后更新。*
