---
name: tabular-review
description: '表格化批量审查——每个文档一行，每个数据点一列，每格注明来源。 适用于M&A尽调（"审查200份合同中的控制权变更/转让/ MAC条款"）
  或任何需要批量比对文档的审查。适用情形：用户说"表格审查"、 "审查表格"、"从这些合同提取字段"、"批量比对"。

  '
argument-hint: '[--schema <file> --docs <folder> --output <xlsx|csv>]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
trigger_phrases:
- 表格审查
- 合规表
legal_sources:
- name: 中华人民共和国民法典
  effective_date: '2021-01-01'
---

## 数据源与判断框架引用

本 skill 引用以下 plugin 根级 references：

- **判断框架**：`../../references/判断框架.md`（公司全生命周期 + 治理主题 + 公司类型判断 + 股权设计 + ESOP + 融资 + 董监高 + 股权转让 + 关联交易 + VIE + ODI + 收购 + 少数股东保护 + 利润分配）
- **数据源清单**：`../../references/数据源清单.md`（[YD]/[WKL]/[GOV]/[BD]/[model] + 市场监管总局/证监会/交易所 + 公司法司法解释 + 上市公司治理准则 + VIE 监管 + ODI 监管）
- **查询路径**：`../../references/查询路径.md`（工商登记 + 司法解释 + 案例库）
- **货币触发主题**：`../../../references/currency-watch.md`
- **数据源注册表**：`../../../references/data-source-registry.md`

来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）详见 `../../references/数据源清单.md` §九。
公司类型判断与股权设计详见 `../../references/判断框架.md` §三/§四。

# /tabular-review — China Mainland

## Purpose

有一堆文档，需要对每份文档回答同样的问题。一份尽调清单。一个供应商合同审计。一个租赁 portfolio 审查。输出是一张表：文档为行，数据点为列，每个格子可追溯到原文。

这不是发现问题。`diligence-issue-extraction` 从2000份文档里找出30个问题。本技能回答关于所有2000份文档的同样15个问题。

本技能输出的每个格子都是**线索，需要人工验证**，不是结论。

---

## 工作流程

### Step 1: 确定文档和列

确认：哪些文档、哪些列、输出到哪里。

### Step 2: 建立列类型体系

每个列有一个**类型**，约束答案格式：

| 类型 | 返回内容 | 适用于 |
|---|---|---|
| `verbatim` | 原文引用，逐字照抄 | 定义词、操作条款原文、任何措辞重要的内容 |
| `classify` | 固定列表中的一个值 | Yes/No、在场/缺席、条款变体 |
| `date` | ISO日期 | 生效日期、到期日、终止通知截止日 |
| `duration` | 数字+单位 | 期限长度、通知期、存续期 |
| `currency` | 数字+币种（CNY/USD/EUR）| 上限、门槛、费用、交易金额 |
| `number` | 纯数字 | 计数、百分比、页码 |
| `free` | 短段自由文本 | 尽量少用——这个类型容易漂移 |

### Step 3: 抽样运行（3-5份文档）

先对3-5份文档运行，调整schema，确认格式正确。

### Step 4: 批量执行

一个子Agent并行处理一份文档。每格：值 + 状态 + 原文引用 + 位置。

### Step 5: 规范化检查

标记异常值和不一致项。

### Step 6: 输出

- `.xlsx` 或 `.csv`（中文编码：UTF-8 with BOM）
- `_sources.csv`（每格的原文来源）
- Markdown格式总是输出

---

## CN特定注意事项

### 货币格式

```python
# CN格式
"¥1,000,000" 或 "CNY 1,000,000"
# 不用 "$1,000,000"
```

### 日期格式

```python
# CN格式
"2025-01-15" 或 "2025年01月15日"
# 不用 "01/15/25" 或 "Jan 15, 2025"
```

### 合同期限

CN劳动合同：无固定期限合同须连续工作满10年或连续两次订立定期合同。尽调时注意区分。

---

## CN常用审查列（参考）

| 列名 | 类型 | 说明 |
|---|---|---|
| 合同名称 | free | 合同全称 |
| 合同编号 | free | 内部编号 |
| 合同相对方 | classify | 客户/供应商/合作伙伴 |
| 合同类型 | classify | 采购/销售/租赁/服务/劳动合同 |
| 签署日期 | date | 格式：YYYY-MM-DD |
| 到期日 | date | 格式：YYYY-MM-DD |
| 自动续期 | classify | 是/否/待确认 |
| 年合同金额 | currency | 格式：¥X,XXX,XXX |
| 控制权变更条款 | classify | 有/无/待确认 |
| 转让限制条款 | classify | 有/无/待确认 |
| 合同主体变更 | classify | 须通知/须同意/无限制 |
| 争议解决方式 | classify | 诉讼/仲裁/协商 |
| 适用法律 | classify | 中国法律/其他 |
| 违约金条款 | verbatim | 引用原文 |
| 备注 | free | 风险提示或特殊情况 |

---

## 输出格式示例

```markdown
## 合同批量审查报告——[项目名称]

**审查日期：** YYYY-MM-DD
**审查文档数：** N份
**审查人：** [姓名]

### 统计摘要

| 状态 | 数量 |
|---|---|
| 已审查 | X |
| 有控制权变更条款 | X |
| 有转让限制条款 | X |
| 须取得同意 | X |
| 待确认 | X |

### 关键发现

**高风险（🔴）：**
- [合同名称]：[控制权变更条款描述] — [风险说明]

**中风险（🟠）：**
- [合同名称]：[转让限制条款描述] — [风险说明]

### 验证工作量

| 列名 | not_found | unclear | needs_review |
|---|---|---|---|
| 控制权变更条款 | X | X | X |
| 转让限制条款 | X | X | X |
| ... | ... | ... | ... |

**输出文件：**
- `审查报告_YYYYMMDD.xlsx`
- `审查报告_YYYYMMDD_sources.csv`
- `审查报告_YYYYMMDD.md`
```

---

## 本技能不做什么

- 不代替人工阅读。只提供结构化线索。
- 不出具法律意见。只描述现象。
- 不保证数据完整性。请人工核实每格内容。

---

*Greater China Legal — corporate-legal tabular-review CN adapter v1.0.0*
*基于 anthropic/claude-for-legal tabular-review 适配中国大陆批量合同审查环境*

*[YD] — 基于 anthropic/claude-for-legal 适配中国大陆法律环境 v1.0.0*
