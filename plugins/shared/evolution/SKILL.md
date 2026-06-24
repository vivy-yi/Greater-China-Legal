---
name: evolution
description: >
  法律 skill 自主学习进化机制——在 auto-test（执行+评估）之上，
  接管"反思归因 → patch 提案 → 人机协作 gate → 回归验证"
  四个认知层环节，形成完整闭环。本技能定义闭环的契约、产物 schema、
  gate 策略、版本化规则与跨场景元学习沉淀。
trigger_phrases:
  - skill 进化
  - 自主学习
  - 自改进
  - 反思
  - skill 优化
  - 闭环修复
  - evolution
  - self-evolving

# ============================================================
# Auto-trigger definitions (per loop-to-harness §9)
# Without these, evolution is design doc only — never auto-attached.
# Thresholds in plugins/shared/evolution/config.yaml under `triggers:`.
# ============================================================
triggers:
  auto:
    - event: auto_test_failure_rate_exceeded
      conditions:
        metric: "eval_dim_failure_rate"
        operator: ">="
        threshold_ref: "triggers.failure_rate_threshold"  # 0.30 in config.yaml
      action: attach_skill
      payload: "REFL phase: load meta/patterns.md + generate reflection"

    - event: auto_test_consecutive_failures
      conditions:
        metric: "consecutive_fail_count"
        operator: ">="
        threshold_ref: "triggers.consecutive_failures"  # 3 in config.yaml
      action: attach_skill

    - event: legal_source_failure_detected
      conditions:
        patch_type: "legal-source-*"
        result: "FAIL"
      action: attach_skill
      payload: "High-risk failure — REFL is mandatory"

    - event: self_audit_phase2_failures_accumulated
      conditions:
        metric: "phase2_fail_count"
        operator: ">="
        threshold_ref: "triggers.self_audit_phase2_fail_threshold"  # 5
      action: suggest_skill
      payload: "Systemic content quality issue — recommend evolution upgrade"

  manual:
    - pattern: "反思|skill 进化|自改进|自优化|闭环修复"
      action: attach_skill
    - pattern: "evolution run|跑一次 evolution"
      action: attach_skill

  integration:
    cron: "0 2 * * *"  # daily 02:00 — auto-test results from previous day
    state_machine:
      - phase: "auto_test_complete"
        condition: "failure_rate >= triggers.failure_rate_threshold"
        action: "attach evolution"
      - phase: "self_audit_complete"
        condition: "phase2_fails >= triggers.self_audit_phase2_fail_threshold"
        action: "suggest evolution"
    delegate: false  # REFL/PATCH must run in main session for context coherence

# Strategy layer is externalized — see config.yaml
strategy_config: plugins/shared/evolution/config.yaml

last_reviewed: 2026-06
legal_frame: cn-mainland
version: 1.1.0
risk_level: medium
---

# /evolution — 法律 Skill 自主学习进化机制

## 设计原则

1. **不替代律师**：所有涉及法条/法律逻辑的 patch 必须经过人审 sign-off。
2. **不脱离 A/B 独立运行**：本机制消费 auto-test 的失败明细（EVAL 阶段产物），但本身不重新执行测试——执行归 auto-test，进化归本技能。
3. **可降级**：人工 review 可随时介入任意阶段；agent 跑挂的环节不阻塞整体流水线。
4. **可追溯**：每个 patch 必须可回滚、可归因到具体失败 case。
5. **跨场景可复用**：机制本身与具体场景解耦——任何 `plugins/legal-scenes/<scene>/` 都可挂载。

## 与其他 shared skill 的关系

```
┌────────────────────────────────────────────────────────┐
│ cold-start-interview                                    │
│   → 提供 Role/法域/公司信息等运行时配置                  │
│     ↓                                                    │
│ self-audit (Phase 1 结构 + Phase 2 内容深度)             │
│   → 输出结构性问题清单 + 内容质量评分                    │
│     ↓                                                    │
│ auto-test (RUN + EVAL 阶段)                              │
│   → 输出每个 case 的 PASS/FAIL/FAIL_detail              │
│     ↓                                                    │
│ ★ evolution (本技能：REFL + PATCH + 回归) ★             │
│   → 反思归因 → patch 提案 → gate → 回归                 │
│     ↓                                                    │
│ SKILL.md 版本化提交                                      │
└────────────────────────────────────────────────────────┘
```

**关键边界**：
- auto-test 管"跑+判"（机械层），本技能管"想+改"（认知层）。
- self-audit 的输出是 evolution 的辅助输入（内容质量维度），不是触发器。
- 本技能不直接修改 SKILL.md，只产出 proposal；最终修改由人/律师 sign-off 后人工落盘或受信任的自动落盘工具执行。

