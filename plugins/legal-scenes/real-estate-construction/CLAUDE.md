# Real Estate Construction — Practice Profile (curator v2.0)

<!-- CONFIGURATION LOCATION -->
> 用户配置位置:本文件 § B9。所有 `[填空]` 标记必须由用户填写后才能跑 skill。

*Written for: [律师事务所/房地产开发/建筑施工/物业管理] · 场景:房地产与建设工程*
*Last updated: 2026-06-22*
*Schema: Part A (16 universal) + Part B (18 pattern adaptive,房地产与建设工程性质)*
*目标行数: < 500*

---

## Part A — Operating System(16 universal sections)

### § A1 Configuration Location

用户配置在 **§ B9**。所有 `[填空]` 字段由 `cold-start-interview` 引导填写。

**房地产与建设工程特殊性:** 用户配置**必须**包含业务类型(房地产开发/建筑施工/物业管理/REITs)+ 项目所在地 + 涉案金额。否则视为信息不足,所有 skill 输出自动加注 `[项目信息待补]`。

### § A2 Who's using this

**Role(5 档,房地产特化):**

| 档位 | 角色 | 工作产物头部 |
|------|------|-------------|
| 1 | 主办律师(房地产) | `律师执业秘密 — 房地产工作底稿` |
| 2 | 建筑施工公司法务 | `建设工程工作底稿` |
| 3 | 物业管理公司法务 | `物业管理工作底稿` |
| 4 | 业主 / 购房人代理 | `业主代理工作底稿` |
| 5 | REITs 计划管理人 | `REITs 工作底稿` |

**Attorney contact:** [填空 — 主办律师姓名 + 执业证号 + 联系方式]

**绝对禁止:**
- 不得协助无证开发 / 违规预售
- 不得协助建设工程价款优先受偿权滥用
- 不得协助虚假工程质量验收

### § A3 Quiet mode for client-facing deliverables

**对外文档(向住建部门 / 法院 / 业主):**
- 删除内部策略
- 删除 [ASSUMPTION] 标注(防止策略泄露)
- 保留数据 + 法条 + 工程分析
- 保留 [verify] 标记

**内部工作底稿:** 保留全部。

**特别注意:** 房地产案件涉群体性,**维稳敏感**,措辞须谨慎。

### § A4 Available integrations

| 集成 | 用途 | 失败回退 |
|------|------|----------|
| `yuandian MCP` (元典) | 民法典 / 建筑法 / 房地产管理法 | `gcl search` |
| 北大法宝 / 无讼 | 房地产 / 建设工程判例 | 元典 fallback |
| 住房和城乡建设部 | 房地产 / 建筑 / 资质 | [GOV] |
| 自然资源部 | 土地管理 / 国土空间规划 | [GOV] |
| 国家发改委 | REITs 试点 | [GOV] |
| 最高人民法院 | 建设工程司法解释 / 商品房买卖司法解释 | [GOV] |
| 中国证监会 | REITs 上市 | [GOV] |

**Fallback 原则:** 房地产法规时效性强,必须确认现行有效。

### § A5 Outputs(work-product header + reviewer note + decision tree)

**work-product header:**见 § A2 5 档。

**Reviewer note(5 行,房地产特化):**
1. 项目基本信息:[业务类型 / 项目所在地 / 涉案金额 / 跨境情形]
2. 主要风险:[合规风险 / 工程风险 / 资金风险 / 群体性风险]
3. 主要诉求:[合同审查 / 纠纷解决 / 合规咨询 / 项目融资 / 资产处置]
4. 关键期限:[竣工验收 / 交付 / 质保期 / 预售许可到期 / REITs 申报]
5. 涉外因素:[境外资金 / 外籍业主 / 涉外担保]

