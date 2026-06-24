# 首次问询协议 — m-and-a 24 字段

> 来源:scene-claudemd-curator `learn-patterns.md` § 0.7 + § 0.19
> 适用:agent 第一次跑 m-and-a / § 9.0 首次使用协议触发 / 用户主动说"重新配置"
> **规则:任何字段为空 → 不要执行任务,先问用户填表**

---

## 0. 触发判断

**进入本协议的条件** —— 满足任一即触发:

| 条件 | 检测方法 |
|------|--------|
| `~/.claude/plugins/config/greater-china-legal/m-and-a/CLAUDE.md` 不存在 | 检查运行配置 |
| 24 字段中 ≥ 1 个为空 | YAML 校验 |
| 用户说"重新配置" / "我们换 deal 了" / "新交易" | 用户意图 |
| § 9.0 "首次使用协议" 被调用 | skill 路由 |

**退出条件**:24 字段全部填完 + 用户确认 + 写入运行配置。

---

## 1. 24 字段分组(6 大类)

### 1.1 公司基本信息(8 字段)

| # | 字段 | 必填 | 示例 | 备注 |
|---|------|-----|------|------|
| 1 | `company_name` | ✅ | "阿里集团" | 公司全称 |
| 2 | `entity_type` | ✅ | "股份有限公司" | 有限责任公司/股份/外资/国企/上市公司 |
| 3 | `industry` | ✅ | "互联网/电商" | 所属行业 |
| 4 | `stage` | ✅ | "上市" | 初创/成长/上市前/上市/国资 |
| 5 | `deal_role` | ✅ | "buyer" | buyer / seller / target / advisor |
| 6 | `deal_size` | ✅ | "5 亿人民币" | 当前主交易规模 |
| 7 | `external_counsel` | ✅ | "汉坤律所" | 外部律师 |
| 8 | `financial_advisor` | ⚠️ | "中金公司" | 财务顾问 |

### 1.2 角色(Pattern 13 — 5 档)

| # | 字段 | 必填 | 5 档选项 | 默认 header |
|---|------|-----|---------|----------|
| 9 | `role` | ✅ | `Lawyer` / `Accountant` / `Appraiser` / `Investment` / `Non_lawyer` | 见 § 9.1 |

**5 档 work-product header**:
- `Lawyer` → "律师执业秘密——律师工作成果"
- `Accountant` → "注册会计师工作底稿——不构成律师意见"
- `Appraiser` → "评估师工作成果——不构成律师意见"
- `Investment` → "投资经理内部参考——请律师审阅"
- `Non_lawyer` → "参考资料——非法律意见——请律师审阅"

### 1.3 法域(Pattern 7+16)

| # | 字段 | 必填 | 5 档 | 备注 |
|---|------|-----|------|------|
| 10 | `jurisdictions` | ✅ | `cn-mainland` / `hk` / `mo` / `tw` / `sg` / `us` / `eu` | 至少 1 个 |
| 11 | `cross_border_deal` | ✅ | true/false | 是否跨境 |
| 12 | `target_jurisdiction` | ⚠️ | "" | 标的公司所在法域 |

### 1.4 数据源(Pattern 4)

| # | 字段 | 必填 | 选项 | fallback |
|---|------|-----|------|---------|
| 13 | `sources.gov` | ✅ | true | 国家市场监管总局/证监会（默认） |
| 14 | `sources.pkulaw` | ⚠️ | true/false | web_search |
| 15 | `sources.wind` | ⚠️ | true/false | pkulaw |
| 16 | `sources.fallback` | ✅ | `web_search` / `bing` | — |

### 1.5 升级路径(Pattern 6+17 — 4 档)

| # | 字段 | 必填 | 阈值 | 升给 |
|---|------|-----|------|------|
| 17 | `approval_chain.junior` | ✅ | <1 亿 | senior(邮件) |
| 18 | `approval_chain.senior` | ✅ | 1-10 亿 / 上市公司 | gc(邮件+会议) |
| 19 | `approval_chain.gc` | ✅ | >10 亿 / 跨境 / 反垄断触发 | ceo(邮件+董事会) |
| 20 | `approval_chain.ceo` | ✅ | 国资 / 重大 / 跨境重大 | board(会议+文件) |

### 1.6 关键阈值 + house style(4 字段)

