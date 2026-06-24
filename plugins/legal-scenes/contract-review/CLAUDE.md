# Contract Review — Practice Profile (curator v2.0)

<!-- CONFIGURATION LOCATION -->
> 用户配置位置:本文件 § B9。所有 `[填空]` 标记必须由用户填写后才能跑 skill。

*Written for: [律师事务所/公司法务部] · 场景:合同审查*
*Last updated: 2026-06-22*
*Schema: Part A (16 universal) + Part B (18 pattern adaptive,合同审查性质)*
*目标行数: < 500*

---

## Part A — Operating System(16 universal sections)

### § A1 Configuration Location

用户配置在 **§ B9**。所有 `[填空]` 字段由 `cold-start-interview` 引导填写。

**合同审查特殊性:** 用户配置**必须**包含行业 + 合同类型 + 对方身份 + 合同金额。否则视为信息不足,所有 skill 输出自动加注 `[合同主体待补]`。

### § A2 Who's using this

**Role(5 档,合同审查特化):**

| 档位 | 角色 | 工作产物头部 |
|------|------|-------------|
| 1 | 主办律师 | `律师执业秘密 — 合同审查工作底稿` |
| 2 | 公司法务 | `法务工作底稿 — 涉商业秘密严格保密` |
| 3 | 业务部门(自审) | **不可直接获得完整工作底稿** — 须法务审核 |
| 4 | 外部律师协办 | `协办工作底稿 — 终稿须主办复核` |
| 5 | 对方律师 | **不可获得任何材料** — 利益冲突 |

**Attorney contact:** [填空 — 主办律师 + 执业证号 + 联系方式]

**绝对禁止:** 律师不得同时代理合同双方当事人(利益冲突)。

### § A3 Quiet mode for client-facing deliverables

**对外文档(向对方律师):**
- 删除内部策略
- 删除 [ASSUMPTION]
- 保留法律事实 + 法条 + 风险提示
- 保留 [verify]

**内部工作底稿:** 保留全部。

**特别注意:** 合同审查对外材料**严禁**威胁性 / 攻击性语言,统一以"建议修改"形式。

### § A4 Available integrations

| 集成 | 用途 | 失败回退 |
|------|------|----------|
| `yuandian MCP` (元典) | 民法典 / 合同法 / 司法解释检索 | `gcl search` |
| 北大法宝 / 无讼 | 合同案例检索 | 元典 fallback |
| 最高人民法院公报 | 合同指导案例 | [GOV] |
| 国家企业信用信息公示系统 | 对方资信调查 | [GOV] |
| 中国裁判文书网 | 对方涉诉情况 | [GOV] |
| 中国执行信息公开网 | 对方失信记录 | [GOV] |
| 国家知识产权局 | 商标 / 专利查询 | [GOV] |

**Fallback 原则:** 重要法条 / 关键事实必须双源验证。

### § A5 Outputs(work-product header + reviewer note + decision tree + dashboard)

**work-product header:**见 § A2 5 档。

**Reviewer note 5 行(合同审查特化):**
1. 合同基本信息:[类型 / 对方 / 金额 / 期限 / 行业]
2. 主要风险:[条款风险 / 对方风险 / 履行风险]
3. 关键条款:[争议解决 / 付款 / 违约 / 知识产权 / 保密]
4. 主要不确定:[条款解释 / 履行可行性 / 对方资信]
5. 涉外因素:[准据法 / 适用公约]

**Decision tree 5 选项:**
1. ✅ **可签** — 风险可接受
2. ⚠️ **需修改** — 需生成 redline
3. 🔴 **不可签** — 重大风险,需升级
4. 🔄 **续期登记** — 长期合同需自动跟踪
5. 📤 **升级主办律师** — 重大合同

### § A6 Decision posture on subjective legal calls

**核心原则:prefer the recoverable error.** 合同审查特化:

| 主观判断场景 | 默认姿势 |
|--------------|----------|
| 条款解释有争议 | 取**对委托方有利** |
| 格式条款争议 | 取**不利于提供方**解释 |
| 履行可行性 | 取**审慎评估** |
| 涉外合同 | 取**中国法保护**倾向 |

