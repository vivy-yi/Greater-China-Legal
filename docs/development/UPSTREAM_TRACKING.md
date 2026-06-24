# Greater China Legal — 上游同步追踪

## Fork 信息

- **上游仓库：** `anthropics/claude-for-legal`
- **分叉时间：** 2026-06-11
- **分叉点 commit：** `9cecd91`（官方结构重组后）
- **上游当前分支：** `main`

## 同步状态

| 同步日期 | 上游 commit | 状态 | 备注 |
|---|---|---|---|
| 2026-06-11 | 9cecd91 | ✅ 已分叉 | 初始分叉 |

## 上游更新追踪

- [ ] 每4周检查上游新 commit
- [ ] 冲突处理：法条引用 → 保留本地版本；Skill内部逻辑 → 本地化优先；框架结构 → 跟随上游
- [ ] 每次同步后更新 `legal-frame-version` 字段

## 已知上游分支

- `main` — 主分支
- `release-2026-06-03` — 发布分支
- `tobin/add-cla-md`
- `tobin/add-cocounsel-legal`
- `tobin/cla-workflow-robustness`
- `tobin/remove-unused-references`

## 同步规则

1. **月度同步**：每月第一个周末执行
2. **冲突处理优先级**：
   - `CLAUDE.md` 法条引用 → 保留本地版本
   - `SKILL.md` 内部逻辑 → 本地化重写优先
   -目录结构（12域） → 完全跟随上游
3. **版本标注**：每次同步后更新 `last-reviewed: YYYY-MM`