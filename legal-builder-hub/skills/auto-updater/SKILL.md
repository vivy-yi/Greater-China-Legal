---
name: auto-updater
description: >
  自动检查并更新已安装的CN legal skills——对比本地版本与远程registry，
  自动下载更新并保留备份。支持全量更新、按场景更新、单个skill更新。
  适用情形：用户说"更新skills"、"检查更新"、"同步最新版本"。
argument-hint: "[--check | --update | --update=skill-name | --all | --scene=scene-name]"
legal_frame: cn-mainland
last_reviewed: 2026-06-13
version: 1.1.0
risk_level: medium
---

# CN Legal Skill Auto-Updater

## 运行模式

### --check（推荐首次）

```
/auto-updater --check
```

只检查，不下载。输出：

```
Updates available for 3 skills:
  dispute-classifier:   1.1.0 → 1.2.0  [feature] 争议分类增强
  nda-review:           1.0.0 → 1.1.0  [fix]     路径引用修复
  breach-notification:   1.0.0 → 1.0.1  [patch]   错别字修正
```

### --update（更新全部）

```
/auto-updater --update
```

1. 读取 manifest 获取所有 GitHub source skills
2. 批量检查远程最新版本
3. 有更新时：自动备份 → 下载 → 验证
4. 更新 manifest 版本号
5. 输出变更摘要

### --update=skill-name（更新单个）

```
/auto-updater --update=dispute-classifier
```

### --scene=scene-name（按场景更新）

```
/auto-updater --scene=contract-review
```

## 备份策略

- 备份目录：`~/.openclaw/skills/.backup/{skill-name}/{commit-hash}/{timestamp}/`
- 保留最近5个备份
- 本地修改过的文件单独标记（diff记录）

## 更新冲突处理

**场景：远程版本与本地修改冲突**

1. 计算本地 diff
2. 尝试3-way merge
3. 能合并：合并后提示用户
4. 不能合并：
   - 输出冲突文件列表
   - 拒绝自动更新
   - 提示用户手动处理：`/skill-manager update dispute-classifier --force`

**--force flag**：覆盖本地修改（危险，仅在确认本地无重要变更时使用）

## manifest 格式

```yaml
skills:
  dispute-classifier:
    version: 1.2.0
    source: github
    repo: vivy-yi/Greater-China-Legal
    path: labor-arbitration/skills/dispute-classifier/SKILL.md
    commit: a1b2c3d
    updated_at: 2026-06-13T10:00:00Z
    status: enabled
  compensation-calculator:
    version: 1.0.0
    source: local
    path: /Users/d/skills/compensation-calculator/SKILL.md
    updated_at: 2026-06-01T08:00:00Z
    status: enabled
```

## Cron 集成建议

建议配置每日自动检查：

```
# ~/.openclaw/cron.yaml
- name: skill-update-check
  schedule: "0 9 * * *"  # 每天9点
  prompt: /auto-updater --check
  deliver: origin
```

---

*[YD] — Greater China Legal auto-updater v1.1.0*