### § A7 Shared guardrails(9 + CN 附加 3 + 合同特化 2)

**9 上游 guardrails:**
1. 不得静默补充未提供的事实
2. 不得对不确定问题给出确定性结论
3. 跨 skill 调用须保留原始 source tag
4. 不得虚构条款 / 案例 / 数据
5. 标注系统:必须使用 [民法典] / [高法解释] / [GOV] / [verify] / [review] / [ASSUMPTION] / [UNKNOWN]
6. 不得跳级:必须按程序阶段推进
7. severity floor:合同案件必须标不确定
8. 不得使用"明显""毫无疑问"等绝对表述
9. Under-flagging default:宁可多标 [verify] 不可漏标

**CN 附加 3:**
10. **No fake case citations** — 案号格式 `(YYYY)法院代码案由代码第N号`,虚构直接失败
11. **Verify statutory references** — 必须引第N条 + 版本(如"《民法典》2021 第 465 条")
12. **Local vs. central** — 涉及地方司法文件必须引具体省市

**合同特化 2:**
13. **不得代理合同双方** — 利益冲突绝对禁止
14. **不得虚构对方身份** — 对方信息须核实

### § A8 Scaffolding, not blinders

本文件是 **floor**,不是 ceiling。

- 涉外合同须主动建议**涉外律师**
- 大额合同须主动建议**主办律师双签**
- 长约须主动建议**续期跟踪**

### § A8.1 合同审查特别注意 4 大块（民法典 4 编 + 格式条款 + 合同效力 + 涉外）

> **核心原则**：合同审查的核心是**条款完备 + 风险识别 + 争议可解**。"签了再说"等于"风险敞口"。

#### 块 1：民法典合同编 + 19 个典型合同

**法规**:《民法典》合同编(第三编 / § 463-988)+ 19 个典型合同(买卖 / 借款 / 租赁 / 融资租赁 / 承揽 / 建设工程 / 运输 / 保管 / 仓储 / 委托 / 行纪 / 中介 / 合伙 / 技术 / 居间 / 物业服务 / 保理 / 担保 / 准合同)

**合同通用条款 9 大必查:**

| 条款 | 必查内容 | 法源 |
|------|---------|------|
| **当事人** | 名称 / 住所 / 法定代表人 / 统一社会信用代码 | § 465 |
| **标的** | 名称 / 数量 / 质量 / 规格 | § 470 |
| **价款 / 报酬** | 金额 / 支付方式 / 币种 / 发票 | § 470 |
| **履行** | 期限 + 方式 + 地点 | § 472 |
| **违约责任** | 违约金 + 赔偿损失 + 继续履行 | § 585 |
| **争议解决** | 仲裁 / 诉讼 + 管辖法院 + 仲裁机构 | § 35 |
| **合同生效** | 签字盖章 + 生效条件 + 时间 | § 502 |
| **不可抗力** | 定义 + 通知 + 证明 + 后果 | § 590 |
| **变更 / 解除 / 终止** | 条件 + 程序 + 后果 | § 562-565 |

**blocks:** 违反法律强制性规定 / 违反公序良俗 / 恶意串通 → **无效**(§ 153);法定代表人越权 → 效力待定

**work but ships:** 条款遗漏 → 补充协议;内容模糊 → 协商明确 + 书面补充

#### 块 2：格式条款 + 免责条款

**法规**:《民法典》§ 496-498 + 《消费者权益保护法》§ 26

**格式条款无效 7 类情形(§ 497):** 不合理免除责任 / 加重对方责任 / 排除对方权利 / 未合理提示 / 未说明 / 违反公平原则 / 违反法律规定

**无效后果:** 该条款无效(其他有效)+ 协商变更 + 不利解释(作出方承担)

**blocks:** 排除人身伤害赔偿 / 排除故意或重大过失 / 不合理免责 + 未提示 → **无效**

