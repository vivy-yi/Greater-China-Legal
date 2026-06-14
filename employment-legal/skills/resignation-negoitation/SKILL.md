---
name: resignation-negoitation
# ⚠️ DEPRECATED: 拼写错误，请使用 resignation-negotiation（标准拼写）
#
# 本 skill 已废弃，仅为历史兼容保留。请使用 resignation-negotiation。
description: |
  【已废弃】原 resignation-negotiation 的 typo 版本。请使用 resignation-negotiation。
  本 skill 已废弃，仅为历史兼容保留。功能请使用 resignation-negotiation。
  适用情形：用户提及resignation negoitation相关事项。
argument-hint: "[核心事实]"
legal_frame: cn-mainland
trigger_phrases:
  - 'resignation-negoitation'
  - 'employment_legal'
legal_sources:
  - name: '中华人民共和国劳动合同法'
    effective_date: '2012-12-28'
  - name: '工伤保险条例'
    effective_date: '2010-12-20'
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

## 数据源与判断框架引用

本 skill 引用以下 plugin 根级 references 与 CLAUDE.md：

- **判断框架**：`../../references/判断框架.md`（跨 skill 决策路由 + 5 节点判断 + 解除子流程）
- **数据源清单**：`../../references/数据源清单.md`（[YD]/[WKL]/[GOV]/[BD]/[model] 标注规则 + 路由优先级）
- **查询路径**：`../../references/查询路径.md`（法规/案例/地方数据实际检索入口）
- **CLAUDE.md**：`../../CLAUDE.md`（核心法规 + 高风险情形 + 各省市差异 + 计算框架）
- **货币触发主题**：`../../../references/currency-watch.md`（高频更新主题清单）
- **数据源注册表**：`../../../references/data-source-registry.md`（GCL 全局数据源治理）

来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）详见 `../../references/数据源清单.md` §六。

# /resignation-negoitation

1. 读取用户提供的信息。
2. 提取关键法律要素。
3. 分析问题类型和适用法律。
4. 输出结构化建议。
5. 升级决策门。

---

# resignation negoitation

## 目的

[说明本技能目的]

## 法域假设

默认中国大陆法域，适用《劳动合同法》和相关法规 `[SME 核查]`。

## 加载信息

- [用户提供的相关信息]

## 工作流程

### 第一步：信息提取

| 信息项 | 内容 |
|--------|------|
| 当事人角色 | 用人单位/员工 |
| 核心问题 | [___] |
| 金额/时间 | [___] |

### 第二步：法律分析 `[SME 核查]`

- **适用法条**：[___]
- **构成要件**：[___]
- **分析结论**：[___]

### 第三步：策略建议

- **建议路径**：[___]
- **风险提示**：[___]

### 第四步：升级决策门

> "这是辅助分析，不构成法律意见。劳动争议须先经过劳动仲裁，建议委托劳动法律师代理。"

## 输出格式

```
# [标题]

## 基本信息
| 要素 | 内容 |
|------|------|
| 当事人角色 | [___] |
| 核心问题 | [___] |

## 法律分析 `[SME 核查]`
- 适用法条：[___]
- 分析结论：[___]

## 策略建议
- [___]

## 建议后续行动
- [ ] [___]
- [ ] 律师代理劳动仲裁 `[SME 核查]`
```

## 本技能不涵盖

- **代理劳动仲裁或诉讼**
- **确认法律效力** — 须由仲裁委或法院确认 `[SME 核查]`
