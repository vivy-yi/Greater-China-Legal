---
name: contract-review
description: >
  TODO: 待补充 description（YAML 安全的描述）
legal_frame: cn-mainland
last_reviewed: 2026-06-24
version: 1.0.0
risk_level: low
trigger_phrases:
  - contract-review
---

> 合同审核 SKILL · 企查查双模式（CLI + MCP）增强版。
> 通过"仅添加批注"的方式审查合同文本（不修改原文），采用四层审核模型完成合同主体核验 × 内容合规审查双重检验，输出带批注合同 + 合同概要 + 综合审核意见 + 业务流程图。
>
> 四层审核模型：
> - **第一层 · 主体核验**：双模式调用企查查（CLI 终端直连用于快速核验、MCP 用于深度风险穿透），核验合同双方的工商登记状态、法定代表人真实性、登记是否含吊销 / 注销 / 异常等致命信号
> - **第二层 · 基础审核**：合同要件完整性（标题、当事人、主体资格、生效条件、签字盖章等）
> - **第三层 · 商务条款**：标的、数量、价款、付款方式、交付时间、质量标准、违约责任、争议解决等核心商务条款
> - **第四层 · 法律条款**：保密条款、竞业禁止、知识产权归属、不可抗力、责任限制、合同解除条件、法律适用等
>
> 输出物：
> - **带批注合同（.docx）**：通过审核人名称编码风险等级（🔴 高 / 🟡 中 / 🟢 低），每条批注含问题类型 + 风险原因 + 修订建议
> - **合同概要（.docx）**：合同核心要素一图速览
> - **综合审核意见（.docx）**：通过 / 整改 / 拒签 三档结论 + 关键风险清单
> - **业务流程图（Mermaid + PNG 渲染）**：合同执行的关键节点流程可视化
>
> 双模式企业核验：QCC CLI（终端直连，低延迟、高可靠、无需 MCP 配置）用于主体快速核验；QCC MCP（深度分析，34 类司法风险全扫描、AI 关联推理）用于风险穿透预警。
>
> 适用场景：法务团队合同审核 / 律师代理客户的合同审查 / 商务签约前合规预审 / 大宗采购合同事前风控 / 投融资交易文件审查。
>
> 输出语言：自动跟随合同主语言（合同为中文则中文输出，英文则英文输出）。
>
> **风险核查采用「先扫后钻」**：先通过企业风险全量扫描一次性分诊 35 项风险维度、快速定位命中项，再对命中维度深入取证——既不漏维度，也避免逐项无效查询。

---

## 🔍 风险维度扫描 · 先扫后钻（统一规范 · 2026-06-08 · 对齐 A 层铁律 5-A）

> 本 SKILL 凡涉及“一次性排查 ≥ 2 个企业风险维度”（司法风险 / 失信 / 被执行 / 限高 / 经营异常 / 行政处罚 / 破产 / 担保 / 税务 等 qcc-risk 维度），**一律按“先扫后钻”执行，禁止逐个原子风险工具散弹枪式调用**（慢 / 贵 / 多为无效调用）：
>
> 1. **第 1 步 · 分诊（先扫）**：先调 `mcp__qcc-risk__get_company_risk_scan`（企业风险扫描）一次返回企业**自身** 35 项风险维度的命中计数（脱水版：有 / 无 + 条数，不含明细）。
> 2. **第 2 步 · 下钻（后钻）**：仅对 `count > 0` 的维度，调对应原子风险工具取明细（具体工具见本 SKILL 工作流 / 术语对照表）。示例：scan 显示「失信 2、被执行 1、其余 0」→ 只下钻 `mcp__qcc-risk__get_dishonest_info` + `mcp__qcc-risk__get_judgment_debtor_info`。
> 3. **`count = 0` 的维度**：直接判定“无记录”，不再调用该维度原子工具。
> 4. **明确单一维度问句**（仅查某一项，如“有没有失信”）→ 直接调对应原子工具，无需先扫（对应 A 层铁律 5-A 路由 3）。
> 5. scan 只分诊、不出明细；要明细必须下钻原子工具。风险结论只陈述“命中维度 + 计数 / 明细”客观事实，**不替客户判定“能不能合作 / 可不可开户”**。
> 6. 先扫后钻发生在**实体锚定确定唯一主体之后**；简称 / 品牌名仍须先 `mcp__qcc-company__get_company_by_query` 锁定主体，再 scan。
> 7. 本轮**仅**引用已上线的 `get_company_risk_scan`（企业**自身**风险扫描）；企业“自身风险”之外的聚合扫描能力尚未上线（Phase 2），本 SKILL **不得引用任何未上线的聚合风险扫描工具**。
>
> 8. **【定性必须有下钻证据】** 对任一风险维度给出**定性判断**（如“多为原告身份 / 属正常维权”“轻微合规瑕疵”“诉讼活跃度正常”等）之前，必须已下钻该维度的明细工具、拿到支撑数据；未下钻则**只陈述 scan 计数并标注“（未取明细）”**，禁止凭 scan 计数或印象给定性。例：scan 显示「裁判文书 77」但未下钻 `mcp__qcc-risk__get_judicial_documents` → 只能写“裁判文书 77 条（未取明细）”，**不得**写“多为原告身份、属正常维权”；如需该定性，必须先下钻 `get_judicial_documents`（可按 `role` 取原告 / 被告分布）再下结论。

