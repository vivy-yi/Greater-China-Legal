---
name: deadlines
description: >
  CN法律援助案件截止日期管理——追踪重要时间节点。
  适用情形：管理案件中的法定期限和重要日期。
argument-hint: "[案件ID] [--list | --add | --check]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# /deadlines — China Mainland

## CN法律援助案件截止日期

### 重要法定期限

| 期限类型 | 时效/期间 | 备注 |
|---|---|---|
| 劳动争议仲裁 | 60日 | 知道权利被侵害之日起 |
| 民事诉讼时效 | 3年 | 一般合同纠纷 |
| 刑事辩护委托 | 随时 | 可随时委托 |
| 上诉期限 | 15日 | 判决送达之日起 |

---

## 截止日期追踪文件

`deadlines.yaml`:
```yaml
deadlines:
  - case_id: "[案件ID]"
    event: "[事项]"
    due_date: YYYY-MM-DD
    status: "pending | completed | missed"
    notified: true/false
```

---

*Greater China Legal — legal-clinic deadlines CN adapter v1.0.0*