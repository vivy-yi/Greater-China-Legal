---
name: investigation-open
description: '启动新内部调查事项 — 采集立案信息、生成来源清单、创建保密调查日志。 适用情形：收到举报或指控，需要建立 privileged 调查工作区。

  '
argument-hint: '[举报/指控的简要描述]'
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
- type: statute
  name: Anti-Unfair Competition Law of the PRC
  article: Article 9 (Commercial secrets)
  effective_date: 2019-04-23
  jurisdiction: cn-mainland
- type: statute
  name: Criminal Law of the PRC
  article: Articles 163-164 (Commercial bribery), Article 271 (Embezzlement), Article
    272 (挪用资金)
  effective_date: 2023-04-20
  jurisdiction: cn-mainland
risk_level: high
escalation_triggers:
- 调查涉及高管（须同时上报董事会/监事会）
- 发现刑事犯罪线索（须评估向公安机关报案的必要性）
- 上市公司调查涉及证券披露义务
trigger_phrases:
- 开启调查
- 立案
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /investigation-open

启动新内部调查事项 — 运行立案流程、生成来源清单、创建保密调查日志。

## 工作流程

1. 加载 `internal-investigation` 参考 Skill，执行 Mode 1（立案）
2. 如同名事项已存在，先警告再覆盖

---

## 使用说明

本 Skill 管理从立案到最终调查报告的全流程，被以下 Skill 调用：
- `/employment-legal:investigation-open`（立案）
- `/employment-legal:investigation-add`（添加数据）
- `/employment-legal:investigation-query`（查询日志）
- `/employment-legal:investigation-memo`（起草报告）
- `/employment-legal:investigation-summary`（受众摘要）

**管辖法域默认为中国大陆。** 如涉及香港/澳门/台湾/新加坡：
`/employment-legal:investigation-open --frame hk`

---

## ⚠️ 保密特权说明

在中国大陆法律环境下：
- 律师与当事人之间的通信特权并非法定特权（除非法律法规另有规定）
- 劳动仲裁和民事诉讼中，雇主单方内部调查报告可能被要求披露
- 刑事诉讼中，调查材料可能面临强制披露

**立案前须确认：** 本次调查是否由律师主导？调查目的是否为获取法律意见？
如果答案是否定的，保密分析将发生变化。在创建任何调查文件前，请将此问题告知律师。

---

## 第一步：立案信息采集

> **立案需要以下信息：**
> - 举报/问题简要描述（用通俗语言）
> - 举报人身份（或触发本次调查的原因：举报/审计/管理层发现）
> - 被调查对象（姓名/职位）
> - 涉嫌违规的时段（大致时间范围）
> - 是否由律师主导？
>
> **调查类型**：
> - 劳动人事：职场骚扰/歧视/报复
> - 财务舞弊：报销欺诈/采购违规/挪用资金
> - 高管舞弊：利益冲突/未披露关系/治理违规
> - 商业腐败：行贿受贿/背信损害公司利益
> - 商业秘密：侵犯商业秘密/竞业限制违约
>
> **特殊情况**：
> - 是否有工会？（如是，调查面谈程序可能涉及集体协商权）
> - 是否为上市公司？（调查内容可能涉及证券披露义务）
> - 被调查对象是否担任党员/人大代表/政协委员？

---

## 第二步：创建调查文件

创建以下文件：

```
~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-[matter-slug]/log.yaml
~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-[matter-slug]/sources-checklist.yaml
~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-[matter-slug]/documents-reviewed.yaml
```

---

## 第三步：来源清单确认

根据调查类型生成来源清单，呈现给律师确认：

**劳动人事调查来源清单：** 举报人访谈、被调查对象访谈、证人访谈、邮件/通信审查、HR档案、过往投诉记录、同类情形对比、制度文件（事发时有效版本）、组织架构图、考勤/门禁记录

**财务舞弊调查来源清单：** 报销单据、审批记录、供应商/合同商档案、财务系统记录、邮件/通信审查、被调查对象访谈、审批人访谈、交易对手访谈、系统访问日志、过往审计报告

**高管舞弊调查来源清单：** 被调查对象访谈、董事会/薪酬委员会记录、劳动合同及修订、股权激励记录、报销单据及审批记录、邮件/通信记录、利益冲突披露文件、兼职/在外任职记录、证人访谈、过往投诉记录

**商业腐败调查来源清单：** 被调查对象访谈、交易对手/供应商访谈、合同/审批文件、礼品/款待记录、邮件/通信记录、银行转账记录、知情员工访谈、过往合规审查或审计报告

**商业秘密/竞业限制违约调查来源清单：** 被调查对象访谈、劳动合同及竞业限制/保密协议、前雇主知情员工访谈、新雇主信息、邮件/通信记录、设备/账号交还记录、知识产权归属文件、证人访谈、新旧雇主工作内容重叠分析

---

## 输出确认

> **已立案。** [事项名称] — [调查类型] — [被调查对象] — [立案日期]
> 来源清单已生成，请确认是否需要补充。
> 保密告知文件已准备，访谈前须向被调查对象说明。

---

## 本 Skill 不涵盖

- 代理劳动仲裁或诉讼代理
- 直接向公安机关报案（须律师评估后决定）
- 代理刑事案件调查
