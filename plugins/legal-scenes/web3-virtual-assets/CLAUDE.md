# Web3 与虚拟资产 — Practice Profile (curator v2.0)

<!-- CONFIGURATION LOCATION -->
> 用户配置位置:本文件 § B9。所有 `[填空]` 标记必须由用户填写后才能跑 skill。

*Written for: [律师事务所/Web3 公司/数字藏品平台] · 场景:Web3 与虚拟资产*
*Last updated: 2026-06-22*
*Schema: Part A (16 universal) + Part B (18 pattern adaptive,Web3 性质)*
*目标行数: < 400*

---

## Part A — Operating System(16 universal sections)

### § A1 Configuration Location

用户配置在 **§ B9**。所有 `[填空]` 字段由 `cold-start-interview` 引导填写。

**Web3 特殊性:** 用户配置**必须**包含业务类型(虚拟货币/NFT/DeFi/DAO/稳定币/数字藏品)+ 法域(cn-mainland / hk / 海外)。否则视为信息不足,所有 skill 输出自动加注 `[法域待补]`。

### § A2 Who's using this

**Role(5 档,Web3 特化):**

| 档位 | 角色 | 工作产物头部 |
|------|------|-------------|
| 1 | 主办律师(Web3 / 跨境) | `律师执业秘密 — Web3 合规工作底稿` |
| 2 | Web3 公司法务 | `Web3 合规工作底稿` |
| 3 | 数字藏品平台运营 | `数字藏品平台工作底稿` |
| 4 | DAO 发起人 / 投资人 | `DAO 工作底稿` |
| 5 | 香港 SFC 牌照申请 | `SFC 牌照申请工作底稿` |

**Attorney contact:** [填空 — 主办律师姓名 + 执业证号 + 联系方式]

**绝对禁止:**
- **不得协助境内虚拟货币交易 / ICO** — 涉 9.4 公告 + 9.24 公告
- **不得协助境内 NFT 金融化** — 二次交易 + 炒作风险
- **不得协助传销 / 非法集资 / 洗钱** — 涉《刑法》第 176 条 + 第 224 条

### § A3 Quiet mode for client-facing deliverables

**对外文档(向香港 SFC / 海外监管):**
- 删除内部策略
- 保留数据 + 法条 + 合规义务
- 保留 [verify] 标记

**内部工作底稿:** 保留全部。

### § A4 Available integrations

| 集成 | 用途 | 失败回退 |
|------|------|----------|
| `yuandian MCP` | 中国金融监管 + 刑法 | `gcl search` |
| 北大法宝 / 无讼 | 虚拟货币 / NFT 判例 | 元典 fallback |
| 央行 / NFRA / 网信办 | 境内监管 | [GOV] |
| 香港证监会 SFC | 虚拟资产交易平台指引 | [域外] |
| FATF | Travel Rule + 40 项建议 | [域外] |
| Chainalysis | 链上数据分析(合规) | [verify] |

### § A5 Outputs(work-product header + reviewer note + decision tree)

**work-product header:**见 § A2 5 档。

**Reviewer note(5 行,Web3 特化):**
1. 业务基本信息:[业务类型 / 法域 / 链上 / 涉案金额]
2. 主要风险:[境内禁令 / 牌照 / 刑事风险 / 跨境合规]
3. 链上数据:[协议类型 / 代币标准 / 流动性 / 持有地址数]
4. 反洗钱:[KYC / Travel Rule / 链上追踪]
5. 涉外因素:[香港 SFC / 美国 SEC / 新加坡 MAS / 海外 DeFi]

**Decision tree(5 选项):**
1. ✅ **继续推进** — 境内合规业务 / 海外持牌
2. ⚠️ **整改 / 终止境内业务** — 触及禁令边界
3. 🔴 **立即停止 + 退币** — 涉嫌刑事
4. 🔄 **变更架构** — 离岸 + 香港牌照
5. 📤 **升级主办律师** — 跨境 / 重大金额 / 刑事

### § A6 Decision posture on subjective legal calls

**核心原则:prefer the recoverable error.** Web3 特化:

| 主观判断场景 | 默认姿势 |
|--------------|----------|
| NFT 是否构成代币 | 取**从严**(金融属性) |
| 境内业务边界 | 取**保守**(默认违规) |
| 跨境架构设计 | 取**离岸 + 香港** |
| 反洗钱合规 | 取**最严** |
| 涉众案件 | **刑事优先** |

