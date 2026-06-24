# 完整路由表 — employment-legal 27 skill × 用户意图

> 来源:scene-claudemd-curator `learn-patterns.md` § 0.1(主入口结构)
> 适用:agent 根据用户意图路由到具体 skill
> **CLAUDE.md § 2 路由表是速查版,本文件是完整版**

---

## 0. 路由原则

1. **先问用户"想做什么"和"涉及哪一员工"** —— 不知道就不路由
2. **主入口优先** —— 5 段生命周期各 1 个主入口,非主入口 skill 不直接路由
3. **关键串接检查** —— 违纪解除前必先 investigation-open / 解除前必先 termination-legality-assessment / 仲裁前必先 labor-arbitration-filing
4. **per-员工判定(Pattern 1)** —— 同一动作,不同员工可能走不同路径(例:三期内违纪 vs 普通违纪)

---

## 1. 按 5 段生命周期分组(主入口已标 🔷)

### 1.1 入职阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **hiring-review** | 审查 offer / 入职合规 | 后接 labor-contract-drafter |
| | labor-contract-drafter | 起草劳动合同 | 需先 hiring-review |
| | probation-period-advisor | 试用期合规审查 | 独立工具 |
| | job-description-legality | 岗位合法性审查 | 独立工具 |
| | non-compete-enforcement | 竞业限制合规 | 需先 hiring-review |

### 1.2 在职阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **social-insurance-compliance** | 社保合规 / 公积金 | 独立工具 |
| | salary-structure-design | 工资结构设计 | 独立工具 |
| | annual-bonus-rules | 年终奖/13 薪规则 | 独立工具 |
| | policy-drafting | 公司政策起草 | 需先 handbook-updates 同步 |
| | handbook-updates | 员工手册更新 | 需先 policy-drafting |
| | work-injury-compensation | 工伤认定/赔偿 | 需先 30 日内申请 |
| | leave-tracker | 假期查询/计算 | 独立工具 |
| | log-leave | 假期登记 | 需先 leave-tracker |
| | sexual-harassment-complaint | 性骚扰投诉处理 | 24 小时内回应 |

### 1.3 离职阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **termination-legality-assessment** | 离职审查(协商/过失/非过失/经济性) | 后接协商或解除方案 |
| | resignation-negotiation | 员工辞职谈判 | 独立工具 |

### 1.4 争议阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **labor-arbitration-filing** | 劳动仲裁申请/应诉 | 必经前置 |

### 1.5 内部调查阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **investigation-open** | 内部调查立案 | 后接 investigation-add / -query / -memo / -summary |
| | investigation-add | 证据收集 | 需先 investigation-open |
| | investigation-query | 调查查询 | 需先 investigation-open |
| | investigation-memo | 调查备忘录 | 需先 investigation-open |
| | investigation-summary | 调查总结 | 需先 investigation-open |

### 1.6 跨国扩张阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **expansion-kickoff** | 跨国扩张启动 | 后接 international-expansion |
| | international-expansion | 跨国用工/EOR/自设实体 | 需先 expansion-kickoff |
| | expansion-update | 扩张进展更新 | 需先 expansion-kickoff |

---

## 2. 按"案件类型"分组(应急/特殊)

| skill | 用户意图 | 严重度 |
|-------|---------|------|
| **termination-legality-assessment** | 解除劳动合同审查 | 🟡 重要 |
| **investigation-open** | 内部调查立案 | 🟡 重要(高管/上市公司 🔴) |
| **labor-arbitration-filing** | 劳动仲裁 | 🟡 重要 |
| **work-injury-compensation** | 工伤认定 | 🟡 重要(30 日内申请) |
| **sexual-harassment-complaint** | 性骚扰投诉 | 🔴 重大 |

---

## 3. 关键串接(强制前置)

> agent 路由时**必须检查**这些串接——违反会导致程序瑕疵或败诉风险。

| 强制串接 | 跳过后果 | 例外 |
|--------|--------|------|
| 违纪解除前 → investigation-open | 解除被认定违法 | 紧急情况/员工已失踪 |
| 解除前 → termination-legality-assessment | 解除程序违法 | 协商一致解除 |
| 仲裁前 → labor-arbitration-filing | 仲裁请求不被受理 | 无 |
| 跨国扩张前 → expansion-kickoff | 扩张方案不完整 | 无 |
| 工伤 → 30 日内申请 | 错过工伤认定时效 | 特殊情况 |

---

## 4. 路由决策树(用户意图 → skill)