---


## 📖 QCC MCP 术语对照表（强制工具映射）

> **使用约定**：本表列出 SKILL 内业务简写与企查查 MCP 工具的精确映射。AI 执行本 SKILL 时遇到下表"业务简写"列的词汇，**必须调用对应"MCP 工具"列**，禁止使用 web search 或自由文本推测替代。完整规范见 [QCC-MCP-TERMINOLOGY.md](../../QCC-MCP-TERMINOLOGY.md)。

| 业务简写 | 规范全名 | 企查查 MCP 工具 |
| --- | --- | --- |
| 失信 | 失信被执行人 | `mcp__qcc-risk__get_dishonest_info` |
| 被执行 | 被执行人 / 判决债务人 | `mcp__qcc-risk__get_judgment_debtor_info` |
| 限高 | 限制高消费 | `mcp__qcc-risk__get_high_consumption_restriction` |
| 限出境 / 限境 | 限制出境 | `mcp__qcc-risk__get_exit_restriction` |
| 终本 | 终结本次执行案件 | `mcp__qcc-risk__get_terminated_cases` |
| 破产 / 重整 | 破产重整 | `mcp__qcc-risk__get_bankruptcy_reorganization` |
| 经营异常 | 经营异常 | `mcp__qcc-risk__get_business_exception` |
| 严重违法 | 严重违法失信 | `mcp__qcc-risk__get_serious_violation` |
| 行政处罚 / 重大处罚 | 行政处罚 | `mcp__qcc-risk__get_administrative_penalty` |
| 股权冻结 | 股权冻结 | `mcp__qcc-risk__get_equity_freeze` |
| 股权出质 | 股权出质 | `mcp__qcc-risk__get_equity_pledge_info` |
| 欠税 | 欠税公告 | `mcp__qcc-risk__get_tax_arrears_notice` |
| 税务异常 / 税务违法 | 税务异常 / 税收违法 | `mcp__qcc-risk__get_tax_abnormal` / `mcp__qcc-risk__get_tax_violation` |
| 受益所有人 / UBO | 受益所有人 | `mcp__qcc-company__get_beneficial_owners` |
| 实控人 / 实际控制人 | 实际控制人 | `mcp__qcc-company__get_actual_controller` |
| 主要人员 / 董监高 | 主要人员 | `mcp__qcc-company__get_key_personnel` |
| 抽查检查 / 双随机 | 双随机抽查 | `mcp__qcc-operation__get_random_check` |
| 吊销 | （登记状态字段判断）| 调 `mcp__qcc-company__get_company_registration_info` 取"登记状态" |
| 资不抵债 | （资产负债率字段判断）| 调 `mcp__qcc-company__get_financial_data` 判断负债率 > 100% |

---

# 合同审核技能

## 概述

