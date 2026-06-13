# Greater China Legal vs. Legal-Skills-Chinese 对比分析

> 分析日期：2026-06-12
> THUYRan/Legal-Skills-Chinese：https://github.com/THUYRan/Legal-Skills-Chinese（248 stars，36 forks）
> vivy-yi/Greater-China-Legal：https://github.com/vivy-yi/Greater-China-Legal

---

## 一、项目定位对比

| 维度 | Greater-China-Legal (GCL) | Legal-Skills-Chinese (THUYRan) |
|---|---|---|
| **核心定位** | 场景优先：法律场景的端到端覆盖 | 能力优先：法律推理能力的原子化拆分 |
| **设计哲学** | 从业务场景出发，反推所需skill | 从认知链路出发，组合最小推理单元 |
| **覆盖范围** | 大中华区（大陆/港/澳/台/新）+ B-phase 9场景54skills | 中国大陆单一法域，38个推理能力 |
| **法域覆盖** | 多法域（cn-mainland/hk/tw/mo/sg） | 仅cn-mainland |
| **复用关系** | A-phase 152个skills + B-phase 54个skills | 36原子 + 2复合，无场景层 |
| **目标用户** | B端AI采访工具 + Agent平台 | 法律从业人员的AI辅助工具 |
| **License** | MIT（fork自Anthropic官方） | CC BY-NC-ND 4.0（不可商业修改） |

---

## 二、架构设计对比

### GCL：场景优先架构

```
三层结构（场景 → 判断树 → 工具）：
┌─────────────────────────────────────────┐
│  CLAUDE.md（运行时配置层）               │
│  法域足迹/数据源/置信度规则/输出格式     │
├─────────────────────────────────────────┤
│  Scene SKILL.md（场景入口）              │
│  场景判断树/业务主流程                   │
├─────────────────────────────────────────┤
│  skills/（原子级业务能力）               │
│  6个核心skill，每个只做场景特定的事       │
├─────────────────────────────────────────┤
│  references/（知识层）                  │
│  查询路径.md / 判断框架.md / 数据源清单   │
└─────────────────────────────────────────┘

9个场景 × 6 skills = 54个场景skill
+ 152个A-phase通用skills（按业务域组织）
+ 5个法域基准文档（LEGAL_FRAMES/）
```

**特点：** 场景封闭、端到端，每个场景可以独立解决一个业务问题。
**局限：** 各场景间有推理逻辑重复（如要素提取、论证链构建在每个skill里都重写了一遍）。

### THUYRan：能力优先架构

```
三层结构（输入 → 处理 → 输出）：
┌─────────────────────────────────────────┐
│  检索 → 推理 → 论证 → 文书               │
│  完整认知链路，无场景概念                │
├─────────────────────────────────────────┤
│  36个原子能力（每个只做一件事）          │
│  2个复合能力（编排原子能力）             │
└─────────────────────────────────────────┘

7个类别：
01 信息检索（5）：case-retrieval / legal-article-retrieval / other-legal-retrieval / legal-norm-validity-check / legal-concept-comprehension
02 事实处理（4）：legal-element-extraction / structured-element-extraction / dispute-issue-identification / evidence-evaluation
03 法律解释（4）：systematic-interpretation / teleological-interpretation / normative-meaning-argumentation
04 法律推理（7）：deductive-reasoning / inductive-reasoning / analogical-reasoning / legal-abductive-reasoning / counterfactual-reasoning / formal-legal-consequence / conflict-resolution
05 论证评估（4）：argument-chain-construction / argument-strength-evaluation / evidence-argument-chain / strategic-risk-prioritization
06 风险判断（6）：dispute-and-performance-risk / internal-compliance-risk-identification / legal-risk-assessment / judicial-value-judgment / administrative-value-judgment / legal-judgment-prediction ✦
07 文书管理（8）：legal-document-formatting / judgment-document-generation ✦ / legal-document-summarization / multi-document-summarization / legal-terminology / case-lifecycle-planning / trial-scheduling-and-deadline-monitoring / billing-and-litigation-budget
```

**特点：** 能力高度复用，组合灵活，每个skill符合"单一职责"。
**局限：** 没有场景概念，复杂任务需要自己组合多个原子能力，对非法律背景用户不友好。

