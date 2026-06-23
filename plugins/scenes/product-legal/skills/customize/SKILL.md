---
name: customize
description: >
  Guided customization of your product counsel practice profile — change one
  thing without re-running the whole cold-start interview. Adjust risk
  calibration, escalation contacts, launch review framework, marketing
  claims posture, or matter workspace paths. Use when the user says
  "change my [thing]", "update my profile", "edit my framework", "retune
  my calibration", or "customize".
legal_frame: cn-mainland
last_reviewed: 2026-06-23
version: 2.0.0
argument-hint: "[section name, or describe what you want to change]"
trigger_phrases:
  - '产品发布'
  - '营销'
  - '合规'
  - '风险'
  - 'customize'
  - '定制'
---

# /customize — cn-mainland 适配版

> ⚠️ **本 skill 已从 Anthropic 原版 claude-for-legal US 版本（v1.0）适配为 GCL cn-mainland 版本（v2.0）。**
>
> **核心变更**：配置路径从 `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md` 改为 `plugins/scenes/product-legal/CLAUDE.md` § B9。集成 / 法规全部替换为 CN 工具与法规。

---

## When this runs

用户输入了 `/product-legal:customize`。他们想改变产品法务 profile 中的某项——风险校准阈值、升级联系人、框架部分——而不重新运行整个冷启动访谈，也不手动编辑 YAML。

## What to do

1. **读取配置。** 读 `plugins/scenes/product-legal/CLAUDE.md`（特别是 § B9 用户配置）和 `plugins/shared/cold-start-interview/references/company-profile.md`（如果存在）。如果插件配置不存在或仍包含 `[填空]` 占位符，说：

   > 你还没有运行 setup。运行 `/product-legal:cold-start-interview` 先——customize 是为你已有的 profile 调整。

2. **显示可定制地图。** 列出 profile 中的内容，分组，每项带当前值的一行摘要：

   - **公司 / 你是谁** — 名称、行业、法域、阶段、执业设置、产品表面 *（跨所有插件共享 — 更改通过 `company-profile.md` 流转）*
   - **启动审查流程** — 接入（Jira / Linear / Asana / 飞书 / 钉钉 / 文档）、审查 SLA、启动分层、PRD 位置
   - **审查框架** — 你审查启动的类别（隐私、IP、安全、声明、监管、可访问性、安全等）和每个的深度
   - **风险校准** — 你公司的 P0 blocker / needs a real look / fine，附示例锚定标签
   - **营销声明** — 浮夸 vs. 支持性的姿态、比较声明框架、最高级、AI 功能声明的 house 规则
   - **人员** — 表面产品合作伙伴、升级链（你的经理、GC、风险委员会）、营销对应人
   - **工作流** — 案件工作区、启动雷达监视节奏、启动审查模板
   - **集成** — 元典 / 北大法宝 / gcl-data-service / 企业 IM 状态，fallbacks

3. **询问他们想改变什么。**

   > 你想调整什么？选择一个部分，或用你自己的话描述更改。

4. **进行更改。** 显示当前值，询问新值，解释下游变化，确认，写入配置。

   示例：
   - *风险校准从"fine"收紧到"needs a real look"用于某种模式：* "`/is-this-a-problem` 和 `/launch-review` 将开始标记这种模式。现有审查保持原样；如果要应用新姿态，重新运行。"
   - *新启动审查类别：* "`/launch-review` 将添加此类别部分。`/is-this-a-problem` 将在分类中模式匹配它。"
   - *营销声明姿态收紧：* "`/marketing-claims-review` 将更多语言标记为需要支持或重构。"
   - **CN 特别** *个保法 / 广告法收紧：* "`/launch-review` 和 `/marketing-claims-review` 将使用更严格的 CN 法规阈值。"

5. **对于共享 profile 更改**（公司名、行业、法域、执业设置、阶段）：写入 `plugins/shared/cold-start-interview/references/company-profile.md` 并注明：

   > 此更改影响所有插件——任何读取你的法域足迹的插件现在看到 [新值]。

6. **关闭。**

   > 完成。你的下一个输出将反映更改。还有其他吗？随时运行 `/product-legal:customize`。

---

## Guardrails

- **永远不要删除一个部分。** 如果用户想"移除"审查类别，提供标记为 `[Not in scope — route elsewhere]` 并命名接管它的插件/团队。
- **标记内部不一致。** 如果更改会使 profile 不一致（例如：AI 功能声明审查开启 + 在 `/ai-governance-legal` 中没有 AI 政策承诺；或"快 SLA"+"每次启动需要 GC 签字"），标记这种张力。
- **标记护栏降级。** `[review]` 标记、来源归属标签和引用法规上的 `[verify]` 标签是承重的——不要删除。声明的支持要求是 `/marketing-claims-review` 存在的原因；削弱它就击败了这个 skill。
- **一次一个更改。** 不要重新问整个访谈。

---

## CN 特别 Guardrails

- **CN 法源更新同步**：个保法 / 广告法 / 电商法 修订时，更改 risk calibration 表 + launch review 框架 + marketing claims posture 都要同步。
- **跨境数据阈值**：如个保法出境阈值 1 万 / 100 万用户调整，需要更新所有相关 skill 的 trigger 阈值。
- **绝对化用语清单**：广告法 § 9 修订时，需要更新 marketing-claims-review 的禁用清单。
- **未成年人保护**：14 岁以下需监护人同意——如年龄阈值调整（个保法 / 未保法修订），需要更新 launch review 框架。
- **平台连带责任**：电商法 § 38 修订时（生命健康 / 其他权益条款），需要更新 launch review 风险评估。

---

*Greater China Legal — product-legal:customize v2.0.0*
*从 Anthropic 原版 claude-for-legal 适配为 GCL cn-mainland*
*最后更新:2026-06-23*