本技能通过**仅添加批注**的方式审查合同（不修改原文）。采用四层审核模型（主体核验、基础审核、商务条款、法律条款），生成：

- 带批注的合同（.docx）
- 合同概要（.docx）
- 综合审核意见（.docx）
- 业务流程图（Mermaid + 渲染图片）

**语言规则：** 检测合同主要语言，所有生成内容（批注、概要、意见、流程图文字）使用该语言输出。参考 **[references/language.md](references/language.md)**。

---

## 企查查企业核验：CLI + MCP 双模式

**🎯 架构原则：CLI 与 MCP 互补使用，发挥各自优势**

| 功能模块 | 推荐工具 | 优势 | 数据来源标注 |
|---------|---------|------|------------|
| **主体信息核验** | QCC CLI（终端直连） | 低延迟、高可靠、无需MCP配置 | 基于企查查 CLI 终端直连获取 |
| **风险穿透预警** | QCC MCP（深度分析） | 18类风险全面扫描、AI深度分析 | 基于企查查 MCP 深度分析 |

### 为什么采用双模式？

- **CLI（终端直连）**：适合主体核验这类标准化查询，响应快、稳定性高
- **MCP（深度分析）**：适合风险穿透这类需要复杂推理的分析，AI增强理解

---

## CLI 配置（推荐用于主体信息核验）

**⚠️ 重要：启用企查查 CLI 企业核验前，确保 CLI 已安装**

### 安装检查：
```bash
# 验证 QCC CLI 是否已安装
qcc --version

# 测试企业信息核验
qcc company get_company_registration_info --searchKey "企查查科技股份有限公司"
```

### 预期输出：
```
正在调用 company/get_company_registration_info...

* 企业名称: 企查查科技股份有限公司
* 统一社会信用代码: 91320594088140947F
* 法定代表人: 陈德强
* 登记状态: 在业
...
```

### CLI 安装（如未安装）：
```bash
# 查看 QCC CLI 安装指南
pip install qcc-cli
# 或从以下地址下载：https://github.com/duhu2000/qcc-cli
```

---

## MCP 配置（用于深度风险分析）

**⚠️ 可选：启用企查查 MCP 进行增强型风险穿透分析**

### 检查清单：
1. ✅ `~/.claude/.mcp.json` 存在且配置正确
2. ✅ `QCC_MCP_API_KEY` 环境变量已设置
3. ✅ Claude Code 已重启以加载 MCP 配置

### 配置步骤：
```bash
# 1. 创建 MCP 配置文件
cat > ~/.claude/.mcp.json << 'EOF'
{
  "mcpServers": {
    "qcc-company": {
      "url": "https://agent.qcc.com/mcp/company/stream",
      "headers": { "Authorization": "Bearer ${QCC_MCP_API_KEY}" }
    },
    "qcc-risk": {
      "url": "https://agent.qcc.com/mcp/risk/stream",
      "headers": { "Authorization": "Bearer ${QCC_MCP_API_KEY}" }
    }
  }
}
EOF

# 2. 设置 API 密钥
export QCC_MCP_API_KEY="your_api_key_here"

# 3. 重启 Claude Code
```

详见：https://github.com/duhu2000/legal-assistant-skills/blob/main/docs/MCP_CONFIGURATION.md

---

## 工作流程

### 执行步骤（必须遵循）

当用户请求合同审核时（如"请审核这份合同"）：

