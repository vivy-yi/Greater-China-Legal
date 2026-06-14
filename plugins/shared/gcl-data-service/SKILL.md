---
name: gcl-data-service
description: >
  GCL 数据源服务——统一管理法律数据查询的 CLI 工具。
  覆盖法条查询、案例检索、法条效力验证。
  所有 SKILL.md 中的 [YD]/[WKL]/[BD]/[GOV] 标注通过本服务实现。
trigger_phrases:
  - 数据源
  - 法条查询
  - 案例检索
  - 效力验证
  - gcl
  - 法律数据库
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: low
---

# /gcl-data-service — 法律数据源管理

## 数据源层次

本服务管理三层数据源，AI 在需要查法条/案例/法规时按优先级调用：

| 优先级 | 数据源 | 标注 | 状态 | 配置 |
|--------|-------|------|------|------|
| 1 | 元典 MCP | `[YD]` | ❌ 须付费 | API key |
| 2 | 北大法宝 MCP | `[WKL]` | ❌ 须付费 | API key |
| 3 | flk.npc.gov.cn | `[GOV]` | ✅ 免费公开 | 已内置 |
| 4 | gov.cn / court.gov.cn | `[GOV]` | ✅ 免费公开 | 已内置 |
| 5 | web_search（备选） | `[web]` | ✅ 免费公开 | 已内置 |

数据源通过 `scripts/gcl` CLI 统一接入。

## 可用命令

### `gcl law <法条名>`

查询法条正文。自动遍历 NPC 数据库 → web_search。

```
用法:
  gcl law 民法典第585条
  gcl law 中华人民共和国民法典 第五百七十七条

输出示例:
  ─── 法条查询: 民法典第585条 ───
  📘 中华人民共和国民法典
     发布: 2020-05-28
     🔗 https://flk.npc.gov.cn/detail/...
     来源: [GOV]

  ⚠️ 备选: web_search 结果
  🔗 https://pkulaw.com/...
     来源: [web]
```

### `gcl cases <关键词>`

检索裁判文书和案例。

```
用法:
  gcl cases 买卖合同 违约金
  gcl cases 数据出境 安全评估 案例

输出示例:
  ─── 案例查询: 买卖合同 违约金 ───
  ⚖️ 最高人民法院关于审理买卖合同纠纷案件...
     🔗 https://court.gov.cn/...
     来源: [GOV]
```

### `gcl verify <法条名>`

验证法条是否现行有效（检查修订/废止公告）。

### `gcl search <关键词>`

通用搜索——同时查法条和案例。

## 数据源配置

使用 `gcl init` 初始化配置，`~/.gcl/config.json` 内容：

```json
{
  "data_sources": {
    "npc_api": {"enabled": true},
    "web_search": {"enabled": true},
    "yuandian_mcp": {"enabled": false, "api_key": ""},
    "pkulaw_mcp": {"enabled": false, "api_key": ""}
  },
  "default_source": "auto"
}
```

## AI 调用流程

当 SKILL.md 需要查法条/案例时：

```
1. 检查 gcl 是否已安装
   → 如未安装，提示用户运行 gcl init
   → 如已安装，继续

2. 确定数据源优先级
   → 检查 ~/.gcl/config.json 中各源启用状态
   → 从启用顺序最高的开始查

3. 执行查询
   → python3 scripts/gcl law <查询内容>
   → 解析输出，提取原文
   → 标注来源（[YD]/[WKL]/[GOV]/[web]）

4. 验证结果可靠性
   → GCL 来源 → 直接引用
   → web 来源 → 标注 [web]，提示"建议到 NPC 数据库确认"
```

## MCP 集成

将 `gcl` 注册为 Claude Code 的 MCP server：

运行 `gcl mcp-config`，输出添加到 `~/.claude/.mcp.json`：

```json
{
  "mcpServers": {
    "gcl-law": {
      "command": "/path/to/scripts/gcl",
      "args": ["law"]
    },
    "gcl-cases": {
      "command": "/path/to/scripts/gcl",
      "args": ["cases"]
    }
  }
}
```

注册后可以在 Claude Code 中直接使用：
```
/gcl:law 民法典第585条
/gcl:cases 合同纠纷 违约金
```

## 数据源管理

| 操作 | 命令 | 说明 |
|------|------|------|
| 初始化 | `gcl init` | 创建 ~/.gcl/config.json |
| 启用 NPC 数据库 | `gcl config set npc_api.enabled true` | 免费数据源 |
| 启用元典 MCP | 设置 `yuandian_mcp.api_key` | 须有元典订阅 |
| 启用北大法宝 MCP | 设置 `pkulaw_mcp.api_key`（详见 references/pkulaw-mcp.md） | 须有北大法宝订阅 |
| 查看状态 | `cat ~/.gcl/config.json` | 各数据源启用状态 |
| 测试连接 | `gcl law 民法典 第1条` | 验证数据源可用性 |

## 本服务不做什么

- 不存储查询结果——每次查询实时检索
- 不验证法条解释的准确性——只返回原文
- 不替代付费法律数据库——免费源可能不全
- 不处理境外法域查询（香港/澳门/台湾/新加坡须单独接入）

---

*Greater China Legal — shared gcl-data-service v1.0.0*