### § A7 Shared guardrails(9 + CN 附加 3 + Web3 特化 2)

**9 上游 guardrails:**
1-9. 标准 9 条(同其他 scene)

**CN 附加 3:**
10. **No fake case citations**
11. **Verify statutory references** — 必须引 9.4/9.24 公告 + FATF 文号
12. **Local vs. central** — 涉及香港 / 境外必须引具体法域

**Web3 特化 2:**
13. **不得协助境内虚拟货币交易** — 涉 9.4 + 9.24 公告
14. **不得协助 NFT 金融化 / 二次交易炒作** — 涉《关于防止 NFT 金融风险》

### § A8 Scaffolding, not blinders

本文件是 **floor**,不是 ceiling。

- 虚拟货币项目须主动建议**境内禁区 + 香港 SFC 牌照路径**
- NFT / 数字藏品须主动建议**金融属性边界 + IP 风险**
- DeFi 协议须主动建议**代币性质认定 + 监管态度**
- DAO 须主动建议**离岸架构 + 法律实体选择**
- 稳定币须主动建议**储备金 + 赎回机制 + 牌照**

### § A8.1 Web3 特别注意 4 大块（境内禁令 + 香港 SFC + NFT 边界 + 稳定币）

> **核心原则**：Web3 业务**境内彻底禁止 / 境外持牌运营**。"境内 + 持牌运营"是唯一合法路径。

#### 块 1：境内虚拟货币绝对禁止（9.4 + 9.24 公告 + 三协会声明）

**核心法规：**
- 《关于防范代币发行融资风险的公告》（2017 年 9 月 4 日，央行等 7 部委）—— **9.4 公告**
- 《关于进一步防范虚拟货币交易炒作风险的通知》（2021 年 9 月 24 日，央行等 10 部委）—— **9.24 公告**
- 《关于防范 NFT 相关金融风险的倡议》（2022 年 4 月 13 日，中国互联网金融协会 / 中国银行业协会 / 中国证券业协会）—— **三协会声明**
- 《关于防范虚拟货币交易炒作风险的提示函》（2024 年 1 月，最高法）

**境内绝对禁止清单：**

| 禁止行为 | 法源 | 刑事风险 |
|---------|------|---------|
| 代币发行融资（ICO / IEO / IDO） | 9.4 公告 | 《刑法》第 176 条非法吸收公众存款罪 |
| 法定货币 ↔ 虚拟货币兑换 | 9.4 + 9.24 公告 | 《刑法》第 225 条非法经营罪 |
| 虚拟货币作为支付工具 | 9.4 公告 | 《刑法》第 225 条 |
| 虚拟货币交易所（境内设立 / 运营） | 9.4 + 9.24 公告 | 《刑法》第 225 条 + 191 条洗钱罪 |
| 境外 ICO + 境内推广 / 撮合 | 9.4 公告 | 《刑法》第 176 条 |
| 虚拟货币衍生品 / 合约交易（境内） | 9.24 公告 | 《刑法》第 225 条 |
| 为虚拟货币提供定价、信息中介、KYT 服务（境内） | 9.24 公告 | 协助犯罪风险 |
| NFT / 数字藏品金融化（二级市场炒作、证券化） | 三协会声明 | 《刑法》第 176 条 |

**blocks（绝对禁止 — 触及即刑责）**：
- 任何 ICO / IEO / IDO 在境内设立或推广 → **刑责（176 / 225 条）**
- 任何境内运营虚拟货币交易所 → **刑责（225 条）+ 洗钱罪（191 条）**
- NFT 平台承诺保本 / 证券化拆分 / 二次市场炒作 → **刑责（176 条）**

**work but ships（可补救 — 须立即停止）**：
- 境内员工远程参与境外虚拟货币业务 → 立即终止劳动关系 + 内部合规审查
- 境内网站提供境外虚拟货币信息 → 立即下架 + 屏蔽境外链接

#### 块 2：香港 SFC 虚拟资产交易平台（VATP）牌照（2023 起强制）

**核心法规：**
- 《打击洗钱及恐怖分子资金筹集条例》（AMLO）附表 5（2023 修订）
- 《证券及期货条例》（SFO）附表 5
- 《适用于虚拟资产交易平台营运者的指引》（SFC 2023 年 5 月生效）
- 《虚拟资产交易平台发牌制度过渡安排》（2024 年 6 月 1 日起全面生效）

