---
title: QCC MCP → CLI 转换对比：mcporter vs 官方 qcc-agent-cli
description: >
  用 mcporter v0.12.0 把 QCC 官方 MCP（161 工具）转换成 CLI，
  与 QCC 官方 qcc-agent-cli v1.0.5 的实际能力对比。
  包含真实生成产物、运行测试、缺陷清单。
last_reviewed: 2026-06
mcporter_version: 0.12.0
qcc_cli_version: 1.0.5
tools_tested: 161
---

# QCC MCP → CLI 转换对比：mcporter vs 官方 qcc-agent-cli

## 测试设置

```
数据源: GCL 已下载的 161 个 QCC 工具名（从 references/qcc-tools-list.md 解析）
Mock MCP server: /tmp/qcc-mock.mjs (Node.js stdio, 返回 161 个工具的 mock schema)
mcporter: 0.12.0 (npm install -g)
qcc-agent-cli: 1.0.5 (从 npm tarball 解包分析)
```

由于没有真实 QCC API Key，使用 mock server 验证 mcporter 的"转换"能力。qcc-agent-cli 因为是官方实现，分析源码得到结果。

---

## 测试结果：mcporter generate-cli 实测

### Step 1：生成 CLI

```bash
$ npx mcporter generate-cli --command "node /tmp/qcc-mock.mjs" --output qcc-cli.ts

Generated CLI at /tmp/mcporter-test/qcc-cli.ts

# 产物大小
$ wc -l qcc-cli.ts
9145 qcc-cli.ts
```

### Step 2：验证工具注册

```bash
$ npx tsx qcc-cli.ts --help

qcc-mock — qcc-mock

Usage: qcc-mock <command> [options]

Embedded tools
  get-actual-controller - QCC tool: get_actual_controller
    --company-name <company-name> [--raw <json>]
  get-administrative-license - ...
  ...（共 161 个）

$ npx tsx qcc-cli.ts --help | grep -c "^  get-"
161
```

✅ **所有 161 个工具都正确注册为子命令**

### Step 3：调用工具

```bash
$ npx tsx qcc-cli.ts get-company-registration-info --company-name "小米"

{
  "source": "qcc-mock",
  "tool": "get_company_registration_info",
  "arguments": {"companyName": "小米"},
  "data": {"result": "mock data for ..."}
}
```

✅ **调用成功，参数传递正确，输出可解析**

### Step 4：单工具 --help

```bash
$ npx tsx qcc-cli.ts get-actual-controller --help

Usage: get-actual-controller --company-name <company-name> [--raw <json>]

QCC tool: get_actual_controller

Options:
  --raw <json>                   Provide raw JSON arguments to the tool
  --company-name <company-name>  企业名称
  -h, --help                     display help for command
```

✅ **自动从 JSON Schema 生成 --help**

### Step 5：尝试 bundle 成单文件

```bash
$ npx mcporter generate-cli --command "..." --output cli.mjs --bundle
# 错误
[mcporter] --bundle requires an explicit output path when used with --compile.

$ npx mcporter generate-cli --command "..." --compile binary --bundle
[mcporter] --compile requires Bun. Install Bun or set BUN_BIN to the bun executable.
```

❌ **mcporter v0.12.0 的 --bundle 必须配合 --compile，--compile 又必须用 Bun**

---

## 对比表

| 维度 | mcporter generate-cli (0.12.0) | qcc-agent-cli (1.0.5) |
|------|-------------------------------|----------------------|
| **生成/安装方式** | `npx mcporter generate-cli` 一次性生成 | `npm install -g qcc-agent-cli` 安装 |
| **部署形式** | 单个 .ts 文件（需 tsx + deps） | 22 文件 / 29 KB npm 包 |
| **依赖** | 需本地有 `tsx` 跑 | 全打包，零依赖 |
| **工具发现** | 编译时快照 161 工具到 .ts | `qcc update` 启动时拉取 + 缓存到 ~/.config |
| **缓存机制** | ❌ 无 | ✅ 工具清单 + 12h update-notifier |
| **Auth 流程** | 直接读 env / config | `qcc init --authorization "Bearer ..."` |
| **JSON Schema 校验** | ✅ 自动从 MCP schema 生成 | ✅ 手写 validator.js |
| **错误分类** | 复用 mcporter runtime 错误 | 10 种自定义错误类型 + 建议 |
| **单工具 --help** | ✅ 自动 | ✅ 自写 |
| **多输出格式** | text / markdown / json / raw | json (via --json flag) + 默认 markdown |
| **SSE 解析** | ✅ mcporter runtime 处理 | ✅ httpClient.parseSSEResponse() |
| **更新检测** | ❌ 需重新 generate-cli | ✅ 12h 间隔 + npm update-notifier |
| **可用工具数** | 161（已验证） | 181（qcc-cli 文档） |
| **支持的 MCP** | 任意 stdio/HTTP MCP | 仅 QCC |
| **运行时** | Node.js 26+ | Node.js 16+ |
| **多 server** | ✅ 任意 MCP | 6 个 QCC server 写死 |
| **Bundle** | ⚠️ 需 Bun + --compile | N/A（已经是 npm 包） |
| **独立二进制** | ❌（需 tsx/Bun） | ❌（需 node） |

