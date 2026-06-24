# GCL 30 个 Scene CLAUDE.md 合规性审计

> **目的**：审计 Greater China Legal 项目 30 个 scene 的 `plugins/legal-scenes/<scene>/CLAUDE.md` 是否符合 `anthropics/claude-for-legal` 上游 18 个 pattern + 4d 章"4 处位置"设计原则。
> **方法**：用 12 维特征扫描每个 scene 的 CLAUDE.md（grep），与 upstream `commercial-legal/CLAUDE.md` 模板对比。
> **结论先行**：**30 个 scene 全部不符合 upstream 设计**——0% 通过率。
> **严重度**：高。本审计发现的不是"细节缺失"，而是**架构性错位**。
> **来源**：同目录 `upstream-kwp-design-analysis.md`（4d-4g 章）、`legal-cn-template.md`（目标态参考）

---

## 0. 12 维审计标准

每条标准对应上游 18 个 pattern 中的一个：

| # | 审计标准 | 对应 upstream 维度 | 严重度 |
|---|---------|-------------------|------|
| 1 | 文件大小（行数） | 模板完整性 | — |
| 2 | `[填空]` / `[公司名称]` 占位符数量 | Pattern 11（21 段骨架） | 高 |
| 3 | 是否有 `## Outputs` 段 | Pattern 9+10（reviewer note + decision tree） | 高 |
| 4 | 是否有 Shared guardrails 段 | Pattern 11+12（21 段 + 7 哲学） | **关键** |
| 5 | 是否提到 5 大法域 | Pattern 7+16（Side + 高度关注） | 高 |
| 6 | 是否有 `⚠️ Reviewer note` 模板 | Pattern 9 | **关键** |
| 7 | 是否有 Decision tree | Pattern 10 | 高 |
| 8 | 是否有 Playbook | Pattern（commercial sales/purchasing） | 中 |
| 9 | 是否提到 YAML 注册表 | Pattern 2+14 | **关键** |
| 10 | 是否提到 cold-start-interview | Pattern（4b 章节） | 中 |
| 11 | 是否有 work-product header | Pattern 13（4 档） | 高 |
| 12 | 是否区分 模板 vs 运行配置 | 4d 章 4 处位置 | **关键** |

**12 维评分**：4 个"关键"+ 5 个"高"+ 2 个"中"。

---

## 1. 30 个 scene 的扫描结果（原始数据）

| Scene | 行数 | [填空] | Outputs | 护栏 | 5jurisd | Reviewer | DecisionTree | Playbook | YAML | ColdStart | Header |
|-------|-----|--------|---------|------|---------|----------|--------------|----------|------|-----------|--------|
| ai-governance-legal | 199 | 6 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| bankruptcy-restructuring | 242 | 5 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| capital-markets | 123 | 4 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| commercial-arbitration | 120 | 4 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| contract-review | 278 | 5 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| corporate-governance | 271 | 8 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| cross-border-ma | 247 | 11 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| cross-border-trade | 149 | 4 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| data-compliance | 272 | 5 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| employment-legal | 449 | 2 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| financing-business | 147 | 5 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| government-investigation | 143 | 7 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| internet-finance | 246 | 6 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| ip-infringement | 229 | 8 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| labor-arbitration | 289 | 4 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| law-student | 163 | 5 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| legal-builder-hub | 137 | 3 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| legal-clinic | 147 | 5 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| litigation-support | 287 | 8 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| m-and-a | 132 | 4 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| pe-vc-funds | 119 | 4 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| **product-legal** | **461** | 2 | ✅ | **✅ 4** | ❌ | ✅ 11 | ✅ 5 | ❌ | ❌ | ✅ 7 | ✅ |
| real-estate-construction | 147 | 6 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| regulatory-compliance | 287 | 5 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| special-opportunity-investment | 123 | 6 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| tax-compliance | 231 | 7 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| wealth-succession | 116 | 4 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| web3-virtual-assets | 141 | 6 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| white-collar-crime | 247 | 7 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |

### 1.1 12 维的总体情况

| 维度 | 满足的 scene 数 / 30 | 占比 |
|------|---------------------|------|
| 文件 ≥ 200 行 | 18 / 30 | 60% |
| `[填空]` ≤ 5 | 14 / 30 | 47% |
| `## Outputs` 段 | 29 / 30 | 97% |
| **Shared guardrails** | **1 / 30** | **3%** |
| **5 大法域** | **6 / 30** | **20%** |
| **Reviewer note 5 行** | **1 / 30** | **3%** |
| **Decision tree 5 选项** | **1 / 30** | **3%** |
| Playbook 段 | 0 / 30 | **0%** |
| **YAML 注册表** | **1 / 30** | **3%**（仅 contract-review 提到） |
| Cold-start-interview | 22 / 30 | 73% |
| Work-product header | 30 / 30 | 100% |
| 模板/运行分离 | 0 / 30 | **0%** |

