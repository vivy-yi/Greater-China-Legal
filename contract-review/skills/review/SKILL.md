---
name: review
description: >
  根据 playbook 审查供应商合同、NDA或SaaS订阅协议。
  从标题识别协议结构，路由至正确审查技能（vendor-agreement-review、nda-review、saas-msa-review），
  并将输出整合为一份备忘录。
  适用情形：用户说"审一下这份合同"、"评估这个MSA"、"这个NDA可以吗"。
argument-hint: '[文件路径 | 合同编号 | 粘贴文本]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

# /review — China Mainland

## Purpose

根据 `../CLAUDE.md` 中的 playbook 审查收到的协议。从标题识别协议结构，选择适当技能，并在 confirm_routing 启用时先确认用户再继续。

## Instructions

1. **加载 `../CLAUDE.md`**

   如有占位符，停止并提示："请先运行 `/shared/agent-ops:cold-start-interview`——我需要在审查前了解您的 playbook。"

   同时读取 `../CLAUDE.md` → `## Review preferences` → `confirm_routing`。如字段缺失，视为 `true`。

2. **获取协议：** 从文件路径、合同编号或粘贴文本。如未提供，询问。

3. **读取文档结构——先读标题**

   提取：
   - 主协议标题
   - 所有附件、附录、补充协议的标题

4. **选择技能**

   | 文档/章节标题包含 | 技能 |
   |---|---|
   | Non-Disclosure、NDA、Confidentiality Agreement（作为主协议）| **nda-review** |
   | Master Services Agreement、Professional Services、Statement of Work、Consulting Agreement | **vendor-agreement-review** |
   | SaaS、Subscription Agreement、Cloud Services | **saas-msa-review** |

5. **运行审查**，整合输出为单一备忘录

---

## 本技能不做什么

- 不做实质性分析。只路由至具体审查技能。
- 不读取附件正文。附件由具体审查技能处理。

---

*Greater China Legal — commercial-legal review CN adapter v1.0.0*
*基于 anthropic/claude-for-legal review 适配中国大陆法律环境*