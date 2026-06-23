# 首次问询协议 — tax-compliance 24 字段

> 来源:scene-claudemd-curator `learn-patterns.md` § 0.7
> 适用:agent 第一次跑 tax-compliance / § 9.0 首次使用协议触发 / 用户主动说"重新配置"
> **规则:任何字段为空 → 不要执行任务,先问用户填表**

---

## 0. 触发判断

**进入本协议的条件** —— 满足任一即触发:

| 条件 | 检测方法 |
|------|--------|
| `~/.claude/plugins/config/greater-china-legal/tax-compliance/CLAUDE.md` 不存在 | 检查运行配置 |
| 24 字段中 ≥ 1 个为空 | YAML 校验 |
| 用户说"重新配置" / "我们换公司了" / "我要做另一家" | 用户意图 |
| § 9.0 "首次使用协议" 被调用 | skill 路由 |

**退出条件**:24 字段全部填完 + 用户确认 + 写入运行配置。

---

## 1. 24 字段分组(6 大类)

### 1.1 公司基本信息(10 字段)

| # | 字段 | 必填 | 示例 | 备注 |
|---|------|-----|------|------|
| 1 | `company_name` | ✅ | "小米科技有限责任公司" | 公司全称 |
| 2 | `entity_type` | ✅ | "有限责任公司" | 有限责任公司/股份有限公司/外资/国企/上市公司 |
| 3 | `industry` | ✅ | "电子制造" | 所属行业 |
| 4 | `stage` | ✅ | "上市" | 初创/成长/上市前/上市/国资 |
| 5 | `taxpayer_type` | ✅ | "一般纳税人" | 一般纳税人/小规模纳税人 |
| 6 | `cit_status` | ✅ | "居民企业" | 居民企业/非居民企业 |
| 7 | `registered_location` | ✅ | "北京市海淀区税务局" | 主管税务机关 |
| 8 | `tax_director` | ✅ | "张三" | 税务负责人 |
| 9 | `external_tax_advisor` | ⚠️ | "普华永道北京" | 外部税务师/律师 |
| 10 | `uscc` | ⚠️ | "91110108MA1234567X" | 统一社会信用代码 |

### 1.2 角色(Pattern 13 — 5 档)

| # | 字段 | 必填 | 5 档选项 | 默认 header |
|---|------|-----|---------|----------|
| 11 | `role` | ✅ | `Lawyer` / `Accountant` / `Tax_agent` / `Finance` / `Non_tax` | 见 § 9.1 |

**5 档 work-product header**:
- `Lawyer` → "律师执业秘密——律师工作成果"
- `Accountant` → "注册会计师工作底稿——不构成律师意见"
- `Tax_agent` → "税务师工作成果——不构成律师意见"
- `Finance` → "财务内部参考——请税务师审阅"
- `Non_tax` → "参考资料——非税务意见——请税务师审阅"

### 1.3 法域(Pattern 7+16)

| # | 字段 | 必填 | 5 档 | 备注 |
|---|------|-----|------|------|
| 12 | `jurisdictions` | ✅ | `cn-mainland` / `hk` / `mo` / `tw` / `sg` | 至少 1 个 |
| 13 | `foreign_shareholders` | ⚠️ | true/false | 是否有外籍股东 → 触发 [域外] 法源 |
| 14 | `cross_border_transactions` | ⚠️ | true/false | 是否有跨境交易 |
| 15 | `overseas_subsidiaries` | ⚠️ | 0 | 海外子公司数量 |

### 1.4 数据源(Pattern 4)

| # | 字段 | 必填 | 选项 | fallback |
|---|------|-----|------|---------|
| 16 | `sources.gov` | ✅ | true | 国家税务总局/财政部（默认开启） |
| 17 | `sources.yuandian` | ⚠️ | true/false | web_search |
| 18 | `sources.pkulaw` | ⚠️ | true/false | yuandian |
| 19 | `sources.fallback` | ✅ | `web_search` / `bing` / `brave` | — |

### 1.5 升级路径(Pattern 6+17 — 4 档)

| # | 字段 | 必填 | 阈值 | 升给 |
|---|------|-----|------|------|
| 20 | `approval_chain.junior` | ✅ | <100 万税额 | senior(邮件) |
| 21 | `approval_chain.senior` | ✅ | 100-1000 万 / 高风险 | tax_director(邮件+会议) |
| 22 | `approval_chain.tax_director` | ✅ | >1000 万 / 跨境 / 转让定价 | cfo(邮件+董事会) |
| 23 | `approval_chain.cfo` | ✅ | 重大 / 偷税 / 虚开嫌疑 | ceo(会议+文件) |

### 1.6 关键阈值 + house style(1 字段)

