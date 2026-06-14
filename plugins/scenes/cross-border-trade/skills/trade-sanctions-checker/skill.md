---
name: trade-sanctions-checker
description: >
  贸易制裁名单核查 — 查询制裁名单，评估交易相对方的制裁风险。
  适用情形：用户描述与本skill相关的业务需求。
argument-hint: "[交易相对方名称/注册地/交易标的/涉及国家]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# Trade Sanctions Checker

## 一、核心定义与适用范围

### 1.1 核心定义
**OFAC（外国资产控制办公室）** 是美国财政部下属机构，负责管理和执行基于美国外交和国家安全目标的制裁计划。OFAC依据总统国家安全权力（IEEPA或类似的）实施制裁，无需国会立法。

**SDN List（特别指定国民清单）** 是OFAC管理的核心制裁清单，列明被禁止交易的对象（个人、实体、船只）。

**Sectoral Sanctions Identifications (SSI)** 是针对俄罗斯特定行业（金融、能源、国防）的限制性指令。

**Blocking Statute（封锁法规）** 如欧盟EU Blocking Statute（EC 2271/96）禁止遵守美国对伊朗、古巴等域外制裁。

### 1.2 制裁类型分类
| 类型 | 范围 | 典型制裁列表 |
|------|------|------------|
| 全面的禁运国家制裁 | Cuba, Iran, North Korea, Syria, Crimea | 禁运+全面封锁 |
| 名单制裁（List-based） | SDN List | 与所列实体交易即禁止 |
| 行业制裁（Sectoral） | Russian SSI | 特定行业限制而非全面禁止 |
| 目标制裁（Targeted） | 特定国家/实体/人 | 针对性强 |
| 次级制裁（Secondary） | 第三国实体参与受制裁交易 | 域外效力最强 |

### 1.3 主要制裁法律依据
| 法律 | 授权范围 |
|------|----------|
| IEEPA (50 USC 1705) | 总统宣布国家紧急状态后实施经济制裁 |
| OFAC Regulations (31 CFR) | OFAC制裁的详细实施规则 |
| UN Security Council Resolutions | 联合国制裁决议（对成员国约束） |
| EU Sanctions Framework | 欧盟独立制裁机制 |

---

## 二、分析框架与操作流程

### 2.1 制裁筛查决策流程

```
STEP 1: 确定交易相关方管辖权
    │
    ├─ 美国因素（US Nexus）？
    │   ├─ 美国个人/实体
    │   ├─ 美国原产商品/技术
    │   ├─ 美元交易（USD clearing）
    │   └─ 过境美国的商品/信息
    └─ 无美国因素 → 检查当地法律（如EU Blocking Statute）

STEP 2: 筛查交易相对方
    │
    ├─ 筛查OFAC SDN List（含SSI、CAPTA List）
    ├─ 筛查BIS Denied Persons / Entity List
    ├─ 筛查联合国安理会决议清单
    ├─ 筛查欧盟制裁清单
    └─ 筛查其他相关政府清单

STEP 3: 筛查交易结构
    │
    ├─ 涉及禁运国家/地区（Cuba, Iran, NK, Syria, Crimea）？
    ├─ 涉及被制裁行业（俄罗斯 SSI）？
    ├─ 涉及被封锁交易（Blocking Statute触发）？
    └─ 涉及规避行为（Evasion typologies）？

STEP 4: 许可与例外判断
    │
    ├─ OFAC General License → 特定类别授权
    ├─ OFAC Specific License → 点名授权（需申请）
    ├─ 适用例外（Exception）条款
    └─ 无许可可用 → 交易禁止

STEP 5: 文档记录
    ├─ 筛查记录保留（至少5年）
    └─ 若发现疑似命中（Potential Match）→ 升级审查
```

### 2.2 制裁名单详解

**OFAC SDN List 命中判断要素：**
- 全名（Name）——需音译匹配
- 别名（AKA）——需穷尽搜索
- 地址（Address）——地址模糊性处理
- 国籍（Nationality）
- 证件号（Passport/ID）
- 组织关联（Entity association）

