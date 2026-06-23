# 首次问询协议 — employment-legal 24 字段

> 来源:scene-claudemd-curator `learn-patterns.md` § 0.7
> 适用:agent 第一次跑 employment-legal / § 9.0 首次使用协议触发 / 用户主动说"重新配置"
> **规则:任何字段为空 → 不要执行任务,先问用户填表**

---

## 0. 触发判断

**进入本协议的条件** —— 满足任一即触发:

| 条件 | 检测方法 |
|------|--------|
| `~/.claude/plugins/config/greater-china-legal/employment-legal/CLAUDE.md` 不存在 | 检查运行配置 |
| 24 字段中 ≥ 1 个为空 | YAML 校验 |
| 用户说"重新配置" / "我换了一家所" / "公司变了" | 用户意图 |
| § 9.0 "首次使用协议" 被调用 | skill 路由 |

**退出条件**:24 字段全部填完 + 用户确认 + 写入运行配置。

---

## 1. 24 字段分组(6 大类)

### 1.1 公司基本信息(9 字段)

| # | 字段 | 必填 | 示例 | 备注 |
|---|------|-----|------|------|
| 1 | `company_name` | ✅ | "阿里巴巴集团" | 公司全称 |
| 2 | `entity_type` | ✅ | "股份有限公司" | 有限责任公司/股份有限公司/外资/国企/上市公司 |
| 3 | `industry` | ✅ | "互联网/电商" | 所属行业 |
| 4 | `stage` | ✅ | "上市" | 初创/成长/上市前/上市/国资 |
| 5 | `employee_count` | ✅ | 50000 | 员工总数 |
| 6 | `legal_team_size` | ✅ | 15 | 法务团队规模 |
| 7 | `has_union` | ✅ | true | 是否有工会 |
| 8 | `has_workers_congress` | ✅ | true | 是否有职代会 |
| 9 | `external_counsel` | ⚠️ | "汉坤律所常年顾问" | 外部律师联系方式 |

### 1.2 角色(Pattern 13 — 5 档)

| # | 字段 | 必填 | 5 档选项 | 默认 header |
|---|------|-----|--------|----------|
| 10 | `role` | ✅ | `Lawyer` / `Accountant` / `Tax_agent` / `HR_legal` / `Non_lawyer` | 见 § 9.1 |

**5 档 work-product header**:
- `Lawyer` → "律师执业秘密——律师工作成果"
- `Accountant` → "注册会计师工作底稿——不构成律师意见"
- `Tax_agent` → "税务师工作成果——不构成律师意见"
- `HR_legal` → "法务/HR 内部参考——请律师审阅"
- `Non_lawyer` → "参考资料——非法律意见——请律师审阅"

### 1.3 法域(Pattern 7+16)

| # | 字段 | 必填 | 5 档 | 备注 |
|---|------|-----|------|------|
| 11 | `jurisdictions` | ✅ | `cn-mainland` / `hk` / `mo` / `tw` / `sg` | 至少 1 个 |
| 12 | `foreign_employees` | ⚠️ | true/false | 是否有外籍员工 → 触发 [域外] 法源 |
| 13 | `cross_border_expansion` | ⚠️ | true/false | 是否有跨国扩张计划 |

### 1.4 数据源(Pattern 4)

| # | 字段 | 必填 | 选项 | fallback |
|---|------|-----|------|--------|
| 14 | `sources.yuandian` | ✅ | true/false | web_search |
| 15 | `sources.pkulaw` | ✅ | true/false | yuandian |
| 16 | `sources.weiken` | ⚠️ | true/false | pkulaw |
| 17 | `sources.beidalu` | ⚠️ | true/false | — |
| 18 | `sources.fallback` | ✅ | `web_search` / `bing` / `brave` | — |

### 1.5 升级路径(Pattern 6+17 — 4 档)

| # | 字段 | 必填 | 阈值 | 升给 |
|---|------|-----|------|------|
| 19 | `approval_chain.junior` | ✅ | <3 人解除 | senior(邮件) |
| 20 | `approval_chain.senior` | ✅ | 3-10 人 / 高风险 | gc(邮件+会议) |
| 21 | `approval_chain.gc` | ✅ | >10 人 / 经济性裁员 / 上市公司 | ceo(邮件+董事会) |
| 22 | `approval_chain.ceo` | ✅ | 国资 / 跨境 / 重大 | board(会议+文件) |

### 1.6 关键阈值 + house style(2 字段)

