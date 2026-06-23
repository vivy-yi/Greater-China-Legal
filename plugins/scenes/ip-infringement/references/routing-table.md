# 完整路由表 — ip-infringement 27 skill × 意图

> 来源:scene-claudemd-curator CLAUDE.md § 2
> 适用:agent 路由用户意图到主入口 skill
> **规则:先问用户"想做什么" → 按本表匹配 → 不要乱调**

---

## 0. 路由决策树

```
用户输入"我要做 X"
  ↓
[Step 1] X 是否涉及特定 IP 类型？
  ├─ 商标 → trademark-search (主入口)
  ├─ 专利 → fto-triage (主入口)
  ├─ 著作权 → content-copyright-dispute (主入口)
  ├─ 商业秘密 → secret-identification-assessment (主入口)
  └─ 维权路径 → infringement-triage (主入口)
  ↓
[Step 2] X 是哪个具体场景？
  ├─ 商标检索 → trademark-search
  ├─ 商标侵权判断 → trademark-infringement-assessment
  ├─ FTO / 专利侵权 → fto-triage + patent-claim-analysis
  └─ ...
```

---

## 1. 5 大业务线主入口路由表

### 1.1 商标（trademark）

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 商标检索 | "商标查询" / "商标检索" / "排查商标" | trademark-search | 商标名/图形？尼斯分类？地域？ |
| 商标检索报告 | "商标报告" / "检索报告" | trademark-search-report | 报告类型？行业？ |
| 商标侵权判断 | "商标侵权" / "近似商标" / "假冒商标" | trademark-infringement-assessment | 商品类别？驰名商标？ |
| 商标许可合同 | "商标许可" / "品牌授权" | brand-license-contract | 许可范围？期限？质量监督？ |

### 1.2 专利（patent）

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| FTO（自由实施） | "FTO" / "自由实施" / "专利风险" | fto-triage | 产品？技术领域？目标市场？ |
| 专利侵权分析 | "专利侵权" / "落入保护范围" / "全面覆盖" | patent-claim-analysis | 权利要求？被控产品？ |
| 专利无效宣告 | "无效宣告" / "现有技术" | patent-invalidity-defense | 无效理由？现有技术？ |
| 专利有效性核查 | "专利有效性" / "专利无效核查" | patent-validity-checker | 申请号/专利号？ |
| 技术交底 | "技术交底" / "专利申请" | invention-intake | 技术方案？附图？ |
| 上市/并购 IP 风险排查 | "IP 风险排查" / "IP clearance" / "并购 IP" | clearance | 标的 IP 清单？ |

### 1.3 著作权（copyright）

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 内容著作权 | "内容侵权" / "文章侵权" / "图片侵权" | content-copyright-dispute | 作品类型？原创性？接触？ |
| 音乐/影视 | "音乐版权" / "影视版权" / "信息网络传播权" | music-film-copyright | 著作权登记？授权链条？ |
| 软件著作权 | "软著侵权" / "代码相似" | software-copyright-analysis | 源代码/目标代码？相似度？ |
| 开源合规 | "开源合规" / "GPL" / "MIT" | oss-review | 开源许可证？商用？分发？ |

### 1.4 商业秘密（trade-secret）

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 商业秘密识别 | "商业秘密" / "秘密性" / "保密性" | secret-identification-assessment | 三性测试？载体？保密措施？ |
| 员工商业秘密风险 | "员工泄密" / "离职" / "在职" | employee-trade-secret-risk | 接触范围？保密协议？ |
| 商业秘密诉讼 | "商业秘密诉讼" / "侵权诉讼" | trade-secret-litigation | 证据？侵权方式？损失？ |

### 1.5 维权路径（enforcement）

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 维权路径选择 | "维权" / "怎么打" / "行政/民事/刑事" | infringement-triage | IP 类型？情节？损失？ |
| 警告函/律师函 | "警告函" / "律师函" / "停止侵权" | cease-desist | 对方明确？侵权证据？ |
| 平台下架 | "下架" / "投诉" / "TRO" | takedown | 平台？商品？投诉理由？ |
| 证据收集/公证 | "证据" / "公证" / "时间戳" | infringement-evidence-collection | 公证/区块链/时间戳？ |
| 赔偿计算 | "赔偿" / "损害" / "许可费倍数" | damage-calculator | 实际损失/获利/许可费？ |
| 整体维权策略 | "维权策略" / "批量维权" | rights-protection-path | 行政/民事/刑事？批量？ |

