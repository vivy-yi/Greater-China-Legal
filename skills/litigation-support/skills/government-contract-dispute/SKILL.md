---
name: government-contract-dispute
description: |
  government-contract-dispute相关法律辅助。
  适用情形：用户提及government-contract-dispute相关事项。
argument-hint: "[关键信息]"
legal_frame: cn-mainland
trigger_phrases:
  - 'government-contract-dispute'
  - 'litigation_support'
legal_sources:
  - name: '中华人民共和国民事诉讼法'
    effective_date: '2023-01-01'
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /government-contract-dispute

1. 读取用户提供的信息。
2. 提取关键事实和法律要素。
3. 按工作流程分析。
4. 输出结构化建议。
5. 升级决策门。

---

# government-contract-dispute

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
