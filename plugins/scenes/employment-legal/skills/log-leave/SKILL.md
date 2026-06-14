---
name: log-leave
description: '中国大陆员工休假登记 — 将新休假记录录入休假跟踪系统，启动年休假/病假/产假/陪产假/ 婚假/丧假/工伤假的期限跟踪。适用情形：员工开始休假，在休假跟踪系统中登记。

  '
argument-hint: '[员工姓名/职位、工作地点、休假类型、起始日期、预计结束日期]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
user_invocable: true
legal_sources:
- type: statute
  name: Labor Law of the PRC
  article: Articles 45-50 (Annual leave, wages)
  effective_date: 2018-12-29
  jurisdiction: cn-mainland
- type: regulation
  name: Regulations on Paid Annual Leave for Employees
  article: Full text
  effective_date: 2008-01-01
  jurisdiction: cn-mainland
- type: statute
  name: Population and Family Planning Regulations (various provinces)
  article: Province-specific
  effective_date: varies by province
  jurisdiction: cn-mainland
risk_level: low
escalation_triggers:
- 产假天数超过法定98天（部分省市有额外生育奖励假）
- 病假连续超过医疗期期限（须评估劳动合同处理）
- 工伤假期满未做劳动能力鉴定（须申请鉴定）
trigger_phrases:
- 请假记录
- 休假
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /log-leave

## 使用说明

本 Skill 用于将中国大陆员工的新休假记录录入休假跟踪系统，开始跟踪期限。

**管辖法域默认为中国大陆。** 如涉及香港/澳门/台湾/新加坡：
`/employment-legal:log-leave --frame hk`

---

## 第一步：收集休假信息

一次性询问以下问题：

> **休假登记需要以下信息：**
> - 员工姓名（或职位，可匿名）
> - 员工工作地点（城市/省份——影响适用哪个省市的规定）
> - 休假类型：年休假 / 病假 / 产假 / 陪产假 / 婚假 / 丧假 / 工伤假 / 其他
> - 休假起始日期
> - 预计结束日期（若未知可留空）
> - 是否为连续休假（非间歇性）

---

## 第二步：确定适用法定标准

根据员工工作地点，查找适用的休假标准：

### 年休假（根据《职工带薪年休假条例》及累计工龄）

| 累计工作年限 | 年休假天数 |
|---|---|
| 满1年不满10年 | 5天 |
| 满10年不满20年 | 10天 |
| 满20年 | 15天 |

### 产假（根据《劳动法》第62条+各省市人口与计划生育条例）

| 类型 | 天数 |
|---|---|
| 基础产假（顺产） | 98天 |
| 难产增加 | +15天 |
| 多胎每多一胎 | +15天 |
| 生育奖励假（多数省市） | +15-30天（须核实当地） |
| 4个月以下流产 | 15天 |
| 4个月以上流产 | 42天 |

### 陪产假（各省市规定差异较大）

| 省市 | 天数 |
|---|---|
| 上海 | 10天 |
| 北京 | 15天 |
| 广东 | 15天 |
| 江苏 | 15天 |
| 浙江 | 15天 |

### 病假

- 无全国统一天数限制，凭医院证明
- 医疗期期限：根据员工实际工作年限计算（3-24个月）
- 病假工资：不低于当地最低工资80%（各省市规定不同）

---

## 第三步：计算首个期限

| 情况 | 期限 | 说明 |
|---|---|---|
| 年休假 | 用人单位须在年度内安排，否则支付300%补偿 | 跨年度安排须在次年3月前确认 |
| 产假 | 产后30日内申领生育津贴（部分省市有差异） | 提醒提交材料至社保 |
| 病假 | 医疗期届满前须评估劳动合同处理 | 连续病假超医疗期须处理 |
| 工伤假 | 工伤认定申请期限为事故发生后30日内 | 须在期限内申请工伤认定 |

---

## 第四步：写入休假登记文件

在 `leave-register.yaml` 中新增记录，格式：

```yaml
leaves:
  - employee: [姓名/职位，可匿名]
    department: [部门]
    jurisdiction: [省市]
    leave_type: [年休假/病假/产假/陪产假/婚假/丧假/工伤假/其他]
    start_date: [YYYY-MM-DD]
    expected_end_date: [YYYY-MM-DD，或 null]
    duration_days: [总天数]
    status: active
    deadlines:
      - type: [期限类型：年休假安排/生育津贴申领/医疗期届满/工伤认定]
        deadline_date: [YYYY-MM-DD]
        action_required: [须执行的操作]
    notes: [备注]
```

---

## 输出确认

> **已登记。** [员工姓名/职位] — [休假类型] — [省市] — [起始日期]开始。
> 首个期限：[期限类型] — [截止日期]（距今天还有[X]天）。
> 休假跟踪将在到期前自动提醒。

---

## 本 Skill 不涵盖

- 休假政策制定（使用 policy-drafting Skill）
- 请假申请审批（HR工作流）
- 产假天数核定（须核实当地人口与计划生育条例）
- 工伤认定申请（须向人社部门提交材料）
