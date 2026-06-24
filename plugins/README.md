# plugins/

GCL 项目的插件根目录。按层次分 7 类（5 主层 + 1 横切 + 1 衍生）：

```
plugins/
├── legal-tools/        ← 第 1 层：外部数据/API/工具封装
├── legal-atomic/       ← 第 2 层：纯法律推理方法论（25 个）
├── legal-documents/    ← 第 3 层：法律文书输出（5 个）
├── legal-operations/   ← 第 4 层：法律文件操作（2 个，有副作用）
├── legal-management/   ← 第 5 层：法律流程管理（7 个）
├── legal-scenes/       ← 业务入口：36 个完整业务包
└── shared/             ← 横切：跨场景共享机制
```

> **历史命名**：本目录最初为 `tools/` `scenes/` `shared/` 三层，2026-06 改名为 `legal-tools/` `legal-scenes/` 以形成一致的 `legal-*` 命名族。
> **历史拆分**：legal-atomic/ 最初混入 14 个非原子 skill（输出/操作/管理），2026-06 拆出到 documents/operations/management 三个新层。

## 各层职责

| 层 | 职责 | 关键性质 |
|---|---|---|
| **legal-tools/** | 外部数据/API/MCP 的封装 | 依赖外部，调用外部资源 |
| **legal-atomic/** | 纯法律推理方法论 | 无副作用，可安全组合 |
| **legal-documents/** | 法律文书输出 | 终产物（判决书/摘要等） |
| **legal-operations/** | 文件操作 | 有副作用（写文件） |
| **legal-management/** | 业务流程管理 | 案件/财务/排期/风险 |
| **legal-scenes/** | 完整法律场景（CLAUDE.md + skills + agents + references + matters） | 业务入口，依赖下层 |
| **shared/** | 跨场景共享机制（业务/演化/质量 3 类） | 不依赖外部 |

## 依赖方向（单向向下）

```
scenes/  ──→  atomic/  ──→  tools/
   │           │
   │           ↓
   │      documents/  ←─── 输出终产物
   │      operations/  ←─── 文件操作
   │      management/  ←─── 流程管理
   │
   └─────→  shared/  ←───────（横切）
```

## 新增 skill 流程

1. **判断归属**：在 4 层中选 1 层（参考"各层职责"）
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