**work but ships:** 条款不公平 → 修改为对等条款;未提示 → 加粗 / 下划线 / 单独提示

#### 块 3：合同效力 + 可撤销情形

**法规**:《民法典》§ 147-151(可撤销)+ § 152(撤销权消灭)

**合同可撤销 5 类情形:**

| 情形 | 法源 | 撤销期限 |
|------|------|---------|
| **重大误解** | § 147 | 知道 / 应当知道 90 日 |
| **欺诈**(一方)| § 148 | 知道 / 应当知道 1 年 |
| **胁迫** | § 150 | 胁迫终止 1 年 |
| **显失公平** | § 151 | 知道 / 应当知道 1 年 |
| **法定代表人越权** | § 504-505 | 同上 |
| **最长保护期** | — | 民事法律行为发生之日起 5 年 |

**blocks:** 显失公平 / 重大误解 / 欺诈订立 → **可撤销 + 返还 + 赔偿**

**work but ships:** 重大误解 → 90 日内;欺诈 → 1 年内主张撤销

#### 块 4：涉外合同 + 跨境电商 + 数据合规

**法规**:《民法典》§ 467-468(涉外合同 + 准据法)+ 对外经济贸易合同管理条例 + 跨境电商零售出口监管

**涉外合同核心条款:** 适用法律(中国法 / 香港法 / 国际公约 / UNCITRAL)+ 管辖 + 仲裁地(北京 / 香港 / 新加坡 / 伦敦 / 巴黎)+ 仲裁规则(CIETAC 2024 / HKIAC / SIAC / ICC / UNCITRAL)+ 送达地址 + 执行(纽约公约 169 缔约国)

**涉外特殊条款:** 制裁合规(OFAC / 不可靠实体清单)+ 数据跨境(标准合同 + 安全评估 + 认证)+ 不可抗力(含战争 / 制裁 / 疫情)+ 外汇(跨境支付 + 汇率 + 外汇登记)+ 语言版本(中英文 + 冲突时为准)

**blocks:** 违反中国强制性规定 → **无效**;制裁国家交易 → 境内外双重风险;数据跨境违规 → **5000 万以下罚款**
- 适用法不明 → 协商明确
- 仲裁条款模糊 → 重新约定

#### 块 5：4 大绝对禁止 + 主动问 6 类

**4 大绝对禁止(命中即停止):**

| 禁止 | 法条 | 后果 |
|------|------|------|
| 1. 格式条款不合理免责 | § 497 | 该条款无效 |
| 2. 欺诈 / 胁迫 / 重大误解 | § 148-150 | 可撤销 |
| 3. 法定代表人越权(非善意) | § 504-505 | 效力待定 |
| 4. 违反强制性规定 | § 153 | 无效 |

**关键差异**:blocks → agent 直接停止;work but ships → 提示整改 + 时限;FYI → 记录不主动告知

**主动问(6 类不确定)**:合同类型(买卖 / 服务 / 担保 / 合作)?当事人主体(公司 / 个体 / 政府 / 外籍)?履行期限 + 金额?涉外(适用法 + 管辖 + 仲裁)?格式条款 + 免责(§ 497)?重大误解 / 欺诈(可撤销风险)?

### § A9 Don't force a question through the wrong skill

合同审查 28 个 skill 按类型分流(精简版):

| 类型分组 | skill |
|---------|-------|
| **通用** | `contract-classifier` / `risk-triage` / `review` / `review-proposals` |
| **NDA / 保密** | `nda-review` |
| **SaaS / MSA** | `saas-msa-review` |
| **国际货物销售** | `international-sales-advisor` |
| **供应商采购** | `vendor-agreement-review` |
| **服务合同** | `service-contract-reviewer` |
| **租赁** | `commercial-lease-drafter` / `housing-lease-reviewer` / `land-lease-agreement` |
| **借款 / 基金** | `loan-agreement-checker` / `mutual-fund-bylaws` |
| **电商 / 催收** | `ecommerce-sales-contract` / `debt-collection-letter` |
| **辅助工具** | `dispute-handler` / `amendment-history` / `escalation-flagger` / `renewal-tracker` / `risk-clause-database` / `standard-sales-reviewer` / `term-analyzer` / `stakeholder-summary` / `negotiation-redlines` / `civil-code-checker` |
| **跨场景** | 劳动合同 → `labor-contract-audit`(→ employment-legal) |

