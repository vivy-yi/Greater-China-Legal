# GCL缺失能力补充分析

> 基于THUYRan/Legal-Skills-Chinese 8个核心skill的完整内容
> 对照GCL现有54个skills，识别真正需要补充的能力

---

## 一、GCL现状：54个skills解决"做什么"，不解决"怎么做"

GCL每个场景skill的核心逻辑是：
```
输入 → 判断树 → 输出结论
```

但THUYRan的skill还解决：
```
输入 → 怎么提取法律事实 → 怎么识别争议焦点 → 怎么三段论推理 → 怎么构建论证链 → 怎么验证法条效力 → 怎么检索类案
```

**差距不在于skill数量，在于认知链路的完整性。**

---

## 二、逐个skill分析：GCL现有skills缺什么

### Skill 1: `legal-element-extraction`（法律要素提取）

**THUYRan的核心内容：**
- 三层事实结构：原始叙述 → 法律相关事实 → 要件事实
- 九类事实单元：主体/行为/时间/地点/对象/结果/因果/主观/程序
- 事实属性四分法：客观事实/主观判断/法律评价/背景信息
- 生活语言→法律语言的转化对照表

**GCL现状：**
- 完全没有这个能力
- 各场景skill假设输入已经是结构化的法律事实
- 用户说"A欠我钱拖着不还"，没有任何skill能处理这个

**补充建议：**
```markdown
## legal-element-extraction
位置：新增为共享原子skill（被所有场景调用）

核心功能：
- 将用户乱糟糟的叙述拆解为最小事实单元
- 归类到九类事实（主体/行为/时间/地点/对象/结果/因果/主观/程序）
- 区分客观事实/主观判断/法律评价/背景信息
- 转化为法律语言（"拖着不还" → "履行期限届满后未履行"）
```

---

### Skill 2: `dispute-issue-identification`（争议焦点识别）

**THUYRan的核心内容：**
- 事实争议 vs 法律争议 的区分方法
- 三级争点分层：核心争点/次级争点/背景性分歧
- 争议焦点表述规范：客观/简洁/可裁判
- 各方主张的支持事由梳理

**GCL现状：**
- labor-arbitration的dispute-classifier做了部分，但粗糙
- contract-review的clause-analyzer做了部分，但没有独立
- 没有统一的争议焦点识别标准

**补充建议：**
```markdown
## dispute-issue-identification
位置：新增为共享原子skill

核心功能：
- 从法律事实中识别争议焦点
- 区分事实争议（当事人对事实本身有分歧）vs 法律争议（对法律评价有分歧）
- 三级分层：核心争点（直接影响裁判结果）/次级争点（影响责任范围）/背景性分歧
- 输出格式：争议焦点清单 + 各方主张 + 对应事实/法律问题
```

---

### Skill 3: `deductive-reasoning`（演绎推理/三段论）

**THUYRan的核心内容：**
```
大前提(P) + 小前提(F) → 结论(C)

直言三段论：所有X都是Y → a是X → a是Y
假言三段论：X→Y / X成立 → Y成立（肯定前件）
           X→Y / ¬Y → ¬X（否定后件，用于抗辩）
```

**GCL现状：**
- 各场景的"合法性判断"skill里隐含了三段论逻辑
- 但没有显式的P-F-C格式输出
- 没有中项识别和链接步骤

**补充建议：**
```markdown
## deductive-reasoning
位置：新增为共享原子skill

核心功能：
- 将法律推理规范化为P-F-C格式
- 识别中项（连接大小前提的桥梁概念）
- 区分肯定前件式/否定后件式（用于抗辩）
- 循环完善：直到逻辑闭环

输出格式：
| 步骤 | 内容 |
|---|---|
| 大前提(P) | [法条/规范] |
| 小前提(F) | [法律事实（对自然事实的定性）] |
| 中项(M) | [连接P和F的概念] |
| 结论(C) | [法律效果] |
```

---

### Skill 4: `evidence-evaluation`（证据评估）

**THUYRan的核心内容：**
- 证据三性：真实性/合法性/关联性
- 证明力评估：直接证据vs间接证据/传来证据vs原始证据
- 证明标准：民事(高度盖然性)/刑事(排除合理怀疑)/行政(明显优势)
- 非法证据排除规则

**GCL现状：**
- litigation-support的evidence-organizer只做组织，没有评估
- litigation-support的fee-calculator涉及诉讼费但不涉及证据
- 完全没有证据评估能力

**补充建议：**
```markdown
## evidence-evaluation
位置：litigation-support场景新增skill

核心功能：
- 评估证据三性（真实性/合法性/关联性）
- 评估证明力（强/中/弱）
- 判断证明标准是否满足（民事/刑事/行政）
- 识别需补强的证据缺口
- 标注非法证据排除风险

输出格式：
| 证据 | 三性评估 | 证明力 | 证明标准 | 风险 |
|---|---|---|---|---|
```

---

### Skill 5: `argument-chain-construction`（论证链构建）

**THUYRan的核心内容：**
- 完整论证链结构：主张→前提→支撑→反驳回应→结论
- 论证强度评估：强/中/弱/存疑
- 薄弱环节识别和标注
- 用于代理词/辩护词/法律意见书

**GCL现状：**
- 各场景skill输出里有论证，但没有统一的格式
- 没有论证强度评估
- 没有反驳预判

**补充建议：**
```markdown
## argument-chain-builder
位置：新增为共享原子skill（被litigation-support/contract-review等调用）

核心功能：
- 将P-F-C推理链转化为完整论证
- 评估论证强度（强/中/弱/存疑）
- 预判对方可能的反驳
- 识别论证链的薄弱环节
- 标注不确定性

输出格式：
### 论证链
1. [主张]：...
2. [支撑前提]：...
3. [反驳回应]：...（若对方反驳）
4. [结论]：...

### 论证强度：强/中/弱
### 薄弱环节：[标注]
```

