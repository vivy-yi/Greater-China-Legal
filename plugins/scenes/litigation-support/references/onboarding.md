# 首次问询协议 — litigation-support 24 字段

> 来源:scene-claudemd-curator `learn-patterns.md` § 0.7
> 适用:agent 第一次跑 litigation-support / § 9.0 首次使用协议触发 / 用户主动说"重新配置"
> **规则:任何字段为空 → 不要执行任务,先问用户填表**

---

## 0. 触发判断

**进入本协议的条件** —— 满足任一即触发:

| 条件 | 检测方法 |
|------|--------|
| `~/.claude/plugins/config/greater-china-legal/litigation-support/CLAUDE.md` 不存在 | 检查运行配置 |
| 24 字段中 ≥ 1 个为空 | YAML 校验 |
| 用户说"重新配置" / "我换了一家所" / "公司变了" | 用户意图 |
| § 9.0 "首次使用协议" 被调用 | skill 路由 |

**退出条件**:24 字段全部填完 + 用户确认 + 写入运行配置。

---

## 1. 24 字段分组(6 大类)

### 1.1 公司基本信息(5 字段)

| # | 字段 | 必填 | 示例 | 备注 |
|---|------|-----|------|------|
| 1 | `firm_name` | ✅ | "汉坤律师事务所" | 律所/法务部名称 |
| 2 | `firm_type` | ✅ | "合伙制" | 合伙制/公司制/个人/公司法务部 |
| 3 | `team_size` | ✅ | 25 | 团队人数 |
| 4 | `primary_jurisdiction` | ✅ | "cn-mainland" | cn-mainland/hk/mo/tw/sg |
| 5 | `stage` | ✅ | "成长" | 初创/成长/上市前/上市/国资/律所 |

### 1.2 角色(Pattern 13 — 4 档)

| # | 字段 | 必填 | 4 档选项 | 默认 header |
|---|------|-----|--------|----------|
| 6 | `role` | ✅ | `Lawyer` / `Accountant` / `Tax_agent` / `Non_lawyer` | 见 § 9.1 |

**4 档 work-product header**:
- `Lawyer` → "律师执业秘密——律师工作成果"
- `Accountant` → "注册会计师工作底稿——不构成律师意见"
- `Tax_agent` → "税务师工作成果——不构成律师意见"
- `Non_lawyer` → "参考资料——非法律意见——请律师审阅"

### 1.3 案件基础信息(8 字段)

| # | 字段 | 必填 | 类型 | 备注 |
|---|------|-----|------|------|
| 7 | `current_matters_count` | ✅ | int | 在办案件总数 |
| 8 | `case_types` | ✅ | 数组 | 合同纠纷/侵权/劳动/IP/行政/刑事/其他 |
| 9 | `primary_courts` | ✅ | 数组 | 基层/中级/高级/最高院 |
| 10 | `case_volume_year` | ✅ | int | 年度新案件数 |
| 11 | `high_value_threshold` | ✅ | int | 升级阈值(元)——默认 1000 万 |
| 12 | `foreign_parties` | ⚠️ | bool | 是否常涉外资 |
| 13 | `cross_border` | ⚠️ | bool | 是否常涉跨境 |
| 14 | `sample_matters` | ⚠️ | 路径 | 5-10 份历史案件材料路径(用于学习 playbook) |

### 1.4 法域(Pattern 7+16)

| # | 字段 | 必填 | 5 档 | 备注 |
|---|------|-----|------|------|
| 15 | `jurisdictions` | ✅ | `cn-mainland` / `hk` / `mo` / `tw` / `sg` | 至少 1 个 |
| 16 | `high_attention_jurisdictions` | ⚠️ | 3 标准命中: 业务量/监管严度/历史诉讼处罚 | 至少 1 个 |
| 17 | `foreign_jurisdiction` | ⚠️ | 美国/欧盟/日韩/其他 | 涉外时必填 |

**5 大法域标识**:
```
cn-mainland  中国大陆(默认)
hk           Hong Kong(普通法系)
mo           Macau(大陆法系)
tw           Taiwan(大陆法系)
sg           Singapore(普通法系)
```

### 1.5 数据源(Pattern 4)

| # | 字段 | 必填 | 选项 | fallback |
|---|------|-----|------|--------|
| 18 | `sources.yuandian` | ✅ | true/false | web_search |
| 19 | `sources.pkulaw` | ✅ | true/false | yuandian |
| 20 | `sources.weiken` | ⚠️ | true/false | pkulaw |
| 21 | `sources.fallback` | ✅ | `web_search` / `bing` / `brave` | — |

### 1.6 升级路径(Pattern 6+17 — 4 档)

| # | 字段 | 必填 | 阈值 | 升给 |
|---|------|-----|------|------|
| 22 | `approval_chain.junior` | ✅ | <100 万 / 简单 | senior(邮件) |
| 23 | `approval_chain.senior` | ✅ | 100-1000 万 / 标准 | partner(邮件+会议) |
| 24 | `approval_chain.partner` | ✅ | 1000 万+ / 重大 | managing_partner(邮件+合伙人会议) |

**额外必升触发器**(任一命中):
- 涉外 → 法务总监 + 跨境律师
- 上市公司 → GC + 董秘
- 国资/政府客户 → 法务总监 + 外部律师
- 涉刑事 → 法务总监 + 刑事律师

---

## 2. YAML 完整 schema(写入运行配置)