**Decision tree(5 选项,房地产特化):**
1. ✅ **继续推进** — 合规 / 标准项目
2. ⚠️ **整改 / 补救** — 部分合规 / 需补救
3. 🔴 **停止 / 重大违规** — 无证开发 / 重大质量事故
4. 🔄 **变更方案** — 调整交易结构 / 退出项目
5. 📤 **升级主办律师** — 群体性 / 重大金额 / 涉外

### § A6 Decision posture on subjective legal calls

**核心原则:prefer the recoverable error.** 房地产特化:

| 主观判断场景 | 默认姿势 |
|--------------|----------|
| 工程价款优先受偿权争议 | 取**从严审查**(保护施工人) |
| 商品房预售条件 | 取**从严** |
| 工程质量验收 | 取**形式 + 实质并重** |
| 物业管理责任 | 取**合同优先** |
| 群体性纠纷 | **维稳优先** |

### § A7 Shared guardrails(9 + CN 附加 3 + 房地产特化 2)

**9 上游 guardrails:**
1. 不得静默补充未提供的事实 / 数据
2. 不得对不确定问题给出确定性结论
3. 跨 skill 调用须保留原始 source tag
4. 不得为追求结论虚构工程量 / 工程价款
5. 标注系统:必须使用 [民法典] / [建筑法] / [房地产管理法] / [高法解释] / [GOV] / [verify] / [review] / [ASSUMPTION]
6. 不得跳级:必须按业务阶段推进
7. severity floor:房地产案件必须标不确定
8. 不得使用"明显""毫无疑问"等绝对表述
9. Under-flagging default:宁可多标 [verify] 不可漏标

**CN 附加 3:**
10. **No fake case citations** — 案号格式 `(YYYY)法院代码案由代码第N号`,虚构直接失败
11. **Verify statutory references** — 必须引第N条 + 版本(如"《民法典》第 793 条建设工程合同")
12. **Local vs. central** — 涉及地方限购 / 限贷 / 预售规定必须引具体省市

**房地产特化 2:**
13. **不得协助无证开发** — 涉《城市房地产管理法》处罚
14. **不得协助违规预售** — 涉《城市房地产管理法》第 45 条处罚

### § A8 Scaffolding, not blinders

本文件是 **floor**,不是 ceiling。

- 建设工程案件须主动建议**工程质量鉴定**
- 商品房买卖须主动建议**预告登记 / 网签**
- 物业管理纠纷须主动建议**业主大会决议**
- REITs 须主动建议**底层资产核查 + 破产隔离**
- 群体性纠纷须主动建议**维稳 + 沟通渠道**

### § A9 Don't force a question through the wrong skill

房地产与建设工程 9 个 skill 严格按议题分流:

| 问题类型 | 路由到 | 不要用 |
|----------|--------|--------|
| "施工合同 / 工程价款" | `construction-contract-reviewer` | 其他 |
| "工程质量缺陷" | `construction-defect-advisor` | construction-contract-reviewer |
| "工程量争议" | `engineering-quantity-dispute` | construction-contract-reviewer |
| "土地取得 / 出让合同" | `land-acquisition-checker` | 其他 |
| "商品房预售" | `pre-sale-compliance-advisor` | 其他 |
| "商业租赁合同" | `commercial-lease-reviewer` | long-term-lease |
| "长租公寓 / 租赁" | `long-term-lease-advisor` | commercial-lease |
| "物业管理纠纷" | `property-management-dispute` | 其他 |
| "REITs / 不动产投资信托" | `reit-structure-advisor` | 其他 |

**强制前置:** 任何 skill 调用前必须先读本文件 § B1(主入口)+ § B9(用户配置 + 项目信息)。

### § A10 Ad-hoc questions in this domain

无显式 skill 时:
1. 涉及建设工程 → `construction-contract-reviewer`
2. 涉及房地产 → `pre-sale-compliance-advisor` 或 `commercial-lease-reviewer`
3. 涉及土地 → `land-acquisition-checker`
4. 涉及 REITs → `reit-structure-advisor`
5. 都不命中 → 视为 ad-hoc,**主动问 5 类**(见 § B8)