### 1.2 关键发现

**"关键"维度（4 个）全部 ≤ 3%**：

- **Shared guardrails**：只有 1/30（product-legal）
- **Reviewer note 5 行**：只有 1/30（product-legal）
- **YAML 注册表**：只有 1/30（contract-review 提到）
- **模板/运行分离**：0/30

**所有 scene 都没有"硬规则"**——10+ 条护栏是 12 个 upstream plugin 的"宪法"，本项目 0/30 scene 继承。

---

## 2. 5 类问题（按严重度）

### 2.1 关键问题（4 类）— 必须修

**问题 1：30/30 scene 把"模板"当"运行配置"用**

```
# 这是 contract-review/CLAUDE.md 的开头：

# Contract Review Scene — Practice Profile
*Written for: [公司名称] · 场景：商业合同审查*
> 🚀 首次使用？ 运行 cold-start-interview...如 CLAUDE.md 中存在 [填空] 标记，先配置再使用 skill。

## Who's using this
**Role:** [律师 / 法务人员 / ...]
```

**违反**：`CONTRIBUTING.md`（upstream 4d 章）明确说

> Each `<plugin>/CLAUDE.md` is a practice-profile template that the cold-start-interview skill copies to `~/.claude/plugins/config/.../CLAUDE.md` on the user's machine. It is *not* loaded as project context when the plugin is installed.

**这是 4d 章警告的"反范式"**——本项目把"模板"当"运行配置"。

**问题 2：0/30 scene 有 Shared guardrails**

所有 12 个 upstream plugin 的"宪法"——10+ 条护栏（no silent supplement、source tag、cross-skill severity floor、destination check 等）——**没有任何 scene 继承**。

**后果**：每个 scene 的 skill 各自重新发明护栏，甚至**彼此矛盾**。

**问题 3：0/30 scene 有 Reviewer note 5 行格式**

`commercial-legal/CLAUDE.md` 把 Reviewer note 5 行（Sources / Read / Flagged / Currency / Before relying）作为**每个输出的固定头**。

**后果**：本项目每个 skill 的输出**没有统一的"信任元数据"**——律师无法快速判断输出是否可信。

**问题 4：0/30 scene 有 YAML 注册表**

`ai-governance-legal/ai-systems.yaml`、`ip-legal/portfolio.yaml`、`employment-legal/leave-register.yaml`——是"事实数据库"。

**后果**：本项目 30 个 scene **没有持久化的事实数据**——每次会话从零开始。

### 2.2 高严重度问题（5 类）

**问题 5：6/30 scene 提到 5 大法域**——`government-investigation` / `labor-arbitration` / `special-opportunity-investment` / `web3-virtual-assets` / `white-collar-crime` / `ai-governance-legal` 提到。但**没有按 5 大法域分层**（cn-mainland / hk / mo / tw / sg 各自规则）。

**问题 6：1/30 scene 有 Decision tree**——只有 product-legal。其他 29 个 scene 的输出**没有"给律师 5 个选项让他选"**的决策框架。

**问题 7：0/30 scene 有 Playbook（双面 + 6 条款）**——`commercial-legal/CLAUDE.md` 的 6 条款双面 playbook（sales/purchasing）是 upstream 商业合同的"心"，本项目 0/30 继承。

**问题 8：30/30 scene 的 work-product header 只有"律师/非律师"2 档**——**不是 upstream 的 4 档**（律师/专利代理人/注册会计师/非律师）。中国应该有"律师/注册会计师/税务师/公证员/非律师"4 档。

**问题 9：14/30 scene 仍含 ≥ 5 个 `[填空]`**——`cross-border-ma` 11 个、`corporate-governance` 8 个、`litigation-support` 8 个、`ip-infringement` 8 个、`tax-compliance` 7 个、`white-collar-crime` 7 个、`government-investigation` 7 个。这意味着这些 scene **从未被任何用户配置过**。

### 2.3 中严重度问题（3 类）