1. **定位合同文件** - 如用户仅提供文件名，在常用目录（~/Downloads、~/.claude/downloads、当前目录）中搜索完整路径
2. **读取合同** 使用可用工具（优先 pandoc，备选直接 XML）- 必须使用第1步中找到的正确完整路径
3. **提取合同主体** 并通过 **QCC CLI**（首选）、**QCC MCP**（备选）或 **Web Search**（最后备选）进行核验
   - **中国企业核验工具优先级：**
     1. **QCC CLI（首选）**：使用 `qcc company get_company_registration_info --searchKey "企业名称"` 进行快速企业核验
        - 如 CLI 返回数据 → 作为权威来源使用
        - 如 CLI 未安装或失败 → 降级到 MCP
     2. **QCC MCP（备选）**：如 CLI 不可用但 MCP 已配置，使用 MCP 工具：
        - `qcc-company/get_company_registration_info` 用于企业核验
        - `qcc-company/get_company_profile` 用于补充信息
        - 如 MCP 返回数据 → 作为权威来源使用
     3. **Web Search（最后备选）**：仅当 CLI 和 MCP 都不可用时使用
   - **数据来源标注**：始终在批注中标注核验来源：
     - CLI 核验 → 标注"基于企查查 CLI 终端直连获取"
     - MCP 核验 → 标注"基于企查查 MCP 服务获取"
     - 风险分析 → 标注"基于企查查 MCP 深度分析"
     - Web Search → 标注"基于公开网络信息查询"
4. **生成所有必需内容**（必须创建以下全部内容）：
   - 合同概要文字 → 作为 `summary_text` 参数传入
   - 综合审核意见文字 → 作为 `opinion_text` 参数传入
   - Mermaid 流程图代码 → 作为 `flowchart_mermaid` 参数传入（可选，如有问题可跳过）
5. **执行工作流程** 通过 `review_contract()` 或 `ContractReviewWorkflow.run_full_workflow()` 并传入所有生成内容：
   ```python
   workflow.run_full_workflow(
       comments=comments,
       output_docx_filename="合同_审核版.docx",
       summary_text=summary_text,      # 合同概要内容
       opinion_text=opinion_text,      # 综合审核意见内容
       flowchart_mermaid=flowchart_mermaid,  # 可选
   )
   ```
   **重要**：不要直接写入文件。让工作流程生成 DOCX 文件。
6. **向用户报告结果** 包含所有输出文件位置

**工作流程生成的输出文件**（DOCX 格式）：
- `{ContractName}_审核版.docx` - 带批注的审核版合同
- `合同概要.docx` - 合同概要（DOCX，非 TXT）
- `综合审核意见.docx` - 综合审核意见（DOCX，非 TXT）
- `business_flowchart.mmd` - Mermaid 源码（可选）
- `审核报告.txt` - 审核报告（TXT 格式）

### 技术步骤

1. 解包合同（.docx）进行 XML 操作
2. 读取合同文字（pandoc 或 XML）
3. 提取并核验合同主体（第0层）
4. 执行三层条款审核（第1-3层）
5. 向文档添加批注
6. 生成合同概要
7. 生成综合审核意见
8. 生成业务流程图并渲染图片
9. 重新打包为 .docx

## 输出命名

- 输出目录：`审核结果：{ContractName}`（中文）或 `Review_Result_{ContractName}`（英文）
- 审核版合同：`{ContractName}_审核版.docx`（中文）或 `{ContractName}_Reviewed.docx`（英文）
- 审核报告：`审核报告.txt`（中文）或 `Review_Report.txt`（英文）

## 批注原则

- **仅添加批注**：不修改原文或格式
- **精确定位**：批注应针对具体条款/段落
- **结构化内容**：每条批注包含问题类型、风险原因和修订建议
- **风险等级**：通过审核人名称携带；**不要**在批注正文中包含"风险等级"行
- **输出语言**：使用合同语言的标签（见 `references/language.md`）

**中文批注示例：**
```
【问题类型】付款条款
【风险原因】第3.2条中合同总金额为10万美元，但第5.1条付款条款中列明100万美元。此不一致可能引起争议。
【修订建议】统一各条款中的总金额，并明确是否含税。
```

## 审核标准

使用四层审核模型和 **[references/checklist.md](references/checklist.md)** 中的详细检查清单。

### 第0层：主体核验（主体真实性）
- 提取所有合同主体（完整法定名称、统一社会信用代码、法定代表人）
- 核验每个主体的注册名称准确性和工商登记状态
- **双模式核验策略：**

#### 步骤1：通过 QCC CLI 进行企业核验（首选）
```bash
# 使用 QCC CLI 进行企业核验（推荐）
qcc company get_company_registration_info --searchKey "企业名称"
```
- **优势**：低延迟、高可靠、无需 MCP 配置
- **使用时机**：所有企业核验任务的首选
- **数据来源标注**："基于企查查 CLI 终端直连获取"
- **失败处理**：如 CLI 未安装或命令失败，自动降级到 MCP