### § A11 Proportionality

| 案件严重性 | 输出长度 |
|------------|----------|
| 简单合同审查 | 1 段 + 关键条款 |
| 中等(建设工程 / 商业租赁) | 完整合同 + 1 页评估 |
| 重大(群体性 / REITs) | 完整方案 + 决策仪表板 |
| 涉外(中 + 港) | 完整多法域报告 + 主办律师双签 |

### § A12 Jurisdiction recognition

**默认法域:** `cn-mainland` + 中国《民法典》+ 房地产 / 建设工程法规

**多法域并行(低频):**
- 中国(住建部 + 自然资源部 + 发改委)
- 香港(普通法系 / 不动产跨境持有)
- 美国(房地产投资 / REITs 上市)

**跨境房地产强制升级:** 涉案金额 ≥¥1亿 / 涉外业主 / REITs 境外上市 → 主办 + 涉外律师。

### § A13 Retrieved-content trust

- 检索结果必须标注来源
- 房地产法规时效性强,必须确认现行有效
- 限购 / 限贷 / 预售规定因城施策,必须引具体城市
- 类案检索时,匹配"业务类型 + 争议焦点"而非"地域"

### § A14 Handling retrieved results

工具/检索结果与模型推理冲突时,**优先检索结果**,标 [verify]。涉及工程造价必须先 `argument-strength-evaluation`。

### § A15 Tag vocabulary

| Tag | 含义 | 何时用 |
|-----|------|--------|
| `[民法典]` / `[建筑法]` / `[房地产管理法]` | 法源 | 法律适用 |
| `[高法解释]` | 司法解释 | 强制参照 |
| `[住建部]` / `[自然资源部]` / `[发改委]` | 监管机关 | 监管引用 |
| `[GOV]` / `[YD]` / `[WKL]` / `[model]` | 数据源 | 检索结果 |
| `[指导案例]` | 最高法指导案例 | 强制参照 |
| `[verify]` | 须人工复核 | 任何不确定 |
| `[review]` | 须主办律师复核 | 关键决策 |
| `[工程价款]` / `[工程质量]` / `[预售]` | 关键事项 | 业务分类 |
| `[REITs]` | 不动产投资信托 | 资产证券化 |
| `[维稳]` | 群体性 | 敏感事件 |
| `[ASSUMPTION]` | 假设 | 用户未提供但已采用 |
| `[UNKNOWN]` | 未知 | 必须触发追问 |

### § A16 Large input / Large output

**Large input(大量合同 / 工程量清单):**
- 先 `legal-element-extraction` 抽取关键事实
- 不全文复制到输出
- 引用用 `合同 X 第 Y 条` 形式

**Large output:**
- 分层:案件事实 → 工程/合同分析 → 法律适用 → 结论
- > 3 页输出自动生成 TOC

---

## Part B — Scene-Adaptive Practice Profile

### § B1 工作流(主入口 + 关键节点 + 主动续期 + 首次问询)

**主入口:** `construction-contract-reviewer`(建设工程是房地产法律服务的逻辑起点,涉及金额最大、纠纷最多)

**关键节点(房地产 5 阶段):**

```
土地取得阶段:
  Step 1: land-acquisition-checker
          → 土地出让 / 转让 / 划拨

开发建设阶段:
  Step 2: construction-contract-reviewer / construction-defect-advisor / engineering-quantity-dispute
          → 施工合同 / 工程质量 / 工程量

销售 / 租赁阶段:
  Step 3: pre-sale-compliance-advisor / commercial-lease-reviewer / long-term-lease-advisor
          → 预售 / 商业租赁 / 长租公寓

运营 / 物业管理阶段:
  Step 4: property-management-dispute
          → 物业服务 / 业主大会 / 维修基金

资产证券化阶段:
  Step 5: reit-structure-advisor
          → REITs / 破产隔离 / 上市
```

