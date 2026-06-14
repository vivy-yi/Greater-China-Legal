---
name: customs-compliance-assessor
description: >
  海关合规评估 — 评估进口报关合规性，识别商品归类/估价风险。
  适用情形：用户描述与本skill相关的业务需求。
argument-hint: "[进口产品/报关口岸/申报商品编码/企业类型]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
  - 跨境
  - 进出口
  - 海关
  - customs compliance
---

# Customs Compliance Assessor

## 一、核心定义与适用范围

### 1.1 核心定义
**海关保证金（CBP Customs Bond）** 是进口商向美国海关与边境保护局（CBP）提交的财务担保，确保进口商履行关税支付和其他海关义务。连续保证金（Continuous Bond）适用于一年内多次进口的进口商。

**保税仓库（Bonded Warehouse）** 是经CBP批准用于存储未清关进口货物的设施，货物在仓库内期间免缴关税。

**自由贸易协定原产地证明（FTA Certificate of Origin）** 是用于申请FTA优惠税率的证明文件，需符合特定原产地规则（Rules of Origin）。

**C-TPAT（海关-商贸反恐怖联盟）** 是美国国土安全部下属项目，通过与进口商合作增强供应链安全，符合条件的企业可享受通关便利。

### 1.2 适用范围
- 美国进口商的海关保证金规划
- 保税仓库存储策略
- USMCA、US-Korea FTA、USMCA等FTA优惠利用
- C-TPAT申请与维护
- FDA、USDA等机构进口要求的海关协调
- 海关审计准备与合规自检

### 1.3 核心法规依据
| 法规 | 管辖 | 主管机构 |
|------|------|----------|
| 19 CFR | 美国海关进出口程序 | CBP |
| 19 USC 1514 | 海关裁定与复议 | CBP / CIT |
| Trade Facilitation Agreement | WTO贸易便利化 | CBP |

---

## 二、分析框架与操作流程

### 2.1 海关保证金决策流程

```
STEP 1: 确定是否需要保证金
    │
    ├─ 商业进口（Commercial Import）→ 必须
    ├─ 个人进口（非商业）→ 特定豁免
    └─ 过境转运（Transit）→ 视情况

STEP 2: 确定保证金类型
    │
    ├─ 单次进口保证金（Single Entry Bond）
    │   └─ 金额≥估计关税+其他费用的10%
    └─ 连续保证金（Continuous Bond）
        └─ 年度保费约$500-$1,000（担保额约$50,000-$100,000起）

STEP 3: 选择保证金保险公司
    │
    ├─ 主要提供商：Berkley Insurance, Great American Insurance, CBIC
    ├─ 评估费率（Premium Rate）
    └─ 评估最低担保额要求

STEP 4: 维护保证金合规
    ├─ 保持充足担保额（Bond Sufficiency）
    ├─ CBP调整时及时补充
    └─ 年度续期
```

### 2.2 FTA原产地规则分析流程

**USMCA原产地判定步骤：**

```
STEP 1: 确定商品税号（HTS 8位）
    │
    └─ 查阅USMCA Appendix（特定产品规则）

STEP 2: 确定原产地类型
    │
    ├─ 完全获得（Wholly Obtained）→ 农林渔产品等
    ├─ 区域价值成分（RVC）→ 制造加工品
    │   ├─ 交易价格法：RVC = (VO / NTV) × 100%
    │   │   └─ 达标线：≥60%（净价法）或 ≥50%（交易价法）
    │   └─ 成本法：RVC = (VO - VNM) / NV
    │       └─ 达标线： ≥50%
    └─ 特定工艺要求（Product-Specific Rules）

STEP 3: 原产地证明文件
    │
    ├─ 出口商/生产商自行签发Certificate of Origin
    ├─ 包含：生产者声明 + 支持文件
    └─ 保留至少5年（进口国要求）

STEP 4: 进口申报
    └─ 在Entry Summary中使用USMCA preference
```

### 2.3 保税仓库操作流程

```
STEP 1: 申请保税仓库批准
    │
    ├─ 向CBP申请（表格CBP-300等）
    ├─ 仓库需符合安全标准
    └─ 缴纳保证金

STEP 2: 货物入库
    │
    ├─ 提交进口摘要（Entry）但不支付关税
    ├─ 货物进入Bonded Warehouse状态
    └─ 计算仓储时限

STEP 3: 仓储期管理
    │
    ├─ 普通保税仓库：5年
    ├─ 私用保税仓库（Private Bonded Warehouse）：5年
    └─ 海关工厂（Foreign Trade Zone）：无期限限制

STEP 4: 出库选项
    │
    ├─ 出口（Export）→ 免关税
    ├─ 国内消费（Domestic Entry）→ 支付关税
    └─ 转移至另一保税仓库 → 保持免税
```