```
用户输入
  │
  ├─ 关键词:offer/入职/劳动合同
  │   └─→ hiring-review 🔷(主入口)
  │
  ├─ 关键词:试用期/工资打折
  │   └─→ probation-period-advisor
  │
  ├─ 关键词:社保/公积金/五险一金
  │   └─→ social-insurance-compliance 🔷(主入口)
  │
  ├─ 关键词:工资/薪酬/年终奖/13 薪
  │   └─→ salary-structure-design / annual-bonus-rules
  │
  ├─ 关键词:政策/员工手册
  │   └─→ policy-drafting / handbook-updates
  │
  ├─ 关键词:工伤/工伤认定
  │   └─→ work-injury-compensation
  │
  ├─ 关键词:请假/年假/病假
  │   └─→ leave-tracker / log-leave
  │
  ├─ 关键词:性骚扰
  │   └─→ sexual-harassment-complaint
  │
  ├─ 关键词:解除/辞退/裁员
  │   ├─ 协商一致 → termination-legality-assessment
  │   ├─ 违纪违规 → investigation-open(先)+ termination-legality-assessment(后)
  │   ├─ 经济性裁员 → termination-legality-assessment(41 条)+ 工会
  │   └─ 三期/医疗期/老员工 → ⚠️ 阻断(不调任何 skill,直接告"绝对不能解除")
  │      路由规则:用户说"怀孕/产假/哺乳/医疗期/工龄 15 年+"
  │      → **不要调任何 skill** → 直接输出"§ 5.3 绝对禁止 + 拒绝继续操作"
  │      → 升级到法务总监 + 外部律师
  │      → 即使业务部门强烈要求,也以"法律强制"为由拒绝
  │
  ├─ 关键词:辞职/主动离职
  │   └─→ resignation-negotiation
  │
  ├─ 关键词:仲裁/员工告我
  │   └─→ labor-arbitration-filing 🔷(主入口)
  │
  ├─ 关键词:调查/举报/舞弊
  │   └─→ investigation-open 🔷(主入口)
  │
  ├─ 关键词:海外/跨国/外派
  │   └─→ expansion-kickoff 🔷(主入口)
  │
  └─ 不确定
      └─→ 主动问用户(6 类主动问见 CLAUDE.md § 5.2)
          - "想做什么?"
          - "涉及哪一员工?"
          - "员工是否在三期/医疗期?"
          - "是否经济性裁员?"
          - "是否工会介入?"
          - "是否涉外/跨境?"
```

---

## 5. 27 skill 总目录(按字母序)

| # | skill | 严重度 | 阶段 |
|---|------|------|------|
| 1 | annual-bonus-rules | 🟢 | 在职 |
| 2 | expansion-kickoff | 🟡 | 扩张(主入口) |
| 3 | expansion-update | 🟢 | 扩张 |
| 4 | handbook-updates | 🟡 | 在职 |
| 5 | hiring-review | 🟡 | 入职(主入口) |
| 6 | internal-investigation | 🟡 | 调查 |
| 7 | international-expansion | 🟡 | 扩张 |
| 8 | investigation-add | 🟡 | 调查 |
| 9 | investigation-memo | 🟢 | 调查 |
| 10 | investigation-open | 🟡 | 调查(主入口) |
| 11 | investigation-query | 🟢 | 调查 |
| 12 | investigation-summary | 🟢 | 调查 |
| 13 | job-description-legality | 🟡 | 入职 |
| 14 | labor-arbitration-filing | 🟡 | 争议(主入口) |
| 15 | labor-contract-drafter | 🟡 | 入职 |
| 16 | leave-tracker | 🟢 | 在职 |
| 17 | log-leave | 🟢 | 在职 |
| 18 | non-compete-enforcement | 🟡 | 入职 |
| 19 | policy-drafting | 🟡 | 在职 |
| 20 | probation-period-advisor | 🟡 | 入职 |
| 21 | resignation-negoitation | ⚠️ | 离职(typo) |
| 22 | resignation-negotiation | 🟢 | 离职 |
| 23 | salary-structure-design | 🟢 | 在职 |
| 24 | sexual-harassment-complaint | 🔴 | 在职 |
| 25 | social-insurance-compliance | 🟡 | 在职(主入口) |
| 26 | termination-legality-assessment | 🟡 | 离职(主入口) |
| 27 | work-injury-compensation | 🟡 | 在职 |

> ⚠️ 注意到第 21 个 `resignation-negoitation` 是 typo(应是 negotiation)——已在第 22 个正确名——需要修复 skill 目录

---

## 6. 与 CLAUDE.md § 2 的关系

- **§ 2 路由表**:速查版(17 个高频意图)
- **本文件**:完整版(27 skill + 决策树 + 串接检查)
- **更新**:新增 skill → 加到本文件 + § 2

---

*Greater China Legal — employment-legal 完整路由表 v1.0.0*
*scene-claudemd-curator § 0.1 主入口结构 适配*
*最后更新:2026-06*
