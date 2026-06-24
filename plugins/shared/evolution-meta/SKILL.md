---
name: evolution-meta
description: >
  evolution 元学习可消费版——把 patterns.md 沉淀的"常见根因 + 修复模板"
  转成 Agent 可在 REFL 阶段主动加载的 skill 入口。
  本技能本身不产出新内容，是 patterns 的 agent-side 视图。
trigger_phrases:
  - 反思模板
  - 根因模式
  - 修复模式
  - evolution meta
  - patterns
last_reviewed: 2026-06
legal_frame: cn-mainland
version: 1.0.0
risk_level: low
---

# /evolution-meta — 反思模式知识库（Agent 视图）

## 用途

本技能是 `plugins/shared/evolution/SKILL.md` 定义的"元学习"环节的**可加载入口**。
当 Agent 进入 REFL 阶段时，调用本 skill 加载历史 patterns，提升归因效率。

**使用方式**：

```
1. Agent 收到 REFL 任务
2. 调用 skill_view(name="evolution-meta")
3. 读取本文件 + 加载场景级 patterns.md
4. 用 patterns 辅助生成 hypothesis
```

## 加载规则

调用本技能时，按以下顺序读取：

1. **本文件**（通用反射模式）
2. `plugins/legal-scenes/<当前场景>/evolution/meta/patterns.md`（场景专属模式）
3. `plugins/shared/evolution/meta/patterns.global.md`（如存在，全局模式）

## 通用反射模式（顶层）

> 这里的模式是历史经验沉淀，新模式会在 patterns.md 累积后回流到这里。

### M-001：trigger 词缺失

**症状**：skill 被正确调用但未引导到专项检查。

**检测方法**：
- 用户 query 含专业术语（如"违约金"），但 skill 输出无对应专项分析
- trigger_phrases 含该术语的同义词但缺核心词

**归因方向**：
- 假设 A：trigger_phrases 缺核心词 → 修 trigger_phrases
- 假设 B：SKILL.md 缺专项 step → 修 SKILL.md

**快速验证**：看 trigger_phrases 是否含用户 query 的核心术语。

**修复模板**：

```yaml
patch_type: content-add
target_section: trigger_phrases
diff_summary: |
  trigger_phrases 增加:
    - <核心词>
    - <同义词 1>
    - <口语化表述>
expected_impact: "+X% 漏检率下降"
```

### M-002：法条引用未引导

**症状**：输出有法律推理但缺具体法条引用，law_citation_accuracy 评估维度必挂。

**检测方法**：
- 输出含"应当""有权"等法律判断但无"民法典 XXX 条"具体引用
- 场景 CLAUDE.md 明确要求引用 [YD]/[WKL] 但 skill 输出未引

**归因方向**：
- 假设 A：SKILL.md 的相关 step 未 mention 数据源
- 假设 B：推理原子能力未调用 legal-norm-validity-check

**修复模板**：

```yaml
patch_type: content-add
target_section: <相关 step>
diff_summary: |
  在 step N 末尾增加：
  "本步骤须引用 [YD] 数据源验证法条有效性，至少引用 1 条具体法条（条号格式：XXX法第N条）"
```

### M-003：跨场景污染

**症状**：某场景的 patch 修复了本场景问题，但其他场景 smoke test 出现新失败。

**检测方法**：
- post_patch 阶段 smoke_test 失败
- 失败 case 与 patch 修改的 trigger 词/step 有交集

**归因方向**：
- 假设 A：trigger_phrases 改得太宽，污染其他场景
- 假设 B：法条引用添加导致其他场景误用

**修复模板**：

```yaml
patch_type: restructure
rationale: |
  当前 trigger 词太宽，需限定到本场景上下文
diff_summary: |
  trigger_phrases 增加场景限定词：
  - 原: "<关键词>"
  - 新: "<场景限定><关键词>"
```

### M-004：场景 CLAUDE.md 规则未传导

**症状**：场景 CLAUDE.md 含明确规则（如"违约金 > 130% 可调整"），但 SKILL.md 输出未应用该规则。

**检测方法**：
- CLAUDE.md 含阈值/规则关键词
- skill 输出未含该规则的应用痕迹

**归因方向**：
- 假设 A：SKILL.md 未引用 CLAUDE.md 规则
- 假设 B：规则在 CLAUDE.md 但 SKILL.md 不知情

**修复模板**：

```yaml
patch_type: content-add
target_section: <相关 step>
diff_summary: |
  增加引用:
  "依据场景 CLAUDE.md 规则：<规则内容>"
  并在 step 中显式应用该规则进行判断
```

### M-005：节标题命名漂移

**症状**：auto-test 期望 `## 风险分析` 但 SKILL.md 实际为 `## 风险评估` 或 `## 风险点`。

**检测方法**：
- has_section 检查失败
- 输出实际含相似内容但标题名不一致

**归因方向**：
- 单一根因：命名规范未统一

**修复模板**：

```yaml
patch_type: format-fix
diff_summary: |
  重命名: "<旧标题>" → "<新标题>"
  （遵循 auto-test 期望的标准节标题：## 工作流程 / ## 风险分析 / ## 输出格式）
```

## 调用本技能的 prompt 模板

```
[场景] <scene>
[失败 case 列表] [...]
[评估维度失败] [...]

请按以下步骤执行 REFL：
1. skill_view(name="evolution-meta") 加载本文件
2. 读取 plugins/legal-scenes/<scene>/evolution/meta/patterns.md
3. 比对失败模式与已有 patterns
4. 若有 high-confidence 模式匹配，优先作为 hypothesis
5. 生成 ≥2 个 hypothesis 并选择 root_cause
6. 输出 reflection 产物到 plugins/legal-scenes/<scene>/evolution/reflections/
```

## 本技能不做什么

- 不直接生成 proposal——那是 evolution 主技能的事
- 不执行测试——那是 auto-test 的事
- 不修改 patterns.md——patterns 的写入是 PATCH 阶段 merge 后的副作用

---

*Greater China Legal — shared evolution-meta v1.0.0*
