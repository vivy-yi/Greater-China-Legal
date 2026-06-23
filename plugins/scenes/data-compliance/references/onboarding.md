# 首次问询协议 — data-compliance 24 字段

> 来源:scene-claudemd-curator `learn-patterns.md` § 0.7
> 适用:agent 第一次跑 data-compliance / § 9.0 首次使用协议触发
> **规则:任何字段为空 → 不要执行任务,先问用户填表**

---

## 0. 触发判断

**进入本协议的条件** —— 满足任一即触发:

| 条件 | 检测方法 |
|------|--------|
| `~/.claude/plugins/config/greater-china-legal/data-compliance/CLAUDE.md` 不存在 | 检查运行配置 |
| 24 字段中 ≥ 1 个为空 | YAML 校验 |
| 用户说"重新配置" / "我换了一家公司" / "产品变了" | 用户意图 |
| § 9.0 "首次使用协议" 被调用 | skill 路由 |

**退出条件**:24 字段全部填完 + 用户确认 + 写入运行配置。

---

## 1. 24 字段分组(6 大类)

### 1.1 公司基本信息(6 字段)

| # | 字段 | 必填 | 示例 | 备注 |
|---|------|-----|------|------|
| 1 | `company_name` | ✅ | "字节跳动" | 公司全称 |
| 2 | `product_service_type` | ✅ | "APP" | APP/网站/小程序/线下/混合 |
| 3 | `user_scale` | ✅ | "DAU 5000 万" | 注册用户数/日活用户数 |
| 4 | `dpo_name` | ✅ | "张明" | 数据保护负责人 |
| 5 | `dpo_contact` | ✅ | "dpo@company.com" | 联系方式 |
| 6 | `external_privacy_counsel` | ⚠️ | "汉坤律所常年顾问" | 外部律师联系方式 |

### 1.2 角色(Pattern 13 — 4 档)

| # | 字段 | 必填 | 4 档选项 | 默认 header |
|---|------|-----|--------|----------|
| 7 | `role` | ✅ | `Lawyer` / `Non_lawyer_with_counsel` / `Non_lawyer_no_counsel` | 见 § 9.1 |

**4 档 work-product header**:
- `Lawyer` → "律师执业秘密——律师工作成果"
- `Non_lawyer_with_counsel` → "参考资料——非法律意见——请律师审阅"
- `Non_lawyer_no_counsel` → "一般信息——非法律意见——请咨询执业律师"

### 1.3 法域(Pattern 7+16)

| # | 字段 | 必填 | 5 档 | 备注 |
|---|------|-----|------|------|
| 8 | `jurisdictions` | ✅ | `cn-mainland` / `hk` / `mo` / `tw` / `sg` | 至少 1 个 |
| 9 | `foreign_users` | ⚠️ | true/false | 是否有境外用户 → 触发 [域外] 法源 |
| 10 | `cross_border` | ⚠️ | true/false | 是否有跨境数据流 |

### 1.4 数据源(Pattern 4)

| # | 字段 | 必填 | 选项 | fallback |
|---|------|-----|------|--------|
| 11 | `sources.yuandian` | ✅ | true/false | web_search |
| 12 | `sources.pkulaw` | ✅ | true/false | yuandian |
| 13 | `sources.fallback` | ✅ | `web_search` / `bing` / `brave` | — |

### 1.5 升级路径(Pattern 6+17 — 4 档)

| # | 字段 | 必填 | 阈值 | 升给 |
|---|------|-----|------|------|
| 14 | `approval_chain.junior` | ✅ | <1 万人 | dpo(邮件) |
| 15 | `approval_chain.dpo` | ✅ | 1-100 万人 | gc(邮件+会议) |
| 16 | `approval_chain.gc` | ✅ | >100 万人 / 敏感 / 涉外 | ceo(邮件+董事会) |
| 17 | `approval_chain.ceo` | ✅ | 上市公司 / 重大泄露 | board(会议+文件) |

### 1.6 关键阈值 + house style(7 字段)

