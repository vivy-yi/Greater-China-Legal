---
name: trade-dispute-advisor
description: >
  国际贸易争议咨询 — 提供货物索赔、货款催收、质量纠纷的解决路径。
  适用情形：用户描述与本skill相关的业务需求。
argument-hint: "[争议类型：货损/拖欠/质量/违约/合同金额]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
  - 跨境
  - 进出口
  - 海关
  - trade dispute
---

# Trade Dispute Advisor

## 一、核心定义与适用范围

### 1.1 核心定义
**反倾销税（Anti-Dumping Duty, AD）** 是对外国商品以低于正常价值（Normal Value）销售并对本国产业造成损害的行为征收的额外关税。

**反补贴税（Countervailing Duty, CVD）** 是对外国政府补贴的进口商品征收的额外关税，用于抵消补贴对本国产业的影响。

**Section 337调查** 是美国国际贸易委员会（USITC）依据1930年关税法第337条对进口贸易中的不公平行为（尤其是知识产权侵权）进行调查并发布排除令的程序。

**保障措施（Safeguard）** 是WTO允许成员国在进口激增对国内产业造成严重损害时临时提高关税或实施配额。

### 1.2 适用范围
- 美国商务部（DOC）对AD/CVD调查程序
- USITC损害调查程序
- WTO争端解决机制（DSU）
- Section 337知识产权排除令
- 中国出口商在AD/CVD中的应诉策略
- 贸易救济措施的配额管理

### 1.3 核心法规依据
| 法规 | 管辖 | 主管机构 |
|------|------|----------|
| 19 USC 1673 | 反倾销税法 | 商务部（DOC）/ USITC |
| 19 USC 1671 | 反补贴税法 | 商务部（DOC）/ USITC |
| 19 USC 1337 | Section 337 | USITC |
| WTO DSU | WTO争端解决程序 | WTO |

---

## 二、分析框架与操作流程

### 2.1 AD/CVD调查程序流程

```
STEP 1: 起诉阶段
    │
    ├─ 美国国内产业代表提交请愿书（Petition）
    ├─ DOC受理并启动调查
    └─ USITC初步损害认定（Preliminary）

STEP 2: DOC调查阶段
    │
    ├─ 问卷调查（Questionnaire）
    ├─ 正常价值（Normal Value）计算
    │   ├─ 出口国国内市场价
    │   ├─ 第三国市场价
    │   └─ 结构价值（Constructed Value）
    ├─ 出口价格（Export Price）或国外市场值（FPV）
    └─ 倾销幅度（Dumping Margin）计算

STEP 3: USITC损害调查阶段
    │
    ├─ 产业损害分析（Material Injury）
    ├─ 因果关系分析（Causal Link）
    └─ 损害威胁分析（Threat of Material Injury）

STEP 4: 初裁与终裁
    │
    ├─ DOC Preliminary Determination（初步裁定）
    ├─ DOC Final Determination（最终裁定）
    └─ USITC Final Determination（最终损害裁定）

STEP 5: 税令执行
    ├─ 若均为肯定裁定 → 发布AD/CVD税令
    └─ 进口商须支付押金或独立保证金
```

### 2.2 正常价值计算方法

**正常价值（Normal Value）确定顺序：**

1. **国内市场价格法**
   - 出口国国内市场同类产品实际销售价格
   - 扣除内陆运费、保险费、管理费等

2. **第三国市场价格法**
   - 若国内销售不足或不存在正常贸易条件

3. **结构价值法（Constructed Value）**
   - 原材料成本 + 加工成本 + SG&A + 利润
   - 用于非市场经济国家（如中国，使用替代国价值）

**倾销幅度计算：**
```
Dumping Margin = (Normal Value - Export Price) / Export Price × 100%
```

**例：**
- Normal Value = $100/unit
- Export Price = $80/unit
- Dumping Margin = ($100 - $80) / $80 × 100% = 25%

### 2.3 Section 337 程序

```
STEP 1: USITC启动调查
    │
    ├─ 基于337条不公平行为指控
    ├─ 常见类型：专利侵权、商标侵权、版权侵权、商业秘密盗窃
    └─ 立案后45天确定调查期限

STEP 2: 证据开示（Discovery）
    │
    ├─ 文件交换
    ├─ 证人质询
    └─ 专家证人

STEP 3: 听证会（Hearing）
    └─ USITC行政法官主持

STEP 4: 初裁（Initial Determination）
    │
    ├─ 违反337条认定
    └─ 推荐补救措施

STEP 5: USITC审议
    │
    └─ 委员会审查，提交总统批准（60天）

STEP 6: 排除令（Exclusion Order）
    ├─ 普遍排除令（GEO）→ 禁止所有侵权商品进入
    ├─ 有限排除令（LEO）→ 仅禁止被诉方商品
    └─ 禁止令（Cease and Desist Order）→ 在美销售禁令
```