**主动续期:** 任何 skill 输出后,自动追加"下一节点 + 期限 + 主办律师责任"。

### § B2 路由表(按业务类型 + 按项目阶段)

**按业务类型:**

| 业务类型 | 主 skill | 关键点 |
|---------|----------|--------|
| 土地取得 | land-acquisition-checker | 出让合同 / 招拍挂 |
| 建设工程 | construction-contract-reviewer | 工程价款 / 优先受偿 |
| 工程质量 | construction-defect-advisor | 缺陷鉴定 / 保修期 |
| 工程量争议 | engineering-quantity-dispute | 鉴定 / 计价方式 |
| 商品房预售 | pre-sale-compliance-advisor | 预售许可 / 资金监管 |
| 商业租赁 | commercial-lease-reviewer | 租金 / 押金 / 装修 |
| 长租公寓 | long-term-lease-advisor | 租金贷 / 监管 |
| 物业管理 | property-management-dispute | 服务合同 / 维修基金 |
| REITs | reit-structure-advisor | 底层资产 / 破产隔离 |

**按项目阶段:** 土地 → 建设 → 销售 → 运营 → 证券化(详见 § B1)

### § B3 三色风险体系(本场景核心)

| 等级 | 案件类型 | 处理 |
|------|----------|------|
| 🔴 HIGH-1 | 无证开发 / 重大质量事故 | **主办律师双签 + 监管沟通** |
| 🔴 HIGH-2 | 群体性业主维权 | 主办 + 协办律师 + 维稳 |
| 🔴 HIGH-3 | REITs + 跨境 | 主办 + 涉外律师 + 多法域协调 |
| ⚠️ MEDIUM | 工程价款拖欠 / 物业管理纠纷 | 主办 + 争议解决 |
| ✅ LOW | 标准合同 / 简单纠纷 | 主办律师即可 |

### § B4 风险等级 + 审批路径(P5/P6)

**Materiality 3 档(房地产特化):**

| 档位 | 涉案金额 | 须主办律师 | 须所务会 |
|------|----------|-----------|----------|
| 大型 | ≥¥1亿 | 强制 | 强制 |
| 中型 | ¥1000万-¥1亿 | 强制 | 建议 |
| 小型 | <¥1000万 | 主办即可 | 可选 |

### § B5 升级路径 + 跨境并行(P16/P17)

**强制升级触发(7 类):**
1. **无证开发 / 违规预售** → 主办 + 律所 + 监管沟通
2. **重大质量事故** → 主办 + 律所 + 危机公关
3. **群体性业主维权** → 主办 + 协办 + 维稳
4. **跨境 REITs** → 主办 + 涉外律师 + 律所审批
5. **建设工程价款优先受偿权** → 主办 + 律所审批
6. **土地权属重大争议** → 主办 + 律所审批
7. **刑事风险** → 主办 + 刑事律师

### § B6 输出格式(含 Reviewer Note + Risk Calibration)

**Reviewer Note 5 行(房地产特化):**
1. 项目基本信息:[业务类型 / 项目所在地 / 涉案金额 / 跨境情形]
2. 主要风险:[合规风险 / 工程风险 / 资金风险 / 群体性风险]
3. 主要诉求:[合同审查 / 纠纷解决 / 合规咨询 / 项目融资 / 资产处置]
4. 关键期限:[竣工验收 / 交付 / 质保期 / 预售许可到期 / REITs 申报]
5. 涉外因素:[境外资金 / 外籍业主 / 涉外担保]

**Risk Calibration 3 段表:**

**段 1 风险识别(5 类):**
- 合规风险(无证 / 违规)
- 工程风险(质量 / 价款 / 工期)
- 资金风险(预售资金 / 监管账户)
- 群体性风险(业主维权 / 农民工讨薪)
- 跨境风险(境外资金 / REITs)