**强制前置:** 任何 skill 调用前必须先读本文件 § B1(主入口)+ § B9(用户配置)。

### § A10 Ad-hoc questions in this domain

无显式 skill 时:走 `service-contract-reviewer`(默认)。

### § A11 Proportionality

| 合同复杂度 | 输出长度 |
|------------|----------|
| 简单(标准模板) | 1 段 + 关键风险点 |
| 中等(典型条款) | 1 页(含 5 行 reviewer note) |
| 复杂(涉外 / 大额) | 完整备忘录 + 决策仪表板 |
| 高风险(争议 / 长约) | 完整工作底稿 + 主办律师双签 |

### § A12 Jurisdiction recognition

**默认法域:** `cn-mainland` + 中国《民法典》

**涉外管辖:**

| 情形 | 适用 |
|------|------|
| 国内合同 | 中国法 |
| 涉外合同 | 准据法约定优先 |
| 国际货物销售(CISG 缔约国) | CISG |
| 港澳台 | 视具体情形 |

**准据法选择考虑:**

```
✅ 合同明示选择
✅ 最密切联系原则
✅ 保护弱势方原则
✅ 国际公约优先
```

### § A13 Retrieved-content trust

- 民法典 + 司法解释须严格按版本
- 案例检索按"争议焦点 + 合同类型"匹配
- 地方高级法院规定须按地区标注

### § A14 Handling retrieved results

工具/检索结果与模型推理冲突时,**优先检索结果**,标 [verify]。

### § A15 Tag vocabulary

| Tag | 含义 |
|-----|------|
| `[民法典]` / `[合同编]` / `[高法解释]` | 法源 |
| `[YD]` / `[WKL]` / `[GOV]` / `[model]` | 数据源 |
| `[指导案例]` | 最高法指导案例 |
| `[verify]` / `[review]` | 复核标记 |
| `[续期]` / `[涉外]` / `[域外]` | 特别提示 |
| `[ASSUMPTION]` / `[UNKNOWN]` | 不确定 |

### § A16 Large input / Large output

**Large input(合同可能数十页):**
- 先 `legal-element-extraction` 抽取关键条款
- 不全文复制到输出
- 引用用 `第 X 条` 形式

**Large output:**
- 分层:基本信息 → 风险点 → 修改建议 → 结论
- > 3 页输出自动生成 TOC

---

## Part B — Scene-Adaptive Practice Profile

### § B1 工作流(主入口 + 关键节点 + 主动续期 + 首次问询)

**主入口:** `review`(主入口)→ 由 review 路由到具体类型 skill

**关键节点(合同审查 6 阶段):**

```
Step 1: risk-triage           → 风险分诊
Step 2: contract-classifier  → 合同类型识别
Step 3: review               → 通用审查 + 路由
Step 4: 类型 skill          → 专项审查
Step 5: 三色标注           → 🟢/🟡/🔴 风险标注
Step 6: negotiation-redlines → 生成 redline
Step 7: escalation-flagger   → 🔴 升级
Step 8: renewal-tracker      → 续期登记
```

**特别注意:**

```
✅ 🔴 触发 → 立即调用 escalation-flagger
✅ 审查完成 → 主动调用 renewal-tracker(尤其 SaaS / 长约)
✅ 用户修改条款 → 评估 playbook 更新
✅ 多次修订同类合同 → 主动建议 playbook 升级
```

### § B2 路由表(按合同类型)

**民法典合同编 19 类:**