**常见命中情形：**
| 情形 | 示例 | 合规要求 |
|------|------|----------|
| 直接交易 | 向SDN List实体直接出口 | 禁止 |
| 代理交易 | 通过中间方与SDN交易 | 禁止（知悉即违规） |
| 船舶运输 | SDN船只挂靠禁运国港口 | 港口拒绝+货物检查 |
| 协助规避 | 帮助SDN转移资产 | 禁止 |

### 2.3 俄罗斯 SSI 专项规则

**OFAC Russian Sanctions Directives（按时间顺序）：**

| Directive | 日期 | 核心限制 |
|-----------|------|----------|
| Directive 1 | 2014 | 禁止向俄罗斯国防、能源行业提供特定物项 |
| Directive 2 | 2014 | 禁止向俄罗斯主要银行提供新融资 |
| Directive 3 | 2014 | 禁止向俄罗斯石油行业提供深海、北极项目物项 |
| Directive 4 | 2014 | 禁止向俄罗斯军事终端用户提供物项 |

**GLINK 规避模式警示：**
- 虚假原产地文件（第三国再出口时伪造中国/土耳其产地）
- 交易结构掩盖最终用户（通过中间公司）
- 金融工具剥离美元清算通道

---

## 三、实务指引与案例库

### 3.1 筛查工具入口
- OFAC Sanctions List Search: https://sanctionssearch.ofac.treas.gov
- OFAC SDN List Download (XML): https://treasury.gov/ofac/downloads/sdn.xml
- BIS Denied Persons/Entity List: https://bis.doc.gov/index.php/compliance-entity-list
- UN Security Council Sanctions List: https://www.un.org/securitycouncil/sanctions
- EU Sanctions Map: https://www.sanctionsmap.eu

### 3.2 License 类型速查
| License类型 | 说明 | 申请周期 |
|-------------|------|----------|
| General License | 自动授权（无需申请） | 不适用 |
| Specific License | 点名授权（需申请） | 数周至数月 |
| Statement of Licensing Policy | 政策说明非正式许可 | 参考性质 |

### 3.3 常见违规模式

| 模式 | 违规认定 | 典型后果 |
|------|----------|----------|
| 不知情抗辩失败 | OFAC: "知悉即违规"（Willful Blindness无效） | 民事罚款 |
| 通过第三国规避 | 伊朗规则：通过土耳其/阿联酋实体转口 | 刑事+民事 |
| SDN船参与禁运港 | 船只被拒绝进入美国港口 | 船舶滞留+罚款 |
| 美国来源成分超标 | 含美国技术的外国商品被俄罗斯最终用户获取 | EAR/OFAC双重责任 |

---

## 升级决策门

**以下情形必须升级至OFAC专业法律顾问或持牌律师：**

1. 交易涉及禁运国家（Cuba, Iran, North Korea, Syria, Crimea）
2. 筛查发现潜在SDN命中（Potential Match）需要进一步调查
3. 涉及特定License申请（Specific License to Engage in Prohibited Transaction）
4. 涉及次级制裁风险（美国主体帮助非美国主体规避制裁）
5. 涉及欧盟Blocking Statute与OFAC制裁冲突（尤其伊朗交易）
6. 涉及被冻结资产或财产解冻程序
7. 涉及OFAC执法调查或和解谈判
8. 涉及刑事制裁风险（故意违规）
9. 涉及船舶被拒绝进入美国港口（PFAOs）
10. 涉及多方管辖权冲突（美国+欧盟+中国同时适用）

---

## 本Skill不涵盖

1. **出口管制EAR/ITAR合规** → 请使用 `export-control-reviewer`
2. **HTS分类与进口关税** → 请使用 `import-tariff-adviser`
3. **Incoterms条款选择** → 请使用 `incoterms-guide`
4. **反倾销/反补贴税争议** → 请使用 `trade-dispute-advisor`
5. **刑事辩护及政府和解** → 必须转介专业刑事辩护律师
6. **实时数据库筛查**（本Skill提供筛查框架，但OFAC/BIS/UN数据库需实时查询）
7. **OFAC执法和解金额计算** → 需OFAC专业顾问
8. **美国国防部国防贸易管制（ITAR）相关制裁** → 需DDTC专项咨询
## 本 Skill 不涵盖

- 制裁名单的实质性移除程序
- OFAC/欧盟等外国制裁的适用判断
- 制裁合规体系的建设方案
- 制裁处罚的应对与申辩
