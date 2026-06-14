---
title: 元典 MCP — 服务与接入参考
description: >
  元典开放平台（Yuandian Open Platform）MCP 接入配置参考。
  gcl CLI 的 paid-tier 数据源。设置 API key 后优先走元典 MCP，标注 [YD]。
  官方文档：https://open.chineselaw.com/llms-full.txt
---

# 元典 MCP · 接入参考

> **信息可信度声明**
> 以下信息来自元典开放平台官方文档（open.chineselaw.com/llms-full.txt）。
> 工具名称以控制台实际看到的为准，或用 `tools/list` 核实。

---

## 一、核心入口链接

| 用途 | 链接 |
|------|------|
| 接口广场（API 目录） | https://open.chineselaw.com/api-square |
| 完整 Agent 文档 | https://open.chineselaw.com/llms-full.txt |
| 短索引（LLM 入口） | https://open.chineselaw.com/llms.txt |
| API JSON 目录 | https://open.chineselaw.com/api/apis?pageNum=1&pageSize=200&sortBy=latest |
| 文档中心 | https://open.chineselaw.com/docs |
| 订阅 API Key | https://open.chineselaw.com |
| MCP Health | https://open.chineselaw.com/mcp/health |

---

## 二、MCP 配置方式

MCP 传输协议：**Streamable HTTP**。

```json
{
  "mcpServers": {
    "yuandian-law": {
      "type": "http",
      "url": "https://open.chineselaw.com/mcp/law/stream",
      "headers": {
        "Accept": "application/json, text/event-stream",
        "Authorization": "Bearer YOUR_API_KEY"
      }
    },
    "yuandian-case": {
      "type": "http",
      "url": "https://open.chineselaw.com/mcp/case/stream",
      "headers": {
        "Accept": "application/json, text/event-stream",
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

兼容 server（可能暴露所有工具）：
```
https://open.chineselaw.com/mcp
```

---

## 三、REST API 直接调用

无需 MCP，直接用 HTTP 调用：

```
GET/POST https://open.chineselaw.com/open/{routeKey}
Header: X-API-Key: YOUR_API_KEY
Header: Content-Type: application/json; charset=utf-8
Header: Accept: application/json
```

---

## 四、API 分类与 MCP 工具名

当前 36 个公开接口，分为 4 类：

### 法律法规（3 个）

| API | MCP 工具名 | 用途 |
|-----|-----------|------|
| 法律法规语义检索 | `yuandian_law_vector_search` | 自然语言查询法规/法条 |
| 法规详情 | `yuandian_rh_fg_detail` | 法规全文与时效性 |
| 法条详情 | `yuandian_rh_ft_detail` | 单条法条内容 |
| 法规关键词检索 | `yuandian_rh_fg_search` | 按名称/关键词检索法规 |
| 法条关键词检索 | `yuandian_rh_ft_search` | 按关键词定位具体条文 |

### 案例文书（3 个）

| API | MCP 工具名 | 用途 |
|-----|-----------|------|
| 案例语义检索 | `yuandian_case_vector_search` | 自然语言检索类案 |
| 案例详情 | `yuandian_rh_case_details` | 裁判文书全文 |
| 普通案例关键词检索 | `yuandian_rh_ptal_search` | 按案由/法院/日期检索 |
| 权威案例关键词检索 | `yuandian_rh_qwal_search` | 指导案例/典型案例检索 |

### 企业信息（20+ 个）

| API | MCP 工具名 | 用途 |
|-----|-----------|------|
| 企业检索 | `yuandian_rh_enterpriseSearch` | 按名称检索企业 |
| 基本信息 | `yuandian_rh_company_info` | 工商登记信息 |
| 聚合总览 | `yuandian_rh_enterpriseAggregationSummary` | 多模块统计 |
| 涉诉信息统计 | — | 案件类别/案由/法院分布 |
| 涉诉文书列表 | — | 企业相关涉诉文书 |
| 开庭/法院公告 | — | 开庭/法院公告列表 |
| 失信/被执行人 | — | 失信/被执行人列表 |
| 股权冻结/出质 | — | 股权冻结/出质列表 |
| 行政处罚/经营异常 | — | 行政处罚/经营异常列表 |
| 商标/专利/软著 | — | 知识产权列表 |
| 变更/年报 | — | 变更记录/企业年报 |

### 幻觉检测（1 个）

| API | MCP 工具名 | 用途 |
|-----|-----------|------|
| 法律幻觉校验 | `yuandian_hall_detect` | 校验文本中法条引用准确性，判定一致/不一致/未命中 |

---

## 五、数据源规模

| 数据库 | 规模（官方） |
|--------|-------------|
| 法律法规库 | 500 万+ |
| 司法案例库 | 1.6 亿+ |
| 企业信息 | 覆盖全国企业 |

---

## 六、与 gcl CLI 的集成

```json
~/.gcl/config.json:
{
  "data_sources": {
    "yuandian_mcp": {
      "enabled": true,
      "api_key": "YOUR_API_KEY"
    }
  }
}
```

接入后 gcl CLI 的调用链路：

```
gcl law 民法典第585条
  → 检查配置: yuandian_mcp.enabled == true
  → POST https://open.chineselaw.com/open/law/vectorSearch
     Header: X-API-Key: xxx
     Body: {"query": "民法典第585条"}
  → 解析返回 JSON
  → 标注 [YD]
  → 输出法条原文
```

未配置时自动降级到免费备选（NPC 数据库 / Brave Search）。

---

## 七、核心优势

相比北大法宝 MCP：

| 维度 | 元典 | 北大法宝 |
|------|------|---------|
| MCP 协议 | Streamable HTTP | 标准 MCP |
| API 调用 | 支持（无 LLM 消耗） | 有 CLI 工具 |
| 企业信息 | ✅ 20+ 个 API | ❌ 无 |
| 幻觉检测 | ✅ 专用 API | ❌ 无 |
| 文档 | ✅ llms-full.txt 247K | 需登录控制台 |
| 工具名 | 可预测（yuandian_*） | 需 tools/list 核实 |

---

## 八、安全规则

- API Key 只存在本地 `~/.gcl/config.json`，不提交到仓库
- 未接入时降级到免费备选
- 最终判断由执业人员承担

---

*Greater China Legal — gcl-data-service reference: 元典开放平台 MCP*
*源文档：https://open.chineselaw.com/llms-full.txt（最新）*