| # | 字段 | 必填 | 默认 | 备注 |
|---|------|-----|------|------|
| 24 | `vat_rate_default` / `cit_rate_default` / `small_low_profit_threshold` / `rd_super_deduction_ratio` / `memo_destination` / `dispute_response_style` / `audit_preparation_style` | ✅ | 见 § 9.1 | 7 子字段 |

---

## 2. YAML 完整 schema(写入运行配置)

```yaml
# ~/.claude/plugins/config/greater-china-legal/tax-compliance/CLAUDE.md
# (运行配置,agent 每次开始对话都读这个)

# === 公司基本信息 ===
company_name: ""
entity_type: ""
industry: ""
stage: ""
taxpayer_type: ""
cit_status: ""
registered_location: ""
tax_director: ""
external_tax_advisor: ""
uscc: ""

# === 角色（Pattern 13 — 5 档）===
role: ""

# === 法域（Pattern 16）===
jurisdictions:
  - cn-mainland
foreign_shareholders: false
cross_border_transactions: false
overseas_subsidiaries: 0

# === 数据源（Pattern 4）===
sources:
  gov: true
  yuandian: false
  pkulaw: false
fallback: web_search

# === 升级路径（Pattern 6+17 — 4 档）===
approval_chain:
  junior: { threshold: "<100 万税额", escalate_to: senior, via: "邮件" }
  senior: { threshold: "100-1000 万 / 高风险", escalate_to: tax_director, via: "邮件+会议" }
  tax_director: { threshold: ">1000 万 / 跨境 / 转让定价", escalate_to: cfo, via: "邮件+董事会" }
  cfo: { threshold: "重大 / 偷税 / 虚开嫌疑", escalate_to: ceo, via: "会议+文件" }

# === 关键阈值 ===
vat_rate_default: 0.13
cit_rate_default: 0.25
small_low_profit_threshold: 0
rd_super_deduction_ratio: 1.00

# === house style ===
memo_destination: ""
dispute_response_style: ""
audit_preparation_style: ""

# === YAML 注册表（Pattern 2 + 14）===
# tax-entities.yaml —— per-纳税主体 18 字段
# transaction-register.yaml —— 关联交易登记
# tax-preference-register.yaml —— 税收优惠资质登记
```

---

## 3. 主动问对话脚本(双模式)

### 模式 A: 快速配置(2 步) — 推荐试用场景

**适用场景**：用户说"我想先试试" / "快速配置一下"。

**Step 1: 公司名 + 角色(2 字段)**
"请问公司全称 + 您本人角色?(律师/税务师/财务/业务)"

**Step 2: 用默认配置开始**
"已用默认配置初始化。涉及跨境/转让定价/重大优惠资质时,会主动补问。"

---

### 模式 B: 完整配置(5 步) — 推荐生产场景

**适用场景**：用户说"完整配置" / "我们要做 IPO 税务合规"。

**Step 1: 触发判断**
"检测到本场景首次使用。我需要先了解贵公司基本信息才能执行任务。需要您回答以下 24 个字段。"

**Step 2: 公司基本信息(10 字段)**
"请问:
1. 公司全称 + 统一社会信用代码?
2. 公司类型?（有限责任公司/股份/外资/国企/上市）
3. 所属行业?
4. 发展阶段?（初创/成长/上市前/上市/国资）
5. 纳税人类型?（一般/小规模）
6. 企业所得税身份?（居民/非居民）
7. 主管税务机关?
8. 内部税务负责人?
9. 是否有外部税务顾问?"

**Step 3: 角色(1 字段)**
"您本人是律师 / 注册会计师 / 税务师 / 财务 / 业务?"(决定输出 header 5 档)

**Step 4: 法域 + 数据源 + 升级路径(11 字段)**
"请问:
- 是否有外籍股东?
- 是否有跨境交易?（如向境外支付/从境外收入）
- 是否有海外子公司?
- 数据源是否已配置 yuandian / pkulaw?
- 升级路径的 4 档审批人是谁?"

**Step 5: 关键阈值(2 字段)**
"最后:
- 增值税默认税率是否 13%?（或行业特殊税率）
- 企业所得税默认税率是否 25%?（或高新 15% / 小微 2.5%-5%）
- 研发加计扣除比例?
- house style?（memo 飞书/钉钉/邮件；争议应对 协商/复议/诉讼；稽查应对 谨慎/标准/快速）"

**写入运行配置 + 确认**：
"配置已写入。现在可以开始任务。"

---

## 4. 已知不重复规则(Pattern § 0.9)

**用户已说明的事实不重复问。** 例如:
- 用户说"我们是一般纳税人" → 不要重复问纳税人类型
- 用户说"我们 25% 标准税率" → 不要重复问 CIT 税率
- 用户说"我们有 3 家海外子公司" → 不要重复问 overseas_subsidiaries

**只问"用户没说但 agent 需要"的事实。**

---

*Greater China Legal — tax-compliance onboarding v3*
*24 字段首次问询 + 5 步主动问对话*
*最后更新:2026-06-20*