---
name: legal-hold
description: '发出/刷新/释放/报告法律保留通知——更新_log.yaml中的legal_hold字段。 适用情形：用户说"发出保留"、"刷新保留"、"释放保留"。

  '
argument-hint: '[slug] [--issue | --refresh | --release | --status]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
- 证据保全
- 诉讼保全
legal_sources:
- name: 中华人民共和国民法典
  effective_date: '2021-01-01'
---

# /legal-hold — China Mainland

## CN证据保留特殊说明

**CN法律下的证据保留义务：**
- 《民事诉讼法》第68条：证据应当妥善保管
- 劳动争议：仲裁时效60日内相关证据须保留
- 合同纠纷：合同履行期间及结束后3年相关证据须保留

---

## CN Legal Hold触发情形

| 情形 | 保留内容 | 期限 |
|---|---|---|
| 劳动争议 | 劳动合同/工资发放/解除文件 | 仲裁+诉讼结束 |
| 合同纠纷 | 合同/往来函件/付款凭证 | 诉讼时效期间+2年 |
| 知识产权 | 设计图纸/源代码/发表记录 | 至侵权诉讼结束 |
| 监管调查 | 所有相关文件 | 调查结束+保存期 |

---

## CN Legal Hold通知要素

**通知须包含：**
1. 保留范围（哪些文件/数据）
2. 保留期间（开始日期+结束条件）
3. 保管人责任
4. 违规后果
5. 联系方式

---

## 输出格式

### --issue（发出）
```
## Legal Hold — [案件名称]

### 保留范围
[具体描述]

### 保管人
[人员列表]

### 保留期限
[开始日期] — [结束条件]

---
⚠️ 须在发出前确认法院/仲裁机构的保留令（如有）
```

### --status（状态报告）
```
## Legal Hold Portfolio Report

### 🔴 活跃保留
[案件] — 发出日期：[日期] — 下次刷新：[日期]

### 🟠 即将刷新（30日内）
[案件] — 下次刷新：[日期]

### ✅ 已释放
[案件] — 释放日期：[日期]
```

---

*Greater China Legal — litigation-legal legal-hold CN adapter v1.0.0*