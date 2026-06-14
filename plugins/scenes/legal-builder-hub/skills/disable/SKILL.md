---
name: disable
description: >
  临时禁用已安装的CN legal skill——保留文件但不加载，用于测试、调试、
  或暂时不需要某skill的场景。比卸载安全，可随时重新启用。
  适用情形：用户说"禁用[xxx]"、"暂时关闭[xxx]"、"不想用这个skill了"。
argument-hint: "[skill-name] [--reason='reason-text']"
legal_frame: cn-mainland
last_reviewed: 2026-06-13
version: 1.1.0
risk_level: low
trigger_phrases:
  - skill
  - 安装
  - 注册表
  - disable
---

# Disable CN Legal Skill

## 使用

```
/disable dispute-classifier
/disable nda-review --reason="测试新版，暂用旧版对照"
```

## 行为

- 不删除任何文件
- 不影响其他依赖此 skill 的 skills
- 在 manifest 中将 status 改为 `disabled`
- 禁用时记录原因（用于审计）

## 验证

禁用后立即验证：

```
/disable dispute-classifier
→ dispute-classifier 已禁用
→ /dispute-classifier 不再出现在 /registry-browser 结果中
→ 依赖它的 skills（如有）仍可运行
```

## 重新启用

```
/skill-manager enable dispute-classifier
```

或直接：

```
/disable dispute-classifier  # 禁用
/enable dispute-classifier   # 重新启用（enable是指向skill-manager的alias）
```

## 与卸载的区别

| 操作 | 文件 | Manifest | 可恢复 |
|---|---|---|---|
| disable | 保留 | status=disabled | enable后立即可用 |
| uninstall | 删除 | 移除条目 | 需要重新install |

---

*[YD] — Greater China Legal disable v1.1.0*
