# 三大 Legal Skill 项目全景对比分析

> GCL vs THUYRan vs cat-xierluo
> 覆盖：项目定位/技能体系/架构设计/质量标准/融合价值

---

## 一、项目基本信息

| | **cat-xierluo/legal-skills** | **THUYRan/Legal-Skills-Chinese** | **vivy-yi/Greater-China-Legal** |
|---|---|---|---|
| **stars** | 343 | 未公开（估计100-200） | 0（新建） |
| **forks** | 53 | 未公开 | 0 |
| **commits** | 620 | 未公开 | ~15 |
| **作者** | 杨卫薪律师（IP/技术纠纷专业） | 未公开（推断：法律研究者） | vivy-yi |
| **最近更新** | 2小时前（极活跃） | 未公开 | 进行中 |
| **许可证** | MIT（工具）/ CC-BY-NC（专业） | 未公开 | MIT |
| **定位** | 律师工作台（工具链+专业应用） | 法律认知推理引擎 | 大中华区法律场景Agent |
| **skill数量** | 49个目录 | 38个 | 54个 |

---

## 二、技能体系对比

### cat-xierluo/legal-skills：律师工作台

**三层架构：**

```
内容获取层（工具）
  wechat-article-fetch    — 公众号抓取
  legal-ocr               — OCR识别（推荐入口）
  funasr-transcribe       — 语音转文字
  universal-media-downloader — 视频下载
  multi-search            — 多主题并行检索

内容处理层（格式转换）
  img2pdf                 — 长截图转PDF
  md2word                 — Markdown转Word
  pdf-organizer            — PDF整理
  transcription-corrector  — 转录稿纠错

法律专业应用层（核心）
  litigation-analysis      — 诉讼分析（判决书/庭审笔录）
  legal-case-analysis      — 通用法律分析引擎
  contract-copilot         — 合同起草与审查（DOCX）
  legal-proposal-generator — 法律服务文档生成
  legal-visualization      — 法律图解生成（draw.io）
  new-case                — 案件材料整理
  court-sms               — 法院短信识别与文书下载
  trademark-assistant      — 商标案件辅助
  yuandian-law-search      — 元典法条/案例检索（API）
  zhihe-legal-research     — 智合AI法律研究（API）
```

**核心特点：**
- 工具链完整：从内容获取→处理→分析→输出全覆盖
- 交付标准高：合同审查必须输出DOCX（含批注/修订版），不是"说说而已"
- 可视化能力强：draw.io XML生成，18个业务条线模板
- 质量工具：skill-lint v2.0.8（安全评估/危险执行/敏感文件/凭证检测）

---

### THUYRan/Legal-Skills-Chinese：法律认知推理引擎

**38个原子能力分7类：**

```
01 信息检索
  case-retrieval                  — 类案检索
  legal-article-retrieval         — 法条检索
  legal-norm-validity-check        — 法条效力核查 ⚡GCL缺

02 事实处理
  legal-element-extraction         — 法律要素提取 ⚡GCL缺
  dispute-issue-identification    — 争议焦点识别
  evidence-evaluation             — 证据评估 ⚡GCL弱

03 法律解释
  systematic-interpretation       — 系统解释
  teleological-interpretation     — 目的解释

04 法律推理
  deductive-reasoning             — 演绎推理（三段论）⚡GCL隐含
  inductive-reasoning             — 归纳推理
  analogical-reasoning            — 类比推理 ⚡GCL缺
  legal-abductive-reasoning       — 追因推理

05 论证组织
  argument-chain-construction     — 论证链构建 ⚡GCL弱
  argument-strength-evaluation     — 论证强度评估 ⚡GCL缺

06 风险评估
  legal-risk-assessment           — 法律风险评估 ⚡GCL弱
  judicial-value-judgment         — 司法价值判断 ⚡GCL缺

07 文书管理
  legal-document-formatting       — 法律文书格式化
  judgment-document-generation    — 裁判文书生成 ⚡GCL缺
  legal-document-summarization   — 法律文书摘要 ⚡GCL缺
```

**核心特点：**
- 认知链路完整：从检索→事实提取→解释→推理→论证→评估→文书
- 推理质量高：每个skill都有P-F-C格式/证明力评估/论证链构建
- 极度原子化：38个skill可以自由组合，但组合方式由用户决定

---

### Greater-China-Legal：多法域场景Agent

**9场景×6skills：**