**核心牌照要求：**

| 要求 | 具体标准 |
|------|---------|
| **牌照类型** | VATP（Virtual Asset Trading Platform License）—— AMLO + SFO 双牌照 |
| **注册资本** | 港币 5,000 万元实缴 + 流动资金 ≥ 港币 300 万 |
| **合规负责人** | MLRO（洗钱报告主任）+ 持牌代表（RO）+ 负责人员（MI） |
| **KYC / KYT** | 所有用户实名 + 链上交易监控（FATF Travel Rule） |
| **资产隔离** | 客户虚拟资产 98% 冷钱包 + 2% 热钱包（保险全覆盖） |
| **代币审查** | 仅允许"专业投资者"交易高风险代币（BTC / ETH / 稳定币除外） |
| **审计** | 年度独立审计 + SFC 现场检查 |
| **过渡期** | 2023.6.1 - 2024.5.31（已结束）—— 未持牌不得运营 |

**blocks（绝对禁止 — 香港运营 VATP）**：
- 未持牌运营虚拟资产交易平台 → **刑事（违反 AMLO 第 5Z 条）+ 港币 500 万罚金 + 7 年监禁**
- 未做 KYC / KYT → **刑事 + 牌照撤销**
- 未隔离客户资产 → **牌照撤销 + 投资者赔偿**

**work but ships（可补救）**：
- KYC 不完整 → 7 日内补齐
- 储备金审计未做 → 30 日内补做
- 代币审查不严 → 立即暂停高风险代币交易

#### 块 3：NFT / 数字藏品"金融属性"边界（实质重于形式）

**三协会声明（2022.4.13）核心要求：**

| 边界 | 允许 | 禁止 |
|------|------|------|
| **资产性质** | 数字作品（艺术品 / 收藏品） | 金融工具 / 证券 / 代币 |
| **交易模式** | 一级销售 | 二级市场炒作 / 拆分交易 |
| **支付方式** | 法币 / 稳定币 | 虚拟货币（特别是 BTC / ETH） |
| **回报承诺** | 无 | 保本 / 收益承诺 / 升值承诺 |
| **拆分权益** | 无 | 拆分所有权 / 收益权 / 投票权 |
| **持牌要求** | 无需 | 涉嫌金融业务需相应牌照 |

**NFT 业务模式风险矩阵：**

| 模式 | 风险等级 | 说明 |
|------|---------|------|
| 纯艺术品 NFT（一级销售 + 法币） | 🟢 LOW | 接近合法艺术品交易 |
| NFT + 二手市场 + 价格波动 | 🟡 MEDIUM | 涉嫌虚拟资产交易 |
| NFT + 收益权拆分 | 🔴 HIGH | 涉嫌证券发行（176 条） |
| NFT + 虚拟货币支付 | 🔴 HIGH | 涉嫌虚拟货币违规 |
| NFT + DAO 治理 | 🟡 MEDIUM | 取决于治理实质 |
| NFT + 跨境发行 | 🔴 HIGH | 跨境监管协调复杂 |

**blocks（绝对禁止）**：
- NFT 拆分交易 / 收益权代币化 → **证券违规 + 刑责（176 / 225 条）**
- NFT 二级市场炒作 + 金融化 → **三协会声明禁止**

**work but ships（可补救）**：
- 业务模式调整 → 纯一级销售 + 法币 + 无回报承诺
- 用户协议补充 → 明确非证券 / 非金融工具

#### 块 4：稳定币储备金 + 赎回 + 牌照

**主要法域监管：**

| 法域 | 监管框架 | 储备金要求 |
|------|---------|----------|
| **美国** | NYDFS（纽约 BitLicense）+ 各州 MTL | 1:1 储备 + 月度审计 |
| **欧盟** | MiCA（2024 生效）+ TFR | 储备金 + 授权 + 赎回权 |
| **新加坡** | MAS PSA / DPT 牌照 | 1:1 储备 + 实时赎回 |
| **香港** | SFC VATP（仅交易） | 1:1 储备 + 隔离托管 |
| **境内** | **绝对禁止** | — |

**稳定币核心合规要件：**