### 架构互补性分析

```
GCL的优势（场景优先）          THUYRan的优势（能力优先）
────────────────────────────  ────────────────────────────
✅ 场景端到端完整              ✅ 推理链路专业完整
✅ 法域多地区覆盖              ✅ 论证质量高（有理论依据）
✅ 有运行时配置层              ✅ 能力可组合复用
✅ 输出格式统一                ✅ 有自我评估机制（argument-strength-evaluation）
❌ 推理逻辑重复                ❌ 无场景概念，对用户不友好
❌ 原子能力薄弱                ❌ 无法务地区差异处理
❌ 论证链构建能力弱            ❌ 无MCP工具规范（虽然文档写得好）
```

---

## 三、技能粒度对比

### 粒度层级对照

| 粒度层级 | GCL | THUYRan |
|---|---|---|
| **场景/复合** | 9场景（labor-arbitration等） | 2个（judgment-doc-gen/legal-judgment-prediction） |
| **业务skill** | 54个（6/场景） | 无 |
| **推理skill** | 无（散落在各场景内） | 36个原子 |
| **工具skill** | 152个A-phase通用 | 无（只有检索类） |

### 等价映射（GCL场景 → THUYRan能力）

| GCL场景 | GCL内含的推理能力 | 对应THUYRan原子能力 |
|---|---|---|
| labor-arbitration | 争议分类/要素提取/合法性判断 | dispute-issue-identification / legal-element-extraction / deductive-reasoning |
| contract-review | 条款分析/风险评估 | dispute-and-performance-risk / legal-document-formatting |
| ip-infringement | 侵权检测/损害赔偿计算 | legal-element-extraction / formal-legal-consequence |
| tax-compliance | 税种判断/发票合规 | structured-element-extraction / legal-risk-assessment |
| litigation-support | 策略制定/证据组织/文书生成 | argument-chain-construction / evidence-evaluation / judgment-document-generation |
| corporate-governance | VIE风险/ODI合规 | internal-compliance-risk-identification / legal-risk-assessment |

**结论：** GCL的每个场景skill里其实都在重复做THUYRan定义的那些推理能力，只是没有显式抽出来。

---

## 四、质量标准对比

### THUYRan的质量保障

| 维度 | 内容 |
|---|---|
| **手写验证** | 全部由执业法律专业人员逐一手写并验证 |
| **触发条件** | 每个skill的description必须包含触发条件 + 能力边界 |
| **理论依据** | 每个类别都标注了理论依据（如演绎推理的Westlaw/Lex Machina，风险评估的Dung论辩框架） |
| **能力边界** | description中必须显式标注"本技能不处理什么" |
| **免责声明** | 覆盖README每个页面，输出须经执业律师审阅 |
| **法域限制** | 明确"类比推理在刑法/税法领域受严格限制" |
| **幻觉处理** | 未接入DB时须标注`[待检索]`，绝不编造 |
| **评审流程** | PR须经法律背景评审者核查三个维度 |

### GCL的质量现状

| 维度 | 现状 |
|---|---|
| **手写验证** | 部分skill有法律内容，非全部经执业人员验证 |
| **触发条件** | frontmatter的description中有argument-hint，但触发条件不统一 |
| **理论依据** | 无标注 |
| **能力边界** | 各skill边界不清晰，有重叠 |
| **免责声明** | README中有，无skill级免责声明 |
| **法域限制** | CLAUDE.md中有法域足迹概念，但skill正文未限制推理方法 |
| **幻觉处理** | references/查询路径.md有数据源，但skill未强制标注 |
| **评审流程** | 无正式评审机制 |

---

## 五、知识组织对比

### THUYRan的知识组织

```
知识链：检索(输入) → 要素提取 → 争议识别 → 法律解释 → 演绎/归纳/类比推理 → 论证构建 → 文书输出

配套知识文件：
- MCP-PKULAW.md：北大法宝MCP的完整接入规范（含SERVICE_ID/CLI命令/数据规模/10+服务分类）
- 每个检索类skill下有独立README说明如何对接MCP
- assets/：SVG标签用于README可视化
- 理论依据标注在每个类别header下
```

### GCL的知识组织

