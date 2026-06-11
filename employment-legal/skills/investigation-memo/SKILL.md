---
name: investigation-memo
description: >
  从调查日志起草或更新保密调查报告。适用情形：调查已有足够信息起草第一份报告，
  或新数据添加后需要更新现有草稿。
argument-hint: "[事项名称]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
user_invocable: true
legal_sources:
  - type: statute
    name: Labor Contract Law of the PRC
    article: Article 39 (Employer's right to dissolve)
    effective_date: 2012-07-01
    jurisdiction: cn-mainland
risk_level: medium
escalation_triggers:
  - 调查报告涉及高管（须上报董事会/监事会）
  - 发现刑事犯罪线索（须评估是否向公安机关报案）
---

# /investigation-memo

从调查日志起草或更新保密调查报告。

## 工作流程

1. 加载 `internal-investigation` 参考 Skill，执行 Mode 4（起草/更新报告）
2. 首次起草时，如高优先级来源仍为开放状态，先警告
3. 如为更新，先显示变更内容再重写
4. 所有输出均标注：保密且机密 — 律师工作成果

---

## 使用说明

**管辖法域默认为中国大陆。** 如涉及香港/澳门/台湾/新加坡：
`/employment-legal:investigation-memo --frame hk`

---

## ⚠️ 中国大陆法律环境说明

在中国大陆法律环境下：
- 律师与当事人之间的通信特权并非法定特权
- 劳动仲裁和民事诉讼中，内部调查报告可能被要求披露
- 刑事诉讼中，调查材料可能面临强制披露

**报告草稿未经法律顾问复核不得对外披露。**

---

## 输出结构

```
【Greater China Legal — 劳动法实务工作成果】
⚠️ 复核提示：
- 本调查报告为内部工作文件，未经法律顾问复核不得对外披露
- 来源标注：[yuandian] = 法律数据库 / [web] = 联网检索(请核实) / [model] = 模型知识(请核实)

---

# [事项名称] — 内部调查报告

## 案件概览
- 事项：[事项名称]
- 立案日期：[ISO日期]
- 调查类型：[类型]
- 被调查对象：[姓名/职位]
- 举报人：[姓名/职位或匿名]
- 涉嫌违规时段：[日期范围]
- 主导律师：[姓名]
- 调查状态：[open / closed / pending-follow-up]

## 指控摘要
[用通俗语言总结举报内容]

## 调查范围
- 访谈：[N]次
- 已审查文档：[N]份
- 来源覆盖情况：[简述]

## 证据发现

### 有利证据
[按条目ID引用，附证据摘要]

### 不利证据
[按条目ID引用，附证据摘要]

### 矛盾之处
[不同来源间的矛盾，附日志条目ID]

## 证据缺口
[尚未获得的信息及重要性]

## 法律分析
[涉嫌违规的法律分析 — 引用相关法律条款]

## 结论与建议
[调查结论及建议采取的行动]

## 附录
- 日志条目清单
- 文档清单
- 来源清单完成情况

---

**⚠️ 复核提示：**
- 本调查报告为内部工作文件，仅供法律顾问和公司管理层阅读
- 未经法律顾问复核不得作为证据使用或对外披露
- 中国大陆法律环境下，内部调查报告的保密性有限，请评估披露风险
```

---

## 本 Skill 依赖

`internal-investigation` 参考 Skill 中的详细报告结构、可信度评估框架、更新规则。

---

## 本 Skill 不涵盖

- 代理劳动仲裁或诉讼代理
- 直接向公安机关报案