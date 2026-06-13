---
name: skill-manager
description: >
  管理CN legal skills的完整生命周期——查看列表、安装、更新、卸载、禁用/启用。
  维护本地 manifest，记录每个 skill 的版本/来源/依赖关系。
  适用情形：用户说"查看已安装skills"、"更新"、"卸载[xxx]"、"禁用[xxx]"。
argument-hint: "[list | install | update | uninstall | disable | enable] [skill-name] [--flags]"
legal_frame: cn-mainland
last_reviewed: 2026-06-13
version: 1.1.0
risk_level: medium
---

# CN Legal Skill Manager

## 命令总览

| 命令 | 说明 |
|---|---|
| `list` | 列出已安装 skills（含版本/来源/状态） |
| `install` | 安装新 skill |
| `update` | 更新已有 skill 到最新版本 |
| `uninstall` | 卸载 skill |
| `disable` | 临时禁用 skill（不删除文件） |
| `enable` | 重新启用已禁用 skill |
| `info` | 显示 skill 详细信息 |
| `deps` | 显示 skill 依赖树 |

## list — 列出已安装 skills

读取 `~/.openclaw/skills/.manifest.yaml`，输出表格：

```
Name              Version  Source                          Status
dispute-classifier  1.2.0   vivy-yi/Greater-China-Legal     enabled
nda-review          1.0.0   local ./my-custom-skill         disabled
compensation-calc   1.1.0   vivy-yi/Greater-China-Legal     enabled
```

**输出格式选项：**
- `--json`：JSON 格式输出（供脚本消费）
- `--outdated`：只显示有可用更新的 skills
- `--by-scene`：按场景分组列出

## install — 安装新 skill

```
/skill-manager install dispute-classifier
/skill-manager install compensation-calculator@1.0.0
/skill-manager install ./local-skill/SKILL.md
```

调用 `skill-installer` 执行实际安装逻辑。

## update — 更新 skills

```
/skill-manager update dispute-classifier      # 更新单个
/skill-manager update --all                    # 更新全部
/skill-manager update --scene=contract-review   # 更新某场景全部
```

**更新策略：**
1. 读取 manifest 获取当前版本和 source URL
2. 对 GitHub source：拉取最新 commit，对比版本号
3. 对本地 source：跳过（无更新源）
4. 有更新时：下载新版本，备份旧版本到 `~/.openclaw/skills/.backup/`
5. 验证新版本可加载
6. 更新 manifest 中的版本号

**版本冲突：** 如果远程版本与本地修改冲突（检测到本地变更），提示用户 [合并/覆盖/取消]。

## uninstall — 卸载 skill

```
/skill-manager uninstall nda-review
/skill-manager uninstall nda-review --force   # 不确认直接删
```

**卸载流程：**
1. 确认 skill 名称（防止误删）
2. 检查依赖：是否有其他 skill 依赖此 skill（从 manifest deps 字段判断）
3. 有依赖则列出并要求确认
4. 备份到 `~/.openclaw/skills/.backup/{skill-name}/{timestamp}/`
5. 删除 `~/.openclaw/skills/{skill-name}/`
6. 从 manifest 移除条目
7. 输出卸载摘要

**--force flag**：跳过所有确认步骤，直接卸载。

## disable — 临时禁用

```
/skill-manager disable nda-review
```

- 不删除文件，将 manifest 条目 status 改为 `disabled`
- 被禁用的 skill 不被 Agent 加载
- 禁用时记录原因（可选参数 `--reason "testing"`）

## enable — 重新启用

```
/skill-manager enable nda-review
```

- 将 manifest 条目 status 改回 `enabled`
- 验证文件仍然存在（不存在则报错）

## info — 详细信息

```
/skill-manager info dispute-classifier
```

输出：
- frontmatter 全部字段
- 安装来源和 commit hash
- 依赖列表
- 被依赖列表（哪些 skills 依赖此 skill）
- 最近更新时间
- 数据源标注

## deps — 依赖树

```
/skill-manager deps dispute-classifier
```

输出该 skill 的依赖有向无环图（DAG），以 ASCII 树展示：

```
dispute-classifier
├── argument-strength-evaluation
│   └── legal-domain-taxonomy
└── (no other deps)
```

---

*[YD] — Greater China Legal skill-manager v1.1.0*
