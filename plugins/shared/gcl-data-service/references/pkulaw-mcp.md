---
title: 北大法宝 MCP — 服务与链接总表
description: >
  北大法宝 MCP 接入配置参考。gcl CLI 的 paid-tier 数据源。
  设置 SERVICE_ID + Token 后，gcl law/cases 自动走北大法宝而非免费备选。
---

# 北大法宝 MCP · 服务与链接总表

> 本文件为 `gcl-data-service` 的付费数据源参考文档。
> 接入后，gcl CLI 的 `law`、`cases`、`verify` 命令自动使用北大法宝为优先数据源，标注 `[WKL]`。

---

## 一、核心入口链接

| 用途 | 链接 |
|---|---|
| MCP 平台首页 | https://mcp.pkulaw.com |
| MCP 应用中心（选服务、拿 SERVICE_ID） | https://mcp.pkulaw.com/apis |
| 文档中心 | https://mcp.pkulaw.com/docs |
| 控制台（管理 Token） | https://mcp.pkulaw.com/console |
| 服务定价 | https://mcp.pkulaw.com/pricing |
| CLI 工具（npm） | https://www.npmjs.com/package/@pkulaw/mcp-cli |
| 示例技能（Gitee） | https://gitee.com/pkulaw/pkulaw-skills |
| 北大法宝官网 | https://www.pkulaw.com |
| ModelScope MCP Server | https://modelscope.cn/mcp/servers/Pkulaw/pkulaw-mcp-law-search |
| 客服 | 400-810-8266 |

---

## 二、MCP 配置方式

```json
{
  "mcpServers": {
    "pkulaw-law-semantic": {
      "url": "https://apim-gw.pkulaw.com/{SERVICE_ID}/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_TOKEN"
      }
    }
  }
}
```

- `SERVICE_ID`：在应用中心选定服务后获得，每个服务不同
- `YOUR_TOKEN`：在控制台创建应用后获得
- 多个服务共用同一 Token，各配各的 `SERVICE_ID`

---

## 三、CLI 接入方式

```bash
npm install -g @pkulaw/mcp-cli
pkulaw-mcp init --authorization "Bearer YOUR_TOKEN"
pkulaw-mcp law-semantic search_article "劳动合同解除"
```

- CLI 返回结构化 JSON，零 LLM 消耗
- 适合 gcl CLI 内部调用

---

## 四、数据源规模

| 数据库 | 规模 |
|--------|------|
| 法律法规库 | 500 万+ |
| 司法案例库 | 1.6 亿+ |
| 行政执法库 | 4250 万+ |
| 检察文书库 | 820 万+ |
| 法学期刊库 | 45 万+ |

---

## 五、与 gcl CLI 的集成

当用户配置了北大法宝 Token：

```
~/.gcl/config.json:
{
  "data_sources": {
    "pkulaw_mcp": {
      "enabled": true,
      "api_key": "YOUR_TOKEN",
      "service_id": "YOUR_SERVICE_ID"
    }
  }
}
```

gcl CLI 的调用链路变为：

```
gcl law 民法典第585条
  → 检查配置: pkulaw_mcp.enabled == true
  → 调用: pkulaw-mcp law-semantic search_article "民法典第585条"
  → 解析 JSON 输出
  → 标注 [WKL]
  → 输出法条原文
```

未配置时自动降级到免费备选（NPC 数据库 / Brave Search）。

---

## 六、安全规则

- Token 和 SERVICE_ID 只存在本地 `~/.gcl/config.json`，不提交到仓库
- 未接入时所有输出标注 `[待检索]`，不编造法条原文
- 本数据源可替换为元典 MCP 或其他等价服务，无需改动 SKILL.md

---

*Greater China Legal — gcl-data-service reference: 北大法宝 MCP*