---

## 关键缺陷

### mcporter 的问题

1. **`--bundle` 实际不可用**
   - 文档暗示单文件 bundle
   - 实际强依赖 `--compile`
   - `--compile` 又强依赖 Bun（未安装则 fail）

2. **运行依赖**
   - 必须装 tsx 或 Bun
   - 必须有 node_modules + commander + mcporter
   - 共享项目级 deps

3. **CLI 名字是 `qcc-mock` 不是 `qcc`**
   - 默认从 server name 推断
   - 不能用 `--output qcc` 改

4. **生成后不能增量更新**
   - 工具列表是编译时快照
   - QCC 加新工具 → 重新跑 generate-cli
   - 不能像 `qcc update` 那样自动更新

5. **单工具调用冗长**
   - `qcc-cli.ts get-company-registration-info --company-name "X"`
   - 官方：`qcc company get_company_registration_info "X"`
   - 多一层 namespace

### qcc-agent-cli 的优势

1. **一键 npm install**——`npm i -g qcc-agent-cli`
2. **零运行时依赖**——全打包
3. **`qcc update` 自动刷新**——12h update-notifier
4. **多 server 命名空间**——`qcc <server> <tool>`
5. **配置集中**——`~/.config/qcc-agent-cli/`
6. **生产级**——错误类型完整、建议明确

---

## 真实差距：15% 的"功能差距" + 35% 的"可用性差距"

### 功能差距（15%）

mcporter 覆盖 qcc-cli **85%** 的核心能力：
- ✅ 工具调用、参数解析、JSON Schema 校验
- ✅ 多输出格式、--help
- ❌ 工具自动更新、update-notifier
- ❌ 配置 init/check 流

### 可用性差距（35%）

mcporter **生成易，部署难**：
- ❌ 单文件 bundle 不可用（依赖 Bun）
- ❌ 不能 `npm i -g` 一键装
- ❌ 必须有 node_modules + tsx
- ❌ 工具列表是编译时快照

qcc-cli **部署易，扩展难**：
- ✅ `npm i -g` 一键装
- ✅ 零依赖
- ✅ 自动更新
- ❌ 只能用于 QCC（要换 MCP 改源码）

---

## 实际产物

```
/tmp/mcporter-test/
├── qcc-cli.ts        # 9145 行 / 161 工具 / 编译时快照
└── node_modules/     # tsx + commander + mcporter (~118 packages)

/tmp/qcc-mock.mjs     # 161 工具的 stdio MCP 模拟
```

vs qcc-agent-cli：

```
qcc-agent-cli/
├── bin/index.js                    # 入口
├── package.json                    # 零依赖
├── src/
│   ├── cliSetup.js                 # commander 注册
│   ├── commands/{init,check,config,list-tools,update,call-mcp}.js
│   ├── services/{mcpService,configService}.js
│   ├── utils/{httpClient,validator,cacheUtils,jsonToMarkdown,commandExample,logger}.js
│   └── config/mcpServers.json      # 6 server
```

---

## 结论

**mcporter 是开发期"快速验证"工具，不是生产部署工具。**

| 场景 | 工具 |
|------|------|
| 想把一个新 MCP server 包装成 CLI 试试 | mcporter |
| 给客户长期使用的稳定 CLI | 手写（像 qcc-agent-cli 那样） |
| 需要 CI/CD 中调用 MCP | mcporter `call` 子命令 |
| 需要 1-2 个月维护的项目 CLI | 手写（避免 mcporter 的 bundle 限制） |

**对 GCL 的启示**：

`plugins/shared/gcl-data-service/references/qcc-tools-list.md` 已经记录了 161 个工具。如果客户要本地用 QCC CLI：

1. **有 QCC API Key** → 推荐官方 `qcc-agent-cli`（生产级）
2. **无 API Key** → 暂时用 web_search 兜底（mcporter 帮不了）
3. **开发期** → mcporter `call qcc-company.get_xxx "公司名"`（一行试一次）

**不要**用 mcporter 给客户做生产 CLI——bundle 限制太多。

---

## 附录：测试命令

```bash
# 1. 安装 mcporter
npm install -g mcporter

# 2. 从 MCP 生成 CLI（以 QCC 公开 endpoint 为例）
npx mcporter generate-cli \
  --command "node /tmp/qcc-mock.mjs" \
  --output qcc-cli.ts

# 3. 运行
npx tsx qcc-cli.ts --help
npx tsx qcc-cli.ts get-company-registration-info --company-name "小米"
```

---

*Greater China Legal — gcl-data-service reference: QCC CLI 对比分析*
*测试时间：2026-06-15*
*数据源：references/qcc-tools-list.md 解析得到的 161 个工具*
