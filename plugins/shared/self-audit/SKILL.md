---
name: self-audit
description: >
  自动 QA 循环——遍历全部场景和 skill，检查内容完整性、
  路径有效性、frontmatter 合规、内容深度。可修复的自动修复，
  不可修复的记录到审计日志。适合定时运行（每周）。
trigger_phrases:
  - 质量检查
  - 自动审计
  - self audit
  - 检查所有skill
last_reviewed: 2026-06
version: 1.0.0
risk_level: low
---

# /self-audit — 自动质量审计

## 审计范围

扫描 `plugins/scenes/` 下全部场景和 `plugins/legal-atomic/` 下的全部原子 skill。

## 工作流程

### Phase 1：结构检查（无 LLM，纯规则）

逐文件检查以下指标，记录到 `_audit-log.yaml`：

| 检查项 | 方法 | 自动修复 |
|--------|------|---------|
| frontmatter 完整性 | name/description/legal_frame/version 是否存在 | ❌ 标记，不自动修复 |
| trigger_phrases 存在 | 数组非空 | ❌ 标记 |
| legal_sources 有 effective_date | 逐条检查 | ❌ 标记 |
| 文件大小 > 500b | wc -c | ❌ 标记 |
| body 含 ## 工作流程 或 ## 核心分析 | grep 存在 | ❌ 标记 |
| 无美版法律术语 | grep UCC/FRCP/Delaware 等 | ❌ 标记 |
| ../../CLAUDE.md 可解析 | test -f 检查 | ✅ 如路径错误，自动修正 |
| references/ 文件存在 | test -f 检查 | ❌ 标记 |

### Phase 2：内容深度评估（需 LLM，对每个 skill）

对每个 body < 2000b 的 SKILL.md，读取内容并评估：

```
评估维度：
- 是否有实质性法律分析（非仅标题）
- 是否包含可操作的工作流步骤
- 是否引用具体法条
- 论证链路是否完整

输出：PASS / WARN / FAIL
```

### Phase 3：修复

仅执行自动修复项（路径修正）。其余标记到审计日志。

### Phase 4：输出报告

```
📋 Self-Audit 报告 — [日期]

场景覆盖：[N]/31 ✅

结构问题：
- frontmatter 缺失：[N] 个文件
- trigger_phrases 缺失：[N] 个文件
- body 过小（<500b）：[N] 个文件
- body 空心（仅标题）：[N] 个文件
- 美版术语：[N] 个文件
- 路径错误：[N] → 已自动修复 [M] 个

内容质量（LLM 评估）：
- PASS：[N]
- WARN：[N]
- FAIL：[N]

详细列表：
[逐文件清单]
```

## 审计日志

每次运行结果追加到 `_audit-log.yaml`：

```yaml
- run_at: 2026-06-15
  scenes_checked: 31
  files_checked: 475
  auto_fixed: 3
  issues:
    - file: plugins/scenes/xxx/skills/yyy/SKILL.md
      severity: warn
      issue: body_too_small
      detail: "仅43行，含frontmatter后正文不足100字"
    - file: plugins/scenes/xxx/skills/zzz/SKILL.md
      severity: error
      issue: missing_legal_frame
      detail: "legal_frame: cn-mainland 字段缺失"
```

## 本技能不做什么

- 不修改 SKILL.md 的内容逻辑——只修复路径。
- 不执行 AI 驱动的功能测试（仅内容质量评估）。
- 不自动触发 cold-start——cold-start 仍由用户手动运行。

---

*Greater China Legal — shared self-audit v1.0.0*