## 四阶段契约

### 阶段 1：REFL（反思归因）

**触发条件**（满足任一）：

| 触发器 | 阈值 | 数据来源 |
|--------|------|----------|
| 失败率超阈 | 某评估维度失败率 ≥ 30% | auto-test `_results.yaml` |
| 连续失败 | 同一 case 连续 N 次 FAIL（N=3） | `_results.yaml` 历史 |
| 高风险失败 | patch_type=legal-source-update 失败 | auto-test 报告 |
| 法条异常 | 引用了已废止法条（legal-norm-validity-check 报警） | legal-atomic |
| 跨场景聚集 | 多个场景出现相同根因模式 | meta/patterns.md 比对 |
| 人工触发 | 律师/架构师手动指定 | 用户指令 |

**执行者**：Agent 主会话（消耗 token，做归因推理）

**输入契约**：

```yaml
trigger_metadata:
  trigger_type: failure_rate | consecutive | high_risk | legal_anomaly | cross_scene | manual
  scene: contract-review
  failed_cases: [case-007, case-012, case-018, case-023]
  eval_dimensions_failed: ["law_citation_accuracy", "risk_coverage"]
  raw_evidence:
    - case_id: case-007
      expected: "民法典 585"
      actual: "(未引用)"
      diff_type: missing_citation
    - case_id: case-012
      expected: "高违约金调整提示"
      actual: "(未提示)"
      diff_type: missing_warning
```

**输出契约**（写到 `plugins/legal-scenes/<scene>/evolution/reflections/YYYY-MM-DD-<id>.md`）：

```yaml
reflection_id: rfl-2026-06-18-001
scene: contract-review
trigger_ref: auto-test-run-2026-06-18
failed_cases: [case-007, case-012, case-018, case-023]
eval_dimensions_failed: ["law_citation_accuracy", "risk_coverage"]
root_cause_hypotheses:
  - id: h1
    hypothesis: "SKILL.md 缺少违约金条款专项检查步骤"
    evidence: "4/4 失败 case 均涉及违约金；SKILL.md 现有 step 3 将违约责任一笔带过"
    confidence: high
  - id: h2
    hypothesis: "trigger_phrases 未覆盖 '违约金/滞纳金/penalty' 关键词"
    evidence: "测试 query 含'50% 违约金'，trigger 命中但未引导到违约金专项检查"
    confidence: medium
  - id: h3
    hypothesis: "现有场景 CLAUDE.md 中违约金规则（第 130% 阈值）未在 SKILL.md 引用"
    evidence: "4/4 失败 case 输出未提及 130% 阈值判断"
    confidence: high
selected_root_cause: h1
rationale: "h1 解释力最强且 h3 是 h1 的具体表现"
```

**执行规则**：

1. 反思时**先加载** `plugins/legal-scenes/<scene>/evolution/meta/patterns.md`，看是否有历史根因模式可复用。
2. 至少生成 ≥2 个 hypothesis，单一 hypothesis 不允许。
3. confidence 分级：
   - `high`：直接证据 ≥3 个失败 case 共享
   - `medium`：2-3 个 case 共享
   - `low`：仅 1 个 case 或仅靠推理
4. confidence=low 的反思**必须人工确认**才进入下一阶段。

### 阶段 2：PATCH（修复提案）

**执行者**：Agent 主会话

**输入**：reflection_id 引用

**Patch 类型矩阵**（决定 gate 策略）：

| Patch 类型 | 例子 | 风险等级 | Gate 策略 | Sign-off 数量 |
|-----------|------|---------|-----------|---------------|
| `content-add` | 增加 trigger 词、加 step、加 case example | low | auto-merge | 0（人 review 后置） |
| `format-fix` | 统一节标题、补 frontmatter 字段 | low | auto-merge | 0 |
| `restructure` | 重组 SKILL.md 章节顺序 | medium | agent 评审 | 1（agent self-check） |
| `legal-source-add` | 新增法条引用 | high | 律师确认 | 1（人/律师） |
| `legal-source-replace` | 替换/废止现有法条 | high | 双律师确认 | 2（必须 ≥2 人） |
| `frame-mismatch` | 跨法域引用错误 | critical | **阻断+报警** | 架构师 + 2 律师 |
| `deletion` | 删除现有 step/法条 | high | 律师确认 | 1 + 影响范围评估 |

**输出契约**（写到 `plugins/legal-scenes/<scene>/evolution/proposals/YYYY-MM-DD-<id>.md`）：

