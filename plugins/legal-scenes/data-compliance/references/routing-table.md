# 完整路由表 — data-compliance 26 skill × 用户意图

> 来源:scene-claudemd-curator `learn-patterns.md` § 0.1
> 适用:agent 根据用户意图路由到具体 skill
> **CLAUDE.md § 2 路由表是速查版,本文件是完整版**

---

## 0. 路由原则

1. **先问用户"想做什么"和"涉及哪一业务/功能"** —— 不知道就不路由
2. **主入口优先** —— 5 段生命周期各 1 个主入口,非主入口 skill 不直接路由
3. **关键串接检查** —— 出境前必先 data-export-assessment / 处理前必先 processing-basis / 上线前必先 pia-assessment / 事故后必先 breach-notification
4. **per-业务/功能判定(Pattern 1)** —— 同一处理,不同业务可能走不同路径

---

## 1. 按 5 段生命周期分组(主入口已标 🔷)

### 1.1 收集阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **use-case-triage** | 新业务/功能上线前风险评估 | 后接 pia-assessment |
| | consent-mechanism-checker | 同意机制审查 | 需先 use-case-triage |
| | processing-basis | 合法性基础选择 | 需先 use-case-triage |
| | rights-exercise-system | 用户行使权利 | 需先 data-inventory |
| | data-inventory | 数据资产盘点 | 独立工具 |
| | medical-data-classification | 健康数据分类 | 需先 use-case-triage |

### 1.2 存储阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **data-localization** | 数据本地化/关基 | 需先 critical-infrastructure-checker |
| | security-certification-advisor | 安全认证 | 独立工具 |

### 1.3 处理阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **pipl-assessment** | PIPL 评估 | 后接 pia-generation |
| | pia-assessment-advisor | PIA 顾问 | 需先 use-case-triage |
| | pia-generation | PIA 报告生成 | 需先 pia-assessment-advisor |
| | policy-monitor | 法规变化跟踪 | 独立工具 |
| | privacy-policy-update | 隐私政策更新 | 独立工具 |
| | clinical-data-sharing-advisor | 健康数据共享 | 需先 medical-data-classification |

### 1.4 出境阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **data-export-assessment** | 数据出境评估(必先) | 后接 scc / 认证 / 安全评估 |
| | scc-implementation-advisor | 标准合同实施 | 需先 data-export-assessment |
| | critical-infrastructure-checker | 关基设施评估 | 需先 use-case-triage |

### 1.5 事故阶段

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| 🔷 | **breach-notification** | 数据泄露 72 小时报告 | 触发应急响应 |
| | cac-enforcement | CAC 执法应对 | 需先 breach-notification |
| | reg-gap-analysis | 合规差距分析 | 独立工具 |
| | subject-rights | 用户权利响应(DSAR) | 需先 rights-exercise-system |

### 1.6 监管 / 备案

| 主入口 | skill | 用户意图 | 关键串接 |
|------|-------|---------|---------|
| | csr-filing-advisor | CSR 备案(网信办) | 需先 data-export-assessment |
| | cac-enforcement | 监管处罚应对 | 见 1.5 |
| | network-product-security-advisor | 网络产品安全审查 | 独立工具 |

---

## 2. 按"严重度"分组(应急/高风险)

| skill | 用户意图 | 严重度 |
|-------|---------|------|
| **breach-notification** | 数据泄露 72 小时报告 | 🔴 紧急 |
| **cac-enforcement** | CAC 处罚应对 | 🔴 重大 |
| **pipl-assessment** | 100 万+ 评估 | 🟡 重要 |
| **data-export-assessment** | 100 万+ 出境 | 🟡 重要 |
| **critical-infrastructure-checker** | 关基设施 | 🟡 重要 |
| **pia-assessment-advisor** | PIA 顾问 | 🟡 重要 |

---

## 3. 关键串接(强制前置)

| 强制串接 | 跳过后果 | 例外 |
|--------|--------|------|
| 数据出境前 → data-export-assessment | 违法出境 | 紧急情况 |
| 数据处理前 → processing-basis | 无合法性基础 | 紧急避险 |
| 上线前 → pia-assessment | 未评估上线 | 内部试用 |
| 事故后 → breach-notification(72 小时) | 超期未报 | 无 |
| 同意前 → consent-mechanism-checker | 无效同意 | 无 |
| 用户权利响应 → 15 日内 | 超期 | 延期通知 |