```
知识链：场景判断 → 场景内skill → 读取CLAUDE.md获取配置 → references/查询路径

配套知识文件：
- LEGAL_FRAMES/：5个法域基准文档（cn-mainland/hk/tw/mo/sg）
- references/查询路径.md：各场景有独立的查询路径（内容有重复）
- SKILL_MD_SCHEMA.md：YAML frontmatter规范
- UPSTREAM_TRACKING.md：上游同步追踪
- scripts/validate-skills.py：格式校验脚本
```

---

## 六、MCP工具集成对比

| 维度 | THUYRan | GCL |
|---|---|---|
| **MCP文档质量** | 极详细：SERVICE_ID/CLI命令/数据规模/10+服务/配置示例 | 仅有`[YD]`/`[GOV]`标注，无实际工具定义 |
| **工具绑定** | skill只定义方法论，不绑定数据库 | skill使用标注引用数据源，但无调用规范 |
| **CLI方案** | 有npm包`@pkulaw/mcp-cli`，可批量查询零LLM消耗 | 无CLI工具方案 |
| **幻觉处理** | 未接入时须标注`[待检索]` | references有路径但未强制 |
| **Token管理** | 明确"只配置在本地客户端，切勿写进SKILL.md" | 无明确规范 |

---

## 七、融合方案

### 方案设计：GCL三层 + THUYRan原子能力注入

```
Greater-China-Legal（四层架构）：
┌─────────────────────────────────────────────────────┐
│ Layer 4：场景应用层（现有9场景 × 6 skills）           │
│  labor-arbitration / contract-review / ip-infringement │
├─────────────────────────────────────────────────────┤
│ Layer 3：业务skill层（现有54个，精简后）              │
│  每个skill只保留场景特定逻辑，调用Layer 2              │
├─────────────────────────────────────────────────────┤
│ Layer 2：推理原子能力层（NEW，借鉴THUYRan）           │
│  legal-element-extraction / deductive-reasoning       │
│  dispute-issue-identification / argument-chain-builder │
│  evidence-evaluation / formal-legal-consequence        │
│  legal-document-formatting / case-retrieval            │
├─────────────────────────────────────────────────────┤
│ Layer 1：知识配置层（现有LEGAL_FRAMES + references）  │
│  5法域基准 + 场景查询路径 + MCP工具规范（NEW）        │
└─────────────────────────────────────────────────────┘
```

### 具体融合措施

#### 措施1：新增legal-atomic/目录

从THUYRan借鉴的6个核心原子能力：

| 原子能力 | 来源 | 作用 | 在GCL哪里重复了 |
|---|---|---|---|
| `legal-element-extraction` | THUYRan | 从非结构化文本提取法律事实/构成要件 | 劳动仲裁(6个)/合同(4个)/IP(6个) 都在做 |
| `deductive-reasoning` | THUYRan | 三段论P-F-C演绎推理 | termination-legality/compensation-calculator等 |
| `dispute-issue-identification` | THUYRan | 识别争议焦点 | 多个skill的"争议判断"步骤 |
| `argument-chain-builder` | THUYRan | 构建完整论证链 | 所有skill的"输出论证"部分 |
| `evidence-evaluation` | THUYRan | 证据三性+证明力评估 | litigation-support的evidence-organizer |
| `formal-legal-consequence` | THUYRan | 从规范+事实推导具体法律后果 | damage-calculator/compensation-calculator |

#### 措施2：Skill精简

每个场景skill精简为：
```
## 加载上下文
读取 ../CLAUDE.md + ../legal-atomic/dispute-issue-identification

## 场景特定判断树
[场景特有的判断逻辑，不重复原子能力]

## 原子能力调用
- 调用 ../legal-atomic/legal-element-extraction → 获取要素清单
- 调用 ../legal-atomic/deductive-reasoning → 获取P-F-C链
- 调用 ../legal-atomic/argument-chain-builder → 生成论证链
```

#### 措施3：MCP工具规范升级

参考THUYRan的MCP-PKULAW.md，写`legal-atomic/references/MCP-TOOLS.md`：

```markdown
# 法律数据MCP工具规范

## 北大法宝MCP（Primary）

### CLI批量查询（零LLM消耗）
```bash
npm install -g @pkulaw/mcp-cli
pkulaw-mcp init --authorization "Bearer YOUR_TOKEN"

