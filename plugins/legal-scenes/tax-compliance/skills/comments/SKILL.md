---
name: comments
description: >
  管理监管意见提交——追踪须提交意见的法规和已提交的评论。
  适用情形：追踪征求意见稿并组织提交监管意见。
argument-hint: "[列出/添加/提交意见]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
trigger_phrases:
  - '税务'
  - '所得税'
  - '增值税'
  - '转让定价'
---

# /comments — China Mainland

## Purpose

监管意见提交是影响立法的重要机会。本技能追踪须提交意见的法规和组织意见提交。

---

## CN立法意见提交机制

**适用情形：** 国务院部委/人大就法规草案向社会征求意见

**提交渠道：**
- 主管部门官网在线提交
- 电子邮件
- 邮寄书面意见

**注意事项：**
- 须在截止日期前提交
- 须明确说明意见对应的条款
- 须提供修改建议而非仅表达反对

---

## CN常见须提交意见的法规

| 类型 | 说明 |
|---|---|
| 部门规章 | 各部委发布，须公示征求意见 |
| 规范性文件 | 重大政策须公示征求意见 |
| 国家标准 | 重要国家标准须公示征求意见 |
| 行业标准 | 行业协会标准须公示征求意见 |

---

## 意见追踪文件

文件路径：`regulatory-legal/comment-tracker.yaml`

```yaml
comments:
  - id: COMMENT-001
    regulation: "[法规名称]"
    issuing_authority: "[发布机关]"
    comment_deadline: 2026-03-01
    status: "pending"  # pending | submitted | withdrawn | not-submitted
    submitted_date: ""
    key_points: "[主要意见要点]"
    outcome: ""  # 意见是否被采纳
```

---

## 输出格式

```
## 监管意见追踪报告

### 🔴 即将截止（7日内）
[法规名称] — 截止：[日期] — 须提交意见

### 🟠 意见征集中
[法规名称] — 截止：[日期] — [状态]

### ✅ 已提交
[法规名称] — 提交日期：[日期] — 采纳情况：[待确认/已采纳/未采纳]
```

---

*Greater China Legal — regulatory-legal comments CN adapter v1.0.0*