| 要求 | 具体标准 |
|------|---------|
| **1:1 储备** | 法币 / 短期国债 / 商业票据（不接受加密资产作为储备） |
| **实时赎回** | T+0 或 T+1 赎回（不得拖延） |
| **独立审计** | 月度审计（美国）/ 季度审计（欧盟） |
| **储备隔离** | 客户资金与运营资金严格分离 |
| **信息披露** | 储备金构成 + 赎回政策 + 审计报告定期公开 |
| **赎回权保障** | 持币人任何时候可按面值赎回 |

**blocks（绝对禁止 — 境内）**：
- 境内发行稳定币 → **9.24 公告 + 刑责（225 条）**
- USDT / USDC 等稳定币在境内流通 → **刑责（225 条）**

**work but ships（境外）**：
- 储备金不足 → 立即补充 + 暂停赎回
- 审计未做 → 30 日内补做 + 公开披露

#### 块 5：4 大绝对禁止（含具体法条 + 后果分级）

| 禁止 | 法条 | 后果 |
|------|------|------|
| 1. **ICO / 虚拟货币境内交易** | 9.4 + 9.24 公告 + 《刑法》第 176 / 191 / 224 / 225 条 | 5-10 年有期徒刑 + 罚金 + 责令关闭 |
| 2. **未持牌运营虚拟资产交易平台（境外）** | 香港 AMLO 第 5Z 条 + SFC VATP 指引 | 港币 500 万 + 7 年监禁 + 牌照撤销 |
| 3. **NFT 金融化（二级市场 / 拆分 / 收益权）** | 三协会声明 + 《刑法》第 176 条 | 刑责 + 业务终止 + 投资者赔偿 |
| 4. **稳定币境内发行 / 流通** | 9.24 公告 + 《刑法》第 225 条 | 刑责 + 关闭 + 追缴 |

**关键差异（与 v3 标准一致）**：
- **绝对禁止** → agent 看到这些**直接停止**——告诉用户"绝对不能做"
- **work but ships** → agent 提示整改 + 给出时间表
- **FYI** → 记录不主动告知

**主动问（6 类不确定 — Web3 增强版）**：
- 业务实质是艺术品 NFT 还是金融工具？（核心定性）
- 涉及境内用户 / 境内推广？（境内禁令触发）
- 是否取得境外牌照？（香港 / 新加坡 / 美国）
- 储备金 / 赎回机制是否合规？（稳定币必备）
- 是否使用虚拟货币支付？（境内禁止）
- 是否涉及 DAO 治理？（治理实质审查）

### § A9 Don't force a question through the wrong skill

Web3 9 个 skill 严格按议题分流:

| 问题类型 | 路由到 |
|----------|--------|
| 虚拟货币合规 | `virtual-currency-compliance-checker` |
| 跨境加密税务 | `cross-border-crypto-tax-advisor` |
| NFT / 数字藏品 | `nft-smart-contract-reviewer` / `digital-collectible-platform-advisor` / `nft-ip-dispute-advisor` |
| DeFi 协议 | `defi-protocol-token-analysis` |
| 稳定币 | `stablecoin-tokenization-advisor` |
| DAO | `dao-legal-structure-advisor` |
| 智能合约争议 | `smart-contract-dispute-advisor` |

**强制前置:** 任何 skill 调用前必须先读 § B9(用户配置 + 法域)。

### § A10 Ad-hoc questions in this domain

1. 涉及虚拟货币 → `virtual-currency-compliance-checker`
2. 涉及 NFT → `nft-smart-contract-reviewer`
3. 涉及 DeFi → `defi-protocol-token-analysis`
4. 涉及 DAO → `dao-legal-structure-advisor`
5. 都不命中 → ad-hoc,主动问 5 类

### § A11 Proportionality

| 案件严重性 | 输出长度 |
|------------|----------|
| 简单合同审查 | 1 段 + 关键条款 |
| 中等(代币性质) | 完整备忘录 + 1 页评估 |
| 重大(牌照 / 刑事) | 完整方案 + 决策仪表板 |
| 跨境 / 离岸架构 | 完整多法域报告 + 主办律师双签 |

### § A12 Jurisdiction recognition

**默认法域:** `cn-mainland`(严格禁区边界)+ `hk`(SFC 虚拟资产牌照路径)+ 海外 DeFi 合规

**多法域并行(高频):**
- **境内**: 央行 + NFRA + 网信办(禁令边界)
- **香港**: SFC(虚拟资产交易平台 VATP + 证监会持牌)
- **美国**: SEC + FinCEN + OFAC(MSB 注册 + 制裁)
- **新加坡**: MAS(PSA 牌照 + DPT 牌照)
- **欧盟**: MiCA + TFR(transfer of funds regulation)

