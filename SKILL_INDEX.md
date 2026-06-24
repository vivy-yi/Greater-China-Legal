# SKILL_INDEX — 律师使用指南

> 本文件是面向**律师 / 法务**的索引。告诉 Claude Code agent：
> "用户问什么时，我应该调哪些 skill"

---

## 1. 6 大能力（按业务场景）

### 合同审查

| 你可以问 | agent 自动跑 |
|---|---|
| "帮我审查这份合同" | contract-review 场景 → contract-clause-analysis → risk-clause-database → 输出审查意见 |
| "这个条款有问题吗" | contract-review → term-analyzer → risk-triage |
| "评估这个 MSA / NDA / 销售合同" | contract-review → saas-msa-review / nda-review / standard-sales-reviewer |
| "合同里有没有不公平条款" | contract-review → review → risk-clause-database |

### 法律研究 / 分析

| 你可以问 | agent 自动跑 |
|---|---|
| "分析这个法律问题" | legal-element-extraction → legal-article-retrieval → case-retrieval → deductive-reasoning → argument-strength-evaluation |
| "查某条法律的最新规定" | legal-article-retrieval → legal-norm-validity-check |
| "类似案例怎么判" | case-retrieval → analogical-reasoning → legal-judgment-prediction |
| "这个案件能赢吗" | legal-judgment-prediction → judicial-value-judgment |

### 文档生成 / 摘要

| 你可以问 | agent 自动跑 |
|---|---|
| "写一份判决书 / 备忘录" | legal-document-formatting → judgment-document-generation |
| "给这份文书做摘要" | legal-document-summarization → multi-document-summarization |
| "分类这份材料属于哪个法律领域" | legal-domain-taxonomy |

### 文件操作（脱敏 / 还原）

| 你可以问 | agent 自动跑 |
|---|---|
| "脱敏这份合同" | legal-document-redaction（自动加载 references/config.md 白黑名单） |
| "还原外审稿" | legal-document-restoration（要求脱敏稿 + 比对文件） |
| "生成可外发版本" | legal-document-redaction（带白名单配置） |

### 案件 / 流程管理

| 你可以问 | agent 自动跑 |
|---|---|
| "新建案件" | matter-workspace new |
| "列出我的案件" | matter-workspace list |
| "切换案件 X" | matter-workspace switch |
| "归档案件" | matter-workspace close |
| "这个案件的截止日是什么" | trial-scheduling-and-deadline-monitoring |
| "这个案件要花多少钱" | billing-and-litigation-budget |

### 合规 / 风险

| 你可以问 | agent 自动跑 |
|---|---|
| "这个产品合规吗" | data-compliance 场景 → medical-data-classification / privacy-policy-update |
| "这个法律风险大不大" | legal-risk-assessment → strategic-risk-prioritization |
| "内部合规有什么漏洞" | internal-compliance-risk-identification |
| "这个合同会不会有履约风险" | dispute-and-performance-risk |

---

## 2. 跨法域支持

agent 默认按 `cn-mainland` 处理。如果你问的是其他法域，按以下关键词触发：

| 法域 | 关键词 |
|---|---|
| `hk`（香港） | "香港"、"HK"、"普通法系"、"普通法" |
| `tw`（台湾） | "台湾"、"TW"、"民国" |
| `mo`（澳门） | "澳门"、"MO" |
| `sg`（新加坡） | "新加坡"、"SG" |
| `eu`（欧盟参考） | "欧盟"、"GDPR"、"跨境数据" |

agent 会按对应法域的合规框架审查。

---

## 3. 怎么和 agent 对话

### ✅ 推荐问法（明确意图）

```
"审查这份合同，重点看付款条款"
"分析这个借款合同纠纷的整体策略"
"脱敏这份判决书，保留双方律师名"
"研究一下跨境数据合规要求"
```

### ❌ 避免问法（太模糊）

```
"看看这个"（不知道要看什么）
"帮我处理一下"（不知道处理什么）
```

### 🟡 复杂任务（用模板）

复杂研究类问题，告诉 agent 用哪个模板：

```
"用合同纠纷分析模板研究这份材料"
"用跨境交易模板审查这个架构"
```

模板列表见 `plugins/legal-research-templates/`。

---

## 4. 常见任务完整流程示例

### 示例 1：合同审查 + 脱敏 + 入库

```
律师：审查这份合同，给出修改意见，然后脱敏生成可外发版

agent 自动跑：
1. contract-review 场景 → 输出审查意见
2. legal-document-redaction → 输出脱敏稿 + 比对文件
3. shared/matter-workspace new → 创建案件工作区
4. 把脱敏稿 + 审查意见存到 matters/<slug>/
```

### 示例 2：法律研究 → 写备忘录

```
律师：研究 A 公司 B 业务模式的合规风险，出一份备忘录

agent 自动跑：
1. legal-element-extraction → 提取法律事实
2. legal-article-retrieval → 查相关法规
3. case-retrieval → 找类似案例
4. legal-risk-assessment → 评估风险
5. multi-document-summarization → 综合摘要
6. legal-document-formatting → 出备忘录
```

### 示例 3：跨境数据合规审查

```
律师：审查这个 SaaS 产品的跨境数据传输合规性

agent 自动跑：
1. data-compliance 场景 → 进入
2. legal-element-extraction → 提取数据流
3. cn-judicial-rules → 查 PIPL / 数据出境
4. case-retrieval → 找 PIPL 案例
5. conflict-resolution → 跨法域冲突
6. legal-risk-assessment → 综合评估
```

---

## 5. 故障排查

| 问题 | 原因 | 解决 |
|---|---|---|
| agent 答非所问 | 没触发对的 skill | 明确说"用 X skill 处理" |
| agent 跳过脱敏 | 误以为是普通问答 | 说"先脱敏再答" |
| 案件数据混乱 | matter-workspace 没切换 | 先 `matter-workspace switch <slug>` |
| 跨法域结果错 | 默认 cn-mainland | 明确说"按 HK 法"或"按 GDPR" |

---

## 6. 安装与升级

详见 `CLAUDE.md` § "安装到 Claude Code"。
升级 skill 后，agent 自动 reload——无需重启。