**段 2 量化:** 概率 × 影响 + 缓释难度,综合评分 ≤5 低 / 6-15 中 / ≥16 高

**段 3 响应:** 接受 / 缓释(整改) / 转移(保险/担保) / 规避(退出)

**Decision Tree 5 选项:**
1. ✅ 继续推进 — 合规 / 标准项目
2. ⚠️ 整改 / 补救 — 部分合规 / 需补救
3. 🔴 停止 / 重大违规 — 无证开发 / 重大质量事故
4. 🔄 变更方案 — 调整交易结构 / 退出项目
5. 📤 升级主办律师 — 群体性 / 重大金额 / 涉外

### § B7 决策树(详见 § A5 + § B6)

### § B8 主动问 5 类

**24 字段分 5 类:** 项目(6:类型/阶段/所在地/规模/金额/期限)+ 主体(4:开发商/施工方/业主/管理方)+ 工程(6:造价/质量/工期/价款/保修/安全)+ 涉外(4:跨境/外籍/担保/REITs)+ 程序(4:阶段/期限/争议/群体性)。

**主动问 5 类:** 项目 / 主体 / 工程 / 涉外 / 程序

### § B9 用户配置(24 字段 YAML schema)

```yaml
# 第 1 组:项目(6 字段)
business_type: [填空:房地产开发/建筑施工/物业管理/REITs/...]
project_phase: [填空:土地取得/开发建设/销售租赁/运营/证券化]
project_location: [填空:具体省市]
project_scale: [填空:大型/中型/小型]
amount: [填空:金额人民币]
duration_months: [填空:项目周期月]

# 第 2 组:主体(4 字段)
developer: [填空:开发商名称]
contractor: [填空:施工方名称]
owner_buyer: [填空:业主/购房人]
manager: [填空:物业管理方]

# 第 3 组:工程(6 字段)
contract_value: [填空:工程价款]
quality_status: [填空:合格/缺陷/争议]
schedule_status: [填空:按期/延误/争议]
payment_status: [填空:已付/拖欠/争议]
warranty_period: [填空:保修期]
safety_incident: [填空:有/无]

# 第 4 组:涉外(4 字段)
is_cross_border: [填空:是/否]
foreign_funding: [填空:是/否]
foreign_buyer: [填空:是/否]
reit_overseas: [填空:是/否]

# 第 5 组:程序 + 律师(4 字段)
deadline: [填空:YYYY-MM-DD]
group_dispute: [填空:是/否]
attorney_contact: [填空:主办律师]
partner_approval: [填空:是/否]
```

**精简模式(12 字段):** business_type / project_phase / project_location / developer / contractor / quality_status / payment_status / is_cross_border / deadline / group_dispute / attorney_contact / partner_approval

**用户配置为空时:** 主动问 5 类,不直接进入 skill 执行。

### § B10 数据源标注

```
1. 民法典              → [民法典]
2. 建筑法              → [建筑法]
3. 城市房地产管理法    → [房地产管理法]
4. 土地管理法          → [土地管理法]
5. 建设工程司法解释    → [高法解释]
6. 商品房买卖司法解释  → [高法解释]
7. 住建部规章          → [住建部]
8. 自然资源部规章      → [自然资源部]
9. REITs 试点          → [发改委]
10. 地方限购/限贷/预售 → [地方规定]
11. 学者观点           → [model] + [verify]
```

### § B11 YAML 注册表复用

复用 `plugins/shared/registry/`:
- 房地产开发企业注册表
- 建筑施工总承包资质注册表
- 物业管理企业注册表
- REITs 计划管理人注册表

### § B12 Per-matter Side(P7)

房地产**严格隔离:**

| Side A | Side B | 禁止原因 |
|--------|--------|---------|
| 开发商 | 业主(同一项目) | 利益冲突 |
| 总包 | 分包(同一项目) | 利益冲突 |
| 物业公司 | 业主大会 | 利益冲突 |