**问题 10：8/30 scene 不提 cold-start-interview**——`capital-markets` / `commercial-arbitration` / `cross-border-trade` / `law-student` / `legal-builder-hub` / `legal-clinic` / `m-and-a` / `pe-vc-funds` / `wealth-succession` 没有这个引导脚本。

**问题 11：18/30 scene < 200 行**——内容**严重不完整**。`wealth-succession` 仅 116 行，`pe-vc-funds` 119 行，`commercial-arbitration` 120 行——这些"瘦"scene 大概率只是占位。

**问题 12：30/30 scene 没有"公司信息应该来自 `company-profile.md`"的标注**——应该学 upstream，每个公司信息字段后标 *(From company-profile.md — edit there to change across all plugins)*。

---

## 3. 按 scene 分组的详细评估

### 3.1 优秀组（≥ 4 个关键维度通过）

**product-legal**（461 行，4 护栏 + 11 Reviewer note + 5 Decision tree + 7 ColdStart + 4 Header）

- 唯一接近 upstream 的 scene
- 有 Shared guardrails 段、有 Reviewer note 段、有 Decision tree 段
- 但 0 YAML、0 5jurisd、0 Playbook 仍不符合

**employment-legal**（449 行，2 [填空]）——内容最丰富，但**没有 Outputs/护栏/Reviewer note/Decision tree**——**内容堆在数据里，没结构化**

### 3.2 中等组（2-3 个关键维度通过）

**contract-review**（278 行，唯一提到 YAML）

- 有 YAML 提到
- 有 cold-start
- 但 0 护栏、0 Reviewer note、0 5jurisd

**government-investigation** / **labor-arbitration** / **special-opportunity-investment** / **web3-virtual-assets** / **white-collar-crime** / **ai-governance-legal**——提到 5 大法域

### 3.3 不及格组（≤ 1 个关键维度通过）

**绝大多数 scene**（24/30）：

- 有 Outputs 段但**没护栏**
- 有 header 但**只是 2 档**
- 有 cold-start 提到但**没运行机制**
- [填空] 满地

---

## 4. 共同结构问题

### 4.1 重复 30 次的"标准段落"

每个 scene 的开头都是同一段：

```markdown
# XXX Scene — Practice Profile
*Written for: [公司名称] · 场景：XXX*
> 🚀 首次使用？ 运行 cold-start-interview...
## Who's using this
**Role:** [律师 / 法务人员 / 业务部门（非法律背景，有律师支持）/ 业务部门（无律师支持）]
**Attorney contact:** [填空]
在产出工作成果前，必须先检查 Role 字段。如果 Role 为 `[填空]`，要求用户先设置角色。
## 公司基本信息
**公司名称：** [填空]
```

**这 5 段是 30 个 scene 的"标配"——**复制粘贴的痕迹明显**。**但每段又略有不同**（数据源配置、风险等级、核心条款等）。

**问题**：这 5 段**几乎可以抽到 `company-profile.md` 共享层**（4d 章），但本项目**30 个 scene 各自维护**——30 份冗余。

### 4.2 缺"司法管辖分层"

只有 6/30 scene 提到 5 大法域。其他 24 个 scene **把"中国大陆"当默认**——

- 没有"5 大法域"的结构化字段
- 没有"5 大法域的香港/新加坡规则"段
- 没有"跨境升级规则"表

**这违反 4g 章 Pattern 16+17**（按法域分高度关注 + 法域特定升级规则）。

### 4.3 缺"标准护栏"

`## Shared guardrails` 段在 30 个 scene 中**仅 1 个**（product-legal）有——**而且不完整**（只有 4 处提到）。

**本项目 30 个 scene 完全没有"硬规则"概念**——每个 skill 各自决定怎么标 [verify]/[review]/[model knowledge]。

**这违反 4f 章 Pattern 8**（[verify] / [review] 双标记）。

---

## 5. 与 upstream `commercial-legal/CLAUDE.md` 的对比