```yaml
proposal_id: prp-2026-06-18-001
reflection_ref: rfl-2026-06-18-001
patch_type: legal-source-add
target_file: plugins/legal-scenes/contract-review/skills/review-payment-clause/SKILL.md
target_section: "## 违约金专项检查"
diff_summary: |
  + 在 step 3 之后新增 step 3.5 "违约金专项检查"
  + 引用《民法典》585 条
  + 引用《最高法关于适用民法典合同编通则若干问题的解释》65 条
  + 引用场景 CLAUDE.md 的 130% 阈值规则
rationale: |
  反射 rfl-2026-06-18-001 识别 h1 为主要根因：
  SKILL.md 缺违约金专项步骤。修复后预期 4/4 失败 case 转为通过。
risk_assessment:
  legal_frame_impact: [cn-mainland]
  scene_impact: [contract-review]
  cross_scene_impact: []
  law_effective_date_verified: true
  law_effective_date: 2021-01-01
expected_impact:
  metric: "违约金条款失败率"
  current_value: "40% (4/10)"
  expected_value: "<10% (1/10)"
  confidence: medium
regression_test_set: [case-007, case-012, case-018, case-023]
smoke_test_set:  # 跨场景冒烟，防止污染
  - scene: m-and-a
    sample_pct: 5
  - scene: employment-legal
    sample_pct: 5
signoff_required: 1
signoff_status: pending  # pending → approved | rejected | blocked
signoff_log: []
```

**生成 patch 时的硬约束**：

1. patch_type 必须从矩阵选，禁止自定义。
2. `law_effective_date_verified` 必须为 true，否则 proposal 标记 invalid，不进入 gate。
3. `expected_impact.confidence=low` 的 proposal 不进入 gate，强制人工 review。
4. 任何 proposal 必须包含 `regression_test_set`（至少 1 个 case），否则提案不完整。

### 阶段 3：GATE（人机协作门）

**执行者**：人工 / 半自动（受信任的工作流）

**决策树**：

```
proposal 提交
  ↓
[自动校验] frontmatter/law_effective_date/test_set 完整性
  ├─ 不通过 → reject（标记 invalid，写日志）
  └─ 通过 ↓
[Gate 策略路由]
  ├─ patch_type=content-add / format-fix → auto-merge 队列
  ├─ patch_type=restructure → agent self-check 队列
  ├─ patch_type=legal-source-add → 律师 sign-off 队列
  ├─ patch_type=legal-source-replace → 双律师 sign-off 队列
  └─ patch_type=frame-mismatch / deletion → 架构师 review + 阻塞
  ↓
[Sign-off 流程]
  每位 sign-off 者写入 signoff_log:
    - signer: <id or alias>
    - decision: approved | rejected | blocked
    - reason: <理由>
    - signed_at: <timestamp>
  ↓
[终态判定]
  ├─ approved ≥ signoff_required 且无 rejected → 进入回归验证
  ├─ 任一 rejected → 终止，写 lessons-learned 到 patterns
  └─ blocked → 升级到架构师 review
```

**关键规则**：

1. **sign-off 不可由 agent 自身完成**——即使 patch_type=restructure，agent self-check 也必须由**独立 agent session**（非生成 proposal 的 session）执行。
2. **高风险 patch（legal-source-*）必须等真人**——agent 不能 sign-off 自己。
3. **每个 sign-off 决定都写日志**，便于审计和元学习。

### 阶段 4：回归验证

**执行者**：auto-test（再次调用）+ 跨场景冒烟 runner

**输入**：

```yaml
regression_run:
  proposal_id: prp-2026-06-18-001
  patch_applied: true
  test_sets:
    must_pass:
      - { set: "failed_cases_set", cases: [case-007, case-012, case-018, case-023] }
    must_not_regress:
      - { set: "scene_full", scene: "contract-review", cases: "all" }
    smoke:
      - { scene: "m-and-a", sample_pct: 5 }
      - { scene: "employment-legal", sample_pct: 5 }
```

**判定矩阵**：

| must_pass | must_not_regress | smoke | 决策 |
|-----------|------------------|-------|------|
| 全过 | 全过 | 全过 | merge ✅ |
| 全过 | ≥1 失败 | 全过 | **人工 review**（可能 patch 有副作用） |
| 全过 | 全过 | ≥1 失败 | 警告 + 人工 review（潜在跨场景污染） |
| ≥1 失败 | 任意 | 任意 | reject + 回滚 + 回到 REFL |
| 任意 | ≥1 失败 | ≥1 失败 | reject + 报警到架构师 |

**回归后产物**：

写入 `plugins/legal-scenes/<scene>/evolution/merge-log.yaml`：

