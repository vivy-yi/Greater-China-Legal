---
name: import-tariff-adviser
description: >
  进口关税筹划 — 分析进口关税税率、优惠原产地规则，提供关税筹划建议。
  适用情形：用户描述与本skill相关的业务需求。
argument-hint: "[产品HS编码/原产地/贸易方式/优惠税率类型]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
  - 跨境
  - 进出口
  - 海关
  - import tariff
---

# Import Tariff Adviser

## 一、核心定义与适用范围

### 1.1 核心定义
**协调关税表（HTS, Harmonized Tariff Schedule）** 是美国使用的10位编码系统，用于确定进口商品的税率和监管要求。HTS基于WCO的HS（协调制度）编码，但扩展至10位以满足美国贸易政策需求。

**Section 301关税** 是美国贸易法301条款授权对特定国家商品征收的额外关税，用于反击不公平贸易行为。2018年起对华商品加征的关税即为此类。

**MFN（最惠国）税率** 是美国对WTO成员国适用的标准关税税率。

### 1.2 适用范围
- 美国进口商品的HTS分类与税率查询
- Section 301附加税（List 1, 2, 3, 4A等）的适用判断
- FTA（自由贸易协定）优惠税率的资格判定
- 税率复议（Protest）和保障措施（Safeguard）查询
- 反倾销/反补贴税（AD/CVD）的查询入口

### 1.3 关键税率类型
| 税率类型 | 说明 | 适用条件 |
|----------|------|----------|
| MFN | 最惠国税率 | WTO成员或适用MFN的国别 |
| Section 301 | 对华额外关税 | 中国原产 + 列入List |
| NAFTA/USMCA | 协定税率 | 符合原产地规则 + 认证文件 |
| GSP | 普惠制 | 指定发展中国家+ GSP清单商品 |
| AD/CVD | 反倾销/反补贴税 | 经调查确认 + DOC裁定 |

---

## 二、分析框架与操作流程

### 2.1 HTS分类决策流程

```
STEP 1: 识别商品HS编码（前6位）
    │
    ├─ 查阅HTS General Notes确定大类
    ├─ 查阅相关Chapter Notes（类注、章注）
    └─ 初步确定HS 6位码

STEP 2: 深入分析确定8位税目
    │
    ├─ 查阅Subheading Explanatory Notes
    ├─ 查阅HTS统计尾注（Statistical Notes）
    └─ 确认8位USITC税目

STEP 3: 确定适用税率
    │
    ├─ General税率（MFN）→ 基础税率
    ├─ Special税率 → FTA/GSP等优惠条件
    └─ Section 301附加 → 对华商品特定税率

STEP 4: 核查Section 301适用性
    │
    ├─ 是否中国原产（country of origin）
    ├─ 是否在List覆盖范围内
    └─ 税率叠加计算（General + Section 301）

STEP 5: 原产地规则（如申请FTA优惠）
    ├─ 完全获得（Wholly Obtained）
    ├─ 实质性改变（Substantial Transformation）
    └─ 特定产品规则（Product-Specific Rules）
```

### 2.2 Section 301关税叠加规则

**当前主要对华301关税Lists（截至2024年）：**

| List | 税率 | 覆盖范围 |
|------|------|----------|
| List 1 (Section 301 Step 1) | 25% | 约340亿美元商品（2018年7月生效） |
| List 2 (Section 301 Step 2) | 25% | 约160亿美元商品（2018年8月生效） |
| List 3 (Section 301 Step 3) | 25% | 约2000亿美元商品（2018年9月生效） |
| List 4A | 15%（后降至7.5%） | 约1200亿美元商品（2019年9月生效） |
| List 4B | 15%（后暂停） | 约1600亿美元商品（2019年12月生效） |

**税率计算示例：**
- 商品HTS: 8471.30.0100（电脑）
- General税率: 0%
- Section 301 List 4A税率: 7.5%
- 实际应付税率: 7.5%

### 2.3 税率复议流程

**进口商可在 CBP 裁决后90天内提出Protest：**

1. 收到CBP裁定或清算通知
2. 确定争议焦点（HTS分类、税率适用、原产地）
3. 准备支持文件（技术规格、用途说明、 prior rulings）
4. 通过CBP的APS系统或书面形式提交Protest
5. 若被拒，可升级至 CBPF-28 或法院诉讼（USCIT或CIT）

---

## 三、实务指引与案例库

### 3.1 分类检索入口
- USITC HTS查询: https://hts.usitc.gov
- CBP Binding Ruling Search: https://rulings.cbp.gov
- USTR Section 301 List查询: https://ustr.gov/301调查
- CBP Protest提交: https://cbp.gov/revenue/protests

### 3.2 常见分类错误

| 错误类型 | 后果 | 纠正方法 |
|----------|------|----------|
| HS前6位归类错误 | 税率错误、清关延误 | 申请Internal Advice或Protest |
| 忽略Section 301 | 少缴税款、利息、罚款 | 自我稽查、主动披露 |
| FTA原产地资格误报 | 补缴税款+罚则、优惠资格丧失 | 提供补充证据或重新申请 |
| 统计尾注忽略 | 数量申报错误、罚款 | 查阅统计尾注 |

### 3.3 Section 301豁免与排除

**豁免（Exclusion）申请：**
- 特定商品可向USTR申请排除（Exclusion）
- 排除有效期通常为申请批准后1年
- 需证明：国内无可替代供应商、技术因素导致无法转移供应链

**排除申请路径：**
- https:// exclusions.uspto.gov （部分商品）
- 通过USTR官网提交评论

---

## 升级决策门

**以下情形必须升级至持牌报关行（Licensed Customs Broker）或国际贸易法律师：**

1. HTS分类涉及产品特性争议（技术规格与分类标准对应关系不明）
2. Section 301税率适用存在争议（商品是否在List覆盖范围内）
3. 原产地裁定涉及实质性改变（Substantial Transformation）认定
4. 潜在AD/CVD税则（已有或可能启动的反倾销调查）
5. 涉及美国法院诉讼（CIT/USCIT）
6. Protest被CBP拒绝后升级
7. 涉及贸易补救措施（Safeguard）的配额管理
8. 多国税制交叉（例：商品经过台湾加工，是否改变原产地）
9. 涉及知识产权边境保护（ Trademark侵权进口）
10. 预估争议税额超过$100,000

---

## 本Skill不涵盖

1. **出口管制与EAR/ITAR合规** → 请使用 `export-control-reviewer`
2. **OFAC及制裁名单筛查** → 请使用 `trade-sanctions-checker`
3. **Incoterms术语选择** → 请使用 `incoterms-guide`
4. **海关商品检验、检疫要求（FDA、USDA等）** → 需单独查询相关机构
5. **反倾销/反补贴税的调查程序和应诉** → 请使用 `trade-dispute-advisor`
6. **美国以外其他国家的关税制度**（欧盟税则、日本关税等）→ 需单独查询
7. **刑事案件或CBP重大违规处罚的抗辩** → 必须转介刑事辩护律师
8. **HTS分类的正式Binding Ruling申请** → 建议通过CBP的正式裁决程序
## 本 Skill 不涵盖

- 海关商品归类的专业判断（须海关归类专家）
- 反倾销/反补贴税的核查
- 关税筹划方案的具体税务申报
- 海关估价的争议解决
