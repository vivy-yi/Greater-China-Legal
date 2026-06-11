---
name: internal-investigation
description: >
  内部调查框架 Skill（不直接调用）— 被 /investigation-open、/investigation-add、
  /investigation-query、/investigation-memo、/investigation-summary 调用。
  管理从立案到最终调查报告的全流程：保密调查日志、文档处理、来源覆盖跟踪、
  Q&A 查询、调查报告起草、受众摘要。
user_invocable: false
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
escalation_triggers:
  - 调查涉及高管或董事会成员（须上报董事会/监事会）
  - 涉及刑事犯罪线索（须评估是否向公安机关报案）
  - 涉及证券违规（上市公司须评估是否须披露）
  - 涉及外籍员工或跨境因素（须考虑适用外国法律）
---

# /internal-investigation

## 使用说明

本 Skill 是内部调查的共享框架，不直接由用户调用。被以下 Skill 调用：
- `/employment-legal:investigation-open`（立案）
- `/employment-legal:investigation-add`（添加数据）
- `/employment-legal:investigation-query`（查询日志）
- `/employment-legal:investigation-memo`（起草报告）
- `/employment-legal:investigation-summary`（受众摘要）

**管辖法域默认为中国大陆。** 如涉及香港/澳门/台湾/新加坡：
`/employment-legal:internal-investigation --frame hk`

---

## ⚠️ 保密特权说明

**文件标注不代表特权成立。** 本 Skill 创建的所有文件均带有保密标注，但在中国大陆法律环境下：
- 律师与当事人之间的通信特权并非法定特权（除非法律法规另有规定）
- 劳动仲裁和民事诉讼中，雇主单方内部调查报告可能被要求披露
- 刑事诉讼中，调查材料可能面临强制披露

**立案前须确认：** 本次调查是否由律师主导？调查目的是否为获取法律意见？

如果答案是否定的（如HR主导，律师仅提供咨询意见），保密分析将发生变化。在创建任何调查文件前，请将此问题告知律师。

---

## 第一步：立案（Mode 1 — investigation-open）

触发条件：用户说"立案"、"开始调查"、"启动一项调查"

### 1.1 信息采集

一次性询问以下问题：

> **立案需要以下信息：**
> - 举报/问题简要描述（用通俗语言）
> - 举报人身份（或触发本次调查的原因：举报/审计/管理层发现）
> - 被调查对象（姓名/职位）
> - 涉嫌违规的时段（大致时间范围）
> - 是否由律师主导？（若是：适用律师工作成果保护。若否：先解决特权问题再继续）
>
> **调查类型**（帮助确定来源清单）：
> - 劳动人事：职场骚扰/歧视/报复
> - 财务舞弊：报销欺诈/采购违规/挪用资金
> - 高管舞弊：利益冲突/未披露关系/治理违规
> - 商业腐败：行贿受贿/背信损害公司利益
> - 商业秘密：侵犯商业秘密/竞业限制违约
>
> **特殊情况**：
> - 是否有工会？被调查对象是否为工会会员？（如是，调查面谈程序可能涉及集体协商权）
> - 是否为上市公司？调查内容是否可能涉及证券披露义务？
> - 被调查对象是否担任党员/人大代表/政协委员？（特殊身份可能影响调查程序）

### 1.2 创建调查文件

创建以下文件：

`~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-[matter-slug]/log.yaml`:

```yaml
# [WORK-PRODUCT HEADER]
matter: "[事项名称]"
matter_slug: "[slug]"
opened: "[ISO日期]"
attorney_directed: [true/false]
allegation: "[通俗语言总结]"
complainant: "[姓名/职位或匿名]"
respondent: "[姓名/职位]"
conduct_timeframe: "[大致日期范围]"
investigation_type: "[劳动人事/财务舞弊/高管舞弊/商业腐败/商业秘密/其他]"
status: open
last_updated: "[ISO日期]"

issues:
  - "[问题1 — 从举报中提炼，如'涉嫌职场骚扰']"
  - "[问题2（如有）]"

entries: []

evidentiary_gaps: []
```

