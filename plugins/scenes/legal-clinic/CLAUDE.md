---
name: legal-clinic
description: >
  Legal clinic practice management — CN法律援助/公益法律服务管理。
  Manages client intake, case assignment, supervisor review, and reporting.
synopsis: >
  CN legal clinic: 法律援助法, 公益法律服务, 法律援助申请审核.
advisory_scale: low
client_types: [legal-clinic, pro-bono]
internal_stakeholders: [clinics, volunteers]
---

# Legal Clinic — China Mainland

## Who's using this

**Role:** [律师 / 法务人员 / 业务部门（非法律背景，有律师支持）/ 业务部门（无律师支持）]
**Attorney contact:** [填空]

**工作成果头部标记：**
- 律师/法务人员 → `Privileged & Confidential — Attorney Work Product`
- 非法务（有律师支持）→ `Research Notes — Not Legal Advice — Review With Attorney Before Acting`
- 非法务（无律师支持）→ `General Information — Not Legal Advice — Consult A Licensed Attorney`

在产出工作成果前，必须先检查 Role 字段。如果 Role 为 `[填空]`，要求用户先设置角色。

## 公司基本信息

**法律诊所名称：** [填空]
**所在院校/机构：** [填空]
**主管单位：** [填空]
**服务对象：** [法律援助受援人 / 公益法律咨询 / 社区法律服务]

## 数据源配置

**数据源标注规则：**
- `[YD]` = 元典 MCP 实际返回
- `[WKL]` = 裁判文书网/无讼
- `[BD]` = 北达检索
- `[GOV]` = 政府平台
- `[web]` = 网络搜索
- `[model]` = 模型推理（须核实）

标注必须诚实——不能因"引用看起来是对的"就把 `[model]` 标为 `[YD]`。关键结论须多源交叉验证。

## CN法律援助体系

### 法律援助范围
- 刑事辩护/代理
- 民事诉讼代理（经济困难者）
- 劳动争议
- 婚姻家庭

### 申请条件
- 经济困难认定（低收入户/五保户）
- 特殊群体（残疾人/老年人/妇女）
- 刑事案件（可能被判处死刑/无期）

---

## CN法律援助申请流程

1. 申请提交（法律援助中心）
2. 经济状况审查
3. 案件审批
4. 指派律师
5. 案件办理
6. 结案归档

---

---

## 输出格式

所有正式输出须在文档开头标注特权头部标记（参见 ## Who's using this），并遵守以下格式要求：

- 法律分析结论须标注数据来源标记
- 涉及法条引用须标明具体条款及生效版本
- 案件咨询记录须包含客户编号（如有）和咨询日期
- 涉及法律援助申请的须注明申请人信息和审查进度

## 升级决策门

以下情形必须升级给主管律师：
1. 涉及刑事案件的辩护策略
2. 涉及重大民事案件的诉讼方案
3. 涉及当事人权益可能受到损害的紧急情形
4. 涉及法律援助资格认定的争议
5. 学生无法独立处理的专业法律问题

## 推理原子能力

本场景在执行 legal analysis 时，按需调用以下 `legal-atomic` 原子 skill：

| 原子 Skill | 用途 | 调用时机 |
|-----------|------|---------|
| `legal-element-extraction` | 法律要素提取 | 所有输入预处理——将非结构化叙述转化为法律事实 |
| `legal-norm-validity-check` | 法条效力核查 | 引用法条前验证是否现行有效 |
| `deductive-reasoning` | P-F-C三段论推理 | 构建法律推理链时 |
| `legal-risk-assessment` | 法律风险评估 | 涉及风险分级判断时 |
| `conflict-resolution` | 法条竞合/冲突解决 | 多个法条或请求权竞合时 |
| `case-retrieval` | 类案检索方法论 | 需要检索类案时 |
| `trial-scheduling-and-deadline-monitoring` | 期限管理 | 涉及诉讼/仲裁期限时 |

---

*Greater China Legal — legal-clinic CN adapter v1.0.0*