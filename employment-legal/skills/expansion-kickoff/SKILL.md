---
name: expansion-kickoff
description: '启动新国家/地区用工扩张规划 — 采集信息、EOR vs 自设实体判断、 跨部门问题清单、地区特殊问题标记、创建持续跟踪器。 适用情形：用户说"要在[国家/地区]招聘"、"扩张到[国家/地区]"、
  "在[国家/地区]的首次招聘"。

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
- type: statute
  name: Social Insurance Law of the PRC
  article: Full text
  effective_date: 2018-12-29
  jurisdiction: cn-mainland
- type: statute
  name: Regulations on the Administration of Foreign-Funded Enterprises
  article: Full text
  effective_date: 2020-01-01
  jurisdiction: cn-mainland
risk_level: medium
escalation_triggers:
- 涉及外籍员工（须就业许可证）
- 涉及香港/澳门/台湾员工（特殊程序）
- 上市公司跨境用工（须评估证券披露义务）
trigger_phrases:
- 扩张启动
- 项目启动
---

# /expansion-kickoff

启动新国家/地区用工扩张规划 — 采集信息、EOR vs 自设实体判断、跨部门问题清单、地区特殊问题标记、创建持续跟踪器。

## 工作流程

1. 加载 `international-expansion` 参考 Skill，执行完整工作流
2. 如该国家/地区的跟踪文件已存在（`expansion-[slug].yaml`），先标记：
   > "[国家/地区]的扩张跟踪文件已存在。使用 `/employment-legal:expansion-update [国家/地区]` 更新，或确认重新开始。"
3. 完成后创建 `expansion-[slug].yaml`

---

## 使用说明

本 Skill 管理跨国用工扩张规划，被以下 Skill 调用：
- `/employment-legal:expansion-kickoff`（启动新国家/地区扩张）
- `/employment-legal:expansion-update`（更新现有扩张跟踪）
- `/employment-legal:international-expansion`（参考框架）

**管辖法域默认为中国大陆（即从中国大陆向海外扩张）。** 如涉及其他法域：
`/employment-legal:expansion-kickoff --frame hk`

---

## 第一步：确认扩张基本信息

询问以下问题（一次性）：

> **扩张基本信息：**
> - 目标国家/地区：[国家/地区]
> - 扩张类型：设立当地法人 / 使用EOR（雇主代理）/ 远程用工
> - 预计招聘规模：[人数]（短期/中期/长期）
> - 招聘岗位类型：[核心业务岗/支持性岗/高管]
> - 预计启动时间：[日期]
> - 是否已有当地合作伙伴或EOR供应商？

---

## 第二步：EOR vs 自设实体判断

根据以下因素判断用工结构：

| 因素 | EOR（雇主代理） | 自设实体（设立公司） |
|---|---|---|
| 招聘规模 | 小规模（1-10人） | 中大规模（10人以上） |
| 用工时长 | 短期/试探性 | 长期稳定 |
| 成本 | 低初始成本 | 高初始成本但长期更低 |
| 合规风险 | EOR承担合规责任 | 公司自行承担合规责任 |
| 控制程度 | 较低 | 较高 |
| 适用场景 | 试探市场、短期项目 | 核心业务长期运营 |

---

## 第三步：跨部门问题清单

协调以下部门确认相关信息：

| 部门 | 须确认事项 |
|---|---|
| 人力资源 | 当地招聘渠道、薪酬基准、福利标准 |
| 法务 | 劳动法合规、劳动合同类型、社保要求、签证/就业许可 |
| 财务 | 薪资支付货币、税务处理、外汇管制 |
| IT | 当地数据隐私要求（GDPR/PDPA等）、数据跨境传输 |
| 合规 | 反商业腐败规定、出口管制（如有） |

---

## 第四步：地区特殊问题标记

根据目标国家/地区，标记特殊问题：

**香港：**
- 普通法系，劳动法差异大
- 强积金（MPF）制度
- 雇佣条例（Employment Ordinance）

**澳门：**
- 葡萄牙民法典延续
- 雇员散位纸（散工/非连续性雇佣）
- 社保制度（强制性）

**台湾：**
- 适用台湾劳动基准法
- 劳动保险/全民健保
- 竞业限制须有合理性且不超过2年

**新加坡：**
- 雇佣法（Employment Act）适用于大多数人
- 中央公积金（CPF）
- 平等就业要求

---

## 输出：扩张跟踪文件

创建 `expansion-[slug].yaml`：

```yaml
# [WORK-PRODUCT HEADER]
country: [国家/地区]
expansion_type: [EOR / entity / remote]
status: planning
opened: [ISO日期]
estimated_headcount: [人数]
estimated_start: [日期]

cross_functional:
  hr: pending
  legal: pending
  finance: pending
  it: pending
  compliance: pending

country_specific_flags:
  - [特殊问题1]
  - [特殊问题2]

eor_vs_entity_decision: [pending / EOR / entity]
next_steps: []
```

---

## 本 Skill 依赖

`international-expansion` 参考 Skill 中的详细框架、跨部门问题清单、简报模板和跟踪器结构。

---

## 本 Skill 不涵盖

- 代理设立当地法人（须联系当地律师或秘书公司）
- EOR供应商选择（须商务评估）
- 签证/就业许可证申请（须向当地移民局申请）