`~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-[matter-slug]/sources-checklist.yaml`:

根据调查类型生成（见下方来源清单模板）。

`~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-[matter-slug]/documents-reviewed.yaml`:

```yaml
# [WORK-PRODUCT HEADER]
matter: "[事项名称]"
total_reviewed: 0
total_surfaced: 0
last_updated: "[ISO日期]"
documents: []
```

### 1.3 来源清单

根据调查类型生成相应的来源清单，呈现给律师并确认：

**劳动人事调查来源清单（职场骚扰/歧视/报复）：**
```yaml
sources:
  - id: 1
    source: "举报人访谈"
    status: open
    notes: ""
  - id: 2
    source: "被调查对象访谈"
    status: open
    notes: ""
  - id: 3
    source: "证人访谈（从举报人和被调查对象陈述中识别）"
    status: open
    notes: ""
  - id: 4
    source: "电子邮件/通信记录审查 — 相关方、相关时间段"
    status: open
    notes: ""
  - id: 5
    source: "HR档案 — 被调查对象绩效历史、过往投诉、处分记录"
    status: open
    notes: ""
  - id: 6
    source: "过往投诉记录 — HR系统中针对被调查对象的过往投诉"
    status: open
    notes: ""
  - id: 7
    source: "同类情形对比数据 — 相似情况历史处理方式"
    status: open
    notes: ""
  - id: 8
    source: "相关制度 — 反骚扰制度、行为准则、举报程序（以事发时有效版本为准）"
    status: open
    notes: ""
  - id: 9
    source: "组织架构图及事发时汇报关系"
    status: open
    notes: ""
  - id: 10
    source: "考勤/门禁记录 — 相关会议或事件的时间验证"
    status: open
    notes: ""
  - id: 11
    source: "访谈前的保密告知文件 — 确认访谈已进行保密告知并有记录"
    status: open
    notes: ""
```

**财务舞弊调查来源清单：**
```yaml
sources:
  - id: 1
    source: "报销单据 — 被调查对象、相关时间段"
    status: open
    notes: ""
  - id: 2
    source: "审批记录 — 审批人、相关费用/交易"
    status: open
    notes: ""
  - id: 3
    source: "供应商/合同商档案 — 合同、发票、付款记录"
    status: open
    notes: ""
  - id: 4
    source: "财务系统记录 — 应付账款、总账相关科目"
    status: open
    notes: ""
  - id: 5
    source: "电子邮件/通信记录 — 被调查对象、审批人、交易对手"
    status: open
    notes: ""
  - id: 6
    source: "被调查对象访谈"
    status: open
    notes: ""
  - id: 7
    source: "审批人访谈"
    status: open
    notes: ""
  - id: 8
    source: "交易对手/供应商访谈（如可接触）"
    status: open
    notes: ""
  - id: 9
    source: "系统访问日志 — 相关账户/系统的审计日志"
    status: open
    notes: ""
  - id: 10
    source: "过往审计报告覆盖相关期间"
    status: open
    notes: ""
  - id: 11
    source: "访谈保密告知文件"
    status: open
    notes: ""
```

**高管舞弊调查来源清单：**
```yaml
sources:
  - id: 1
    source: "被调查对象访谈"
    status: open
    notes: ""
  - id: 2
    source: "董事会/薪酬委员会记录 — 相关决议、会议纪要、审批文件"
    status: open
    notes: ""
  - id: 3
    source: "劳动合同及任何修订"
    status: open
    notes: ""
  - id: 4
    source: "股权激励记录 — 授予、行权、归属"
    status: open
    notes: ""
  - id: 5
    source: "报销单据及审批记录"
    status: open
    notes: ""
  - id: 6
    source: "电子邮件/通信记录 — 被调查对象、相关交易对手"
    status: open
    notes: ""
  - id: 7
    source: "利益冲突披露文件（或未披露记录）"
    status: open
    notes: ""
  - id: 8
    source: "兼职/在外任职记录"
    status: open
    notes: ""
  - id: 9
    source: "证人访谈 — 直接下属、同级、董事会成员"
    status: open
    notes: ""
  - id: 10
    source: "针对被调查对象的过往投诉或疑虑记录"
    status: open
    notes: ""
  - id: 11
    source: "访谈保密告知文件"
    status: open
    notes: ""
```