```
场景A 劳动仲裁      — dispute-classifier/termination-legality/
                       compensation-calculator/region-adjudicator/
                       arbitration-filing/negotiation-advisor

场景B 合同审查      — contract-classifier/term-analyzer/
                       civil-code-checker/risk-pre-screening/
                       negotiation-advisor/dispute-handler

场景C 数据合规      — data-asset-inventory/pipl-assessment/
                       cac-enforcement-tracker/legal-basis-checker/
                       cross-border-transfer/dsar-response

场景D 公司治理      — company-type-selector/governance-structure/
                       financing-round-advisor/vie-risk-analyzer/
                       odi-compliance/capital-change-filing

场景E 知识产权侵权  — infringement-detector/trademark-search/
                       patent-validity-checker/evidence-collection/
                       rights-protection-path/fee-calculator

场景F 税务合规      — tax-type-classifier/invoice-compliance/
                       transfer-pricing-risk/vat-credit-calculator/
                       cross-border-tax/tax-dispute-handler

场景G 跨境并购      — due-diligence/structuring-advisor/
                       transaction-doc-review/approval-flow/
                       fdi-odi-filing/closing-checklist

场景H 互联网金融    — license-type-checker/qualification-gap-assessment/
                       consumer-protection-checker/compliance-doc-generator/
                       ongoing-compliance-monitor/data-security-assessment

场景I 诉讼支持      — strategy-designer/evidence-organizer/
                       lawsuit-doc-generator/procedure-timeline/
                       fee-calculator/appeal-path-checker
```

**核心特点：**
- 多法域：大中华区（大陆/香港/澳门/台湾/新加坡）
- 场景完整覆盖：端到端（判断→分析→文书→流程）
- 上游同步机制：月度workflow自动同步Anthropic更新
- 数据源治理：五级标注（[YD]/[WKL]/[BD]/[GOV]/[model]）

---

## 三、架构设计对比

| 维度 | cat-xierluo | THUYRan | GCL |
|---|---|---|---|
| **组织方式** | 工具链 + 专业应用 | 原子能力自由组合 | 场景容器 |
| **Skill粒度** | 中等（一个skill解决一类问题） | 极细（一个skill一个推理动作） | 中等（一个skill一个判断/操作） |
| **输入假设** | 用户已有材料（PDF/判决书/合同） | 通用输入（须自己组合） | 用户描述（须先提取事实） |
| **输出形式** | 文件交付（DOCX/SVG/图表） | 结构化文本 | 结构化判断+建议 |
| **场景化** | 有（litigation/contract/visualization） | 无（纯推理） | 有（9个业务场景） |
| **多法域** | 无（仅cn-mainland） | 无（仅cn-mainland） | 有（大中华区） |
| **Agent架构** | .claude/ + .agents/ + SKILL.md | SKILL.md（纯） | CLAUDE.md + SKILL.md + references/ |
| **知识配置** | 无 | 无 | LEGAL_FRAMES/（5法域基准） |
| **MCP工具** | yuandian-law-search（API） | MCP-PKULAW（但很简略） | [YD]标注（未实现） |
| **版本规范** | frontmatter version字段 | 无 | frontmatter version字段 |
| **质量工具** | skill-lint v2.0.8 | 无 | scripts/validate-skills.py |

---

## 四、质量标准对比

| 维度 | cat-xierluo | THUYRan | GCL |
|---|---|---|---|
| **法律声明** | 无 | 4条法律声明（极详细） | 3条风险提示 |
| **输入前置检查** | 无 | 3条前置检查 | 无 |
| **输出格式规范** | 强（模板化） | 中（格式建议但不强制） | 中（有格式但不统一） |
| **错误防范** | 无 | 7种常见错误+防范措施 | 无 |
| **质量检查清单** | 无 | 14条自检清单 | 无 |
| **持续更新机制** | 有（changelog/decisions/tasks） | 无 | 无 |
| **许可证管理** | 完善（MIT/CC-BY-NC双轨） | 无 | 无 |
| **作者署名** | 强制（微信ywxlaw） | 无 | 可选 |
| **交付物规范** | 极强（DOCX三件套等） | 无 | 无 |

---

## 五、真正互补的部分

### GCL缺但THUYRan有的（P0）

| THUYRan Skill | GCL现状 | 融合价值 |
|---|---|---|
| `legal-element-extraction` | **完全没有** | 所有场景的输入预处理 |
| `legal-norm-validity-check` | **完全没有** | 引用法条前必须验证效力 |
| `deductive-reasoning` | termination-legality隐含 | 显式P-F-C三段论格式 |
| `analogical-reasoning` | **没有** | 类案推理方法论 |
| `argument-strength-evaluation` | **没有** | 论证强度自检 |
| `judicial-value-judgment` | **没有** | 司法价值判断 |
| `judgment-document-generation` | lawsuit-doc-generator有但弱 | 裁判文书格式规范 |

### GCL缺但cat-xierluo有的（P0）

| cat-xierluo Skill | GCL现状 | 融合价值 |
|---|---|---|
| `contract-copilot` | contract-review有但弱 | DOCX批注/修订版交付链 |
| `legal-visualization` | **完全没有** | draw.io图表生成，18业务条线 |
| `skill-lint` | scripts/validate-skills.py有但不完善 | 安全评估/危险执行检测 |
| `court-sms` | **没有** | 法院短信→文书下载归档 |
| `new-case` | **没有** | 案件材料标准化整理 |
| `multi-search` | **没有** | 多主题并行深度检索 |
| `legal-proposal-generator` | **没有** | 模块化生成法律服务文档 |