#### 步骤2：通过 QCC MCP 进行企业核验（备选）
如 CLI 不可用但 MCP 已配置，使用 MCP 工具进行企业核验：
- **可用工具**：
  - `qcc-company/get_company_registration_info` - 企业工商信息
  - `qcc-company/get_company_profile` - 企业简介
  - `qcc-company/get_key_personnel` - 主要人员
- **优势**：无需本地 CLI 安装，通过 Claude MCP 集成工作
- **数据来源标注**："基于企查查 MCP 服务获取"

#### 步骤3：通过 QCC MCP 进行风险穿透（增强）
```bash
# 使用 QCC MCP 进行18类深度风险分析（如已配置）
# 需要 QCC_MCP_API_KEY 环境变量
```
- **可用工具**：
  - `qcc-risk/get_dishonest_info` - 失信信息
  - `qcc-risk/get_judgment_debtor_info` - 被执行人
  - `qcc-risk/get_business_exception` - 经营异常
  - ...（共18类）
- **优势**：AI 增强理解、全面风险扫描
- **数据来源标注**："基于企查查 MCP 深度分析"

#### 步骤4：备选方案
1. **MCP（如 CLI 不可用）**：使用 `qcc-company/get_company_registration_info` 进行企业核验
2. **Web Search（最后备选）**：如 CLI 和 MCP 都不可用，使用 Web Search 搜索"[企业名称] 工商登记信息"
3. **人工核验**：对于关键合同，要求对方提供营业执照复印件

#### 在批注中记录来源
始终标注核验来源：
- CLI 核验 → "【数据来源】基于企查查 CLI 终端直连获取"
- MCP 企业核验 → "【数据来源】基于企查查 MCP 服务获取"
- MCP 风险分析 → "【数据来源】基于企查查 MCP 深度分析"
- Web 搜索 → "【数据来源】基于公开网络信息查询"

### 第1层：基础（文字质量）
- 数字、日期、术语准确性
- 编号和引用一致性
- 清晰明确无歧义
- 格式和标点质量

### 第2层：商务条款
- 范围、交付物、数量/规格
- 价格和付款计划
- 交付/验收程序
- 权利/义务和履约保证

### 第3层：法律条款
- 生效和期限/终止
- 责任/处罚和救济
- 争议解决和适用法律
- 保密、不可抗力、知识产权、通知、授权

**风险等级（通过审核人名称编码）：**
- 🔴 高风险：核心业务歧义（价格、范围、权利/义务）
- 🟡 中风险：重要但非核心歧义
- 🔵 低风险：实际影响极小

## 合同概要

以合同语言生成结构化、客观的概要。
- 参考 **[references/summary.md](references/summary.md)**（英文模板）
- 使用 **[references/language.md](references/language.md)** 进行语言选择和中文标签

输出文件：`合同概要.docx`（中文）或 `Contract_Summary.docx`（英文）（默认字体：仿宋；如语言需要请调整）

## 综合审核意见

以合同语言为业务团队生成简洁的两段式回复。
- 参考 **[references/opinion.md](references/opinion.md)**

输出文件：`综合审核意见.docx`（中文）或 `Consolidated_Opinion.docx`（英文）（默认字体：仿宋；如语言需要请调整）

## 业务流程图（Mermaid）

按要求生成 Mermaid 流程图并渲染为图片。
- 参考 **[references/flowchart.md](references/flowchart.md)**

**实现：** 从 `scripts/mermaid_renderer.py` 调用 `render_mermaid_code()`。本技能将：
1. 将 Mermaid 代码写入 `.mmd` 文件
2. 使用 `mmdc`（mermaid-cli）渲染为 PNG 图片
3. 如未安装 `mmdc`，仅生成 `.mmd` 文件（无图片）

**不要**使用 matplotlib 或其他 Python 库渲染流程图。

输出：
- `business_flowchart.mmd`
- `business_flowchart.png`（如 mmdc 可用）