### 1.6 横向工具

| 用户意图 | 触发词 | 主入口 skill | 主动问 |
|---------|-------|------------|-------|
| 侵权识别 | "识别侵权" / "技术比对" | infringement-detector | 来源？技术/商标比对？ |
| 证据指南 | "证据指南" / "如何取证" | evidence-guide | 证据类型？取证方式？ |
| IP 资产盘点 | "IP 资产" / "商标清单" / "专利清单" | portfolio | IP 资产清单？ |
| 合同 IP 条款审查 | "IP 条款" / "合同审查" | ip-clause-review | 合同类型？IP 条款？ |

---

## 2. 未列入的意图(转交或询问)

**用户意图未在表中时:**
1. **首先** → 用 AskUserQuestion 工具问"您具体想做什么?"
2. **其次** → 用 infringement-triage 入口 skill 路由
3. **再次** → 找最近的 skill(避免乱调)

**典型未列入场景 + 默认路由**:

| 未列入意图 | 默认路由 |
|----------|---------|
| "我们要做 IP 战略规划" | portfolio + ip-clause-review + 多 IP 类型 |
| "我们被起诉专利侵权" | patent-claim-analysis + patent-invalidity-defense + evidence-collection |
| "我们想 IPO 上市" | clearance + portfolio + ip-clause-review |
| "我们收到警告函" | cease-desist + infringement-triage |
| "我们想做驰名商标认定" | trademark-infringement-assessment + portfolio |
| "我们想做专利布局" | fto-triage + invention-intake + clearance |

---

## 3. 多 skill 协同场景

### 3.1 商标维权全流程链

```
trademark-search (商标检索)
  + trademark-infringement-assessment (侵权判断)
  + infringement-evidence-collection (证据收集)
  + cease-desist (警告函)
  + takedown (平台下架)
  + damage-calculator (赔偿计算)
  + rights-protection-path (维权策略)
```

### 3.2 专利侵权应对链

```
fto-triage (FTO 风险评估)
  + patent-claim-analysis (侵权分析)
  + patent-invalidity-defense (无效宣告)
  + infringement-evidence-collection (证据)
  + damage-calculator (赔偿)
  + rights-protection-path (维权策略)
```

### 3.3 跨境电商 IP 维权链

```
clearance (上市前 IP 风险排查)
  + trademark-search (商标检索)
  + takedown (亚马逊/eBay 投诉)
  + infringement-evidence-collection (公证)
  + rights-protection-path (海关 + 平台 + 诉讼)
```

### 3.4 商业秘密刑事报案链

```
secret-identification-assessment (三性测试)
  + infringement-evidence-collection (侵权证据)
  + employee-trade-secret-risk (员工追溯)
  + rights-protection-path (行政 → 民事 → 刑事)
```

---

## 4. 路由避坑(Pattern § 0.8)

### 4.1 不能直接做的"路由表阻断规则"

| 用户说 | ❌ 不能直接做 | ✅ 必须先做 |
|--------|------------|----------|
| "我们要起诉对方商标侵权" | 不能直接起诉 | 必须先 trademark-search + 证据保全 |
| "我们要发警告函" | 不能直接发 | 必须先 infringement-triage + 证据 |
| "我们要做专利无效" | 不能直接申请 | 必须先 patent-invalidity-defense + 现有技术检索 |
| "我们要做开源合规审查" | 不能直接审 | 必须先 oss-review |
| "我们要申请驰名商标" | 不能直接申请 | 必须先 trademark-infringement-assessment |

### 4.2 路由红线

**以下意图 agent 必须**:
1. 立即升级到 IP 律师(§ 5.2)
2. 停止继续路由
3. 提示用户

| 路由红线 | 升级目标 |
|---------|---------|
| 假冒注册商标刑事风险 | 立即停止 + 商标律师 + 刑事律师 |
| 假冒专利刑事风险 | 立即停止 + 专利律师 + 刑事律师 |
| 侵犯著作权刑事风险 | 立即停止 + 著作权律师 + 刑事律师 |
| 商业秘密刑事报案 | 立即升级 + IP 律师 |
| 跨境电商大规模侵权 | 立即升级 + IP 律师 + 海关律师 |
| SEP / 标准必要专利 | 立即升级 + IP 律师 + 反垄断律师 |

---

*Greater China Legal — ip-infringement routing-table v3*
*5 大业务线主入口 + 27 skill 完整路由*
*最后更新:2026-06-20*