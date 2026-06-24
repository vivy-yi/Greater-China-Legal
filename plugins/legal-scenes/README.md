# legal-scenes/ — 法律场景（36 个完整业务包）

每个场景是**完整业务包**，不是单个 skill。

## 职责

提供**法律业务入口**——每个场景对应一类业务（合同审查、诉讼支持、合规审查等），由 Claude Code session 按用户意图进入。

## 场景标准结构

```
<scene-name>/
├── CLAUDE.md             ← 必填：场景级实践画像（v3 标准 ~290-500 行）
├── skills/<skill>/SKILL.md ← 场景特有 skill（可选）
├── agents/<name>.md      ← 定时调度 agent（可选）
├── hooks/hooks.json      ← 事件驱动钩子（可选）
├── references/           ← 场景内参考文档（可选）
├── matters/<slug>/       ← 案件工作区（运行时创建）
└── tests/                ← 自测用例（可选）
```

## 36 个场景

合同审查 / 数据合规 / 刑事辩护 / 家庭法 / 行政诉讼 / 反垄断 / 强制执行 / 海事法 / 环境保护 / 资本与证券市场 / 跨境贸易 / 跨境并购 / 公司治理 / 劳动仲裁 / 合规监管 / 雇佣法律 / 证据/政府调查 / 知识产权 / 法律援助 / 诉讼支持 / 并购 / 私募股权 / 法律诊所 / 法学院 / 律师协办 / 债务 / 财富传承 / 网络金融 / 房地产与建筑 / 互联网金融 / Web3 虚拟资产 / 白领犯罪 / 产品法律 / 金融业务 / 跨境特殊机会投资 / 仲裁

## CLAUDE.md 标准（v3 一体化模式）

**不再拆分 references/**——所有内容写到 ~290-500 行的 CLAUDE.md。

推荐结构：
- **Part A — Operating System**（16 universal sections）：配置位置、用户角色、quiet mode、可用集成、输出格式、决策姿态、共享 guardrails、scaffolding、升级触发、ad-hoc、比例、管辖识别、检索信任、检索结果处理、tag 词汇、大输入/输出
- **Part B — Scene-Adaptive Practice Profile**（18 pattern adaptive）：工作流、路由表、三色体系、风险等级、升级触发、输出模板、决策树、主动问、用户配置、数据源标注、YAML 注册表、per-matter side、enforcement posture、risk calibration、设计哲学、推理原子能力调用流程、跨场景协作（§ B17 脱敏/还原）

## CLAUDE.md 不需要 frontmatter

CLAUDE.md 本身**不需要 YAML frontmatter**——它是 AI 运行时上下文文档，不是 skill。

## 新增场景流程

1. 创建目录：`plugins/legal-scenes/<scene-name>/`
2. 写 CLAUDE.md（按 v3 标准 ~290-500 行）
3. 加 skills（按需）
4. 加 agents（按需）
5. **重要**：在 § B16 写明"推理原子能力调用流程"
6. **重要**：如果涉及脱敏/还原，加 § B17 钩子
7. 校验：`python3 scripts/validate-skills.py`

## 详见

- `plugins/README.md`
- `.claude/skills/scene-claudemd-curator/SKILL.md` —— scene CLAUDE.md 馆长（v3 一体化方法）
- `memory/scene-claudemd-v3-standard.md`