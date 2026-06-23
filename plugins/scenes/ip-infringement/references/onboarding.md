# 首次问询协议 — ip-infringement 24 字段

> 来源:scene-claudemd-curator `learn-patterns.md` § 0.7 + § 0.19
> 适用:agent 第一次跑 ip-infringement / § 9.0 首次使用协议触发 / 用户主动说"重新配置"
> **规则:任何字段为空 → 不要执行任务,先问用户填表**

---

## 0. 触发判断

**进入本协议的条件** —— 满足任一即触发:

| 条件 | 检测方法 |
|------|--------|
| `~/.claude/plugins/config/greater-china-legal/ip-infringement/CLAUDE.md` 不存在 | 检查运行配置 |
| 24 字段中 ≥ 1 个为空 | YAML 校验 |
| 用户说"重新配置" / "我们新增 IP 资产了" | 用户意图 |
| § 9.0 "首次使用协议" 被调用 | skill 路由 |

**退出条件**:24 字段全部填完 + 用户确认 + 写入运行配置。

---

## 1. 24 字段分组(6 大类)

### 1.1 公司基本信息(7 字段)

| # | 字段 | 必填 | 示例 | 备注 |
|---|------|-----|------|------|
| 1 | `company_name` | ✅ | "华为技术有限公司" | 公司全称 |
| 2 | `entity_type` | ✅ | "股份有限公司" | 有限责任公司/股份/外资/国企/上市公司 |
| 3 | `industry` | ✅ | "通信/电子" | 所属行业 |
| 4 | `stage` | ✅ | "上市" | 初创/成长/上市前/上市/国资 |
| 5 | `ip_role` | ✅ | "right-holder" | right-holder / accused / neutral / advisor |
| 6 | `external_ip_counsel` | ✅ | "柳沈律所" | 外部 IP 律师 |
| 7 | `ip_management_head` | ✅ | "张三" | IP 管理负责人 |

### 1.2 角色(Pattern 13 — 5 档)

| # | 字段 | 必填 | 5 档选项 | 默认 header |
|---|------|-----|---------|----------|
| 8 | `role` | ✅ | `Lawyer` / `Patent_Agent` / `IP_Legal` / `Engineer` / `Non_lawyer` | 见 § 9.1 |

**5 档 work-product header**:
- `Lawyer` → "律师执业秘密——律师工作成果"
- `Patent_Agent` → "专利代理人工作成果——不构成律师意见"
- `IP_Legal` → "IP 法务内部参考——请律师审阅"
- `Engineer` → "技术参考资料——请 IP 律师审阅"
- `Non_lawyer` → "参考资料——非法律意见——请律师审阅"

### 1.3 法域(Pattern 7+16)

| # | 字段 | 必填 | 5 档 | 备注 |
|---|------|-----|------|------|
| 9 | `jurisdictions` | ✅ | `cn-mainland` / `hk` / `mo` / `tw` / `sg` / `us` / `eu` / `jp` | 至少 1 个 |
| 10 | `cross_border_ip` | ✅ | true/false | 是否跨境 IP |
| 11 | `target_jurisdictions` | ⚠️ | [us, eu, jp] | 涉及国家/地区列表 |

### 1.4 数据源(Pattern 4)

| # | 字段 | 必填 | 选项 | fallback |
|---|------|-----|------|---------|
| 12 | `sources.gov` | ✅ | true | 国知局/版权局（默认） |
| 13 | `sources.cnipa` | ✅ | true | 中国专利电子申请网 |
| 14 | `sources.yuandian` | ⚠️ | true/false | web_search |
| 15 | `sources.pkulaw` | ⚠️ | true/false | yuandian |
| 16 | `sources.fallback` | ✅ | `web_search` / `bing` | — |

### 1.5 升级路径(Pattern 6+17 — 4 档)

| # | 字段 | 必填 | 阈值 | 升给 |
|---|------|-----|------|------|
| 17 | `approval_chain.junior` | ✅ | <10 万赔偿 / 单次侵权 | senior(邮件) |
| 18 | `approval_chain.senior` | ✅ | 10-100 万 / 批量 / 跨境 | gc(邮件+会议) |
| 19 | `approval_chain.gc` | ✅ | >100 万 / SEP / 跨境重大 | ceo(邮件+董事会) |
| 20 | `approval_chain.ceo` | ✅ | 刑事 / 上市公司 / 重大跨境 | board(会议+文件) |