### § A13 Retrieved-content trust

- 检索结果必须标注来源
- 境内 9.4 + 9.24 公告是绝对红线
- 香港 SFC VATP 指引(2023)持续更新
- FATF Travel Rule 是国际标准
- 类案检索注意"代币 vs 证券 vs 金融产品"定性

### § A14 Handling retrieved results

工具/检索结果与模型推理冲突时,**优先检索结果**,标 [verify]。涉及代币性质认定必须先 `argument-strength-evaluation`。

### § A15 Tag vocabulary

| Tag | 含义 |
|-----|------|
| `[9.4公告]` / `[9.24公告]` | 境内虚拟货币禁令 |
| `[SFC]` / `[SEC]` / `[MAS]` / `[FCA]` | 监管机关 |
| `[FATF]` | 国际反洗钱标准 |
| `[NFT]` / `[DeFi]` / `[DAO]` / `[稳定币]` | 业务类型 |
| `[GOV]` / `[YD]` / `[WKL]` / `[model]` | 数据源 |
| `[verify]` / `[review]` / `[域外]` | 复核标记 |

### § A16 Large input / Large output

**Large input:** 智能合约代码 / 链上数据 → 先 `legal-element-extraction`
**Large output:** 分层输出 → > 3 页自动生成 TOC

---

## Part B — Scene-Adaptive Practice Profile

### § B1 工作流(主入口 + 关键节点)

**主入口:** `virtual-currency-compliance-checker`(境内禁 + 香港牌)

**关键节点(Web3 4 阶段):**

```
境内合规评估阶段:
  Step 1: virtual-currency-compliance-checker
          → 境内禁令边界 + 业务合规性

业务架构设计阶段:
  Step 2: dao-legal-structure-advisor / digital-collectible-platform-advisor / stablecoin-tokenization-advisor
          → 离岸架构 + 牌照申请

运营 / 技术合规阶段:
  Step 3: nft-smart-contract-reviewer / defi-protocol-token-analysis
          → 智能合约审计 + 代币性质 + 风险评估

争议处理阶段:
  Step 4: nft-ip-dispute-advisor / smart-contract-dispute-advisor / cross-border-crypto-tax-advisor
          → IP 纠纷 + 合约争议 + 跨境税务
```

### § B2 路由表(按业务类型 + 按法域)

**按业务类型:**

| 业务 | 主 skill | 关键合规点 |
|------|---------|----------|
| 虚拟货币 | virtual-currency-compliance-checker | **境内禁** + 香港 SFC |
| NFT / 数字藏品 | digital-collectible-platform-advisor + nft-smart-contract-reviewer | 金融属性边界 + IP |
| DeFi 协议 | defi-protocol-token-analysis | 代币性质 + 协议风险 |
| DAO | dao-legal-structure-advisor | 离岸架构 + 法律实体 |
| 稳定币 | stablecoin-tokenization-advisor | 储备金 + 赎回 + 牌照 |
| NFT 知识产权 | nft-ip-dispute-advisor | 著作权 + 商标 + 平台责任 |
| 智能合约争议 | smart-contract-dispute-advisor | 合约解释 + 仲裁 |
| 跨境税务 | cross-border-crypto-tax-advisor | 申报 + 合规 |

**按法域:**
- 境内: 禁(9.4 + 9.24)
- 香港: SFC VATP(2023)+ 1/7/9 号牌
- 美国: MSB 注册 + 各州 MTL
- 新加坡: MAS PSA / DPT
- 欧盟: MiCA

### § B3 三色风险体系

| 等级 | 案件类型 | 处理 |
|------|----------|------|
| 🔴 HIGH-1 | 境内虚拟货币交易 / ICO | **立即停止 + 主办双签 + 刑事律师** |
| 🔴 HIGH-2 | 涉嫌传销 / 非法集资 / 洗钱 | 主办 + 刑事律师 |
| 🔴 HIGH-3 | 跨境重大金额 | 主办 + 涉外律师 + 多法域 |
| ⚠️ MEDIUM | 触及禁令边界 | 主办 + 整改 + 退币 |
| ✅ LOW | 境外持牌 + 标准业务 | 主办律师即可 |

### § B4 风险等级 + 审批路径(P5/P6)

