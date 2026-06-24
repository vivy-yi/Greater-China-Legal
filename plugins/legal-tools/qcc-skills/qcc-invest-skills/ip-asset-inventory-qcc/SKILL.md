---
name: ip-asset-inventory-qcc
description: >
  TODO: 待补充 description（YAML 安全的描述）
legal_frame: cn-mainland
last_reviewed: 2026-06-24
version: 1.0.0
risk_level: low
trigger_phrases:
  - ip-asset-inventory-qcc
---

> 知产资产清单 SKILL · 企查查 MCP V2.0 增强版。
> 科技企业投资、并购、IPO 申报前的知识产权资产核查工具，输出"S/A/B/C"四档 IP 资产评级。
>
> 核心能力：
> - **专利清单 + 发明占比**（`mcp__qcc-ipr__get_patent_info`）—— 发明 / 实用新型 / 外观三类计数 + 发明授权率
> - **商标清单 + 国际分类覆盖**（`mcp__qcc-ipr__get_trademark_info`）—— 主品牌 + 子品牌 + 防御性商标矩阵 + 45 类覆盖度
> - **软件著作权 + 作品著作权**（`mcp__qcc-ipr__get_software_copyright_info` + `get_copyright_work_info`）—— 核心代码 + 视觉设计资产确权
> - **V2.0 知产出质**（`mcp__qcc-ipr__get_ipr_pledge`）—— 识别已被质押融资的 IP，无形资产负担清查
> - **V2.0 历史专利 / 商标轨迹**（`mcp__qcc-history__get_historical_patent` + `get_historical_trademark`）—— 已失效 / 已转让 IP 识别"流失型"主体
> - **网络服务备案**（`mcp__qcc-ipr__get_internet_service_info`）—— ICP / APP / 小程序 / 算法备案完整性
> - **技术标准参与**（`mcp__qcc-ipr__get_standard_info`）—— 国标 / 行标 / 团标参编度反映行业话语权
>
> 适用场景：科技型企业投前 DD / 并购前 IP 尽调 / IPO 申报知产资产披露 / 高新技术企业资质复核 / 知识产权融资抵押前估值。
>
> 使用方式：/ip-asset-inventory 企业名称 [--format md|docx|pptx]

**命令**：`/ip-asset-inventory` · **MCP 工具集**：`qcc-company, qcc-risk, qcc-history, qcc-executive, qcc-operation, qcc-ipr`

---

# 知产资产清单 · 企查查 MCP V2.0 增强版

## SKILL 定位

科技企业 IP 资产核查工具。V2.0 新增知产出质 + 历史专利/商标两层能力，识别已被质押融资或已退出的 IP。

## 工作流维度

1. 专利清单（qcc-ipr get_patent_info）+ 发明占比
2. 商标清单（get_trademark_info）+ 核心分类
3. 软件著作权（get_software_copyright_info）
4. 作品著作权（get_copyright_work_info）
5. **V2.0 新工具：知产出质**（get_ipr_pledge —— 无形资产是否已抵押融资）
6. **V2.0 新能力：历史专利 / 商标**（qcc-history —— 已失效 / 已转让的 IP 轨迹）
7. 技术标准参与（get_standard_info —— 行业影响力）

## 评级

IP 资产评级 S/A/B/C



## MCP 依赖

- 必选：qcc-company / qcc-risk
- V2.0 强烈建议：qcc-history（历史追溯）/ qcc-executive（法代画像）/ qcc-operation（经营活跃度）

## 输出模板

- 章节 1：决策摘要（评级 + 关键判断 + 推荐 Action）
- 章节 2：数据来源
- 章节 3-6：各维度扫描结果（详见上文）
- 章节 7：V2.0 能力增量说明
- 章节 8：综合评级 × 处置建议

## 参数

- `--format md|docx|pptx`：输出格式，默认 md

## 边界与免责

本 SKILL 基于企查查 MCP V2.0 公开数据生成。特定法律场景（如商标近似性的最终判定 / 劳动仲裁的实体审查）需配合专业律师做实质审查。


**SKILL 版本**：v2.0 | **适配 MCP 版本**：146 工具 / 6 Server 全量

---

## 报告输出纪律（内部规则 · 严禁出现在最终报告中）

1. **一律业务语言**：报告正文、备注、数据来源说明中不得出现 MCP 工具代码名（`get_xxx` / `mcp__qcc-xxx`）、server 名（qcc-company 等）、schema / manifest / 字段名等技术词；数据来源统一用业务表述（如"企查查工商登记数据 / 企查查风险信息数据 / 企查查财务数据"）。"企查查 MCP"作为对外产品名仅允许出现在「数据来源」固定句式中。
2. **禁止内部用语**：SKILL / SKILL.md / V1.0 / V2.0 / 增强版 / 新能力 / 维度编号 / 评级引擎规则等开发概念不得出现在报告中；「Decision Pack」一律写「决策摘要」。
3. **禁止执行过程独白**：不输出"我将按照…/第一步获取…/已锁定主体/接下来…"等过程描述，直接输出报告正文。
4. **禁止运行时状态泄漏**：积分余额、配额、调用受限、超时重试、在线体验版本等不得写入报告；某维度数据未获取时统一写"本次未核验 / 未发现公开记录"。
5. **数据零推算**：只引用工具返回的原始数字；禁止自行加总、相减、加权、估算（含"推算 / 估算值"字样）；工具未返回的字段留空或写"未披露"，不得编造。
6. 本节及全部内部执行规则只约束 AI 行为，严禁以任何形式抄入报告。
