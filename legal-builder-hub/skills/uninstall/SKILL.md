---
name: uninstall
description: >
  从本地环境卸载CN legal skill——删除文件并从manifest移除，支持强制卸载。
  卸载前自动备份，支持恢复。
  适用情形：用户说"卸载[xxx]"、"删除[xxx] skill"、"不需要[xxx]了"。
argument-hint: "[skill-name] [--force] [--keep-backup]"
legal_frame: cn-mainland
last_reviewed: 2026-06-13
version: 1.1.0
risk_level: high
---

# Uninstall CN Legal Skill

## 安全卸载流程

```
/uninstall dispute-classifier
```

**确认步骤：**

```
正在卸载: dispute-classifier v1.2.0
来源: vivy-yi/Greater-China-Legal
安装时间: 2026-06-10

⚠️  警告：以下 skills 依赖 dispute-classifier：
  - compensation-calculator
  - escalation-flagger

卸载后，以上 skills 可能无法正常工作。

确认卸载？ [y/N]
```

输入 `y` 确认。

## 备份

卸载前自动备份到：
`~/.openclaw/skills/.backup/{skill-name}/{commit-hash}/{timestamp}/`

**恢复命令（如误删）：**
```bash
cp -r ~/.openclaw/skills/.backup/dispute-classifier/.../* ~/.openclaw/skills/dispute-classifier/
```

## --force flag

跳过确认步骤，直接卸载（危险）：

```
/uninstall dispute-classifier --force
```

## --keep-backup flag

卸载但不删除备份文件（默认会清理30天前的备份）：

```
/uninstall dispute-classifier --keep-backup
```

## 依赖检查

- 卸载前检查 manifest 中的依赖关系
- 有依赖时列出并要求确认
- 防止级联破坏（某skill被卸载导致其他skills失效）

## 错误处理

| 错误 | 处理 |
|---|---|
| skill不存在 | 提示 `/skill-manager list` 查看已安装skills |
| 依赖检查失败 | 拒绝卸载，列出依赖skills |
| 写入权限不足 | 提示手动删除 `rm -rf ~/.openclaw/skills/{skill-name}/` |

---

*[YD] — Greater China Legal uninstall v1.1.0*