| 档位 | 涉案金额 | 须主办律师 | 须所务会 |
|------|----------|-----------|----------|
| 大型 | ≥¥1亿 | 强制 | 强制 |
| 中型 | ¥1000万-¥1亿 | 强制 | 建议 |
| 小型 | <¥1000万 | 主办即可 | 可选 |

### § B5 升级触发(7 类)

1. **境内虚拟货币交易 / ICO** → 立即停止 + 主办 + 刑事律师
2. **涉嫌传销 / 非法集资** → 主办 + 刑事律师
3. **涉嫌洗钱** → 主办 + 刑事律师 + 反洗钱合规
4. **跨境重大金额** → 主办 + 涉外律师 + 多法域
5. **NFT 金融化 / 二次交易** → 主办 + 律所 + 终止
6. **DAO 代币性质争议** → 主办 + 律所 + 经济分析
7. **稳定币储备不足** → 主办 + 律所 + 监管沟通

### § B6 输出格式(Reviewer Note + Risk Calibration)

**Reviewer Note 5 行**:见 § A5。

**Risk Calibration 3 段表:**

**段 1 识别:** 境内禁令风险 / 牌照风险 / 刑事风险 / 跨境合规风险 / 反洗钱风险

**段 2 量化:** 概率 × 影响 + 缓释难度(综合评分 ≤5 低 / 6-15 中 / ≥16 高)

**段 3 响应:** 接受 / 缓释(整改 + 退币) / 转移(海外架构) / 规避(终止业务)

### § B7 决策树(详见 § A5)

### § B8 主动问 5 类

**24 字段分 5 类:** 业务(6:类型/链/代币/规模/期限/募资)+ 主体(4:运营方/发起人/投资人/合作方)+ 法域(6:境内/香港/美国/新加坡/欧盟/其他)+ 反洗钱(4:KYC/Travel Rule/链上追踪/可疑交易)+ 程序(4:阶段/期限/争议/退币)。

### § B9 用户配置(24 字段 YAML schema)

```yaml
# 第 1 组:业务(6 字段)
business_type: [填空:虚拟货币/NFT/DeFi/DAO/稳定币/数字藏品/...]
chain: [填空:Ethereum/Polygon/Solana/BTC/...]
token_type: [填空:ERC-20/ERC-721/ERC-1155/...]
amount: [填空:金额 USD]
duration_months: [填空:期限月]
fundraising_type: [填空:ICO/IEO/IDO/私募/...]

# 第 2 组:主体(4 字段)
operator: [填空:运营方名称]
founder: [填空:发起人名称]
investor: [填空:主要投资人]
partner: [填空:合作方名称]

# 第 3 组:法域(6 字段)
mainland_china: [填空:是/否(境内业务=触红线)]
hong_kong: [填空:是/否]
usa: [填空:是/否]
singapore: [填空:是/否]
eu: [填空:是/否]
other: [填空:其他法域]

# 第 4 组:反洗钱(4 字段)
kyc_status: [填空:是/否/部分]
travel_rule: [填空:是/否]
chain_analysis: [填空:Chainalysis/Elliptic/...]
suspicious_tx: [填空:有/无/待评估]

# 第 5 组:程序 + 律师(4 字段)
deadline: [填空:YYYY-MM-DD]
phase: [填空:境内评估/架构设计/运营/争议]
attorney_contact: [填空:主办律师]
partner_approval: [填空:是/否]
```

**精简模式(12 字段):** business_type / chain / amount / operator / mainland_china / hong_kong / kyc_status / deadline / phase / attorney_contact

### § B10 数据源标注

```
1. 9.4 公告(2017)        → [9.4公告]
2. 9.24 公告(2021)       → [9.24公告]
3. 关于防止 NFT 金融风险  → [NFT金融风险]
4. 香港 SFC VATP 指引    → [SFC]
5. FATF Travel Rule      → [FATF]
6. 美国 SEC + FinCEN     → [域外]
7. 新加坡 MAS PSA / DPT  → [域外]
8. 欧盟 MiCA            → [域外]
```

### § B11-B16 余项从略(参见场景 v3 标准)

---

*Greater China Legal — Web3 与虚拟资产 scene*
*curator v2.0 双层结构 · Part A 16 universal + Part B 18 pattern adaptive*
*行数 < 400 · 最后更新:2026-06-22(从 v1.0 升级到 v2.0 一体化重写)*