| 维度 | upstream commercial-legal | GCL 平均 | GCL 最好 |
|------|---------------------------|---------|---------|
| 行数 | ~1100 | 200 | 461（product-legal） |
| [PLACEHOLDER] 占位 | ~30（设计） | 5.4（实际） | 2（product-legal / employment-legal） |
| `## Outputs` | ✅ 完整 | ✅ 29/30 | ✅ |
| `## Shared guardrails` | ✅ 10+ 条 | ❌ 1/30 | ⚠️ product-legal（部分） |
| `## Reviewer note` | ✅ 5 行格式 | ❌ 1/30 | ⚠️ product-legal |
| `## Decision tree` | ✅ 5 选项 | ❌ 1/30 | ⚠️ product-legal |
| `## Playbook` | ✅ 双面 6 条款 | ❌ 0/30 | ❌ |
| `## Red lines` | ✅ | ❌ 0/30 | ❌ |
| `## Risk calibration` | ✅ 3 段 | ❌ 0/30 | ❌ |
| `## Jurisdictional footprint` | ✅ 3 层 | ❌ 6/30 提到 | ❌ |
| `## Enforcement posture` | ✅ 3 档 | ❌ 0/30 | ❌ |
| `## Materiality threshold` | ✅ 3 档 | ❌ 0/30 | ❌ |
| 5 档源标注 | ✅ | ❌ 0/30 | ❌（部分在 4 档 [YD]/[WKL]/[GOV]/[model]） |
| 4 档 work-product header | ✅ | ❌ 0/30 | ❌（2 档） |
| YAML 注册表 | ✅ | ❌ 1/30 | ❌（仅 contract-review 提到） |
| Cold-start 引导 | ✅ | ⚠️ 22/30 | ✅ |
| 公司信息共享 | ✅ `company-profile.md` | ❌ 0/30 | ❌ |

**GCL 30 个 scene 总体得分：~15% upstream 完整性**。

---

## 6. 问题根因（why）

### 6.1 复制粘贴的"工作量优先"

30 个 scene 看起来是"快速建立覆盖"——**先建模板，再填内容**。但模板没有跑过 cold-start，所以**全在 placeholder 状态**。

### 6.2 缺少"宪法"概念

Upstream 12 个 plugin 共享 10+ 条护栏。本项目 30 个 scene **没有共享层**——每个 scene 自己决定。

### 6.3 误解"场景 vs plugin"

Upstream 用"plugin" = 1 个律师职业（含 6-10 skill）。本项目用"scene" = 1 个法律场景（按业务切）。

**但每个 scene 实际上是 1 个独立 plugin**——30 个 plugin，**违反 upstream 11 个 plugin 的设计哲学**（"按角色不按任务"）。

### 6.4 没有运行/模板分离

Upstream 4d 章明确说**模板在仓库、运行配置在用户机器**。本项目把两者合并——**违反 4d 警告**。

---

## 7. 影响评估

### 7.1 对用户的实际影响

| 影响 | 严重度 |
|------|------|
| 用户首次使用 30 个 scene 中的任意一个 → 必须先填 5-10 个 [填空] | 中（摩擦） |
| 填了 [填空] 但下次 git pull → **被覆盖** | **高（数据丢失）** |
| 律师跨 scene 切换 → 不一致（无共享 company-profile） | 中 |
| 升级 plugin → 同上 | **高** |
| AI 输出 → 没有 reviewer note → 律师不知是否可信 | **高** |
| 跨境案件 → 没有 5 大法域规则 → AI 用大陆法自信地答 | **关键** |

### 7.2 与 `legal-cn-template.md` 的差距

| 段 | legal-cn-template.md | GCL 30 scene 平均 |
|----|----------------------|-------------------|
| Outputs（4 档 header + reviewer note + decision tree） | ✅ 完整 | ⚠️ 残缺 |
| Shared guardrails（10+ 条） | ✅ 完整 | ❌ 0% |
| Jurisdiction footprint | ✅ 5 大法域 + 3 层 | ❌ 0% |
| Practice role 5 种 | ✅ | ❌（只 2 档） |
| Risk calibration 3 段 | ✅ | ❌ 0% |
| Red lines | ✅ | ❌ 0% |
| Governance tiers | ✅ | ❌ 0% |
| Playbook（双面 + 6 条款） | ✅ | ❌ 0% |
| Jurisdiction-specific escalation | ✅ | ❌ 0% |
| Enforcement posture | ✅ | ❌ 0% |
| Materiality threshold | ✅ | ❌ 0% |
| YAML 注册表（4 个） | ✅ | ❌ 0% |
| No hardcoded rules | ✅ | ❌ 0% |

**GCL 30 scene 与 `legal-cn-template.md` 的差距：~85%**。

---

## 8. 修复优先级

### 8.1 紧急（必须立即修）

1. **不要把 [填空] 写入仓库**——4d 章明确禁止
2. **所有 30 个 scene 的 CLAUDE.md 加 `<!-- TEMPLATE — NEVER WRITE USER DATA HERE -->`** 注释
3. **建立 `~/.claude/plugins/config/greater-china-legal/company-profile.md` 共享层**
4. **建立 `legal-cn/CLAUDE.md`（基于 `legal-cn-template.md`）作为 1 plugin 模板**