| # | 字段 | 必填 | 默认 | 备注 |
|---|------|-----|------|------|
| 18 | `pipi_threshold` | ✅ | 100 万 | 触发 PIA 阈值 |
| 19 | `sensitive_pii_types` | ✅ | 7 类(列表) | 生物/宗教/身份/医疗/金融/行踪/未成年人 |
| 20-24 | 7 类敏感类型各 1 字段 | ⚠️ | true/false | 具体是否处理 |

---

## 2. YAML 完整 schema(写入运行配置)

```yaml
# ~/.claude/plugins/config/greater-china-legal/data-compliance/CLAUDE.md
# (运行配置,agent 每次开始对话都读这个)

# === 公司基本信息 ===
company_name: ""
product_service_type: ""  # APP/网站/小程序/线下/混合
user_scale: ""  # 注册用户数/日活用户数
dpo_name: ""
dpo_contact: ""
external_privacy_counsel: ""

# === 角色(Pattern 13)===
role: ""  # Lawyer/Non_lawyer_with_counsel/Non_lawyer_no_counsel

# === 法域(Pattern 7+16)===
jurisdictions: ["cn-mainland"]
foreign_users: false
cross_border: false

# === 数据源(Pattern 4)===
sources:
  yuandian: true
  pkulaw: true
  fallback: "web_search"

# === 升级路径(Pattern 6+17)===
approval_chain:
  junior:
    threshold: "<1 万人"
    escalate_to: dpo
    via: "邮件"
  dpo:
    threshold: "1-100 万人"
    escalate_to: gc
    via: "邮件+会议"
  gc:
    threshold: ">100 万人 / 敏感 / 涉外"
    escalate_to: ceo
    via: "邮件+董事会"
  ceo:
    threshold: "上市公司 / 重大泄露"
    escalate_to: board
    via: "会议+文件"

# === 关键阈值 ===
pipi_threshold: 1000000  # 100 万人
sensitive_pii_types: []  # 7 类敏感(列表)
```

---

## 3. YAML 注册表(Pattern 2+14)

### 3.1 `data-inventory.yaml`(per-业务/功能)

```yaml
# 维护在 ~/.claude/plugins/config/greater-china-legal/data-compliance/data-inventory.yaml
# 用 /data-compliance:data-inventory 自动维护
business_units:
  - id: BU-001
    name: ""
    function: ""  # 注册/支付/营销/AI 推荐...
    pii_volume: 0  # 处理用户数
    pii_types: []  # 6 类个人信息(姓名/身份证/手机/位置/IP/生物...)
    sensitive_pii: []  # 7 类敏感(生物/宗教/医疗/金融/行踪/未成年人/特定身份)
    processing_basis: ""  # 6 类合法性基础
    consent_mechanism: ""  # 单独/一般/默示
    risk_level: ""  # HIGH/MEDIUM/LOW
    last_pia_date: YYYY-MM-DD
    next_pia_date: YYYY-MM-DD
```

### 3.2 `consent-records.yaml`(同意记录)

```yaml
# 维护在 ~/.claude/plugins/config/greater-china-legal/data-compliance/consent-records.yaml
# 用 /data-compliance:consent-mechanism-checker 自动维护
consents:
  - user_id: ""
    purpose: ""  # 处理目的
    consent_type: ""  # 单独/一般
    consent_time: YYYY-MM-DD
    withdraw_time: YYYY-MM-DD
    status: ""  # 已同意/已撤回
```

### 3.3 `dsar-records.yaml`(主体权利行使记录)

```yaml
# 维护在 ~/.claude/plugins/config/greater-china-legal/data-compliance/dsar-records.yaml
# 用 /data-compliance:dsar-response 自动维护
requests:
  - request_id: ""
    user_id: ""
    request_type: ""  # 查阅/复制/更正/删除/转移/撤回同意
    request_time: YYYY-MM-DD
    response_deadline: YYYY-MM-DD  # 15 日内
    response_time: YYYY-MM-DD
    status: ""  # 已处理/已超期/拒绝
```

---

## 4. 主动问对话脚本(5 步)

> 不要一次性问 24 字段——分 5 步,逐步推进。

### Step 1: 公司基本信息(开场)

