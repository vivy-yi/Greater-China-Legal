---
name: investigation-add
description: >
  向开放调查事项添加数据 — 文档、访谈笔录或观察记录。
  批量处理文档，标记相关项，记录所有已审查文档。
  适用情形：新证据、访谈笔录或文档收到，需要添加到开放调查中。
argument-hint: "[事项名称或slug，然后粘贴或附加数据]"
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
risk_level: medium
escalation_triggers:
  - 发现新的刑事犯罪线索（须重新评估是否向公安机关报案）
  - 发现高管涉案（须通知董事会/监事会）
---

# /investigation-add

向开放调查事项添加数据 — 批量处理文档、标记相关项、记录所有已审查文档。

## 工作流程

1. 加载 `internal-investigation` 参考 Skill，执行 Mode 2（添加数据）
2. 处理后显示文档筛选率和相关文档列表
3. 提示更新来源清单（如数据覆盖清单中的某项）

---

## 使用说明

**管辖法域默认为中国大陆。** 如涉及香港/澳门/台湾/新加坡：
`/employment-legal:investigation-add --frame hk`

---

## 第一步：确认事项

如果存在多个调查文件夹，先确认数据属于哪个事项。如果只有一个，直接继续。

询问（如果上下文不清晰）：
- 访谈笔录（谁的访谈？）
- 文档批次（邮件、记录、文件）
- 律师笔记或观察记录

---

## 第二步：文档筛选

对任何文档批次，应用以下筛选标准。符合以下任一条件的文档即为"相关文档"：

**筛选条件：**
1. 包含调查任何一方的姓名（举报人、被调查对象、访谈记录中提及的证人）
2. 在关键违规时段内由任一方创建或收到
3. 包含与举报类型相关的关键词
4. 包含明示或暗示的承认（"我不应该"、"我知道这看起来不对"、"不要书面记录"、"删除这个"）
5. 包含与日志中已有陈述相矛盾的语言
6. 在诉讼中可能敏感的语言：歧视性用语、威胁、涉及受保护特征或活动的讨论、符合举报模式的财务违规
7. 访谈中提及但尚未出现的文档类型 → 记录为证据缺口，不作为相关文档

**每份文档的处置：**
- `surfaced`：符合一条或多条筛选条件 → 作为日志条目添加
- `reviewed-nothing-significant`：已审查，不符合筛选条件 → 仅记录一行说明

---

## 第三步：处理后报告

```
文档审查完成。
已审查：[N]份文档
标记为相关：[N]份
记录为已审查/无重大发现：[N]份
新发现证据缺口：[N]份

相关文档：
[列表，含一行说明及触发的筛选条件]
```

---

## 第四步：更新来源清单

如果添加的数据对应清单中的某一项，询问律师是否应标记为完成或进行中。不要自动标记。

---

## 本 Skill 依赖

`internal-investigation` 参考 Skill 中的详细筛选逻辑、日志条目格式、来源追踪规则。

---

## 本 Skill 不涵盖

- 代理劳动仲裁或诉讼代理
- 直接向公安机关报案