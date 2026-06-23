# 完整路由表 — tax-compliance 24 skill × 意图

> 来源:scene-claudemd-curator CLAUDE.md § 2
> 适用:agent 路由用户意图到主入口 skill
> **规则:先问用户"想做什么" → 按本表匹配 → 不要乱调**

---

## 0. 路由决策树

```
用户输入"我要做 X"
  ↓
[Step 1] X 是否在 5 大业务线范围？
  ├─ 否 → "请告诉我想做什么" + 提示
  └─ 是 → [Step 2] X 是哪个业务线？
        ├─ 入口路由 → tax-type-classifier
        ├─ VAT/发票 → invoice-compliance-checker
        ├─ 企所税 → eit-return-reviewer
        ├─ 转让定价 → transfer-pricing-checker
        ├─ 跨境 → cross-border-tax-checker
        ├─ 个税 → individual-income-tax-planner
        ├─ 争议 → tax-dispute-handler
        └─ 法规更新 → reg-feed-watcher
```

---

## 1. 5 大业务线主入口路由表

### 1.1 入口路由（tax-type-classifier）

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 不知道涉及什么税 | "我要交什么税" | tax-type-classifier | 企业类型？主营业务？ |
| 综合性税务咨询 | "我们公司有哪些税" | tax-type-classifier + 多 skill | 综合判定 |

### 1.2 VAT/发票合规

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 发票合规检查 | "发票合规" / "虚开发票" / "三流合一" | invoice-compliance-checker | 发票类型？交易内容？ |
| 增值税税率判断 | "增值税税率" / "13% / 9% / 6% / 3%" | vat-rate-classification-advisor | 业务类型？小规模/一般？ |
| 增值税进项抵扣 | "进项抵扣" / "不能抵扣" | input-tax-credit-checker / vat-credit-calculator | 是否合规凭证？不得抵扣项？ |
| 消费税合规 | "消费税" | consumption-tax-compliance | 商品类型？ |

### 1.3 企业所得税/扣除

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 汇算清缴 | "汇算清缴" / "企所税" / "纳税调整" | eit-return-reviewer | 纳税调整项？弥补亏损？ |
| 扣除项目合规 | "扣除" / "限额" / "招待费" | deduction-compliance-checker | 发票齐全？限额比例？ |
| 税收优惠申请 | "高新" / "加计扣除" / "小微" | tax-preference-application-advisor | 高新？研发？小微？ |

### 1.4 转让定价/跨境

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 关联交易转让定价 | "转让定价" / "关联交易" / "利润率" | transfer-pricing-checker | 关联交易类型？利润率？避税地？ |
| 转让定价风险评估 | "转让定价风险" / "被调查" / "APA" | transfer-pricing-risk | 是否被调查？需 APA？ |
| BEPS 双支柱 | "BEPS" / "双支柱" / "GloBE" | beps-compliance-advisor | 全球收入？跨国集团？ |
| 跨境支付扣缴 | "跨境" / "代扣代缴" / "预提所得税" | cross-border-tax-checker | 支付类型？对方国家？是否常设机构？ |
| 协定待遇 | "税收协定" / "避免双重征税" | tax-treaty-application-advisor | 是否签税收协定？税收居民证明？ |

### 1.5 个人所得税

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 综合所得 | "个人所得税" / "综合所得" / "专项附加" | individual-income-tax-planner | 综合所得？专项附加扣除？ |
| 高净值筹划 | "高净值" / "海外收入" / "资产配置" | high-net-worth-tax-optimization | 资产规模？海外收入？ |
| 股权激励 | "股权激励" / "ESOP" / "上市前激励" | equity-incentive-tax-advisor | 激励类型？上市前/后？ |

### 1.6 争议应对

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 税务稽查应对 | "税务稽查" / "税务检查" / "补缴税款" | tax-dispute-handler | 稽查阶段？通知内容？ |
| 行政复议 | "行政复议" / "复议申请" | tax-dispute-handler | 是否已处罚？60 日内？ |
| 行政诉讼 | "起诉税务局" / "行政诉讼" | tax-dispute-handler | 是否复议前置？6 个月？ |