---

## 4. 路由决策树(用户意图 → skill)

```
用户输入
  │
  ├─ 关键词:新功能/上线/风险评估
  │   └─→ use-case-triage 🔷(主入口)
  │
  ├─ 关键词:数据出境/备份境外/标准合同/安全评估
  │   └─→ data-export-assessment 🔷(主入口,触发 § 5.2 涉外升级)
  │
  ├─ 关键词:数据泄露/安全事件/被攻击
  │   └─→ breach-notification 🔷(主入口,72 小时报告)
  │
  ├─ 关键词:PIA/个人信息影响评估
  │   └─→ pia-assessment-advisor / pia-generation
  │
  ├─ 关键词:用户查/更正/删除/转移
  │   └─→ rights-exercise-system
  │
  ├─ 关键词:关基/CIIO/网络产品
  │   └─→ critical-infrastructure-checker / network-product-security-advisor
  │
  ├─ 关键词:CAC 处罚/网信办/合规审计
  │   └─→ cac-enforcement / reg-gap-analysis
  │
  ├─ 关键词:健康/医疗/病历
  │   └─→ medical-data-classification / clinical-data-sharing-advisor
  │
  ├─ 关键词:隐私政策/cookie/告知
  │   └─→ privacy-policy-update
  │
  ├─ 关键词:数据盘点/data inventory
  │   └─→ data-inventory
  │
  ├─ 关键词:同意/撤回/单独同意
  │   └─→ consent-mechanism-checker
  │
  ├─ 关键词:法规变化/新规/执法
  │   └─→ policy-monitor
  │
  ├─ 关键词:GDPR/CCPA/PDPA/涉外
  │   └─→ use-case-triage + § 5.2 涉外升级
  │
  └─ 不确定
      └─→ 主动问用户(6 类主动问见 CLAUDE.md § 5.2)
          - "想做什么?"
          - "涉及哪一业务/功能?"
          - "处理多少个人信息?用户数?"
          - "是否包含敏感个人信息?"
          - "是否关键信息基础设施?"
          - "是否涉外?"
```

---

## 5. 26 skill 总目录(按字母序)

| # | skill | 严重度 | 阶段 |
|---|------|------|------|
| 1 | breach-notification | 🔴 | 事故(主入口) |
| 2 | cac-enforcement | 🔴 | 事故 |
| 3 | clinical-data-sharing-advisor | 🟡 | 处理 |
| 4 | consent-mechanism-checker | 🟡 | 收集 |
| 5 | critical-infrastructure-checker | 🟡 | 出境(关基) |
| 6 | csr-filing-advisor | 🟢 | 监管 |
| 7 | data-export-assessment | 🟡 | 出境(主入口) |
| 8 | data-inventory | 🟢 | 收集/存储 |
| 9 | data-localization | 🟡 | 存储(主入口) |
| 10 | dpa-review | 🟢 | 处理 |
| 11 | dsar-response | 🟢 | 事故 |
| 12 | healthcare-ai-compliance | 🟡 | 处理 |
| 13 | medical-data-classification | 🟡 | 收集/存储 |
| 14 | network-product-security-advisor | 🟡 | 监管 |
| 15 | pia-assessment-advisor | 🟡 | 处理 |
| 16 | pia-generation | 🟢 | 处理 |
| 17 | pipl-assessment | 🟡 | 处理(主入口) |
| 18 | policy-monitor | 🟢 | 处理 |
| 19 | privacy-policy-update | 🟢 | 处理 |
| 20 | processing-basis | 🟢 | 收集 |
| 21 | reg-gap-analysis | 🟢 | 事故 |
| 22 | rights-exercise-system | 🟢 | 收集 |
| 23 | scc-implementation-advisor | 🟡 | 出境 |
| 24 | security-certification-advisor | 🟢 | 存储 |
| 25 | subject-rights | 🟢 | 事故 |
| 26 | use-case-triage | 🟡 | 收集(主入口) |

---

## 6. 与 CLAUDE.md § 2 的关系

- **§ 2 路由表**:速查版(13 个高频意图)
- **本文件**:完整版(26 skill + 决策树 + 串接检查)
- **更新**:新增 skill → 加到本文件 + § 2

---

*Greater China Legal — data-compliance 完整路由表 v1.0.0*
*scene-claudemd-curator § 0.1 主入口结构 适配*
*最后更新:2026-06*