### 2.4 C-TPAT认证流程

**Tier等级结构：**
- Tier 1: 进口商（Importers）
- Tier 2: 国内制造商（Domestic Manufacturers）
- Tier 3: 承运人、报关行等（Service Providers）

**C-TPAT Benefits：**
- 减少查验率（Reduced Exam Rate）
- 优先查验通道
- 参与CTPAT MX（墨西哥过境便利）
- 商业伙伴识别（Business Partner Engagement）

---

## 三、实务指引与案例库

### 3.1 FTA利用率提升策略

**常见FTA一览（美国签署）：**
| FTA | 生效日期 | 参与国 | 典型优惠 |
|-----|----------|--------|----------|
| USMCA | 2020 | 美国、加拿大、墨西哥 | 汽车0%关税、农产品 |
| US-Korea FTA (KORUS) | 2012 | 美国、韩国 | 汽车、纺织品优惠 |
| US-Australia FTA | 2005 | 美国、澳大利亚 | 农产品、工业品 |
| US-Peru TPA | 2009 | 美国、秘鲁 | 纺织品、农产品 |
| US-Colombia TPA | 2012 | 美国、哥伦比亚 | 纺织品、农产品 |
| US-Singapore FTA | 2004 | 美国、新加坡 | 全面开放 |

**优惠利用率低的常见原因：**
- 不知道商品符合FTA条件
- 不知道如何申请Certificate of Origin
- 原产地规则不达标
- 文件保存不当（未保留5年）
- 认证程序繁琐

### 3.2 保税仓库使用场景

| 场景 | 保税仓库优势 |
|------|--------------|
| 进口商品等待销售旺季 | 避免先缴关税，资金占用降低 |
| 商品需分类/改装但未确定销售市场 | 保持灵活性 |
| 进口商品进入Foreign Trade Zone进行增值加工 | 可再出口免关税 |
| 进口展览品 | 展览后退回无需缴关税 |

### 3.3 海关审计准备自检清单

**合规内审5年留存文件：**
- [ ] 进口Entry Summary（CBP 7501）
- [ ] 付款记录（海关发票）
- [ ] HTS分类依据
- [ ] 原产地证明文件（如适用FTA）
- [ ] 担保文件（Bonds）
- [ ] 查验记录
- [ ] Protest及复议文件

**常见违规发现：**
| 违规类型 | 后果 |
|----------|------|
| HTS分类错误 | 补缴关税+利息+潜藏罚款 |
| 遗漏Section 301税 | 补缴+利息 |
| FTA资格虚报 | 补缴+罚则（欺诈性） |
| 违禁品转入内销 | 查封+罚款+刑事 |

---

## 升级决策门

**以下情形必须升级至Licensed Customs Broker或国际贸易法律师：**

1. CBP发起海关审计（Audit）并发出Information Request
2. 涉及保税仓库内商品处理违规指控
3. FTA原产地资格争议（是否满足Rules of Origin）
4. 涉及C-TPAT资格被暂停或撤销
5. 连续保证金不足（Bond Insufficiency）被CBP追缴
6. 涉及知识产权边境执法（扣押侵权商品）
7. 涉及商品被CBP归类为"禁止进口"（Detention）
8. 涉及CBP罚款通知（Pre-Penalty Notice）的抗辩
9. 涉及Foreign Trade Zone（FTZ）操作违规
10. 涉及进口商资格被取消（Importer of Record disqualification）

---

## 本Skill不涵盖

1. **出口管制EAR/ITAR合规** → 请使用 `export-control-reviewer`
2. **HTS分类与税率确定** → 请使用 `import-tariff-adviser`
3. **OFAC及制裁名单筛查** → 请使用 `trade-sanctions-checker`
4. **Incoterms条款选择** → 请使用 `incoterms-guide`
5. **反倾销/反补贴税争议** → 请使用 `trade-dispute-advisor`
6. **FDA进口许可（Prior Notice, Import Alert）** → 需FDA专项咨询
7. **USDA动植物检疫进口要求** → 需USDA APHIS专项咨询
8. **刑事辩护（走私、欺诈）** → 必须转介刑事辩护律师
9. **CBP行政罚款和解谈判** → 建议通过专业报关行或律师
10. **美国以外其他国家海关制度** → 需单独查询
## 本 Skill 不涵盖

- 海关归类决定的具体申请
- 海关稽查应对陪同
- 海关行政处罚的申辩
- 知识产权海关保护的申请
