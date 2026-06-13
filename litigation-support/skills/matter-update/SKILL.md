---
name: matter-update
description: '向案件历史文件追加带日期的事件——记录新进展、状态变化、风险重评估。 适用情形：用户要"记录案件更新"、"记下新进展"。

  '
argument-hint: '[slug] [简要事件描述]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
trigger_phrases:
- 案件进展
- 诉讼更新
legal_sources:
- name: 中华人民共和国民法典
  effective_date: '2021-01-01'
---

# /matter-update — China Mainland

## 更新内容

**事件类型：**
- 新进展
- 状态变化
- 风险重评估
- 截止日期变化
- 和解权限变化

**默认日期：** 今天

---

## 输出

- 追加带日期条目到 `history.md`
- 更新 `_log.yaml` 中的 `last_updated` 为今天
- 应用任何字段更新

---

*Greater China Legal — litigation-legal matter-update CN adapter v1.0.0*