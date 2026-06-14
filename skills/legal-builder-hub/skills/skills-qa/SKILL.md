---
name: skills-qa
description: >
  质量审查CN legal skill——检查frontmatter完整性、触发词质量、中文本地化、数据源标注。
  返回分数和改进建议，低于阈值拒绝安装。
  适用情形：安装前审查新skill、批量检查已有skills质量、定期质量审计。
argument-hint: "[skill-name | --all | --scene=scene-name]"
legal_frame: cn-mainland
last_reviewed: 2026-06-13
version: 1.1.0
risk_level: medium
---

# CN Legal Skill QA Framework

## 评分维度（满分100）

| 维度 | 分值 | 及格线 |
|---|---|---|
| frontmatter完整性 | 25 | 20 |
| 触发词质量 | 25 | 18 |
| 步骤可执行性 | 25 | 18 |
| 中文本地化 | 15 | 10 |
| 数据源标注 | 10 | 8 |

**总分 < 60 分：拒绝安装（返回改进建议）**
**总分 60-79 分：警告通过（建议改进）**
**总分 >= 80 分：通过**

## 逐项检查

### 1. frontmatter完整性（25分）

必需字段：name, description, argument-hint, legal_frame, version, risk_level

每缺失1个字段 -4分，最高扣25分。

### 2. 触发词质量（25分）

检查点：
- [ ] description 包含 `适用情形` 说明
- [ ] argument-hint 格式为 `[参数描述]`
- [ ] 触发词≥3个（中文逗号分隔或独立句子）
- [ ] 触发词覆盖主场景和常见变体

### 3. 步骤可执行性（25分）

检查点：
- [ ] 步骤编号连续（1→2→3）
- [ ] 每步有明确操作（做什么+怎么做）
- [ ] 无 US 残留引用（Ironclad/CLM/CourtListener/Slack等）
- [ ] 输出格式说明清晰

### 4. 中文本地化（15分）

- [ ] legal_frame 为 cn-mainland/hk/mo/sg/tw 时，description/mainmatter 为中文
- [ ] 英文术语有中文注释（如"CLM系统→合同管理系统"）
- [ ] 无英文语法错误导致的歧义

### 5. 数据源标注（10分）

- [ ] 存在 [YD]/[WKL]/[BD]/[GCL]/[model] 标注
- [ ] 脚注在文件底部，不在 frontmatter 内

## 输出格式

```
## {skill-name} QA Report

总分：{score}/100  [{pass/warn/fail}]

--- 详细评分 ---
frontmatter:   {score}/25  {missing_fields}
触发词质量:   {score}/25  {issues}
步骤可执行性: {score}/25  {issues}
中文本地化:   {score}/15  {issues}
数据源标注:   {score}/10  {issues}

--- 改进建议 ---
1. {建议1}
2. {建议2}
```

## 批量QA

```
/skills-qa --all      # 审查所有已安装 skills
/skills-qa --scene=labor-arbitration  # 审查某场景全部 skills
```

批量输出汇总表：

```
Skill                    Score  Status   Critical Issues
dispute-classifier        88    PASS
compensation-calculator    72    WARN    缺[YD]标注
nda-review                55    FAIL    英文内容未本地化
```

---

*[YD] — Greater China Legal skills-qa v1.1.0*