**商业腐败/反腐败调查来源清单：**
```yaml
sources:
  - id: 1
    source: "被调查对象访谈"
    status: open
    notes: ""
  - id: 2
    source: "交易对手/供应商访谈"
    status: open
    notes: ""
  - id: 3
    source: "合同/审批文件 — 涉及相关交易的合同、发票、付款凭证"
    status: open
    notes: ""
  - id: 4
    source: "礼品/款待记录 — 反商业贿赂制度项下的登记记录"
    status: open
    notes: ""
  - id: 5
    source: "电子邮件/通信记录 — 被调查对象、交易对手"
    status: open
    notes: ""
  - id: 6
    source: "银行转账记录"
    status: open
    notes: ""
  - id: 7
    source: "知情员工访谈"
    status: open
    notes: ""
  - id: 8
    source: "过往合规审查或审计报告"
    status: open
    notes: ""
  - id: 9
    source: "访谈保密告知文件"
    status: open
    notes: ""
```

**商业秘密/竞业限制违约调查来源清单：**
```yaml
sources:
  - id: 1
    source: "被调查对象访谈（入职前/离职后竞业/保密义务）"
    status: open
    notes: ""
  - id: 2
    source: "劳动合同及竞业限制/保密协议"
    status: open
    notes: ""
  - id: 3
    source: "前雇主知情员工访谈"
    status: open
    notes: ""
  - id: 4
    source: "新雇主信息（通过公开渠道或员工陈述）"
    status: open
    notes: ""
  - id: 5
    source: "电子邮件/通信记录 — 被调查对象在新旧雇主间的通信"
    status: open
    notes: ""
  - id: 6
    source: "设备/账号交还记录"
    status: open
    notes: ""
  - id: 7
    source: "知识产权归属文件 — 发明转让协议、保密协议"
    status: open
    notes: ""
  - id: 8
    source: "证人访谈 — 同事、项目相关人员"
    status: open
    notes: ""
  - id: 9
    source: "被调查对象在新雇主的工作内容与原雇主业务的重叠分析"
    status: open
    notes: ""
  - id: 10
    source: "访谈保密告知文件"
    status: open
    notes: ""
```

---

## 第二步：添加数据（Mode 2 — investigation-add）

触发条件：用户说"添加到[事项]调查"或粘贴文档/访谈笔录

### 2.1 确认事项

如果存在多个调查文件夹，先确认数据属于哪个事项。如果只有一个，直接继续。

### 2.2 确认数据类型

询问（如果上下文不清晰）：
- 访谈笔录（谁的访谈？）
- 文档批次（邮件、记录、文件）
- 律师笔记或观察记录
- 保密告知确认文件

### 2.3 文档筛选标准

对任何文档批次，应用以下筛选标准。符合以下任一条件的文档即为"相关文档"：

**筛选条件：**
1. 包含调查任何一方的姓名（举报人、被调查对象、访谈记录中提及的证人）
2. 在关键违规时段内由任一方创建或收到
3. 包含与举报类型相关的关键词（从立案和过往日志条目中识别，根据访谈中出现的新术语更新关键词列表）
4. 包含明示或暗示的承认（"我不应该"、"我知道这看起来不对"、"不要书面记录"、"删除这个"）
5. 包含与日志中已有陈述相矛盾的语言 → 标注具体矛盾及对应的日志条目
6. 在诉讼中可能敏感的语言：歧视性用语、威胁、涉及受保护特征或活动的讨论、符合举报模式的财务违规
7. 访谈中提及但尚未出现在文档集中的文件类型（如访谈中提到某次会议但无日历邀请记录）→ 记录为证据缺口，不作为相关文档