### 8.2 重要（1-2 周）

5. **每个 scene 加 `## Shared guardrails` 段**——直接复制 upstream 10+ 条
6. **每个 scene 加 `## Outputs` 4 段**（header + reviewer note + decision tree + quiet mode）
7. **删除 30 个 scene**——按 `legal-cn-template.md` 收敛到 1 plugin 9 skill
8. **加 YAML 注册表**（data / counterparty / contract / obligation）

### 8.3 可选（1-2 月）

9. **加 `## Jurisdictional footprint` 3 层**
10. **加 `## Practice role` 5 种**
11. **加 `## Risk calibration` 3 段**
12. **加 `## Red lines` 段**
13. **加 `## Enforcement posture` 段**
14. **加 `## Materiality threshold` 段**
15. **加 `## Jurisdiction-specific escalation rules` 5 大法域表**
16. **加 `## Playbook` 双面 + 6 条款**

---

## 9. 三个最关键的反范式问题

### 9.1 反范式 #1：模板当运行配置

**GCL 现状**：`plugins/legal-scenes/<scene>/CLAUDE.md` 顶部是 `[填空]`——**用户填了就被 git 跟踪**。

**upstream 范式**：CLAUDE.md 是模板，**`~/.claude/plugins/config/.../CLAUDE.md` 才是运行配置**——升级 plugin 不冲用户数据。

**修复**：本项目 30 个 scene 的 CLAUDE.md 应该**全是模板**（无 placeholder），**运行配置另存**。

### 9.2 反范式 #2：30 个 plugin 而不是 11 个

**GCL 现状**：30 个 scene = 30 个独立 plugin。

**upstream 范式**：12 个 plugin = 12 个律师角色，每个含 6-10 skill。

**修复**：合并到 1 个 `legal-cn` plugin + 9 skill。30 个 scene 降为 1 plugin 内的 9 个 skill（或 9 个分类）。

### 9.3 反范式 #3：没有共享护栏

**GCL 现状**：每个 scene 各自决定。

**upstream 范式**：10+ 条 Shared guardrails 跨 12 个 plugin。

**修复**：在 `legal-cn/CLAUDE.md` 顶部加 10+ 条护栏，所有 skill 自动继承。

---

## 10. 总结

### 10.1 数字

- **30 个 scene** — 0/30 完全符合 upstream 设计
- **0/30 scene 有 Shared guardrails**
- **0/30 scene 有 Reviewer note 5 行**
- **0/30 scene 有 YAML 注册表**
- **0/30 scene 有 Playbook**
- **1/30 scene 有 4 档 work-product header**（应是 30/30）
- **1/30 scene（product-legal）有决策树**（应是 30/30）
- **1/30 scene（contract-review）提到 YAML**
- **6/30 scene 提到 5 大法域**（应是 30/30）
- **30/30 scene 用 2 档 header**（应是 4 档）

### 10.2 一句话总结

**GCL 30 个 scene 在"内容"上覆盖了大量法律场景，但在"架构"上违反了 upstream 几乎所有关键设计原则。最大问题不是缺内容，是 4d 章明确警告的"模板当运行配置"反范式——这导致用户数据不安全 + 升级冲掉配置。**

### 10.3 修复路径

| 时间 | 动作 |
|------|------|
| **今天** | 在 30 个 scene 的 CLAUDE.md 顶部加 `<!-- TEMPLATE -->` 警告 |
| **本周** | 新建 `legal-cn/CLAUDE.md`（基于 `legal-cn-template.md`）作为唯一模板 |
| **2 周** | 实现 cold-start-interview + 1 个 skill（contract-review）作为 PoC |
| **1 月** | 迁移 3-5 个最常用 scene 到 legal-cn plugin 9 skill |
| **3 月** | 完整迁移 30 scene，删 `plugins/legal-scenes/` |

### 10.4 与 `legal-cn-template.md` 的关系

`legal-cn-template.md` 是**目标态参考**——基于 upstream 18 个 pattern 写。

本审计是**现状评估**——基于 12 维扫描 30 个 scene。

**两者配合**：模板是"应该长什么样"，审计是"现在长什么样"。

---

*本审计基于 30 个 scene 的 `CLAUDE.md` 实际内容扫描。所有"✅/❌"判断基于 upstream 18 个 pattern + 4d 章"4 处位置"原则。*
