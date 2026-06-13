---
name: related-skills-surfacer
description: >
  基于当前skill推荐相关skills——分析skill的主题、场景、触发词，
  从registry找出相关的skills。帮助用户发现可能不知道存在的工具。
  适用情形：用户说"有没有类似的"、"这个还能做什么"、"补充工具"。
argument-hint: "[current-skill-name] [--limit=5]"
legal_frame: cn-mainland
last_reviewed: 2026-06-13
version: 1.1.0
risk_level: low
---

# Related Skills Surfacer

## 推荐算法

基于4个信号加权打分：

| 信号 | 权重 | 说明 |
|---|---|---|
| 场景重叠 | 40% | 同一 scene/ 目录下的 skills |
| 触发词相似 | 30% | argument-hint 中的关键词重叠 |
| 标签重叠 | 20% | frontmatter 标签（risk_level/legal_frame） |
| 依赖关系 | 10% | manifest 中记录的依赖 skills |

## 推荐逻辑

```
输入: dispute-classifier

1. 找到 dispute-classifier 的 scene = labor-arbitration
2. 列出同 scene 下的所有其他 skills
3. 计算与 dispute-classifier 的相似度得分
4. 返回 top N（默认5个），按得分排序
```

## 输出格式

```
## dispute-classifier 相关 skills

### 同场景推荐（labor-arbitration）
1. **compensation-calculator**  [score: 0.72]
   共享场景：劳动仲裁
   互补用途：计算赔偿金额，disputeclassifier定类后接着算钱
   触发词重叠：劳动争议, 赔偿, 计算
   → 安装: /skill-installer compensation-calculator

2. **escalation-flagger**  [score: 0.61]
   共享场景：劳动仲裁
   互补用途：判断是否需要升级，disputeclassifier评估风险后escalation-flag判断升级路径
   触发词重叠：风险, 升级
   → 安装: /skill-installer escalation-flagger

### 跨场景相关（常见组合）
3. **nda-review**  [score: 0.43]
   互补场景：合同审查
   推荐原因：劳动纠纷常涉及竞业限制/保密协议，nda-review是合同审查入口
   → 安装: /skill-installer nda-review

### 你可能不知道的原子能力
4. **argument-strength-evaluation**  [score: 0.35]
   底层工具：法律论证评估
   推荐原因：disputeclassifier的分类结果可以作为argument-strength的输入
   → 安装: /skill-installer argument-strength-evaluation
```

## --limit 参数

```
/related-skills-surfacer dispute-classifier --limit=3
```

限制返回数量。

## 场景链路推荐

部分skills天然形成链路，推荐时一并说明：

| 起点 | → 常用链路 | 说明 |
|---|---|---|
| dispute-classifier | → compensation-calculator | 分类→计算 |
| nda-review | → risk-clause-database | 审查→风险提取 |
| breach-notification | → dpa-review | 发现泄露→评估义务 |
| entity-compliance | → ai-tool-handoff | 治理→AI合规 |
| reg-feed-watcher | → gap-surfacer | 监控→缺口跟踪 |

---

*[YD] — Greater China Legal related-skills-surfacer v1.1.0*