# 法规语义检索
pkulaw-mcp law-semantic search_article "劳动合同解除 经济补偿"

# 案例语义检索
pkulaw-mcp case-semantic search_case "竞业限制 违约金"

# 法条溯源（核查法条有效性）
pkulaw-mcp law-article trace "劳动合同法第38条"
```

### MCP协议接入（对话式）
```json
{
  "mcpServers": {
    "pkulaw-law-semantic": {
      "url": "https://apim-gw.pkulaw.com/{SERVICE_ID}/mcp",
      "headers": { "Authorization": "Bearer YOUR_TOKEN" }
    }
  }
}
```

## 元典开放平台MCP（Secondary）

[同格式写出]
```

#### 措施4：免责声明标准化

每个skill的footer统一加上：

```
---

⚠️ **法律声明**：本skill输出为供执业法律专业人员审阅的草稿，不构成法律意见，不可替代律师判断。AI生成内容可能存在偏差或遗漏，最终结论须由具备执业资格的法律专业人员作出。
```

#### 措施5：Skill评审机制

参考THUYRan的CONTRIBUTING.md，在`docs/`下新增`CONTRIBUTING-SKILL.md`：

```markdown
## SKILL.md 质量标准

### 必填项
1. YAML frontmatter：`name`/`description`/`argument-hint`/`legal_frame`/`risk_level`
2. `description`必须包含：触发条件 + 适用情形 + 能力边界（"本技能不处理..."）
3. 工作流程：分步骤，含判断树或决策逻辑
4. 输出格式：明确的格式化输出示例

### 推荐项
5. 理论依据：引用法条/司法解释/学理
6. 置信度规则：标注不确定时的处理方式
7. 常见错误：列举容易搞错的地方

### 评审清单
- [ ] 触发条件是否明确（非模糊描述）
- [ ] 能力边界是否清晰（无越界承诺）
- [ ] 判断树是否有穷尽（边界情况是否覆盖）
- [ ] 法条引用是否标注时效（"截至2026年X月现行有效"）
- [ ] 输出格式是否可直接使用（不是泛泛而谈）
- [ ] 是否有幻觉风险标注（数据源是否[MCP待接]）
```

---

## 八、融合优先级

| 优先级 | 措施 | 工作量 | 价值 |
|---|---|---|---|
| **P0** | 新增legal-atomic/目录（6个原子能力） | 中 | 解决skill重复，提升推理质量 |
| **P0** | 升级MCP-TOOLS.md | 低 | 让数据源从标注变成可用工具 |
| **P1** | 精简9场景54个skills，调用Layer 2 | 高 | 架构清晰，长期可维护 |
| **P1** | Skill级免责声明 | 低 | 降低法律风险 |
| **P2** | 新增CONTRIBUTING-SKILL.md评审规范 | 低 | 建立质量门槛 |
| **P2** | THUYRan的`legal-terminology`技能 | 低 | 统一术语规范 |
| **P3** | 引用THUYRan的`argument-strength-evaluation` | 低 | 输出质量自检 |

---

## 九、结论与建议

### 核心结论

1. **两者是互补关系，不是竞争关系**
   - THUYRan = 推理能力层（How，法律问题怎么推理）
   - GCL = 场景应用层（What，在什么场景解决什么问题）
   - 两者组合才完整

2. **GCL最需要补的短板**
   - Layer 2推理原子能力（目前skill里重复写了很多，但质量不如THUYRan）
   - MCP工具规范（目前只有标注，没有实际可用的工具定义）
   - Skill质量标准（缺乏THUYRan那种"手写+执业律师验证"的机制）

3. **THUYRan的局限GCL可以填补**
   - THUYRan无法处理多法域（大中华区）
   - THUYRan无法处理端到端场景（只有原子能力）
   - THUYRan无B端产品化方案

### 建议路径

```
Phase 1（立即可做）：补Layer 2
- 新增 legal-atomic/ 目录，6个核心原子能力
- 升级 MCP-TOOLS.md

Phase 2（下一迭代）：质量提升
- 各skill精简 + 统一footer免责声明
- 新增 CONTRIBUTING-SKILL.md

Phase 3（长期）：生态建设
- 建立skill评审机制
- 与THUYRan社区合作（标注来源而非fork）
```
