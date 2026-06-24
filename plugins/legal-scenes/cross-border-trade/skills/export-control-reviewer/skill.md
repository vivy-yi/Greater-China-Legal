---
name: export-control-reviewer
description: >
  出口管制合规核查 — 核查货物/技术出口是否需要许可证，判断是否在管制清单范围内。
  适用情形：用户描述与本skill相关的业务需求。
argument-hint: "[产品名称/HS编码/出口目的地/最终用途]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
  - 跨境
  - 进出口
  - 海关
  - export control
---

# Export Control Reviewer

## 一、核心定义与适用范围

### 1.1 核心定义
**出口管制（Export Control）** 是指对特定货物、技术、软件及服务的跨境转移进行监管的法律框架。核心法规包括美国EAR（出口管理条例）、ITAR（国际武器贸易条例）以及多边出口管制机制。

**ECCN（Export Control Classification Number）** 是10位字母数字分类代码，用于识别受控物项的技术参数和管制原因。

### 1.2 适用范围
- 物理商品、技术数据、软件的跨境转移
- 视同出口（deemed export）——向外国公民在境内转让技术
- 外国直达（foreign direct product）规则
- 再出口（re-export）操作
- 触发USML/CCL分类的交易

### 1.3 核心法规依据
| 法规 | 管辖 | 主管机构 |
|------|------|----------|
| EAR (15 CFR 730-774) | 商业及两用物项 | 商务部工业与安全局 (BIS) |
| ITAR (22 CFR 120-130) | 国防军用物项 | 国务院防务贸易管制局 (DDTC) |
| CCL (Commerce Control List) | 两用物项具体分类 | BIS |

---

## 二、分析框架与操作流程

### 2.1 分类决策树

```
STEP 1: 判断是否属于"物项"（Item）
    │
    ├─ 有形商品 → 物理检查 + HTS归类
    ├─ 技术数据 → 技术描述分析
    └─ 软件 → 功能性分析（源码/目标码）

STEP 2: 判断是否属于USML管制（ITAR）
    │
    ├─ 军在用清单（USML）类别匹配
    │   └─ 是 → ITAR许可，向DDTC申请
    └─ 否 → 进入EAR分析

STEP 3: CCL/ECCN分类（EAR）
    │
    ├─ 寻找对应ECCN（5位类别+3位产品组代码）
    │   └─ 例：3A001 = 电子器件类，Cat 3, Product Group A
    ├─ 评估管制原因（Reason Code）
    │   ├─ A: 军需/国家安全
    │   ├─ B: 导弹技术
    │   ├─ C: 核生化
    │   ├─ D: 加密
    │   ├─ E: 犯罪防控
    │   └─ S: 反恐等特殊管制
    └─ 确定Destination Chart中对该国的许可要求

STEP 4: 许可判断
    ├─ License Required → 申请BIS license
    ├─ License Exception可用 → 适用对应异常条款
    └─ No License Required → 记录文档，合法出口
```

### 2.2 关键合规测试

**Step-by-Step 审查清单**

1. **物品项是否受控？**
   - 搜索BIS SNAP-R系统或ECCN Search Tool
   - 对照CCL确认ECCN编码

2. **目的地是否受控？**
   - BIS Country Chart核对
   - 特别关注：禁运国（Cuba, Iran, North Korea, Syria, Crimea）

3. **最终用途是否可疑？**
   - 军事最终用途（MEU）审查
   - 核最终用途（NEU）审查
   - WMD扩散审查

4. **最终用户是否受限？**
   - BIS Entity List / Denied Persons List
   - OFAC SDN List交叉比对
   - 实际控制人穿透审查

5. **许可例外是否适用？**
   - 常见例外：ENC（加密）、STA（战略贸易授权）、RPL（给合法最终用户的零件）

### 2.3 常见违规模式

| 模式 | 风险 | 案例 |
|------|------|------|
| ECCN归类错误（低类别替代） | 民事罚款最高$300K/次，刑事最高20年监禁 | 某科技公司将对华出口芯片错误归类为EAR99 |
| 视同出口未审批 | 视同出口等同于实际出口 | 研究员向中国籍学生分享受控源码 |
| 许可证后使用 | 许可与实际用途不符 | 购买的许可设备被转用于禁用途 |
| 未知ECCN即发货 | "不知情"非抗辩理由 | 以"样品"名义出口未做分类审查 |