## 技术说明

核心工作流程：
1. 解包 → 2. 企业核验 → 3. 添加批注 → 4. 概要 → 5. 意见 → 6. 流程图 → 7. 重新打包

API 和实现细节：
- **[references/technical.md](references/technical.md)**

## 企业核验设置（CLI + MCP 双模式）

本技能支持**双模式企业核验**：
- **QCC CLI**：终端直连用于企业核验（低延迟、高可靠）
- **QCC MCP**：模型上下文协议用于深度风险分析（AI增强、全面）

### 第1层：QCC CLI 设置（企业核验必需）

**推荐给所有用户 - 提供最快最可靠的企业核验。**

#### 安装
```bash
# 安装 QCC CLI
pip install qcc-cli

# 验证安装
qcc --version

# 使用真实公司测试
qcc company get_company_registration_info --searchKey "企查查科技股份有限公司"
```

#### 可用 CLI 工具
| 工具 | 用途 | 示例 |
|------|------|------|
| `qcc company get_company_registration_info` | 企业核验 | `qcc company get_company_registration_info --searchKey "XXX公司"` |
| `qcc company get_shareholder_info` | 股东信息 | `qcc company get_shareholder_info --searchKey "XXX公司"` |
| `qcc company get_key_personnel` | 主要人员 | `qcc company get_key_personnel --searchKey "XXX公司"` |

#### CLI 输出示例
```
正在调用 company/get_company_registration_info...

* 企业名称: 企查查科技股份有限公司
* 统一社会信用代码: 91320594088140947F
* 法定代表人: 陈德强
* 登记状态: 在业
* 注册资本: 36225万元
* 成立日期: 2014-03-12
...
```

### 第2层：QCC MCP 设置（深度风险分析可选）

**启用以增强18类风险穿透分析。**

#### 功能
启用 QCC MCP 后，本技能自动：
- 执行18类深度风险扫描（失信记录、被执行、经营异常、税务违规、破产等）
- AI 增强的风险理解和上下文分析
- 生成综合风险评估报告