**每份文档的处置：**
- `surfaced`：符合一条或多条筛选条件 → 作为日志条目添加
- `reviewed-nothing-significant`：已审查，不符合筛选条件 → 仅在 documents-reviewed.yaml 中记录一行说明

**文档批次处理后报告：**

```
文档审查完成。
已审查：[N]份文档
标记为相关：[N]份
记录为已审查/无重大发现：[N]份
新发现证据缺口：[N]份

相关文档：
[列表，含一行说明及触发的筛选条件]
```

### 2.4 写入日志条目

对每个相关文档，在 `log.yaml` 中追加：

```yaml
- entry_id: [自动递增]
  entry_type: [interview / document / attorney-note / gap]
  date_of_event: "[事件发生日期 — 非记录日期]"
  date_logged: "[ISO日期时间]"
  source: "[证人姓名/职位，或文档文件名/描述]"
  source_type: [complainant / respondent / witness / document / attorney-note]
  issues: ["[本条目涉及的调查问题]"]
  significance: [high / medium / background]
  summary: "[本条目对记录的贡献 — 2-5句话]"
  quote: "[如有重要原文则引用，否则为空]"
  contradicts_entry: [entry_id 或 null]
  corroborates_entry: [entry_id 或 null]
  credibility_note: ""
  pull_criterion: "[触发的筛选条件 — 仅用于文档]"
  privilege: attorney-work-product
```

对于证据缺口：

```yaml
- gap_id: [自动递增]
  description: "[应该存在但尚未找到的文档/来源]"
  identified_from: "[提出此缺口的日志条目或陈述]"
  source_to_obtain: "[从何处获取]"
  priority: [high / medium / low]
  status: open
```

### 2.5 更新来源清单

如果添加的数据对应清单中的某一项，询问律师是否应标记为完成或进行中。不要自动标记——律师决定何时一项来源已充分覆盖。

---

## 第三步：查询日志（Mode 3 — investigation-query）

触发条件：用户提出针对调查的问题（如"[证人]关于[某事]说了什么"、"哪些文档印证"、"我们还需要什么"、"双方各自最强的证据是什么"）

读取完整日志后再回答。回答类型：

**事实查询**（"[X]关于[Y]说了什么"）：
从日志条目中回答，注明条目ID。如果日志中没有该主题的信息："本调查日志（[N]条条目）中未见关于[主题]的信息。这可能值得作为缺口记录。"

**冲突查询**（"陈述在哪里矛盾"）：
呈现所有 contradicts_entry 链接。对每个冲突：说明冲突内容、哪些条目存在张力、以及（如有）印证冲突的文档证据。

**覆盖查询**（"我们还需要什么"/"缺口是什么"）：
读取 sources-checklist.yaml 和 log.yaml 中的 evidentiary_gaps。报告：
- 已完成/进行中的来源
- 高优先级缺口及来源
- 建议下一步

---

## 第四步：起草调查报告（Mode 4 — investigation-memo）

触发条件：用户说"起草调查报告"、"写一份调查报告"、"整理调查结果"

读取完整日志。

输出结构：

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
- 访谈：[N]次（举报人、被调查对象、证人）
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

## 第五步：受众摘要（Mode 5 — investigation-summary）

触发条件：用户说"给管理层一个总结"、"给审计委员会的报告"、"给HR的说明"

读取完整日志，根据受众调整详细程度：

**管理层摘要（董事会/高管）：**
- 结论先行
- 关键证据摘要（3-5条）
- 建议行动（简洁）
- 不含敏感细节（保护被调查对象隐私、保留内部调查完整性）

**HR摘要：**
- 可采取的行动建议
- 须注意的合规问题
- 后续跟踪事项
- 不含调查细节（保密需要）

---

## 文件存储路径

所有调查文件存储于：
`~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-[matter-slug]/`

---

## 本 Skill 不涵盖

- 代理劳动仲裁或诉讼代理
- 直接向公安机关报案（须律师评估后决定）
- 刑事案件调查（须由有资质的调查机构或律师进行）