---
name: matter-briefing
description: |
  matter-briefing相关法律辅助。
  适用情形：用户提及matter-briefing相关事项。
argument-hint: "[关键信息]"
legal_frame: cn-mainland
trigger_phrases:
  - 'matter-briefing'
  - 'litigation_support'
legal_sources:
  - name: '中华人民共和国民事诉讼法'
    effective_date: '2023-01-01'
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

## 数据源与判断框架引用

本 skill 引用以下 plugin 根级 references：

- **判断框架**：`../../references/判断框架.md`（诉讼全流程 35 skill + 14 类时效 + 案由分析 + 管辖判断 + 证据规则 + 保全 + 强制措施 + 执行 + 行政复议/诉讼 + 案件管理 + 上诉 + 刑事案件 + 政府合同）
- **数据源清单**：`../../references/数据源清单.md`（[YD]/[WKL]/[GOV]/[BD]/[model] + 最高法司法解释 + 法院体系 + 仲裁机构 + 知产法院 + 涉外）
- **查询路径**：`../../references/查询路径.md`（法规 + 案例 + 司法解释）
- **货币触发主题**：`../../../references/currency-watch.md`
- **数据源注册表**：`../../../references/data-source-registry.md`

来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）详见 `../../references/数据源清单.md` §十一。
诉讼时效详见 `../../references/判断框架.md` §三（**时效管理是高风险点**）。

# /matter-briefing

1. 读取用户提供的信息。
2. 提取关键事实和法律要素。
3. 按工作流程分析。
4. 输出结构化建议。
5. 升级决策门。

---

# matter-briefing

## 目的

[说明本技能的目的和功能]

## 法域假设

默认中国大陆法域 `[SME 核查]`。

## 加载信息

- [用户提供的相关信息]

## 工作流程

### 第一步：提取关键信息

- **信息项1**：[___]
- **信息项2**：[___]

### 第二步：分析

[分析逻辑和指引]

### 第三步：升级决策门

> "这是辅助分析，不构成法律意见。建议在采取法律行动前由专业律师审核。"

## 输出格式

```
# [标题]

## 关键信息
| 要素 | 内容 |
|------|------|
| [___] | [___] |

## 分析
[结构化分析内容]

## 建议后续行动
- [ ] [___]
```

## 本技能不涵盖

- **代理诉讼或仲裁**
- **确认法律效力** — 所有结论标注 `[SME 核查]`