```yaml
# ~/.claude/plugins/config/greater-china-legal/litigation-support/CLAUDE.md
# (运行配置,agent 每次开始对话都读这个)

# === 公司基本信息 ===
firm_name: ""
firm_type: ""  # 合伙制/公司制/个人/公司法务部
team_size: 0
primary_jurisdiction: "cn-mainland"
stage: ""

# === 角色(Pattern 13)===
role: ""  # Lawyer/Accountant/Tax_agent/Non_lawyer

# === 案件基础信息 ===
current_matters_count: 0
case_types: []
primary_courts: []
case_volume_year: 0
high_value_threshold: 10000000  # 1000 万
foreign_parties: false
cross_border: false
sample_matters: ""  # 路径

# === 法域(Pattern 7+16)===
jurisdictions: ["cn-mainland"]
high_attention_jurisdictions: []
foreign_jurisdiction: ""

# === 数据源(Pattern 4)===
sources:
  yuandian: true
  pkulaw: true
  weiken: false
  fallback: "web_search"

# === 升级路径(Pattern 6+17)===
approval_chain:
  junior:
    threshold: "<100 万 / 简单"
    escalate_to: senior
    via: "邮件"
  senior:
    threshold: "100-1000 万 / 标准"
    escalate_to: partner
    via: "邮件+会议"
  partner:
    threshold: "1000 万+ / 重大"
    escalate_to: managing_partner
    via: "邮件+合伙人会议"

# === 关键阈值(诉讼场景)===
prescription_period: 3  # 一般民事 3 年
labor_prescription: 1
work_injury_prescription: 1
appeal_period_civil: 15
appeal_period_administrative: 6
```

---

## 3. 主动问对话脚本(5 步)

> 不要一次性问 24 字段——分 5 步,逐步推进。

### Step 1: 公司基本信息(开场)

```
你好!这是第一次使用 litigation-support 场景。我需要先了解 5 个基本信息:

1. 您所在律所/法务部的名称是?
2. 机构类型?(合伙制/公司制/个人/公司法务部)
3. 团队规模?(律师/法务人数)
4. 主要法域?(cn-mainland / hk / mo / tw / sg,多选)
5. 公司/律所阶段?(初创/成长/上市前/上市/国资/律所)
```

### Step 2: 角色 + 案件基础信息

```
谢谢!接下来了解角色和案件情况:

6. 您的角色?(律师/注册会计师/税务师/法务/非法务)
7. 当前在办案件总数?
8. 主要案件类型?(合同纠纷/侵权/劳动/IP/行政/刑事/其他,多选)
9. 经常打交道的法院级别?(基层/中级/高级/最高院)
10. 年度新案件数?
11. 升级阈值(默认 1000 万,您这边习惯?)
12. 是否常涉外资/跨境案件?
13. 有 5-10 份历史案件材料想让我学习吗?(可选)
```

### Step 3: 法域 + 高度关注

```
14. 涉及哪些法域?(至少 1 个)
15. 哪几个法域"高度关注"?(按 3 标准:业务量/监管严度/历史诉讼处罚)
16. 是否常涉境外法域?(美国/欧盟/日韩/其他)
```

### Step 4: 数据源

```
17. 元典 MCP 是否连接?(yes/no)
18. 北大法宝 MCP 是否连接?
19. 威科先行 MCP 是否连接?
20. 备选数据源(默认 web_search)?
```

### Step 5: 升级路径

```
21. <100 万 / 简单案件——升给谁?(高级律师?)
22. 100-1000 万 / 标准案件——升给谁?(合伙人?)
23. 1000 万+ / 重大案件——升给谁?(管理合伙人?)
```

### 收尾:确认 + 写入

```
全部填完,确认写入运行配置?
位置:~/.claude/plugins/config/greater-china-legal/litigation-support/CLAUDE.md

确认后,后续每次对话开始 agent 都会先读这个文件——不再重复问。
```

---

## 4. 用户主动更新字段

> 填完后用户仍可改——按字段影响范围分级:

| 字段影响 | 哪些字段 | 更新方式 |
|--------|--------|--------|
| **低影响**(可随时改) | `team_size` / `case_volume_year` / `sample_matters` | 直接修改 |
| **中影响**(影响输出 header) | `role` / `firm_type` / `primary_jurisdiction` | 修改后下次任务生效 |
| **高影响**(影响升级链路) | `approval_chain` / `high_value_threshold` | 修改后立即生效,但**输出会标注"已变更"** |
| **重置**(需要重跑 24 字段) | `firm_name` 变更 / `primary_jurisdiction` 变更 / 案件类型全部变了 | 重跑 onboarding |

---

## 5. 与 § 9.1 / § 9.2 的关系

- **§ 9.1** CLAUDE.md 内的 schema(精简版,展示用)
- **§ 9.2** matter.yaml + matter.md 案件级 schema
- **本文件** 用户级(律所/团队)首次问询 24 字段(完整版)

**数据流**:
```
onboarding(本文件) → ~/.claude/plugins/config/.../CLAUDE.md
                              ↓
                        § 9.1 运行时引用
                              ↓
                  § 9.2 matter.yaml 案件级
                              ↓
                  skill 执行时读取
```

---

*Greater China Legal — litigation-support 首次问询协议 v1.0.0*
*scene-claudemd-curator § 0.7 通用 pattern 适配*
*最后更新:2026-06*