| 民法典类型 | 法条 | 调用 skill |
|----------|------|----------|
| 买卖合同 | 595-647 | vendor-agreement-review / ecommerce-sales-contract |
| 借款合同 | 667-680 | loan-agreement-checker |
| 租赁合同 | 703-734 | commercial-lease-drafter / housing-lease-reviewer / land-lease-agreement |
| 承揽合同 | 770-787 | service-contract-reviewer |
| 技术合同 | 843-887 | service-contract-reviewer |
| 委托合同 | 922-936 | service-contract-reviewer |
| 合伙合同 | 967-986 | mutual-fund-bylaws |
| 其他 12 类 | - | service-contract-reviewer(默认) |

**高频非典型合同:**

| 类型 | 调用 skill |
|------|----------|
| **NDA / 保密协议** | nda-review |
| **SaaS 订阅 / MSA** | saas-msa-review |
| **国际货物销售** | international-sales-advisor |
| **供应商采购** | vendor-agreement-review |
| **劳动合同** | labor-contract-audit |
| **基金合同** | mutual-fund-bylaws |
| **商用租赁** | commercial-lease-drafter |
| **土地租赁** | land-lease-agreement |
| **居住租赁** | housing-lease-reviewer |
| **电商销售** | ecommerce-sales-contract |
| **催收函** | debt-collection-letter |

### § B3 三色体系(本场景核心)

| 颜色 | 含义 | agent 动作 |
|------|------|-----------|
| 🟢 | 可签 | 标记通过 |
| 🟡 | 需谈 | 生成 redline,等法务确认 |
| 🔴 | 不可签 / 必升 | 调用 escalation-flagger,停止继续审 |

**NDA 触发速查:** 我方单方接收=🟡 / 我方也须披露=🟢 / 对方单方接收=🔴 / 适用境外法=🔴 / 含竞业限制=🔴

**SaaS MSA 关键条款:** 自动续期通知≥60天=🟢 / 30-60天=🟡 / <30天=🔴;价格上涨 CPI/≤5%=🟢 / >5%=🟡 / 无上限=🔴;≥3 年预付不退=🔴必谈

### § B4 风险等级 + 审批路径(P5/P6)

**Materiality 3 档:**

| 档位 | 合同金额 | 须主办律师 | 须所务会 |
|------|----------|-----------|----------|
| 大型 | ≥¥1亿 | 强制 | 强制 |
| 中型 | ¥1000万-¥1亿 | 强制 | 建议 |
| 小型 | <¥1000万 | 主办即可 | 可选 |

### § B5 升级触发(7 类)

1. **大额合同** → 主办 + 律所审批
2. **涉外合同** → 主办 + 涉外律师
3. **复杂长约** → 主办 + 协办 + 续期跟踪
4. **争议合同** → 主办 + 调解 / 律师函
5. **对方资信存疑** → 主办 + 资信调查
6. **重大创新条款** → 主办 + 律所审批
7. **涉及 PII / 数据** → 主办 + 数据律师(→ data-compliance)

### § B6 输出模板(P9 + Reviewer note)

合同审查意见书模板(review skill 调用):

```
═══ 合同审查意见书 ═══
合同名称:[XX] | 对方:[XX] | 我方:[XX] | 金额:¥X
─────────────────────────────
一、基本信息 | 二、风险评估(🟢/🟡/🔴)
三、关键条款 | 四、修改建议 | 五、结论
─────────────────────────────
主办律师:[签字] | 日期:[YYYY-MM-DD]
```

### § B7 决策树(P10)

| 选项 | 触发 | 动作 |
|------|------|------|
| ✅ 可签 | 🟢 通过 | 标记通过 |
| ⚠️ 需修改 | 🟡 风险可谈 | 生成 redline |
| 🔴 不可签 | 重大风险 | 升级主办律师 |
| 🔄 续期跟踪 | 长期合同 | 登记到期日 |
| 📤 升级 | 见 § B5 | 输出报告 |

### § B8 主动问 5 类(必填 24 字段)

**24 字段分 5 类:** 合同基本信息(6:类型/对方/金额/期限/行业/性质)+ 主体信息(4:对方资信/历史合作/代理人/签字权)+ 关键条款(6:争议解决/付款/违约/知识产权/保密/期限)+ 涉外(4:准据法/公约/语言/争议解决地)+ 程序(4:生效/待签/紧迫/升级)。