---

## 三、实务指引与案例库

### 3.1 标准操作流程（SOP）

**出口合规筛查流程（建议时长：复杂交易2-4小时）**

1. **信息收集（Input Required）**
   - 交易相对方全称、地址、联系方式
   - 物品项详细描述（含型号、技术参数）
   - 出口国、目的地国家、过境国
   - 最终用途声明（End-Use Certificate）
   - 最终用户身份及关联企业

2. **分类审查（Classification）**
   - BIS SNAP-R系统ECCN检索
   - USML类别匹配（ITAR）
   - 查表确认管制原因和许可要求

3. **筛查比对（Screening）**
   - BIS Entity List / Denied Persons / Unverified List
   - OFAC SDN List（含Sectoral Sanctions Identifications）
   - 联合国安理会决议清单
   - 美国国务院与禁运相关清单

4. **许可决策（License Determination）**
   - 许可Required → 申请流程 + 等待审批
   - License Exception可用 → 文件记录 + 条件确认
   - No License → 出口文件准备

5. **记录存档（Documentation）**
   - 保留至少5年（EAR要求）
   - 包含分类依据、筛查结果、许可文件

### 3.2 分类检索入口
- BIS SNAP-R: https://snapr.bis.doc.gov
- BIS ECCN Search: https://www.bis.doc.gov/index.php/regulations/commerce-control-list-classification
- CCL PDF: https://www.bis.doc.gov/index.php/regulations/export-administration-regulations

### 3.3 处罚标准速查
| 违规类型 | 民事罚款 | 刑事罚款 | 监禁 |
|----------|----------|----------|------|
| 违反EAR | 最高$300,000/违规或两倍损失 | 最高$1,000,000/违规 | 最高20年 |
| 违反ITAR | 最高$1,000,000/违规 | 最高$1,000,000/违规 | 最高20年 |
| 视同出口未批 | 同上 | 同上 | 同上 |

---

## 升级决策门

**以下情形必须升级至持牌国际贸易法律师或BIS/DDTC直接咨询：**

1. 目的地为禁运国家或地区（Cuba, Iran, North Korea, Syria, Crimea地区）
2. 涉及ITAR管制的国防物项（USML Category I-VIII）
3. 最终用途涉及军事、核、导弹、生化扩散（WMD）领域
4. 最终用户为BIS Entity List、Denied Persons或OFAC SDN List所列实体
5. ECCN分类涉及管制原因A/B/C/D（国家安全、导弹、核、生化）
6. 涉及再出口（re-export）且原许可不允许第三方转让
7. 潜在刑事违规风险（故意规避出口管制）
8. 单一违规事件涉及金额超过$500,000或数量规模较大
9. 涉及"外国直达产品"（Foreign Direct Product）规则适用争议
10. 出口物项存在功能增强或性能参数边界情况（borderline classification）

**升级时提供：完整交易描述、已收集的分类信息、已完成的筛查结果**

---

## 本Skill不涵盖

1. **进口关税与HTS分类** → 请使用 `import-tariff-adviser`
2. **制裁名单实时筛查** → 请使用 `trade-sanctions-checker`（本Skill提供筛查框架，但实时数据库需外部工具）
3. **Incoterms条款选择** → 请使用 `incoterms-guide`
4. **反倾销/反补贴税（AD/CVD）** → 请使用 `trade-dispute-advisor`
5. **原产地规则及FTA优惠税率** → 请使用 `customs-compliance-assessor`
6. **美国以外其他国家出口管制**（欧盟两用物项法规EC 428/2009、日本外汇法等）→ 需单独咨询
7. **刑事辩护及政府和解谈判** → 必须转介持牌律师
8. **ITAR注册及许可申请表格填写** → 建议直接咨询DDTC或专业合规顾问
## 本 Skill 不涵盖

- 出口许可证申请格式文本（由专业律师起草）
- 军事用途出口管制的特殊审批
- 外国出口管制法律的适用判断（域外管辖争议）
- 出口管制处罚听证与申辩