### 2.4 中国企业应诉要点

**AD/CVD应诉策略：**
| 阶段 | 策略 | 要点 |
|------|------|------|
| 立案通知 | 及时响应 | 20天内提交应答 |
| 问卷调查 | 完整准确 | 数据不一致导致不利推定 |
| 现场核查 | 合规配合 | CBP现场核查是常规程序 |
| 初裁 | 争取低税率 | 提供充分证据 |
| 复审（Administrative Review） | 年度申请 | 避免高税率延续 |

**重要时限：**
- DOC问卷应答：30天（可申请延期）
- 现场核查准备：提前30天
- 复审申请：每年1月31日截止

---

## 三、实务指引与案例库

### 3.1 典型AD/CVD案例

**案例：光伏产品双反案（2012）**
- 产品：晶体硅光伏电池及组件
- 中国企业税率：约30%-250%（各企业单独税率）
- 结果：税令执行后中国光伏产品对美出口大幅下降

**案例：轮胎特保案（2009）**
- 措施：3年防卫性关税（第一年35%，第二年30%，第三年25%）
- 法律依据：WTO Safeguard Agreement
- 结果：中国输美轮胎数量下降

### 3.2 WTO争端解决流程

**DSB（争端解决机构）程序：**
1. 磋商（Consultations）：60天内
2. 专家组（Panel）设立：DSB投票
3. 专家组报告：6个月内
4. 上诉机构（Appellate Body）审议：60天内（但当前上诉机构瘫痪）
5. DSB通过报告：上诉后30天内

**上诉机构危机：**
- 自2019年起美国阻止新成员任命
- 上诉机构仅剩1人（无法运作）
- 实务中各方探索替代机制（Multi-Party Interim Appeal Arbitration）

### 3.3 Section 337 应对要点

| 策略 | 说明 |
|------|------|
| 专利无效抗辩 | 请求美国专利商标局（PTO）多方复审（IPR） |
| 不侵权抗辩 | 分析权利要求范围 |
| 不可执行抗辩 | 专利权滥用 |
| 国内产业不足抗辩 | USITC需证明国内产业存在 |
| 公共利益例外 | 公共健康、能源等领域可例外 |

---

## 升级决策门

**以下情形必须升级至国际贸易法律师（含WTO代理资质）或专业AD/CVD应诉事务所：**

1. DOC启动AD/CVD调查并发出问卷（美国商务部正式立案）
2. 中国企业被征收高额税率（>50%）需申请年度复审
3. USITC启动Section 337调查
4. 涉及中国出口商品被纳入美国实体清单/特别措施
5. 涉及WTO争端解决机制（需具备DSU代理资质）
6. 涉及美国国内产业对华商品提出的保障措施申请
7. 涉及AD/CVD税令执行期间的绕过行为（如第三国组装）
8. 涉及刑事处罚的贸易案件
9. 涉及联邦法院对贸易裁决的上诉（USCIT/Court of Appeals）
10. 涉及贸易救济措施配额管理中的合规问题

---

## 本Skill不涵盖

1. **出口管制EAR/ITAR合规** → 请使用 `export-control-reviewer`
2. **HTS分类与进口关税** → 请使用 `import-tariff-adviser`
3. **OFAC及制裁名单筛查** → 请使用 `trade-sanctions-checker`
4. **Incoterms条款选择** → 请使用 `incoterms-guide`
5. **海关合规及FTA原产地规则** → 请使用 `customs-compliance-assessor`
6. **美国刑事辩护（走私、欺诈）** → 必须转介专业刑事辩护律师
7. **美国专利诉讼（地区法院）** → 需专利诉讼专项律师
8. **WTO上诉机构代理（当前机制受损）** → 需专业WTO律师评估替代方案
9. **欧盟对华AD调查应诉** → 需欧盟贸易法专项律师
10. **海关税令的行政复核（Administrative Remedy）** → 建议通过专业报关行
## 本 Skill 不涵盖

- 国际贸易仲裁/诉讼的代理
- 信用证开证与审证
- 货损鉴定与保险理赔
- 外贸合同的具体条款起草
