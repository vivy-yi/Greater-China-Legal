# SKILL.md YAML Frontmatter Schema

## 目的

定义 Greater China Legal 项目中每个 SKILL.md 文件的 YAML frontmatter 规范。所有 Skill 文件必须遵循此 schema。

---

## 必需字段

```yaml
name: {skill-name} # Skill 名称（英文，kebab-case）
description: {description} # 简短描述（Agent 决定是否调用）
trigger_phrases:                      # 触发短语（数组）
  - /{domain}:{skill-name}
  - /{domain}:{skill-name} --frame {frame}
legal_frame: {cn-mainland|hk|mo|tw|sg}  # 法域标识
last_reviewed: YYYY-MM # 最后审查日期
version: 1.0.0                       # Skill 版本
user_invocable: true|false           # 是否可被用户直接调用
```

---

## 可选字段

```yaml
# 来源标注（法律引用）
legal_sources:
  - type: statute|case-law|regulation
    name: {法律名称}
    article: {条款编号}
    effective_date: YYYY-MM-DD
    jurisdiction: {cn-mainland|hk|mo|tw|sg}

# 分类标签
tags:
  - {tag1}
  - {tag2}

# 风险等级（用于中国大陆法域）
risk_level: low|medium|high

# 升级钩子（触发律师核实的条件）
escalation_triggers:
  - {条件描述}

# 输出格式
output_format: {format-name}

# 依赖的 Skill
depends_on:
  - {domain}/{skill-name}
```

---

## 法域标识（legal_frame）

| 值 | 法域 | 说明 |
|---|---|---|
| `cn-mainland` | 中国大陆 | 默认法域 |
| `hk` | 香港 | 普通法系 |
| `mo` | 澳门 | 大陆法系（葡萄牙遗产） |
| `tw` | 台湾 | 大陆法系 |
| `sg` | 新加坡 | 普通法系 |

---

## 示例

### 大陆版（默认）

```yaml
---
name: termination-review
description: Analyze employment termination documents for legal risks under PRC Labor Contract Law
trigger_phrases:
  - /employment-legal:termination-review
  - /employment-legal:termination-review --frame cn-mainland
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
user_invocable: true
legal_sources:
  - type: statute
    name: Labor Contract Law of the PRC
    article: Articles 36, 39, 40, 41, 42, 46, 47, 48, 87
    effective_date: 2012-07-01
    jurisdiction: cn-mainland
risk_level: high
escalation_triggers:
  - Involves protected groups under Article 42 (occupational disease, onsite injury, medically confirmed illness)
  - Mass layoff under Article 41 involving 20+ employees or 10%+ of workforce
  - Termination during medical treatment period under Article 42
---
```

### 香港版

```yaml
---
name: termination-review
description: Analyze employment termination documents for legal risks under Hong Kong Employment Ordinance
trigger_phrases:
  - /employment-legal:termination-review --frame hk
legal_frame: hk
last_reviewed: 2026-06
version: 1.0.0
user_invocable: true
legal_sources:
  - type: statute
    name: Employment Ordinance (Cap. 57)
    article: Sections 9, 10, 11, 12, 13, 14, 32K, 32L
    effective_date: 2023-06-30
    jurisdiction: hk
  - type: case-law
    name: Zhong Xiu v P & H Development Ltd
    article: [2017] 1 HKLRD 427
    effective_date: 2017
    jurisdiction: hk
risk_level: high
escalation_triggers:
  - Unlawful dismissal claims under Section 32K
  - Discrimination claims under Anti-discrimination Ordinances
  - Summary dismissal without proper cause
---
```

---

## 质量检查

每个 SKILL.md 提交前必须通过以下检查：

1. **法域标识**：必须包含 `legal_frame` 字段，且值在允许列表中
2. **时效标注**：所有法律引用必须包含 `effective_date`
3. **触发短语**：必须包含至少一个 trigger phrase
4. **禁止美版引用**：不得出现 UCC、FRCP、Delaware law、FIRREA 等美版法律术语

---

## 验证脚本

参见 `scripts/validate-skills.py`