### 1.6 IP 资产 + house style(4 字段)

| # | 字段 | 必填 | 默认 | 备注 |
|---|------|-----|------|------|
| 21 | `ip-portfolio.yaml` 资产总数 | ⚠️ | 0 | 商标/专利/著作权/商业秘密总数 |
| 22 | `ip-portfolio.yaml` 跨境资产数 | ⚠️ | 0 | 涉外 IP 资产 |
| 23 | `memo_destination` | ⚠️ | "" | 飞书/钉钉/邮件 |
| 24 | `enforcement_style` | ✅ | "协商" | 协商/行政/民事/刑事 |

---

## 2. YAML 完整 schema(写入运行配置)

```yaml
# ~/.claude/plugins/config/greater-china-legal/ip-infringement/CLAUDE.md

# === 公司基本信息 ===
company_name: ""
entity_type: ""
industry: ""
stage: ""
ip_role: ""
external_ip_counsel: ""
ip_management_head: ""

# === 角色 ===
role: ""

# === 法域 ===
jurisdictions:
  - cn-mainland
cross_border_ip: false
target_jurisdictions: []

# === 数据源 ===
sources:
  gov: true
  cnipa: true
  yuandian: false
  pkulaw: false
fallback: web_search

# === 升级路径 ===
approval_chain:
  junior: { threshold: "<10 万赔偿 / 单次侵权", escalate_to: senior, via: "邮件" }
  senior: { threshold: "10-100 万 / 批量 / 跨境", escalate_to: gc, via: "邮件+会议" }
  gc: { threshold: ">100 万 / 标准必要专利 / 跨境重大", escalate_to: ceo, via: "邮件+董事会" }
  ceo: { threshold: "刑事 / 上市公司 / 重大跨境", escalate_to: board, via: "会议+文件" }

# === IP 资产登记（Pattern 1 + 14）===
ip_portfolio_count: 0
ip_portfolio_cross_border: 0

# === house style ===
memo_destination: ""
enforcement_style: ""

# === YAML 注册表 ===
# ip-portfolio.yaml —— per-IP 资产 18 字段
# infringement-cases.yaml —— 维权案件登记
# ip-licenses.yaml —— 许可合同登记
```

---

## 3. 主动问对话脚本(双模式)

### 模式 A: 快速配置(2 步) — 推荐试用场景

**Step 1: 公司名 + IP 角色(2 字段)**
"请问公司全称 + 您在 IP 事务中是 right-holder(权利方)/accused(被控侵权方)/neutral(中立分析)/advisor(顾问)?"

**Step 2: 用默认配置开始**
"已用默认配置初始化。涉及驰名商标 / SEP / 跨境电商 / 商业秘密刑事 / 上市公司 时,会主动补问。"

---

### 模式 B: 完整配置(5 步) — 推荐生产场景

**Step 1: 触发判断**
"检测到本场景首次使用。我需要先了解贵公司基本信息 + IP 资产概况。"

**Step 2: 公司基本信息(7 字段)**
"请问:1) 公司全称 2) 类型 3) 行业 4) 发展阶段 5) IP 角色 6) 外部 IP 律师 7) IP 管理负责人?"

**Step 3: 角色(1 字段)**
"您本人是律师 / 专利代理人 / IP 法务 / 业务 / 工程师?"

**Step 4: 法域 + 数据源(7 字段)**
"请问:是否跨境 IP? 涉及哪些国家/地区? yuandian / pkulaw 是否已配置?"

**Step 5: 升级路径 + IP 资产 + house style(9 字段)**
"最后:4 档审批人? 商标/专利/著作权/商业秘密资产总数? 涉外 IP 资产数? memo 飞书/钉钉/邮件? 维权风格 协商/行政/民事/刑事?"

---

## 4. 已知不重复规则(Pattern § 0.9)

**用户已说明的事实不重复问。** 例如:
- 用户说"我们是手机公司" → 推断属于消费电子行业,不再重复问"行业"
- 用户说"我们有 200 个商标" → 不要再问"商标数量"
- 用户说"我们做跨境电商到亚马逊" → 推断跨境 IP,不再问"是否跨境"

---

*Greater China Legal — ip-infringement onboarding v3*
*24 字段首次问询 + 双模式*
*最后更新:2026-06-20*