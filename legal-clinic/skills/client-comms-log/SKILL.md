---
name: client-comms-log
description: >
  CN法律援助当事人沟通记录——追踪与当事人的所有沟通。
  适用情形：记录与援助申请人的每次沟通。
argument-hint: "[案件ID] [--add | --list]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

# /client-comms-log — China Mainland

## CN法律援助沟通记录

### 记录要素

- 日期
- 沟通方式（电话/面谈/书面）
- 内容摘要
- 须跟进的的事项

---

## 沟通记录文件

`comms-log.yaml`:
```yaml
comms:
  - date: YYYY-MM-DD
    method: "phone | in-person | written"
    summary: "[摘要]"
    follow_up: "[须跟进事项]"
    status: "pending | completed"
```

---

*Greater China Legal — legal-clinic client-comms-log CN adapter v1.0.0*