```
你好!这是第一次使用 data-compliance 场景。我需要先了解 6 个基本信息:

1. 公司名称?
2. 产品/服务类型?(APP/网站/小程序/线下/混合)
3. 用户规模?(注册用户数/日活用户数)
4. DPO 姓名?
5. DPO 联系方式?
6. 外部隐私律师联系方式?(选填)
```

### Step 2: 角色 + 法域

```
谢谢!接下来了解角色和法域:

7. 您的角色?(律师/法务人员(有律师支持)/非法务(无律师支持))
8. 涉及哪些法域?(cn-mainland 必填,其他选填)
9. 是否有境外用户?
10. 是否有跨境数据流?
```

### Step 3: 数据源

```
11. 元典 MCP 是否连接?(yes/no)
12. 北大法宝 MCP 是否连接?
13. 备选数据源(默认 web_search)?
```

### Step 4: 升级路径

```
14. <1 万人处理——升给谁?(DPO?)
15. 1-100 万人处理——升给谁?(GC?)
16. >100 万人 / 敏感 / 涉外——升给谁?(CEO?)
17. 上市公司 / 重大泄露——升给谁?(董事会?)
```

### Step 5: 关键阈值

```
18. 触发 PIA 的用户数阈值?(默认 100 万)
19. 是否处理 7 类敏感个人信息?
20-26. 7 类敏感各 1 字段(生物/宗教/医疗/金融/行踪/未成年人/特定身份)
```

### 收尾:确认 + 写入

```
全部填完,确认写入运行配置?
位置:~/.claude/plugins/config/greater-china-legal/data-compliance/CLAUDE.md

确认后,后续每次对话开始 agent 都会先读这个文件——不再重复问。
```

---

## 5. 主动问规则(用户已说明的事实不重复问)

> ⚠️ **重要**——主动问**只问用户没说的事实**

| 类别 | 已知 → 不问 | 未知 → 必问 |
|------|------------|----------|
| 个人信息 | 用户说"200 万用户" → 不问"多少用户" | 用户说"数据处理" → 问"多少用户" |
| 敏感信息 | 用户说"含身份证号" → 不问"是否敏感" | 用户说"个人信息" → 问"是否敏感" |
| 跨境 | 用户说"备份到欧盟" → 不问"是否跨境" | 用户说"个人信息" → 问"是否跨境" |
| 自动化决策 | 用户说"AI 推荐" → 不问"是否自动化" | 用户说"处理" → 问"是否自动化" |
| 关基 | 用户说"金融" → 不问"是否关基" | 用户说"运营者" → 问"是否关基" |
| DPO | 用户说"我们 DPO 是张明" → 不问"是否有 DPO" | 用户说"数据处理" → 问"是否有 DPO" |

---

## 6. 用户主动更新字段

> 填完后用户仍可改——按字段影响范围分级:

| 字段影响 | 哪些字段 | 更新方式 |
|--------|--------|--------|
| **低影响**(可随时改) | `dpo_contact` / `external_privacy_counsel` | 直接修改 |
| **中影响**(影响输出 header) | `role` / `product_service_type` | 修改后下次任务生效 |
| **高影响**(影响升级链路) | `approval_chain` / `user_scale` | 修改后立即生效,但**输出会标注"已变更"** |
| **重置**(需要重跑 24 字段) | `company_name` 变更 / `jurisdictions` 变更 | 重跑 onboarding |

---

## 7. 与 § 9.1 / § 9.2 的关系

- **§ 9.1** CLAUDE.md 内的 schema(精简版,展示用)
- **§ 9.2** data-inventory.yaml + consent-records.yaml + dsar-records.yaml per-业务/功能 schema
- **本文件** 用户级(公司/团队)首次问询 24 字段(完整版)

**数据流**:
```
onboarding(本文件) → ~/.claude/plugins/config/.../CLAUDE.md
                              ↓
                        § 9.1 运行时引用
                              ↓
                  § 9.2 data-inventory.yaml per-业务
                              ↓
                  skill 执行时读取
```

---

*Greater China Legal — data-compliance 首次问询协议 v1.0.0*
*scene-claudemd-curator § 0.7 通用 pattern 适配*
*最后更新:2026-06*
