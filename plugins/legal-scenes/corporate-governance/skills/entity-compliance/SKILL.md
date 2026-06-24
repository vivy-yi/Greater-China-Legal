---
name: entity-compliance
description: '公司合规追踪——初始化、报告即将到期的备案、更新状态、执行健康审计、导出CSV。 根据公司类型和管辖机关计算备案截止日期，显示未来30/60/90天到期的事项。
  适用情形：用户说"公司合规"、"备案截止日"、"工商年报"、"公司状态"、 "有什么要到期了"、"公司健康检查"。

  '
argument-hint: '[--init | --report [--days N] | --update | --sweep | --audit | --export]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
- 公司合规
- 合规管理
legal_sources:
- name: 中华人民共和国民法典
  effective_date: '2021-01-01'
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /entity-compliance — China Mainland

## Purpose

年度报告、税务申报工商年报、信息公示——每个公司都有自己的一套备案时间表，错过截止日期会有处罚。本技能维护一个统一的追踪文件。

## CN合规时间表

### 年度报告（工商年报）

**截止日期：** 每年1月1日至6月30日（报送上一年度）

**公示内容：**
- 股东认缴和实缴出资额、出资方式、出资期限
- 企业开业、存续状态
- 联系方式
- 主营业务
- 资产负债状况

**未年报后果：**
- 列入经营异常名录
- 满3年未履行公示义务 → 列入严重违法企业名单
- 罚款：2000元至2万元（情节严重）

---

### 税务申报

| 申报类型 | 截止日期 |
|---|---|
| 月度增值税申报 | 每月15日前 |
| 季度企业所得税预缴 | 每季度15日前 |
| 年度企业所得税汇算清缴 | 每年5月31日前 |
| 年度个人所得税全员申报 | 每年3月31日前 |

---

### 社保公积金

| 事项 | 截止日期 |
|---|---|
| 社保月度申报 | 每月15日前 |
| 公积金月度汇缴 | 每月15日前 |

---

### 公司变更备案

**须在30日内备案的情形：**
- 法定代表人变更
- 注册资本变更
- 经营范围变更
- 住所变更
- 股东变更

**须在45日内备案的情形：**
- 公司章程修改

---

## Modes

### Mode 1: 初始化（--init）

从 `../CLAUDE.md` 的 entity table 中读取公司列表，初始化合规追踪文件。

### Mode 2: 报告（--report）

**默认回溯窗口：** 未来90天

**输出格式：**

```markdown
## 合规报告——YYYY年MM月

### 🔴 15天内到期

| 公司 | 事项类型 | 截止日期 | 状态 |
|---|---|---|---|
| [名称] | [工商年报/税务申报] | [日期] | [待处理/已完成] |

### 🟠 30天内到期

[同上表格]

### 🟡 60-90天内到期

[同上表格]

---

**下一步行动：**
- [ ] [具体行动1]
- [ ] [具体行动2]
```

### Mode 3: 更新（--update）

手动更新备案状态。读取上一次报告，根据实际完成情况更新。

### Mode 4: 健康审计（--audit）

**检查项：**
- 年报是否在期限内提交
- 税务是否按时申报
- 营业执照是否公示
- 注册资本是否实缴（如适用）
- 公司章程是否已备案

**输出格式：**

```markdown
## 公司合规健康审计——[公司名称]

**审计日期：** YYYY-MM-DD
**上一次合规更新：** [日期]

### 合规状态

| 事项 | 状态 | 最近更新时间 | 下次截止日 |
|---|---|---|---|
| 工商年报 | ✅已提交 / ⚠️待提交 / ❌逾期 | [日期] | YYYY-06-30 |
| 税务申报 | ✅正常 / ⚠️待申报 / ❌逾期 | [日期] | [日期] |
| 注册资本 | ✅已实缴 / ⚠️部分 / ❌未到位 | [日期] | — |

### 风险提示

[如有任何不合规项，说明风险和整改建议]
```

---

## 追踪文件结构

```yaml
# corporate-governance/entities/compliance-tracker.yaml
entities:
  - name: "[公司全称]"
   统一社会信用代码: "[代码]"
    company_type: "[有限责任公司/股份有限公司/外商投资企业]"
    registration_authority: "[市监局]"
    registered_capital: [金额]
    paid_up_capital: [金额]
    founding_date: "YYYY-MM-DD"
    fiscal_year_end: "12-31"

compliance_schedule:
  annual_report:
    deadline: "06-30"  # 每年6月30日
    last_submitted: "YYYY-06-15"
    status: "current"  # current / pending / overdue

  tax_filings:
    vat:
      frequency: "monthly"
      deadline: "15"  # 每月15日
      last_filed: "YYYY-MM-15"
      status: "current"
    enterprise_income_tax:
      frequency: "quarterly"
      deadline: "15"  # 每季度15日
      last_filed: "YYYY-MM-15"
      status: "current"

  social_security:
    deadline: "15"  # 每月15日
    last_filed: "YYYY-MM-15"
    status: "current"

  change_registrations:
    # 如有变更，记录变更日期和备案日期
    last_change: "YYYY-MM-DD"
    change_type: "[变更类型]"
    registration_deadline: "YYYY-MM-DD"
    registration_status: "completed/pending/overdue"
```

---

## 本技能不做什么

- 不代办备案。只追踪和提醒。
- 不提供税务建议。只提供时间表。
- 不保证信息准确性。请在官方平台核实截止日期。

---

*Greater China Legal — corporate-legal entity-compliance CN adapter v1.0.0*
*基于 anthropic/claude-for-legal entity-compliance 适配中国大陆公司合规环境*

*[YD] — 基于 anthropic/claude-for-legal 适配中国大陆法律环境 v1.0.0*