| # | 字段 | 必填 | 默认 | 备注 |
|---|------|-----|------|------|
| 23 | `local_minimum_wage` / `social_insurance_base_min` / `social_insurance_base_max` / `wage_payment_day` / `non_compete_compensation_ratio` | ✅ | 各省市不同 | 5 个子字段 |
| 24 | `memo_destination` / `dispute_response_style` / `termination_decision_style` | ⚠️ | 飞书/钉钉/邮件 | house style |

---

## 2. YAML 完整 schema(写入运行配置)

```yaml
# ~/.claude/plugins/config/greater-china-legal/employment-legal/CLAUDE.md
# (运行配置,agent 每次开始对话都读这个)

# === 公司基本信息 ===
company_name: ""
entity_type: ""  # 有限责任公司/股份有限公司/外资/国企/上市公司
industry: ""
stage: ""  # 初创/成长/上市前/上市/国资
employee_count: 0
legal_team_size: 0
has_union: false  # 是否有工会
has_workers_congress: false  # 是否有职代会
external_counsel: ""

# === 角色(Pattern 13)===
role: ""  # Lawyer/Accountant/Tax_agent/HR_legal/Non_lawyer

# === 法域(Pattern 7+16)===
jurisdictions: ["cn-mainland"]
foreign_employees: false
cross_border_expansion: false

# === 数据源(Pattern 4)===
sources:
  yuandian: true
  pkulaw: true
  weiken: false
  beidalu: false
  fallback: "web_search"

# === 升级路径(Pattern 6+17)===
approval_chain:
  junior:
    threshold: "<3 人解除"
    escalate_to: senior
    via: "邮件"
  senior:
    threshold: "3-10 人 / 高风险"
    escalate_to: gc
    via: "邮件+会议"
  gc:
    threshold: ">10 人 / 经济性裁员 / 上市公司"
    escalate_to: ceo
    via: "邮件+董事会"
  ceo:
    threshold: "国资 / 跨境 / 重大"
    escalate_to: board
    via: "会议+文件"

# === 关键阈值 ===
local_minimum_wage: ""  # 当地最低工资
social_insurance_base_min: ""  # 社保缴费基数下限
social_insurance_base_max: ""  # 社保缴费基数上限
wage_payment_day: 15
non_compete_compensation_ratio: 0.30  # 竞业限制补偿(建议 ≥ 30%)

# === house style ===
memo_destination: ""  # 飞书/钉钉/邮件
dispute_response_style: ""  # 协商/调解/仲裁
termination_decision_style: ""  # 谨慎/标准/快速
```

---

## 3. YAML 注册表(Pattern 2+14)

### 3.1 `employees.yaml`(per-员工 18 字段)

```yaml
# 维护在 ~/.claude/plugins/config/greater-china-legal/employment-legal/employees.yaml
# 用 /employment-legal:employee-registry list | add | edit | show
employees:
  - id: EMP-001
    name: ""
    entry_date: YYYY-MM-DD
    contract_type: ""  # 固定期限/无固定期限/以完成一定工作任务为期限
    probation_end: YYYY-MM-DD
    position: ""
    department: ""
    is_high_management: false  # 高管 → 竞业限制适用
    has_technical_secrets: false  # 接触技术秘密 → 竞业限制适用
    is_pregnant: false  # 孕期 → 绝对禁止解除
    is_maternity_leave: false  # 产期 → 绝对禁止解除
    is_nursing: false  # 哺乳期 → 绝对禁止解除
    is_medical_leave: false  # 医疗期 → 绝对禁止解除
    is_work_injury: false  # 工伤 → 绝对禁止解除
    consecutive_years: 0  # 连续工作年限 → ≥15 年且距退休 <5 年 → 绝对禁止解除
    is_union_role: false  # 工会法定义务期间 → 绝对禁止解除
    salary: 0
    non_compete_signed: false
    non_compete_compensation: 0  # 元/月
    last_review_date: YYYY-MM-DD
```

### 3.2 `leave-register.yaml`(假期登记)

```yaml
# 维护在 ~/.claude/plugins/config/greater-china-legal/employment-legal/leave-register.yaml
# 用 /employment-legal:leave-tracker 自动维护
leaves:
  - employee_id: EMP-001
    leave_type: ""  # 年假/病假/事假/婚假/产假/陪产假
    start_date: YYYY-MM-DD
    end_date: YYYY-MM-DD
    days: 0
    remaining: 0
    status: ""  # 已批准/待批准/已用
```

---

## 4. 主动问对话脚本(5 步)

