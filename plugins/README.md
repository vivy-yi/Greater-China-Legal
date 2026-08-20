# plugins/

GCL 项目的插件根目录。按**语义分层**共 7 类（外部连接 / 原子动作 / 复合动作 / 产出物 / 经营层 / 工作环境 / 自维护）：

```
plugins/
├── legal-tools/        ← 外部世界：数据源 / API / 连接器（17）
├── legal-atomic/       ← 法律原子操作：推理方法论（25）
├── legal-scenes/       ← 法律复合操作：业务入口（36 场景 · 501 skills）
├── legal-documents/    ← 产出物：文书生成 / 摘要 / 格式（5）
├── legal-management/   ← 经营层：排期 / 预算 / 风险 / 检索（7）
├── shared/             ← 工作环境：案件 / 用户 / 脱敏预处理（4）
└── legal-builder-hub/  ← 自维护：skill 管理 / 进化 / 安装（14）
```

> **历史命名**：本目录最初为 `tools/` `scenes/` `shared/` 三层，2026-06 改名为 `legal-tools/` `legal-scenes/` 以形成一致的 `legal-*` 命名族。
> **历史拆分**：legal-atomic/ 最初混入 14 个非原子 skill（输出/操作/管理），2026-06 拆出到 documents/operations/management 三个新层；2026-08 将 legal-operations（脱敏/还原）并入 shared/ 作输入输出预处理，legal-builder-hub 提升为顶层插件包。

## 各层职责

| 层 | 语义 | 职责 | 关键性质 |
|---|---|---|---|
| **legal-tools/** | 外部世界 | 数据源 / API / MCP / 连接器的封装 | 依赖外部，调用外部资源 |
| **legal-atomic/** | 原子动作 | 纯法律推理方法论（要素提取 / 三段论 / 效力核查…） | 无副作用，可安全组合 |
| **legal-scenes/** | 复合动作 | 36 个完整法律业务包（CLAUDE.md + skills + agents + hooks + references + matters） | 业务入口，组合原子动作 |
| **legal-documents/** | 产出物 | 法律文书终产物（判决书 / 摘要 / 格式 / 多源归纳） | 输出端 |
| **legal-management/** | 经营层 | 案件排期 / 期限监控 / 计费预算 / 风险排序 / 类案检索 | 调度端，管理案子 |
| **shared/** | 工作环境 | 案件工作区 / 冷启动配置 / 文书脱敏与还原（输入输出预处理） | 支撑所有层 |
| **legal-builder-hub/** | 自维护 | skill 安装 / 注册 / 进化 / 自测 / QA（完整 Claude Code 插件包） | 服务 skill 体系本身 |

## 动作链（单向依赖）

```
  外部世界          动作              产出
legal-tools ──→  legal-atomic ──→  legal-scenes ──→  legal-documents
(数据源/连接器)    (原子推理)         (复合业务包)        (文书终产物)

    经营层                   工作环境                   自维护
legal-management      shared              legal-builder-hub
(排期/预算/风险)       (案件/用户/脱敏)      (skill 管理/进化)
        │                   │                     │
        └─────────────── 均依赖 / 支撑 ────────────┘
```

## 新增 skill 流程

1. **判断归属**：按上表语义选 1 层（参考"各层职责"）
2. **查看该层 README**：命名规范、frontmatter 要求
3. **创建目录**：`plugins/<layer>/<skill-name>/SKILL.md`
4. **YAML frontmatter**：name / description / legal_frame / last_reviewed / version / risk_level / trigger_phrases
5. **校验**：`python3 scripts/validate-skills.py`
6. **修复**：`python3 scripts/fix-skills-frontmatter.py --fix`

## 相关工具

- `scripts/validate-skills.py` — 校验 SKILL.md frontmatter 合规
- `scripts/fix-skills-frontmatter.py` — 自动修复 5 类常见 frontmatter 错误
- `scripts/lint-tool-scope.py` — 检查工具调用范围
- `scripts/orchestrate.py` — 多场景编排

## 详见

- 每个子目录的 README（同级文件）
- 项目根 `CLAUDE.md`
- `.claude/skills/scene-claudemd-curator/` —— 场景 CLAUDE.md 治理工具
