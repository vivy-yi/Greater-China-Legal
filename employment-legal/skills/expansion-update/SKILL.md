---
name: expansion-update
description: '更新进行中的跨国扩张项目状态 — 重新计算已解锁项、标记逾期项、 呈现下一优先事项。适用情形：自上次会面后有工作进展，需要更新扩张跟踪器。

  '
argument-hint: '[国家/地区名称]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
user_invocable: true
legal_sources:
- type: statute
  name: Labor Contract Law of the PRC
  article: Article 10-17 (Labor relationship establishment)
  effective_date: 2012-07-01
  jurisdiction: cn-mainland
risk_level: low
escalation_triggers:
- 扩张项目逾期超过30天（须评估是否继续推进）
- 发现目标国家/地区法律重大变化（须重新评估合规方案）
trigger_phrases:
- 业务扩张
- 人员扩充
---

# /expansion-update

返回开放扩张跟踪器，根据自上次会面以来的进展更新项目状态。重新计算已解锁项、标记逾期项、呈现下一优先事项。

## 工作流程

1. 读取跟踪文件：`expansion-[slug].yaml`
2. 如文件不存在："> [国家/地区]的扩张跟踪文件未找到。运行 `/employment-legal:expansion-kickoff [国家/地区]` 启动。"
3. 显示当前状态
4. 一次性询问更新（不要逐一询问每个项目）
5. 应用更新，如有项目完成则检查是否解锁其他项目
6. 标记逾期项目
7. 写入更新后的跟踪文件并确认

---

## 使用说明

**管辖法域默认为中国大陆。** 如涉及其他法域：
`/employment-legal:expansion-update --frame hk`

---

## 显示当前状态

```
[国家/地区] 扩张 — 上次更新 [日期]
开放：[N] | 进行中：[N] | 已完成：[N] | 阻塞：[N]

下一优先事项（按截止日期或依赖关系排序）：
  [事项] — 负责人：[负责人]
  [事项] — 负责人：[负责人]
  [事项] — 负责人：[负责人]
```

---

## 询问更新

> 自我们上次查看以来，哪些事项有进展？请告诉我变化情况（例如："EOR决定已做出——选择Deel"、"外部律师已委托——周四安排通话"、"PE分析仍在开放，等待税务部门意见"）。您也可以新增事项或更改截止日期。

---

## 逾期标记

```
⚠️ 逾期：[事项] — 原定截止 [日期]，负责人：[负责人]
```

---

## 依赖关系处理

当某一项目被标记为完成时，检查是否有其他项目因此被解锁：
- EOR决定完成 → 可以启动EOR合同谈判
- 实体设立完成 → 可以启动招聘流程
- 劳动合同模板确认 → 可以开始当地招聘

---

## 输出确认

```
跟踪器已更新 — [N]项关闭，[N]项仍开放。
下一优先事项：[最优先的开放项]。
```

---

## 本 Skill 依赖

`international-expansion` 参考 Skill 中的详细跟踪器结构、项目状态规则和依赖关系逻辑。

---

## 本 Skill 不涵盖

- 代理设立当地法人
- EOR供应商选择
- 签证/就业许可证申请