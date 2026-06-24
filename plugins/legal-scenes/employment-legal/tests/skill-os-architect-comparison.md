# CLAUDE.md 对比测试：scene-claudemd-curator vs scene-os-architect

> **目的：** 在 Claude Code agent CLI 中真实运行 agent，比较两个 CLAUDE.md 在同一法律任务下的输出质量。
> **测试场景：** employment-legal
> **测试日期：** 2026-06-20

---

## Setup

```
# 在 Claude Code 中：
# 1. 备份当前 CLAUDE.md
cp plugins/legal-scenes/employment-legal/CLAUDE.md /tmp/CLAUDE.md.scene-claudemd-curator

# 2. 切换到新 CLAUDE.md
cp plugins/legal-scenes/employment-legal/CLAUDE.md.os-architect-design plugins/legal-scenes/employment-legal/CLAUDE.md

# 测试结束后恢复
cp /tmp/CLAUDE.md.scene-claudemd-curator plugins/legal-scenes/employment-legal/CLAUDE.md
```

---

## Test Cases

### Case 1：试用期违纪解除（红线 + 关键串接）

**User input：**
> 我们公司一名员工入职 3 个月，今天发现他上班时间打游戏，被监控拍到了。我们要立即解除他。

**Expected output should include:**
- Recognition of probation-period dismissal
- Trigger of `internal-investigation` before termination
- Question about 规章制度是否经民主程序
- Flag of § 5.2 (must-escalate) or equivalent
- Work-product header
- Reviewer note
- Decision tree

### Case 2：孕期女职工解除（绝对禁止）

**User input：**
> 我们公司有一名女员工刚怀孕，但我们部门重组需要裁员，可以直接解除她吗？赔偿 N+1。

**Expected output should include:**
- Immediate stop signal (绝对禁止)
- Reference to 劳动合同法 42 条
- 2N + 恢复劳动关系 outcome
- Flag to escalate to lawyer
- No "you can do this with N+1" response

### Case 3：15 年老员工协商解除（边界判断）

**User input：**
> 我们公司有一名老员工，连续工作满 18 年，距退休 3 年。最近表现不佳，我们想和他协商解除，能给多少补偿？

**Expected output should include:**
- Distinction: 单方解除（禁止）vs 协商解除（合法）
- Reference to 劳动合同法 42 条
- N + 1 calculation
- Suggestion to use resignation-negotiation, not termination-legality-assessment

### Case 4：工伤员工医疗期（边界判断）

**User input：**
> 我们公司一名员工上班路上骑电动车摔了，骨折住院 2 个月。现在医疗期结束，我们想解除他。可以吗？

**Expected output should include:**
- Verify if this is 工伤 (上下班合理路线)
- Medical period calculation (按工龄)
- Flag if in medical period (禁止解除)
- If 工伤, additional protections (工伤保险条例)

### Case 5：经济性裁员 25 人（流程 + 升级）

**User input：**
> 我们公司要经济性裁员，预计裁 25 人，占公司总人数的 12%。流程应该怎么走？

**Expected output should include:**
- 触发 § 5.2 must-escalate (20+ 或 10%+)
- 4 步流程：30 日通知工会 / 工会意见 / 劳动部门报告 / 优先留用
- N vs N+1 compensation choice
- Escalate to GC + outside counsel

---

## 评估维度（每个 case 评分 0-1）

| 维度 | 评分标准 |
|------|---------|
| **路由正确性** | 是否调用了正确的 skill |
| **红线识别** | 是否正确识别绝对禁止 / 必升 |
| **关键串接** | 是否先调查后解除（违纪场景） |
| **主动问质量** | 是否问了关键事实（规章制度、协商意愿等） |
| **升级判断** | 是否正确判断需要律师介入 |
| **输出格式** | work-product header / reviewer note / decision tree 是否齐 |
| **法条引用** | 是否准确（合同法 39/42 等）|
| **CN 本地化** | 是否用 CN 法律术语（不是 US FRCP 等）|

**总分：8 维 × 1 分 = 8 分**

**及格线：6/8**

---

## 对比执行方式

```bash
# Run Case 1-5 with current CLAUDE.md (scene-claudemd-curator output)
# Record agent output for each case
# Score each case

# Swap to new CLAUDE.md (scene-os-architect output)
cp CLAUDE.md.os-architect-design CLAUDE.md

# Run Case 1-5 again with new CLAUDE.md
# Record agent output
# Score each case

# Compare scores
```

---

## 输出格式建议

每个 case 跑完后，记录：

```markdown
## Case N: [题目]

### Output
[agent 真实输出]

### Score
| Dimension | Score |
|-----------|-------|
| 路由正确性 | X/1 |
| 红线识别 | X/1 |
| 关键串接 | X/1 |
| 主动问质量 | X/1 |
| 升级判断 | X/1 |
| 输出格式 | X/1 |
| 法条引用 | X/1 |
| CN 本地化 | X/1 |
| **Total** | **X/8** |

### Observations
- [什么做得好]
- [什么没做对]
- [建议]
```

---

## 重要说明

**这个测试必须是真实 AI 运行**，不是 AI 模拟。

**为什么？** 因为：
1. AI 模拟 = 我（chat Claude）描述"agent 会怎么做"——这是假的
2. 真实测试 = Claude Code agent CLI 实际加载 CLAUDE.md + 实际处理任务 + 输出真实结果

**正确做法**：
1. 在 Claude Code 中实际运行（需要您的真机环境）
2. 捕获真实输出
3. 评分
4. 对比

**为什么我不能做？** 因为我是在这个对话里的 AI，没有 Claude Code agent CLI 环境，无法执行 skill。

**我只能**：
- 设计测试脚本（已完成此文档）
- 设计评分标准（已完成）
- 等您在 Claude Code 中真实跑完后，把结果给我看，我帮您分析