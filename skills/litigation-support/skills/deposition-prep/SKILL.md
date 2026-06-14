---
name: deposition-prep
description: '为证人构建 deposition outline — 从案件理论组织话题，呈现弹劾材料。 适用情形：用户要求"某证人depo prep"或"构建depo
  outline"。

  '
argument-hint: '[证人名称]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
- 取证
- 询问
- 质证
legal_sources:
- name: 中华人民共和国民法典
  effective_date: '2021-01-01'
---

## 数据源与判断框架引用

本 skill 引用以下 plugin 根级 references：

- **判断框架**：`../../references/判断框架.md`（诉讼全流程 35 skill + 14 类时效 + 案由分析 + 管辖判断 + 证据规则 + 保全 + 强制措施 + 执行 + 行政复议/诉讼 + 案件管理 + 上诉 + 刑事案件 + 政府合同）
- **数据源清单**：`../../references/数据源清单.md`（[YD]/[WKL]/[GOV]/[BD]/[model] + 最高法司法解释 + 法院体系 + 仲裁机构 + 知产法院 + 涉外）
- **查询路径**：`../../references/查询路径.md`（法规 + 案例 + 司法解释）
- **货币触发主题**：`../../../references/currency-watch.md`
- **数据源注册表**：`../../../references/data-source-registry.md`

来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）详见 `../../references/数据源清单.md` §十一。
诉讼时效详见 `../../references/判断框架.md` §三（**时效管理是高风险点**）。

# /deposition-prep — China Mainland

## CN证人准备要点

### 证人分类

| 证人类型 | 准备重点 |
|---|---|
| 我方证人 | 强化有利事实、准备弹劾对方的问题 |
| 对方证人 | 找出矛盾、挑战可信度 |
| 专家证人 | 技术/财务问题的专业意见 |
| 事实证人 | 与案件事实的直接接触 |

---

### CN Deposition特殊说明

**CN场景下：** 证人证言主要用于：
- 劳动仲裁的证人证言
- 民事诉讼的证人出庭
- 公证保全的证人证言

**注意：** CN民事诉讼中证人出庭较少，更多依赖书面证据。

---

## 准备大纲结构

### 1. 背景问题
- 与案件的关联
- 与当事人的关系
- 在事件中的角色

### 2. 关键文件问题
- 文件的形成过程
- 对文件内容的了解
- 与文件相关的决策

### 3. 案件理论话题
- 支持我方理论的事实
- 挑战对方理论的事实

### 4. 弹劾材料
- 之前陈述的矛盾
- 与书面证据的冲突
- 偏见/利益冲突

---

## 输出格式

```
## Deposition Outline — [证人名称]

### 证人信息
- 类型：[我方/对方/专家/事实]
- 与案件关联：[描述]

### 大纲结构

#### 背景
- [问题] — [目的]

#### 关键文件
- [问题] — [目的]

#### 案件理论话题
- [问题] — [目的]

#### 弹劾材料（如有）
- [矛盾点] — [来源]

### 注意事项
[须特别关注的点]
```

---

*Greater China Legal — litigation-legal deposition-prep CN adapter v1.0.0*