### 1.7 法规更新（横向工具）

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 法规监控 | "新政策" / "法规更新" / "国家税务总局公告" | reg-feed-watcher | 监控哪个税种？ |
| gap 分析 | "合规差距" / "差距分析" | gap-surfacer / gaps | 与现有合规对比？ |
| 政策更新 | "政策变化" / "政策对比" | policy-diff / policy-redraft | 政策变化？ |
| 评审 | "review" / "批注" / "comments" | comments | 需 review？ |

---

## 2. 未列入的意图(转交或询问)

**用户意图未在表中时:**
1. **首先** → 用 AskUserQuestion 工具问"您具体想做什么?"
2. **其次** → 用 tax-type-classifier 入口 skill 路由
3. **再次** → 找最近的 skill(避免乱调)

**典型未列入场景 + 默认路由**:

| 未列入意图 | 默认路由 |
|----------|---------|
| "我们要做税务筹划" | high-net-worth-tax-optimization + tax-preference-application-advisor |
| "我们要 IPO 税务合规" | eit-return-reviewer + transfer-pricing-checker + tax-preference-application-advisor |
| "我们要做 VIE 架构" | cross-border-tax-checker + transfer-pricing-checker |
| "我们被国税局约谈了" | tax-dispute-handler(必须立即升级) |
| "我们要做 ESG 税务" | reg-feed-watcher + 升税务律师 |
| "我们不知道该不该交这个税" | tax-type-classifier |

---

## 3. 多 skill 协同场景

### 3.1 IPO 税务合规链

```
tax-type-classifier (识别)
  → eit-return-reviewer (历史税务合规审计)
  → transfer-pricing-checker (关联交易合规)
  → tax-preference-application-advisor (高新资质)
  → tax-dispute-handler (未决争议)
```

### 3.2 跨境架构搭建链

```
tax-type-classifier (识别中国税务)
  + cross-border-tax-checker (中国扣缴义务)
  + tax-treaty-application-advisor (协定待遇)
  + transfer-pricing-checker (集团内转让定价)
  + beps-compliance-advisor (GloBE 影响)
```

### 3.3 稽查应对链

```
tax-dispute-handler (应对策略)
  + tax-type-classifier (涉及税种)
  + eit-return-reviewer (历史汇算清缴)
  + invoice-compliance-checker (发票合规审计)
  + transfer-pricing-checker (关联交易合规)
```

---

## 4. 路由避坑(Pattern § 0.8)

### 4.1 不能直接做的"路由表阻断规则"

| 用户说 | ❌ 不能直接做 | ✅ 必须先做 |
|--------|------------|----------|
| "我们要补缴税款" | 不能直接算补缴金额 | 必须先 tax-dispute-handler 看是否有争议空间 |
| "我们想做转让定价" | 不能直接做 APA | 必须先 transfer-pricing-checker 做风险评估 |
| "我们要申请高新" | 不能直接申请 | 必须先 tax-preference-application-advisor 评估资质 |
| "我们要跨境支付" | 不能直接代扣 | 必须先 cross-border-tax-checker 判断协定待遇 |

### 4.2 路由红线

**以下意图 agent 必须**:
1. 立即升级到税务律师/会计师(§ 5.2)
2. 停止继续路由
3. 提示用户

| 路由红线 | 升级目标 |
|---------|---------|
| "虚开发票" | 税务律师 + 刑事律师 |
| "偷税" | 税务律师 + 财务总监 |
| "骗取出口退税" | 税务律师 + 海关律师 |
| "抗税" | 立即停止 + 报警 |
| "避税安排" | 转让定价专业律师 |

---

*Greater China Legal — tax-compliance routing-table v3*
*5 大业务线主入口 + 24 skill 完整路由*
*最后更新:2026-06-20*