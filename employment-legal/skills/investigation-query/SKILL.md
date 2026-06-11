---
name: investigation-query
description: >
  针对开放调查日志提问 — 证人说了什么、陈述在哪里矛盾、证据缺口是什么、
  各问题最强证据是什么。适用情形：律师需要查询调查记录而不重读每条日志。
argument-hint: "[事项名称] [问题]"
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
risk_level: low
escalation_triggers:
  - 发现重大证据矛盾可能影响调查结论（须律师评估）
---

# /investigation-query

针对调查日志回答问题 — 证人说了什么、陈述在哪里矛盾、证据缺口是什么、各问题最强证据是什么。

## 工作流程

1. 加载 `internal-investigation` 参考 Skill，执行 Mode 3（查询）
2. 回答时始终注明日志条目ID
3. 如果日志中没有相关信息，明确说明并提议记录为证据缺口

---

## 使用说明

**管辖法域默认为中国大陆。** 如涉及香港/澳门/台湾/新加坡：
`/employment-legal:investigation-query --frame hk`

---

## 查询类型

**事实查询**（"[X]关于[Y]说了什么"）：
从日志条目中回答，注明条目ID。
如果日志中没有该主题的信息：
> "本调查日志（[N]条条目）中未见关于[主题]的信息。这可能值得作为缺口记录。"

**冲突查询**（"陈述在哪里矛盾"）：
呈现所有矛盾链接。对每个冲突：说明冲突内容、哪些条目存在张力、以及（如有）印证冲突的文档证据。

**覆盖查询**（"我们还需要什么"/"缺口是什么"）：
读取 sources-checklist.yaml 和 evidentiary_gaps。报告：
- 已完成/进行中的来源
- 高优先级缺口及来源
- 建议下一步

**证据强度查询**（"各方最强的证据是什么"）：
逐一分析各调查问题，列出支持/不利的证据，注明条目ID。

---

## 示例

```
/employment-legal:investigation-query [事项名称]
被调查对象关于12月团队聚餐说了什么？
```

```
/employment-legal:investigation-query [事项名称]
举报人和被调查对象的陈述在哪里矛盾？
```

```
/employment-legal:investigation-query [事项名称]
我们还需要什么？
```

---

## 本 Skill 依赖

`internal-investigation` 参考 Skill 中的详细查询逻辑、条目引用规则、缺口标记模板。

---

## 本 Skill 不涵盖

- 代理劳动仲裁或诉讼代理
- 法律结论陈述（仅呈现日志中的事实记录）