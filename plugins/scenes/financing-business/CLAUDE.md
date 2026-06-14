---
name: financing-business
description: |
  financing business法律服务场景。
last_reviewed: 2026-06
version: 1.0.0
upgrade_threshold: 涉及金融犯罪/刑事风险立即移交专业律师
---


> 🚀 **首次使用？** 运行 `cold-start-interview`（位于 `plugins/shared/cold-start-interview`）完成场景配置。如 CLAUDE.md 中存在 `[填空]` 标记，先配置再使用 skill。

# Financing Business

## Who's using this

**Role:** [律师 / 法务人员 / 业务部门（非法律背景，有律师支持）/ 业务部门（无律师支持）]
**Attorney contact:** [填空]

**工作成果头部标记：**
- 律师/法务人员 → `Privileged & Confidential — Attorney Work Product`
- 非法务（有律师支持）→ `Research Notes — Not Legal Advice — Review With Attorney Before Acting`
- 非法务（无律师支持）→ `General Information — Not Legal Advice — Consult A Licensed Attorney`

在产出工作成果前，必须先检查 Role 字段。如果 Role 为 `[填空]`，要求用户先设置角色。

---

## 公司基本信息

**公司名称：** [填空]
**融资业务类型：** [填空：保理/融资租赁/供应链金融/资产证券化/其他]
**监管状态：** [填空：已持牌/申请中/无牌]
**外部律师：** [填空]

---

## 数据源配置

| 优先级 | 数据源 | 用途 |
|--------|--------|------|
| 1 | yuandian MCP | 融资法规/监管规定 |
| 2 | 金融监管总局官网 | 融资业务监管政策 |
| 3 | web_search | 备用查询 |

### 降级规则

| 数据源 | 不可用时的降级 |
|--------|-------------|
| yuandian MCP | web_search 搜索"[法规] [关键词]" |
| 两者均不可用 | 明确告知用户，使用法律推理 |

---

## 风险等级

| 风险等级 | 条件 | 处理方式 |
|---------|------|---------|
| 🔴 HIGH | 无牌经营/违规融资/资金链断裂 | 强制外部律师审核 |
| ⚠️ MEDIUM | 合规差距/合同风险 | 建议审核 |
| ✅ LOW | 持牌经营/标准化业务 | 快速处理 |

---

## 输出格式

### 工作成果头部

```
═══════════════════════════════════════
融资业务合规分析备忘录
═══════════════════════════════════════
公司名称：[自动填写]
业务类型：[融资业务类型]
日期：[自动填写]
风险等级：[HIGH/MEDIUM/LOW]
═══════════════════════════════════════
```

在使用工作成果头部前，检查 `## Who's using this` 的 Role 字段，按相应角色添加 privilege 标记。

---

## 升级决策门

出现以下情形，立即升级至专业律师：
- 涉嫌非法吸收公众存款/非法集资
- 涉及金融犯罪（洗钱/诈骗）
- 面临吊销执照风险
- 涉及跨境融资

---

## 核心能力

## 推理原子能力
## 推理原子能力调用流程

本场景的工作流程中，按以下顺序调用 `legal-atomic` 原子能力：

| 顺序 | 原子 Skill | 调用时机 |
|------|-----------|---------|
| 0 | `legal-element-extraction` | 收到用户输入后立即调用，将非结构化叙述转化为结构化法律事实 |
| 1 | `legal-norm-validity-check` | 在任何法条引用前调用，验证法条是否现行有效 |
| 2 | `deductive-reasoning` | 在分析阶段，将待判断的问题转化为 P-F-C 三段论格式 |
| 3 | `conflict-resolution` | 发现多个法条或请求权可能竞合时调用 |
| 4 | `evidence-argument-chain` | 需要组织证据与主张对应关系时调用 |
| 5 | `argument-strength-evaluation` | 输出结论前，标注论证强度（强/中/弱/存疑） |
| 6 | `legal-risk-assessment` | 在风险分级判断时调用 |
| 7 | `case-retrieval` | 需要检索类案时调用 |

### 追问规则（关键）

legal-element-extraction 的输出包含 `## 待补充事实` 节。如果该节非空：

1. **暂停当前分析流程**
2. 向用户逐一提问待补充事实，例如：
   > "请问合同中关于[知识产权归属/数据存储位置/价格调整机制]的条款是什么？这会影响后续判断。"
3. 用户补充后，**回到 Step 0 重新执行 legal-element-extraction**，将新信息并入结构化事实
4. 当待补充事实清空后，继续后续分析

**不得在待补充事实未清空的情况下输出最终结论。** 缺失关键事实的结论标注为「推定结论，须在事实补全后复核」。

| 顺序 | 原子 Skill | 调用时机 |
|------|-----------|---------|
| 0 | `legal-element-extraction` | 收到用户输入后立即调用，将非结构化叙述转化为结构化法律事实 |
| 1 | `legal-norm-validity-check` | 在任何法条引用前调用，验证法条是否现行有效 |
| 2 | `deductive-reasoning` | 在分析阶段，将待判断的问题转化为 P-F-C 三段论格式 |
| 3 | `conflict-resolution` | 发现多个法条或请求权可能竞合时调用 |
| 4 | `evidence-argument-chain` | 需要组织证据与主张对应关系时调用 |
| 5 | `argument-strength-evaluation` | 输出结论前，标注论证强度（强/中/弱/存疑） |
| 6 | `legal-risk-assessment` | 在风险分级判断时调用 |
| 7 | `case-retrieval` | 需要检索类案时调用 |

每个 scene skill 的工作流程第一步应为「法律要素提取」，最后一步前应为「论证强度评估」。


本场景在执行 legal analysis 时，按需调用以下 `legal-atomic` 原子 skill：

| 原子 Skill | 用途 | 调用时机 |
|-----------|------|---------|
| `legal-element-extraction` | 法律要素提取 | 所有输入预处理——将非结构化叙述转化为法律事实 |
| `legal-norm-validity-check` | 法条效力核查 | 引用法条前验证是否现行有效 |
| `legal-risk-assessment` | 法律风险评估 | 涉及风险分级判断时 |
| `conflict-resolution` | 法条竞合/冲突解决 | 多个法条或请求权竞合时 |
| `deductive-reasoning` | P-F-C三段论推理 | 构建法律推理链时 |
| `case-retrieval` | 类案检索方法论 | 需要检索类案时 |
| `structured-element-extraction` | 结构化要素提取 | 处理结构化数据时 |