```yaml
- proposal_id: prp-2026-06-18-001
  merged_at: 2026-06-19T10:30:00
  merged_by: <signer-id>
  pre_patch:
    pass_rate: 60%  # 6/10
    failed_cases: [case-007, case-012, case-018, case-023]
  post_patch:
    pass_rate: 95%  # 19/20
    still_failing: [case-019]
  cross_scene_smoke: passed
  decision: merged
  lessons_learned: |
    h1 归因准确，patch 类型选对，回归一次过。
    模式 p-001（trigger 词缺失）已确认，复用模板。
  pattern_matched: p-001
  pattern_strengthened: true
```

## 元学习（meta-learning）

### 模式沉淀

`plugins/legal-scenes/<scene>/evolution/meta/patterns.md` 累积**跨次反思+patch 的复用模式**：

```yaml
patterns:
  - id: p-001
    name: "trigger 词缺失导致漏检"
    description: |
      SKILL.md 的 trigger_phrases 未覆盖用户真实表述的关键术语，
      导致 skill 被调用但未引导到专项检查。
    observed_count: 3
    first_observed: 2026-06-10
    last_observed: 2026-06-18
    scenes_affected: [contract-review, employment-legal]
    resolution_template: |
      反思时优先检查 trigger_phrases 是否覆盖用户真实表述；
      修复时优先添加缺失的同义词/口语化术语
    confidence: high
    proposal_template: |
      patch_type: content-add
      target_section: trigger_phrases
      diff_summary: "增加 X、Y、Z 关键词"
  
  - id: p-002
    name: "法条引用未引导 → 评估必挂"
    description: |
      SKILL.md 未显式引导引用 [YD]/[WKL] 数据源，
      导致输出虽有法律推理但缺引用，评估维度 law_citation_accuracy 必挂。
    observed_count: 5
    scenes_affected: [contract-review, m-and-a, ip-infringement]
    resolution_template: |
      反思时检查 SKILL.md 是否在相关 step 显式 mention 数据源引用
```

### 模式匹配规则

每次 REFL 阶段开始时：

1. 加载 `plugins/shared/evolution-meta/SKILL.md`（Agent 可消费版）
2. 比对当前失败模式与已有 patterns
3. **若 confidence=high 且 observed_count≥3**：直接复用 resolution_template，缩短 REFL 流程
4. **若 confidence=medium**：作为 hypothesis 之一，但需独立证据
5. **若新根因**：反思完成后**自动追加**到 patterns.md，observed_count=1

### 跨场景模式同步

- `plugins/legal-scenes/<scene>/evolution/meta/patterns.md` 是场景级
- `plugins/shared/evolution/meta/patterns.global.md` 是全局级（人审后从场景级晋升）
- 晋升规则：某 pattern 在 ≥3 个场景出现，自动建议晋升

## 文件组织规范

### 场景级 evolution 目录

```
plugins/legal-scenes/<scene>/
├── CLAUDE.md
├── skills/
├── tests/                          # A 的测试集（未来）
└── evolution/                      # C 的产物
    ├── README.md                   # 目录说明 + 当前状态
    ├── reflections/                # 阶段 1 产物
    │   ├── _TEMPLATE.md
    │   └── YYYY-MM-DD-<id>.md
    ├── proposals/                  # 阶段 2 产物
    │   ├── _TEMPLATE.md
    │   └── YYYY-MM-DD-<id>.md
    ├── merge-log.yaml              # 阶段 4 合并记录
    └── meta/
        └── patterns.md             # 元学习模式
```

### 命名规范

- reflection_id: `rfl-YYYY-MM-DD-NNN`（NNN 3 位顺序号）
- proposal_id: `prp-YYYY-MM-DD-NNN`
- 文件名与 ID 一致：`YYYY-MM-DD-NNN.md`

## 本技能不做什么

- **不执行测试**——执行归 auto-test，本技能只消费其产物。
- **不直接修改 SKILL.md**——只产出 proposal，落盘由 sign-off 后的人工/受信任工具执行。
- **不替代律师**——所有 legal-source-* 类型 patch 必须有真人 sign-off。
- **不修改全局框架**——CLAUDE.md / LEGAL_FRAMES/ 等全局文件的修改走架构师 review，不在本技能范围。
- **不跨法域自动迁移**——若某 patch 影响多法域，必须显式评估每法域的 impact，禁止隐式覆盖。

## 调度建议

| 频率 | 触发 | 阶段 |
|------|------|------|
| 每日 | auto-test 全量跑完 | REFL 触发器（失败率超阈） |
| 每周 | self-audit 跑完 | REFL 触发器（内容质量 WARN/FAIL） |
| 每次 SKILL.md 变更 | git hook | 强制跑 auto-test → REFL |
| 人工触发 | 律师/架构师指令 | 任意阶段 |

## 版本演进

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.0.0 | 2026-06-18 | 初版：四阶段契约 + gate 策略 + 元学习框架 |

---

*Greater China Legal — shared evolution v1.0.0*
