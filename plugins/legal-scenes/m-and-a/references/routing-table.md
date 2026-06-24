# 完整路由表 — m-and-a 19 skill × 意图

> 来源:scene-claudemd-curator CLAUDE.md § 2
> 适用:agent 路由用户意图到主入口 skill
> **规则:先问用户"想做什么" → 按本表匹配 → 不要乱调**

---

## 0. 路由决策树

```
用户输入"我要做 X"
  ↓
[Step 1] X 是否在 6 大业务线范围？
  ├─ 否 → "请告诉我想做什么" + 提示
  └─ 是 → [Step 2] X 是哪个业务线？
        ├─ 交易结构/DD → deal-structurer / due-diligence / valuation
        ├─ 协议/签约 → sha-negotiator / signing-closing-checklist
        ├─ 监管审批 → regulatory-approval-tracker / approval
        ├─ 跨境 → red-chip / odi-filing / fem-procedures
        ├─ 公开市场 → tender-offer-3 / going-private-3
        ├─ 信息披露 → disclosure
        └─ 交割后整合 → post-closing-integration
```

---

## 1. 6 大业务线主入口路由表

### 1.1 交易结构与 DD

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 设计交易结构 | "交易结构" / "结构设计" / "deal structure" | deal-structurer | 标的类型？股权/资产？支付方式？ |
| 尽职调查 | "尽调" / "DD" / "due diligence" | due-diligence + due-diligence-checker | DD 范围？资料室？时间表？ |
| 估值/定价 | "估值" / "定价" / "EBITDA 倍数" | valuation | 估值方法？可比公司？EBITDA 倍数？ |

### 1.2 协议与签约

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 股东协议谈判 | "SHA" / "股东协议" / "drag-along" | sha-negotiator | 优先权？反稀释？ |
| 签约交割 | "SPA" / "交割条件" / "签约" | signing-closing-checklist | 交割条件？前置审批？ |

### 1.3 监管审批

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 监管审批追踪 | "反垄断" / "商务部" / "发改委" / "外汇" | regulatory-approval-tracker | 5 类审批？时限？ |
| 内部审批 | "内部审批" / "董事会" / "股东会" | approval | 决策层级？ |

### 1.4 跨境架构

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 红筹/VIE | "红筹" / "VIE" / "WFOE" / "上市架构" | red-chip | 上市地？协议控制？ |
| ODI 备案 | "ODI" / "境外投资" / "发改委 11 号文" | odi-filing | 投资金额？目的地？敏感行业？ |
| 外资准入 | "外资准入" / "负面清单" / "FEM" | fem-procedures | 准入特别管理？ |

### 1.5 信息披露（横向工具）

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 上市公司信息披露 | "信披" / "公告" / "持股变动" / "关联交易" | disclosure | 上市公司？持股比例？ |

### 1.6 公开市场操作

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 公开要约收购 | "要约" / "tender offer" / "部分要约" | tender-offer-scheme-design-checker | 收购比例？要约价？ |
| 私有化方案设计 | "私有化" / "退市" / "going private" | going-private-scheme-design-checker | 私有化方式？财团？ |
| 要约价格评估 | "要约价格" / "公允性" | tender-offer-price-evaluation-advisor | 评估方法？ |
| 私有化价格评估 | "私有化价格" | going-private-price-evaluation-advisor | 评估方法？ |
| 要约审批程序 | "要约审批" / "证监会" | tender-offer-approval-procedure-advisor | 程序？时限？ |
| 私有化审批程序 | "私有化审批" | going-private-approval-procedure-advisor | 程序？时限？ |

### 1.7 交割后整合

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 100 天计划 | "整合" / "post-closing" / "100 天" | post-closing-integration | 整合范围？关键岗位？ |

---

## 2. 未列入的意图(转交或询问)

**用户意图未在表中时:**
1. **首先** → 用 AskUserQuestion 工具问"您具体想做什么?"
2. **其次** → 用 deal-structurer 入口 skill 路由
3. **再次** → 找最近的 skill(避免乱调)

**典型未列入场景 + 默认路由**:

| 未列入意图 | 默认路由 |
|----------|---------|
| "我们要做 IPO" | deal-structurer(主入口)+ disclosure + going-private(反向) |
| "我们要做 VIE" | red-chip + fem-procedures + odi-filing |
| "我们要反垄断申报" | regulatory-approval-tracker + deal-structurer |
| "我们被上市公司收购" | disclosure + sha-negotiator + tender-offer-3 |
| "我们要做国资并购" | approval + regulatory-approval-tracker + signing-closing-checklist |
| "我们要做跨境换股" | odi-filing + red-chip + fem-procedures + sha-negotiator |

---

## 3. 多 skill 协同场景

### 3.1 跨境并购全流程链

```
deal-structurer (设计结构)
  + due-diligence + due-diligence-checker (DD)
  + valuation (估值)
  + sha-negotiator (股东协议)
  + red-chip / odi-filing / fem-procedures (跨境合规)
  + regulatory-approval-tracker (5 类审批)
  + signing-closing-checklist (签约交割)
  + post-closing-integration (整合)
```

### 3.2 上市公司私有化全流程链

```
disclosure (信息披露规划)
  + going-private-scheme-design-checker (方案)
  + going-private-price-evaluation-advisor (价格)
  + going-private-approval-procedure-advisor (程序)
  + sha-negotiator (股东协议)
  + regulatory-approval-tracker (证监会沟通)
  + signing-closing-checklist (退市交割)
```

### 3.3 上市公司公开要约收购链

```
disclosure (信披规划)
  + tender-offer-scheme-design-checker (方案)
  + tender-offer-price-evaluation-advisor (要约价)
  + tender-offer-approval-procedure-advisor (审批程序)
  + regulatory-approval-tracker (证监会)
  + sha-negotiator (大股东协议)
  + signing-closing-checklist (要约交割)
```

---

## 4. 路由避坑(Pattern § 0.8)

### 4.1 不能直接做的"路由表阻断规则"

| 用户说 | ❌ 不能直接做 | ✅ 必须先做 |
|--------|------------|----------|
| "我们要收购某上市公司" | 不能直接要约 | 必须先 disclosure + going-private 评估 |
| "我们想做红筹上市" | 不能直接搭 VIE | 必须先 red-chip 评估可行性 |
| "我们要做反垄断申报" | 不能直接报 | 必须先 regulatory-approval-tracker 评估阈值 |
| "我们要跨境换股" | 不能直接换 | 必须先 odi-filing + fem-procedures |
| "我们要国资并购" | 不能直接签 | 必须先 approval + 进场交易 |

### 4.2 路由红线

**以下意图 agent 必须**:
1. 立即升级到外部律师(§ 5.2)
2. 停止继续路由
3. 提示用户

| 路由红线 | 升级目标 |
|---------|---------|
| 经营者集中达到申报标准但未申报 | 立即停止 + 反垄断律师 |
| 国有股权转让未进场交易 | 立即停止 + 国资律师 |
| 上市公司重大资产重组未停牌 | 立即停止 + 证监会沟通律师 |
| 跨境换股未完成外汇登记 | 立即停止 + 外管律师 |
| 外资准入禁止领域 | 立即停止 + 外资律师 |

---

*Greater China Legal — m-and-a routing-table v3*
*6 大业务线主入口 + 19 skill 完整路由*
*最后更新:2026-06-20*