---

### Skill 6: `conflict-resolution`（冲突解决/法条竞合）

**THUYRan的核心内容：**
- 三大冲突类型：法条竞合/证据矛盾/争点优先级
- 解决原则：上位法优于下位法/特别法优于一般法/新法优于旧法
- 请求权竞合处理：对比各请求权的构成要件/诉讼时效/赔偿范围
- 刑法竞合：想象竞合vs法条竞合

**GCL现状：**
- 完全没有这个能力
- references/里没有任何skill处理"两个法条打架听谁的"

**补充建议：**
```markdown
## conflict-resolution
位置：新增为共享原子skill

核心功能：
- 识别法条竞合：同一位阶一般法vs特别法/上下位法/新旧法
- 请求权竞合时对比各请求权的利弊
- 证据矛盾时适用证据优势原则
- 争点优先级排序

使用时机：
- 当legal-element-extraction识别出的法律评价存在多个法条依据时
- 当contract-review发现条款同时适用合同法和消费者保护法时
- 当compensation-calculator发现N+1和违法解除赔偿重叠时
```

---

### Skill 7: `case-retrieval`（类案检索）

**THUYRan的核心内容：**
- 检索三种类型：法律适用型/事实查明型/证据采信型
- 关键词提取：规范性关键词+非规范性关键词
- 类案检索四步：问题定性→信息收集→关键词提取→数据库检索
- 地域/时间/审级范围确定
- 效力分级：指导性案例/典型案例/普通案例

**GCL现状：**
- references/查询路径.md只有"去哪查"的路径
- 没有"怎么查关键词""怎么评估相似度""怎么判断效力层级"的方法论

**补充建议：**
```markdown
## case-retrieval
位置：references/目录下新增方法论文档

核心内容：
- 三种检索类型的关键词提取方法
- 检索范围确定（地域/时间/审级）
- 类案相似度评估标准
- 效力层级判断（指导性案例>典型案例>普通案例）
- 检索报告格式

注意：
- 本skill不直接调用案例库，只定义方法论
- 真实检索依赖MCP工具（北大法宝/元典）
- 未接入工具时标注[待检索]，不编造案例
```

---

### Skill 8: `legal-norm-validity-check`（法条效力核查）

**THUYRan的核心内容：**
- 三维效力检查：时间效力/层级效力/冲突检查
- 六种效力状态：现行有效/已修正/部分失效/已废止/已失效/尚未生效
- 效力溯源方法（必须来自真实数据源）
- 立法法相关条款作为依据

**GCL现状：**
- 完全没有这个能力
- 各场景引用法条时没有验证效力

**补充建议：**
```markdown
## legal-norm-validity-check
位置：新增为共享原子skill

核心功能：
- 验证法条是否现行有效
- 验证制定主体是否有权/层级是否正确
- 验证是否与上位法/同位法冲突
- 标注效力状态：✅ VALID / 🔄 AMENDED / ⚠️ PARTIAL / ❌ REPEALED

使用时机：
- 任何skill引用法条之前
- conflict-resolution发现可能存在法条冲突时

注意：
- 必须调用MCP工具或标注[待核实]
- 绝不凭记忆判断法条是否被修订
```

---

## 三、补充优先级

| 优先级 | Skill | 原因 | 工作量 |
|---|---|---|---|
| **P0** | `legal-element-extraction` | 基础设施，所有场景都需要 | 高 |
| **P0** | `deductive-reasoning` | 所有合法性判断都依赖三段论 | 中 |
| **P0** | `legal-norm-validity-check` | 极高风险，引用失效法条直接导致错误结论 | 低 |
| **P1** | `dispute-issue-identification` | 各场景争议焦点识别不统一 | 中 |
| **P1** | `evidence-evaluation` | litigation-support缺失证据评估 | 中 |
| **P2** | `conflict-resolution` | 处理法条打架，无此能力 | 中 |
| **P2** | `argument-chain-builder` | 各场景论证格式不统一 | 低 |
| **P3** | `case-retrieval` | 已有查询路径，缺方法论 | 低 |

---

## 四、补充后的GCL架构

```
Greater-China-Legal（补充后）：

Layer 3：场景应用层（现有9场景）
  labor-arbitration / contract-review / data-compliance / ...
  ↓ 调用
Layer 2：推理原子能力层（新增8个）
  legal-element-extraction    ← 新增P0
  deductive-reasoning         ← 新增P0
  legal-norm-validity-check   ← 新增P0
  dispute-issue-identification← 新增P1
  evidence-evaluation         ← 新增P1
  conflict-resolution         ← 新增P2
  argument-chain-builder      ← 新增P2
  case-retrieval              ← 新增P3
  ↓ 调用
Layer 1：知识配置层（现有LEGAL_FRAMES + references + MCP工具）
```

---

## 五、THUYRan skill质量评价

| 评价维度 | THUYRan | GCL现状对比 |
|---|---|---|
| **触发条件** | description中明确列出触发词+场景 | 只有argument-hint，触发条件不明确 |
| **能力边界** | description中显式"本技能不处理..." | 部分skill有，部分没有 |
| **工作流程** | 分阶段分步骤，有判断树 | 有但不规范 |
| **输入格式** | 明确两种输入格式 | 不统一 |
| **输出格式** | 有格式模板和示例 | 部分有，部分没有 |
| **理论依据** | 标注理论来源 | 无 |
| **免责声明** | 每个skill都有 | 无 |
| **置信度标注** | 有 | 无 |
| **幻觉处理** | 强制标注[待检索] | 无强制要求 |