### cat-xierluo缺但THUYRan有的

| THUYRan Skill | cat-xierluo现状 | 融合价值 |
|---|---|---|
| `legal-element-extraction` | 无 | 事实整理前置 |
| `deductive-reasoning` | 无 | 推理格式规范 |
| `dispute-issue-identification` | litigation-analysis有但不规范 | 争议焦点识别 |
| `legal-norm-validity-check` | 无 | 法条效力实时核查 |

---

## 六、融合路线图

### 优先级P0（GCL必须补）

```
1. legal-element-extraction（已完成试点）
   → 融入各场景输入预处理

2. legal-visualization（cat-xierluo）
   → 新增到b-scenes/common/或litigation-support/
   → draw.io XML生成，18个业务条线模板
   → 解决GCL所有skill输出"只能文字"的问题

3. contract-copilot（cat-xierluo）
   → 升级现有contract-review的DOCX输出能力
   → 分层审查（宏观/中观/微观）+ P0/P1/P2风险分级
   → 交付物：审核修订版DOCX + 审查意见书DOCX

4. skill-lint（cat-xierluo）
   → 升级scripts/validate-skills.py
   → 增加安全评估（危险执行/敏感文件/凭证检测）
   → 与skill-authoring规范对齐

5. legal-norm-validity-check（THUYRan）
   → 新增atomic skill
   → 引用法条时必须验证效力+时间状态+层级
```

### 优先级P1（有价值但非必须）

```
6. deductive-reasoning P-F-C格式（THUYRan）
   → 融入termination-legality等判断类skill

7. court-sms（cat-xierluo）
   → 新增litigation-support辅助skill
   → 法院短信→文书归档

8. new-case（cat-xierluo）
   → 新增litigation-support辅助skill
   → 案件材料标准化整理

9. deductive-reasoning（THUYRan）
   → 融入strategy-designer论证链

10. multi-search（cat-xierluo）
    → 升级references/查询路径.md为并行检索
```

### 优先级P2（锦上添花）

```
11. judgment-document-generation（THUYRan）
    → 升级lawsuit-doc-generator

12. analogical-reasoning（THUYRan）
    → 新增atomic skill

13. argument-strength-evaluation（THUYRan）
    → 融入strategy-designer
```

---

## 七、三项目关系总结

```
Anthropic官方(claude-for-legal)
    ↓ fork
Greater China Legal (GCL)
    ├── 9场景×6skills（场景完整覆盖）
    ├── 多法域（大中华区）
    └── LEGAL_FRAMES/（知识配置）

THUYRan/Legal-Skills-Chinese
    ├── 38原子推理能力（认知链路完整）
    └── 推理质量标准（P-F-C/论证链/三性评估）

cat-xierluo/legal-skills
    ├── 工具链（OCR/下载/转写）
    ├── 专业应用（litigation/contract/visualization）
    └── 质量工具（skill-lint）

融合公式：
GCL（场景+法域）
  + THUYRan（推理方法论）
  + cat-xierluo（工具链+交付标准+质量工具）
  = 大中华区法律Agent完整工作台
```

---

## 八、融合后的GCL架构

```
Greater-China-Legal/
├── CLAUDE.md                     ← 项目级Agent配置
├── LEGAL_FRAMES/                 ← 5法域知识基准（不变）
├── SKILL_MD_SCHEMA.md            ← Skill规范（不变）
├── scripts/
│   ├── validate-skills.py        ← 升级：+skill-lint安全评估
│   └── sync-upstream.py          ← 月度同步（不变）
│
├── b-scenes/                     ← 9场景层（不变）
│   ├── labor-arbitration/
│   ├── contract-review/          ← 升级：+contract-copilot输出
│   ├── data-compliance/
│   ├── company-governance/
│   ├── ip-infringement/           ← +legal-visualization
│   ├── tax-compliance/
│   ├── cross-border-ma/
│   ├── internet-finance/
│   └── litigation-support/       ← 升级：+court-sms/+new-case
│
├── b-scenes/legal-atomic/        ← 新增：THUYRan原子能力
│   ├── legal-element-extraction/ ← ✅已完成
│   ├── legal-norm-validity-check/ ← P0待做
│   ├── deductive-reasoning/       ← P1
│   ├── dispute-issue-identification/ ← P1
│   ├── evidence-evaluation/      ← 升级现有organizer
│   ├── argument-chain-builder/    ← P1
│   └── references/
│       └── case-retrieval-method.md ← 升级references/
│
└── b-scenes/legal-tools/         ← 新增：cat-xierluo工具skill
    ├── legal-visualization/       ← P0
    ├── court-sms/                 ← P1
    ├── new-case/                  ← P1
    └── multi-search/              ← P1
```

---

*分析日期：2026-06-13*