> 不要一次性问 24 字段——分 5 步,逐步推进。

### Step 1: 公司基本信息(开场)

```
你好!这是第一次使用 employment-legal 场景。我需要先了解 9 个基本信息:

1. 公司名称?
2. 实体类型?(有限责任公司/股份有限公司/外资/国企/上市公司)
3. 所属行业?
4. 公司阶段?(初创/成长/上市前/上市/国资)
5. 员工总数?
6. 法务团队规模?
7. 是否有工会?
8. 是否有职工代表大会?
9. 外部律师联系方式?(选填)
```

### Step 2: 角色 + 法域

```
谢谢!接下来了解角色和法域:

10. 您的角色?(律师/注册会计师/税务师/法务 HR/非法务)
11. 涉及哪些法域?(cn-mainland 必填,其他选填)
12. 是否有外籍员工?
13. 是否有跨国扩张计划?
```

### 主动问规则(用户已说明的事实不重复问)

> ⚠️ **重要**——主动问**只问用户没说的事实**

| 类别 | 已知 → 不问 | 未知 → 必问 |
|------|------------|----------|
| 三期/医疗期 | 用户说"怀孕 7 个月" → 不问"是否三期" | 用户说"解除"没说 → 主动问 |
| 涉外/跨境 | 用户说"中国 A 公司" → 不问"是否涉外" | 用户说"员工" → 主动问 |
| 工龄/退休 | 用户说"工龄 3 年" → 不问"几年工龄" | 用户说"老员工" → 问"具体几年" |
| 合同类型 | 用户说"固定期限合同" → 不问"合同类型" | 用户说"解除" → 问"合同类型" |
| 是否已发函 | 用户说"收到律师函" → 不问"是否发函" | 用户说"想解除" → 问"程序进度" |

### Step 3: 数据源

```
14. 元典 MCP 是否连接?(yes/no)
15. 北大法宝 MCP 是否连接?
16. 威科先行 MCP 是否连接?(选填)
17. 北达 API 是否连接?(选填)
18. 备选数据源(默认 web_search)?
```

### Step 4: 升级路径

```
19. <3 人解除案件——升给谁?(高级律师?)
20. 3-10 人 / 高风险案件——升给谁?(法务总监?)
21. >10 人 / 经济性裁员 / 上市公司——升给谁?(CEO?)
22. 国资 / 跨境 / 重大——升给谁?(董事会?)
```

### Step 5: 关键阈值 + house style

```
23. 当地最低工资标准? / 社保缴费基数上下限? / 工资支付日? / 竞业限制补偿标准?
24. 工作成果发到哪里?(飞书/钉钉/邮件)
    争议响应风格?(协商/调解/仲裁)
    解除决策风格?(谨慎/标准/快速)
```

### 收尾:确认 + 写入

```
全部填完,确认写入运行配置?
位置:~/.claude/plugins/config/greater-china-legal/employment-legal/CLAUDE.md

确认后,后续每次对话开始 agent 都会先读这个文件——不再重复问。
```

---

## 5. 用户主动更新字段

> 填完后用户仍可改——按字段影响范围分级:

| 字段影响 | 哪些字段 | 更新方式 |
|--------|--------|--------|
| **低影响**(可随时改) | `team_size` / `legal_team_size` / `memo_destination` | 直接修改 |
| **中影响**(影响输出 header) | `role` / `entity_type` / `stage` | 修改后下次任务生效 |
| **高影响**(影响升级链路) | `approval_chain` / `has_union` / `local_minimum_wage` | 修改后立即生效,但**输出会标注"已变更"** |
| **重置**(需要重跑 24 字段) | `company_name` 变更 / `jurisdictions` 变更 / 员工管理类型全变 | 重跑 onboarding |

---

## 6. 与 § 9.1 / § 9.2 的关系

- **§ 9.1** CLAUDE.md 内的 schema(精简版,展示用)
- **§ 9.2** employees.yaml + leave-register.yaml per-员工 / per-假期 schema
- **本文件** 用户级(公司/团队)首次问询 24 字段(完整版)

**数据流**:
```
onboarding(本文件) → ~/.claude/plugins/config/.../CLAUDE.md
                              ↓
                        § 9.1 运行时引用
                              ↓
                  § 9.2 employees.yaml per-员工
                              ↓
                  skill 执行时读取
```

---

*Greater China Legal — employment-legal 首次问询协议 v1.0.0*
*scene-claudemd-curator § 0.7 通用 pattern 适配*
*最后更新:2026-06*
