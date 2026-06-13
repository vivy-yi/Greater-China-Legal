---
name: review-proposals
description: >
  审查并批准（或拒绝）playbook-monitor agent 待处理的 playbook 更新提案，
  并将批准变更应用到 practice profile。
  适用情形：playbook-monitor agent 提出提案，用户说"审查 playbook 提案"、
  "有哪些待处理更新"，或想要逐步审查偏差驱动的 playbook 变更。
argument-hint: "[无需参数——从待处理提案文件工作]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

# /review-proposals — China Mainland

## Purpose

逐步审查 playbook-monitor agent 待处理的 playbook 更新提案，并将批准的变更应用到 `../CLAUDE.md`。

## Instructions

1. **加载 playbook-monitor agent**，运行第5步（审查和批准流程）

2. **如提案文件不存在或为空：** 回复"无待处理提案。Playbook 已是最新的。"不再继续。

3. **逐个展示提案。** 对每个提案显示完整提案块，提供四个选项：接受、拒绝、修改、延期。

4. **对于接受或修改：** 显示对 `../CLAUDE.md` 的精确 diff。仅在律师明确确认后应用。

5. **对于拒绝或延期：** 记录决定。不修改 `../CLAUDE.md`。

6. **所有提案解决后：** 显示变更摘要，然后存档提案文件。

---

*Greater China Legal — commercial-legal review-proposals CN adapter v1.0.0*
*基于 anthropic/claude-for-legal review-proposals 适配中国大陆法律环境*

*[YD] — 基于 anthropic/claude-for-legal 适配中国大陆法律环境 v1.0.0*
