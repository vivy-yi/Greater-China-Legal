---
name: gaps
description: >
  管理监管合规差距——追踪开放的政策缺口和补救状态。
  适用情形：追踪监管新规与内部政策之间的差距，直到差距关闭。
argument-hint: "[列出/添加/更新/关闭差距]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

# /gaps — China Mainland

## Purpose

监管差距被找出后容易被遗忘。本技能追踪差距直到关闭，并通知责任人。

---

## 差距追踪文件

文件路径：`regulatory-legal/gap-tracker.yaml`

```yaml
gaps:
  - id: GAP-001
    requirement: "[监管要求]"
    regulation: "[法规名称+条款]"
    policy_affected: "[受影响的政策名称]"
    gap_type: "partial"  # none | partial | full | new-policy | watch | comment-decision
    owner: "[责任人]"
    owner_slack: "[Slack ID]"
    opened: 2026-01-01
    due: 2026-06-01  # 监管生效日期或内部截止日期
    status_verified: true
    status: "open"  # open | in-progress | closed | risk-accepted
    notified: false
    resolution: ""  # 关闭时填写
```

---

## CN监管合规差距分析框架

### Step 1：识别监管新规要求

**CN主要监管领域及关键法规：**

| 领域 | 核心法规 | 生效日期 |
|---|---|---|
| 数据安全 | 《数据安全法》2021-09-01 | 2021-09-01 |
| 个人信息保护 | 《个人信息保护法》2021-11-01 | 2021-11-01 |
| 算法推荐 | 《互联网信息服务算法推荐管理规定》2022-03-01 | 2022-03-01 |
| App治理 | 《移动互联网应用程序信息服务管理规定》2022-08-01 | 2022-08-01 |
| 反垄断 | 《反垄断法》2022-08-01修订 | 2022-08-01 |
| 网络安全 | 《网络安全法》2017-06-01 | 2017-06-01 |

---

### Step 2：对照内部政策

- 内部政策是否涵盖该要求？
- 要求是否已被完整落实？
- 是否存在执行空白？

---

### Step 3：差距分类

| gap_type | 含义 |
|---|---|
| none | 政策已覆盖且已落实 |
| partial | 政策已覆盖但部分落实 |
| full | 政策未覆盖或重大缺口 |
| new-policy | 需要制定新政策 |
| watch | 须持续监控 |
| comment-decision | 须提交立法意见 |

---

### Step 4：补救状态

| status | 含义 |
|---|---|
| open | 待处理 |
| in-progress | 进行中 |
| closed | 已关闭 |
| risk-accepted | 风险已接受（高管决策）|

---

## 输出格式

```
## 监管合规差距报告

### 🔴 紧急（监管生效日期临近）
[GAP-ID] [法规] — [差距描述] — 截止：[日期]

### 🟠 进行中
[GAP-ID] [法规] — [差距描述] — 责任人：[名称]

### 🟡 待处理
[GAP-ID] [法规] — [差距描述] — 截止：[日期]

### ✅ 已关闭
[GAP-ID] [法规] — [补救措施] — 关闭日期：[日期]
```

---

*Greater China Legal — regulatory-legal gaps CN adapter v1.0.0*