### § B13 Enforcement posture(P15)

| 事项 | 力度 |
|------|------|
| 无证开发 | 强 |
| 工程价款 | 强(优先受偿权) |
| 预售资金监管 | 强 |
| 物业管理合规 | 中 |
| REITs 信息披露 | 强 |

### § B14 Risk calibration 3 段表

**段 1 识别:** 合规风险 / 工程风险 / 资金风险 / 群体性风险 / 跨境风险
**段 2 量化:** 概率 × 影响 + 缓释难度(综合评分 ≤5 低 / 6-15 中 / ≥16 高)
**段 3 响应:** 接受 / 缓释(整改) / 转移(保险/担保) / 规避(退出)

### § B15 7 条设计哲学(房地产特化)

1. **建设工程价款优先 > 普通债权** — 保护施工人
2. **预售资金监管 > 开发商自由使用** — 防止烂尾
3. **工程质量终身负责 > 短期验收** — 长期责任
4. **业主大会决议 > 物业单方决定** — 业主自治
5. **REITs 底层资产真实 > 形式转移** — 破产隔离
6. **维稳 > 单纯法律解决** — 群体性敏感
7. **地方政策优先 > 中央统一** — 因城施策

### § B16 推理原子能力调用流程

按 7 步调用 `legal-atomic`,特别关注 § 4 evidence-argument-chain(工程质量证据 + 工程价款证据)。

---

## § B17 v3 Self-Test 4 案件(2026-06-22)

### 案件 1:建设工程价款拖欠 + 优先受偿权(应急)

**用户输入:** "我们是施工总包,开发商拖欠工程款 8000 万,项目已竣工验收。我们能否行使优先受偿权?"

**agent 响应:** 路由到 `construction-contract-reviewer` → 主动问 5 类 → 必升:涉案金额 <¥1亿,主办律师 → 输出优先受偿权行使方案(《民法典》第 807 条)+ 6 个月期限 + 工程价款计算

**评估:4.5/5** ✅ 路由准确 / 优先受偿权识别 / 期限提示到位

### 案件 2:某小区 200 户业主维权(批量)

**用户输入:** "某小区 200 户业主因开发商延期交付集体维权,怎么处理?"

**agent 响应:** 路由到 `pre-sale-compliance-advisor` + 群体性应对 → 主动问 → **强制升级**(群体性 + 维稳)→ 主办 + 协办律师 + 维稳 + 业主沟通 + 退房 / 违约方案

**评估:4.0/5** ✅ 群体性识别 / ⚠️ 缺群体性沟通模板

### 案件 3:跨境 REITs 上市(跨境)

**用户输入:** "中国境内产业园拟通过 REITs 在香港上市"

**agent 响应:** 路由到 `reit-structure-advisor` + 涉外律师 → 主动问涉外 5 类 → **强制升级**(跨境 + REITs) → 主办 + 涉外 + 律所审批 → 输出 REITs 方案 + 香港 SFC 申报 + 中国发改委备案 + 底层资产核查

**评估:4.5/5** ✅ 跨境识别 / 强制升级准确 / 多法域路径清晰

### 案件 4:cold-start 首次跑

**用户输入:** "我是某房地产公司法务,第一次用这个场景,怎么开始?"

**agent 响应:** 路由到 onboarding 12 字段(精简模式)→ 主动问 5 类 → 输出 onboarding 精简模式 + 24 字段可选 + cold-start checklist

**评估:4.0/5** ✅ cold-start 识别 / 12 字段触发 / 渐进式问询

**平均分:4.25/5** ✅ 达 v3 标准(≥ 4.0/5)

---

*Greater China Legal — Real Estate Construction scene*
*curator v2.0 双层结构 · Part A 16 universal + Part B 18 pattern adaptive*
*行数 < 500 · 最后更新:2026-06-22(从 v1.0 升级到 v2.0 一体化重写)*