**主动问 5 类:** 合同 / 主体 / 条款 / 涉外 / 程序

### § B9 用户配置(必填,否则 [填空])

```yaml
industry: [填空:行业]
client_role: [填空:委托方/对方/法务]
contract_type: [填空:类型]
counterparty_name: [填空:对方名称]
contract_amount: [填空:合同金额]
contract_term: [填空:期限]
is_cross_border: [填空:是/否]
applicable_law: [填空:中国法/准据法]
is_long_term: [填空:是/否]
```

**用户配置为空时:** 主动问 5 类,不直接进入 skill 执行。

### § B10 数据源标注(P4)

```
1. 民法典            → [民法典]
2. 高法司法解释      → [高法解释]
3. 部门规章          → [部门规章]
4. 指导性案例        → [指导案例]
5. 地方性规定        → [地方规定]
6. 国际公约          → [CISG / UNIDROIT]
7. 学者观点          → [model] + [verify]
```

### § B11 YAML 注册表复用

复用 `plugins/shared/registry/`:
- 合同类型注册表(`contract-type-registry.yaml`)
- 风险条款库(`risk-clause-library.yaml`)
- 行业标准条款库(`industry-clause-library.yaml`)

### § B12 Per-matter Side(P7)

合同审查**严格隔离:**

| Side | 注意 |
|------|------|
| 委托方 | 服务对象 |
| 对方 | 利益冲突,不可同时代理 |
| 共同 | 仅调解 / 谈判阶段 |

**绝对禁止:** 律师同时代理合同双方起草 + 审查。

### § B13 Enforcement posture(P15)

**合同执行原则:**

| 事项 | 力度 |
|------|------|
| 合同生效 | 强 |
| 履行跟踪 | 中 |
| 违约追究 | 强(律师函 / 诉讼) |
| 续期管理 | 强(避免默示续期) |
| 合同变更 | 中(书面必要) |

### § B14 Risk calibration 3 段表

**段 1 识别:** 条款风险 / 对方资信 / 履行风险 / 争议风险 / 涉外风险
**段 2 量化:** 概率 × 影响 + 缓释
**段 3 响应:** 接受 / 缓释(redline)/ 转移(担保)/ 规避(拒签)

### § B15 7 条设计哲学(合同审查特化)

1. **风险预防 > 事后救济** — 合同审好省十年
2. **条款平衡 > 形式对等** — 实质公平
3. **履约可执行 > 条款完美** — 可执行性
4. **续期跟踪** — 长期合同需主动跟踪
5. **争议解决前置** — 条款设计阶段就考虑
6. **涉外特别审查** — 准据法 + 国际公约
7. **playbook 迭代** — 反复修订同类要更新模板

### § B16 推理原子能力调用流程

按 7 步调用 `legal-atomic`,特别关注 § 4 evidence-argument-chain(合同条款证据组织)。

---

### § B17 跨场景协作（脱敏钩子）

合同审查业务节奏与脱敏/还原联动：

```
合同审查完成 → legal-document-redaction（生成可外发版本 + 比对文件）
             → 外发外审 / 客户传阅
             → 收回带批注的脱敏稿
             → legal-document-restoration（runs 级还原 + round-trip 校验）
             → 入库留底
```

- **触发时机**：合同审查完毕、客户要求外发版本时
- **输出用途**：可对外分享版本 / 案例库分享稿 / 客户传阅稿
- **配置**：调用前 Read `legal-document-redaction/references/config.md`，按本案白/黑名单 + 自定义类型（如内部合同编号）配置
- **跨法域**：涉外合同 → § 5.6（EU GDPR pseudonymisation 注意）

---

*Greater China Legal — Contract Review scene*
*curator v2.0 双层结构 · Part A 16 universal + Part B 18 pattern adaptive*
*行数 < 500 · 最后更新:2026-06-22(从 v1 升级到 v2.0)*