#### 设置步骤
1. **申请 QCC MCP API 密钥**
   - 访问 [企查查 MCP 门户](https://agent.qcc.com) 申请访问权限
   - 获取您的 API 密钥

2. **设置环境变量**
   ```bash
   export QCC_MCP_API_KEY="your_api_key_here"
   ```

3. **配置 MCP 服务器**
   ```bash
   cat > ~/.claude/.mcp.json << 'EOF'
   {
     "mcpServers": {
       "qcc-company": {
         "url": "https://agent.qcc.com/mcp/company/stream",
         "headers": { "Authorization": "Bearer ${QCC_MCP_API_KEY}" }
       },
       "qcc-risk": {
         "url": "https://agent.qcc.com/mcp/risk/stream",
         "headers": { "Authorization": "Bearer ${QCC_MCP_API_KEY}" }
       }
     }
   }
   EOF
   ```

4. **验证设置**
   ```bash
   python -c "from scripts.qcc_mcp_client import QccMcpClient; c = QccMcpClient(); print('✅ MCP 已启用' if c.is_enabled() else '❌ MCP 未启用')"
   ```

### 双模式行为矩阵

| 场景 | 企业核验 | 风险分析 | 数据来源标注 |
|------|---------|---------|------------|
| CLI ✅ MCP ✅ | CLI（首选） | MCP（增强） | CLI: "基于企查查 CLI 终端直连获取" / Risk: "基于企查查 MCP 深度分析" |
| CLI ✅ MCP ❌ | CLI | Web Search 备选 | CLI: "基于企查查 CLI 终端直连获取" |
| CLI ❌ MCP ✅ | **MCP（备选）** | MCP | **MCP: "基于企查查 MCP 服务获取"** / Risk: "基于企查查 MCP 深度分析" |
| CLI ❌ MCP ❌ | Web Search | Web Search | "基于公开网络信息查询" |

### 批注模板示例

#### CLI 企业核验（正常）
```
【问题类型】主体信息核实
【核实结果】经企查查 CLI 终端直连获取：
  - 企业全称：XXX科技有限公司
  - 法定代表人：张三
  - 统一社会信用代码：91350100M0001XXXXX
  - 登记状态：存续（在业）
【核实结论】企业工商信息正常。
【修订建议】建议核实签署人授权情况。
```
**审核人**: 🟡 中风险-主体核验

#### MCP 风险穿透（发现高风险）
```
【问题类型】主体司法执行风险
【风险企业】XXX建设有限公司
【风险原因】基于企查查 MCP 深度分析，发现该企业存在以下高风险事项：
  1. 失信信息（老赖）
  2. 被执行人（金额500万元）
  3. 限制高消费
【法律后果】上述风险可能导致企业履约能力严重受限。
【修订建议】🔴 建议立即终止合作谈判或要求提供担保。
```
**审核人**: 🔴 高风险-司法执行


## 依赖

- Python 3.9+（推荐 3.10+）
- pandoc（系统安装）
- defusedxml
- Mermaid CLI（`mmdc`）用于渲染
- python-docx 用于富文本输出
- requests（用于 QCC MCP API 调用，可选）

## 故障排除（简要）

### 文档问题
- **Word 中批注缺失**：运行 `doc.verify_comments()` 并重新保存
- **find_paragraph 失败**：缩短搜索文字；确认实际段落文字
- **Mermaid 渲染失败**：确保 `mmdc` 已安装；使用 Chrome 路径或 Puppeteer 配置

### CLI 问题
- **QCC CLI 未找到**：使用 `qcc --version` 验证安装；使用 `pip install qcc-cli` 重新安装
- **CLI 命令失败**：检查网络连接；验证 API 密钥权限
- **CLI 输出为空**：公司名称可能需要完全匹配；尝试使用完整法定名称

### MCP 问题
- **QCC MCP 不工作**：验证 `QCC_MCP_API_KEY` 是否已设置；检查到 https://agent.qcc.com 的网络连接
- **MCP 工具未加载**：配置 `.mcp.json` 后重启 Claude Code

## 示例

参考 **[references/examples.md](references/examples.md)** 获取完整工作流程示例。

## 重要规则

1. 绝不修改合同原文
2. 企业核验（第0层）必须在条款审核（第1-3层）之前完成
3. 审核所有四层，不要跳过项目
4. 确保风险等级准确一致
5. 保持批注精确、专业、可操作
6. 流程图必须严格来自合同文字
7. 概要仅客观描述，不含风险分析
8. 意见仅反映已识别的发现

## 许可证

SPDX-License-Identifier: Apache-2.0

Copyright (c) 2026 JiCheng

Licensed under the Apache License, Version 2.0. See repository root `LICENSE`.

---

## 报告输出纪律（内部规则 · 严禁出现在最终报告中）

1. **一律业务语言**：报告正文、备注、数据来源说明中不得出现 MCP 工具代码名（`get_xxx` / `mcp__qcc-xxx`）、server 名（qcc-company 等）、schema / manifest / 字段名等技术词；数据来源统一用业务表述（如"企查查工商登记数据 / 企查查风险信息数据 / 企查查财务数据"）。"企查查 MCP"作为对外产品名仅允许出现在「数据来源」固定句式中。
2. **禁止内部用语**：SKILL / SKILL.md / V1.0 / V2.0 / 增强版 / 新能力 / 维度编号 / 评级引擎规则等开发概念不得出现在报告中；「Decision Pack」一律写「决策摘要」。
3. **禁止执行过程独白**：不输出"我将按照…/第一步获取…/已锁定主体/接下来…"等过程描述，直接输出报告正文。
4. **禁止运行时状态泄漏**：积分余额、配额、调用受限、超时重试、在线体验版本等不得写入报告；某维度数据未获取时统一写"本次未核验 / 未发现公开记录"。
5. **数据零推算**：只引用工具返回的原始数字；禁止自行加总、相减、加权、估算（含"推算 / 估算值"字样）；工具未返回的字段留空或写"未披露"，不得编造。
6. 本节及全部内部执行规则只约束 AI 行为，严禁以任何形式抄入报告。
