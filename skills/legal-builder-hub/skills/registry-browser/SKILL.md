---
name: registry-browser
description: >
  浏览Greater China Legal skill registry——按场景、标签、法律领域搜索可用skills。
  返回匹配skills的摘要、触发词、依赖关系，帮助用户找到所需skill。
  适用情形：用户说"有哪些合同审查的skill"、"查询劳动仲裁相关skill"、"找一个评估风险条款的工具"。
argument-hint: "[search-term | --scene=scene-name | --tag=tag | --list-scenes]"
legal_frame: cn-mainland
last_reviewed: 2026-06-13
version: 1.1.0
risk_level: low
---

# CN Legal Skill Registry Browser

## 搜索模式

**关键词搜索**

```
/registry-browser 合同审查
/registry-browser 赔偿计算
/registry-browser 诉讼时效
```

返回所有 description 或触发词中包含关键词的 skills，以相关度排序。

**场景浏览**

```
/registry-browser --scene=labor-arbitration
/registry-browser --scene=contract-review
/registry-browser --scene=ip-infringement
```

返回该场景下所有 skills。

**标签筛选**

```
/registry-browser --tag=risk-assessment
/registry-browser --tag=template
/registry-browser --tag=chinese-law
```

返回所有含该标签的 skills。

**列出所有场景**

```
/registry-browser --list-scenes
```

返回所有可用场景的列表。

## GCL Registry 完整场景

| 场景 | 中文名 | 包含 skills |
|---|---|---|
| `labor-arbitration` | 劳动仲裁 | dispute-classifier, compensation-calculator, evidence-collection, escalation-flagger, ... |
| `contract-review` | 合同审查 | nda-review, saas-msa-review, vendor-agreement-review, amendment-history, renewal-tracker, ... |
| `ip-infringement` | 知识产权侵权 | cease-desist, portfolio, risk-assessment, ... |
| `data-compliance` | 数据合规 | breach-notification, dpa-review, dsar-response, ... |
| `product-legal` | 产品法务 | launch-review, marketing-claim-review, feature-flag-review, ... |
| `regulatory-legal` | 监管合规 | reg-feed-watcher, gap-surfacer, policy-diff, ... |
| `corporate-governance` | 公司治理 | entity-compliance, board-minutes, ai-tool-handoff, ... |
| `legal-atomic` | 法律原子能力 | argument-strength-evaluation, norm-validity, element-extraction, ... |

## 返回格式

每个匹配 skill 返回：

```
## {skill-name}  [{scene}]  v{version}

{description 摘要}

**触发词**: {argument-hint}
**法律框架**: {legal_frame}
**风险等级**: {risk_level}
**数据源**: {source-tag}

[安装命令]
```

## 搜索结果排序

1. 关键词精确匹配 description > 触发词 > 标签
2. 场景内优先
3. 风险等级（高 > 中 > 低）
4. 版本号（高 > 低）

## 热门 Skills 推荐

当用户说"随便看看"或`--list-scenes`时，返回每个场景的 top skill：

| 场景 | Top Skill | 用途 |
|---|---|---|
| labor-arbitration | `dispute-classifier` | 劳动纠纷分类 |
| contract-review | `nda-review` | 合同审查 |
| ip-infringement | `cease-desist` | 侵权分析 |
| data-compliance | `dpa-review` | 数据保护评估 |
| legal-atomic | `argument-strength-evaluation` | 法律论证评估 |

---

*[YD] — Greater China Legal registry-browser v1.1.0*
