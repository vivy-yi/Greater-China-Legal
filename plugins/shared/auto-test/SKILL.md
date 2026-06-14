---
name: auto-test
description: >
  场景功能自测与自改进循环——对每个场景的 SKILL.md 执行
  模拟用户查询，评估输出质量，记录失败，自动修复。
  适合定时运行（每日或每次批量更新后）。
trigger_phrases:
  - 自测
  - 自动测试
  - auto test
  - 回归测试
  - 功能测试
last_reviewed: 2026-06
legal_frame: cn-mainland
version: 1.0.0
risk_level: low
---

# /auto-test — 场景功能自测与自改进

## 测试文件结构

每个场景下有一个 `tests/` 目录，包含该场景的测试用例：

```
plugins/scenes/<scene>/
├── CLAUDE.md
├── skills/<skill>/SKILL.md
└── tests/
    ├── <test-name>.md           ← 测试用例定义
    └── _results.yaml            ← 运行结果累积
```

### 测试用例格式

每个 `.md` 文件定义一个测试场景：

```markdown
---
# 必须字段
target: skills/<skill>/SKILL.md   # 被测 skill（相对场景目录）
type: functional                  # functional / regression / edge-case
priority: high                    # high / medium / low

# 评估条件（至少满足一个）
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["民法典", "违约"]
  - no_placeholder: true
  - starts_with_header: true

# 测试输入
query: >
  "审一下这份供应商合同，金额80万，对方适用美国法律，
   违约金50%。"

# 预期输出特征
expected:
  - section: "风险等级"
    type: must
  - section: "修改建议"
    type: should
  - term: "民法典第585条"
    type: must
  - term: "涉外民事关系法律适用法"
    type: must
---

# [测试名称] — [测试场景描述]
```

## 工作流程

### Step 0：扫描变更

检查 `git diff --name-only HEAD~1` 或指定场景，确定哪些 scene skill 有变更。

### Step 1：加载测试用例

对每个有变更的场景，读取 `tests/` 下所有 `.md` 文件。

### Step 2：执行测试

对每个测试用例：

1. 读取测试文件的 `target` 和 `query`
2. 加载场景 CLAUDE.md（含 Role、数据源、推理原子能力调用流程）
3. 加载 target skill 的 SKILL.md
4. 以 query 为输入，执行整个工作流
5. 收集输出

### Step 3：评估输出

对照测试用例的 `expected` 和 `checks` 字段逐条检查：

| 检查项 | 方法 | 判定 |
|--------|------|------|
| `contains` 关键词 | 输出含指定术语？ | PASS/FAIL |
| `has_section` 节标题 | 输出含指定节？ | PASS/FAIL |
| `body_lines` 行数 | 输出正文≥N行？ | PASS/FAIL |
| `no_placeholder` 填空 | 输出无[填空]标记？ | PASS/FAIL |
| `type:must` | 必选项未通过 → FAIL | FAIL |
| `type:should` | 建议项未通过 → WARN | PASS but warn |

### Step 4：生成报告

```
📋 Auto-Test 报告 — [日期]

====================
场景: contract-review
====================
  ✅ vendor-agreement-review — 供应商合同审查 (0.4s)
  ⚠️ review-proposals — 审查提案修改 (expected "民法典第585条" not found)
  ❌ renewal-tracker — 续约追踪 (输出含[填空]标记)

====================
场景: data-compliance
====================
  ✅ pipl-assessment — PIPL合规评估 (0.3s)
  ❌ data-export-assessment — 数据出境评估 (expected section "风险等级" missing)

====================
汇总
====================
总测试: 24
通过: 19
警告: 2
失败: 3
```

### Step 5：失败分析与自修复

对每个 FAIL 的测试：

1. **分析根因**：
   - 输出太短 → SKILL.md body 过薄
   - 缺失法条引用 → SKILL.md 没写 legal_sources 或没引用
   - 含[填空] → cold-start 未运行
   - 节标题名称不一致 → SKILL.md 的节命名与 expected 不匹配

2. **自修复方案**：

| 失败原因 | 自动修复措施 |
|---------|-------------|
| 输出太短（< 30 行） | 在 SKILL.md body 追加标准工作流模板 |
| 缺失法条引用 | 从 skill name 和场景推断涉及法条，追加到 `legal_sources` |
| 含[填空] | 提示用户运行 cold-start |
| 节标题不一致 | 统一为标准节标题（## 工作流程 / ## 风险分析 / ## 输出格式） |

3. **修复后重跑测试**

### Step 6：回写测试结果

每次运行结果追加到 `tests/_results.yaml`：

```yaml
- run_at: 2026-06-15
  scene: contract-review
  skill: vendor-agreement-review
  test: supplier-msa-review
  result: PASS
  duration: 0.4
  auto_fixed: false

- run_at: 2026-06-15
  scene: data-compliance
  skill: data-export-assessment
  test: cross-border-data-flow
  result: FAIL
  duration: 0.8
  auto_fixed: true
  fix: "added legal_sources for PIPL第38条"
  post_fix_result: PASS
```

## 每周测试计划

如无指定场景，按以下顺序覆盖：

| 日期 | 覆盖范围 |
|------|---------|
| 周一 | contract-review + m-and-a + corporate-governance |
| 周二 | data-compliance + ip-infringement + employment-legal |
| 周三 | tax-compliance + regulatory-compliance + white-collar-crime |
| 周四 | litigation-support + commercial-arbitration + labor-arbitration |
| 周五 | 剩余场景 + 汇总 + 修复确认 |
| 周末 | 不执行 |

## 本技能不做什么

- 不验证法条引用的准确性——只检查术语存在性。
- 不替代真实律师的审核。
- 不修改 SKILL.md 的法律逻辑——只修复结构性问题。

---

*Greater China Legal — shared auto-test v1.0.0*