| # | 字段 | 必填 | 默认 | 备注 |
|---|------|-----|------|------|
| 21 | `antitrust_china_revenue_threshold` | ✅ | "" | 反垄断申报阈值(单一/合计 4 亿/20 亿) |
| 22 | `listing_exchange` | ⚠️ | "" | 沪/深/北/港/纳斯达克/纽交所 |
| 23 | `memo_destination` | ⚠️ | "" | 飞书/钉钉/邮件 |
| 24 | `deal_closure_style` | ✅ | "谨慎" | 谨慎/标准/快速 |

---

## 2. YAML 完整 schema(写入运行配置)

```yaml
# ~/.claude/plugins/config/greater-china-legal/m-and-a/CLAUDE.md

# === 公司基本信息 ===
company_name: ""
entity_type: ""
industry: ""
stage: ""
deal_role: ""
deal_size: ""
deal_currency: "CNY"
external_counsel: ""
financial_advisor: ""

# === 角色 ===
role: ""

# === 法域 ===
jurisdictions:
  - cn-mainland
cross_border_deal: false
target_jurisdiction: ""

# === 数据源 ===
sources:
  gov: true
  pkulaw: false
  wind: false
fallback: web_search

# === 升级路径 ===
approval_chain:
  junior: { threshold: "<1 亿", escalate_to: senior, via: "邮件" }
  senior: { threshold: "1-10 亿 / 上市公司", escalate_to: gc, via: "邮件+会议" }
  gc: { threshold: ">10 亿 / 跨境 / 反垄断触发", escalate_to: ceo, via: "邮件+董事会" }
  ceo: { threshold: "国资 / 重大 / 跨境重大", escalate_to: board, via: "会议+文件" }

# === 关键阈值 ===
antitrust_china_revenue_threshold: ""
antitrust_china_revenue_party: ""
antitrust_china_revenue_other: ""
listing_exchange: ""

# === house style ===
memo_destination: ""
deal_closure_style: ""

# === YAML 注册表（Pattern 2 + 14）===
# deals.yaml —— per-deal 18 字段
# target-companies.yaml —— 标的公司登记
# regulatory-approvals.yaml —— 审批进度登记
```

---

## 3. 主动问对话脚本(双模式)

### 模式 A: 快速配置(2 步) — 推荐试用场景

**适用场景**:用户说"我想先试试" / "快速配置一下"。

**Step 1: 公司名 + 角色 + deal 角色(3 字段)**
"请问公司全称 + 您本人角色?(律师/会计师/评估师/投资经理/业务) + 您在当前 deal 是 buyer/seller/target/advisor?"

**Step 2: 用默认配置开始**
"已用默认配置初始化。跨境/上市公司/反垄断触发/国资场景,会主动补问。"

---

### 模式 B: 完整配置(5 步) — 推荐生产场景

**适用场景**:用户说"完整配置" / "我们要做 IPO 重组" / "我们要跨境并购"。

**Step 1: 触发判断**
"检测到本场景首次使用。我需要先了解贵公司基本信息 + 当前 deal 概况。"

**Step 2: 公司基本信息(8 字段)**
"请问:1) 公司全称 2) 公司类型 3) 行业 4) 发展阶段 5) 您在 deal 是 buyer/seller/target/advisor? 6) 交易规模 7) 外部律师 8) 财务顾问?"

**Step 3: 角色(1 字段)**
"您本人是律师 / 注册会计师 / 评估师 / 投资经理 / 业务?"

**Step 4: 法域 + 数据源(7 字段)**
"请问:是否跨境? 标的所在法域? yuandian/pkulaw/wind 是否已配置? 反垄断申报阈值是否清楚?"

**Step 5: 升级路径 + house style(8 字段)**
"最后:4 档审批人是谁? 反垄断阈值多少? 上市公司? memo 飞书/钉钉/邮件? deal 节奏 谨慎/标准/快速?"

---

## 4. 已知不重复规则(Pattern § 0.9)

**用户已说明的事实不重复问。** 例如:
- 用户说"我们做的是 A 股上市公司收购" → 不要重复问"是否上市公司"
- 用户说"标的是美国公司" → 不要重复问"是否跨境"
- 用户说"5 亿人民币" → 不要重复问"deal_size"

---

*Greater China Legal — m-and-a onboarding v3*
*24 字段首次问询 + 双模式(快速/完整)*
*最后更新:2026-06-20*