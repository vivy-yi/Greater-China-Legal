---
name: skill-installer
description: >
  将CN legal skill安装到本地环境——从GitHub registry克隆或从本地文件安装。
  支持单文件安装、目录安装、版本锁定。安装前验证skill质量，安装后写入manifest。
  适用情形：用户说"安装skill"、"添加[xxx]"、"我需要一个[xxx功能]的skill"。
argument-hint: "[skill-name@version] 或 [GitHub URL] 或 [本地路径]"
legal_frame: cn-mainland
last_reviewed: 2026-06-13
version: 1.1.0
risk_level: medium
---

# CN Legal Skill Installer

## 安装模式

**模式A — GitHub registry 安装（推荐）**

```
/skill-installer dispute-classifier
```

1. 从 vivy-yi/Greater-China-Legal registry 查找 skill
2. 读取 SKILL.md 头部验证 frontmatter
3. 检查 `argument-hint` 和 `description` 是否包含触发词
4. 写入 `~/.openclaw/skills/{skill-name}/SKILL.md`
5. 写入 manifest 条目：`~/.openclaw/skills/.manifest.yaml`
6. 验证：执行 `/skill-name --help` 确认可加载

**模式B — GitHub URL 安装**

```
/skill-installer https://github.com/vivy-yi/Greater-China-Legal/blob/main/labor-arbitration/skills/compensation-calculator/SKILL.md
```

1. 用 `curl` 获取原始文件内容
2. 同上验证 + 写入流程

**模式C — 本地文件安装**

```
/skill-installer ./my-skill/SKILL.md
```

1. 读取本地文件
2. 验证 frontmatter 完整性（必需字段：name/description/argument-hint/legal_frame/version/risk_level）
3. 生成 skill name（用 frontmatter 的 name，或从文件名推断）
4. 写入 `~/.openclaw/skills/{name}/SKILL.md`
5. 追加 manifest 条目

## 验证检查清单

安装前执行，不通过则拒绝安装：

- [ ] frontmatter 包含所有必需字段（name/description/argument-hint/legal_frame/version/risk_level）
- [ ] description 包含 `适用情形` 说明触发词
- [ ] argument-hint 格式为 `[参数描述]`
- [ ] 无硬编码路径（如 `/commercial-legal/`、`../../corporate/`）
- [ ] 中文内容为主（legal_frame: cn-mainland/hk/mo/sg/tw 时内容应为中文）
- [ ] 数据源标注存在（[YD]/[WKL]/[BD]/[GCL]/[model]）

## 版本管理

- 不带版本号：安装 latest
- 带版本号：`skill-name@1.0.0` 精确锁定
- 更新：`--update` flag 升级到最新版本
- manifest 中记录：name/version/source/commit-hash

## 冲突处理

- 同名 skill 已存在：提示用户选择 [覆盖/重命名/取消]
- 不同 source 的同名 skill：拒绝，提示 `--force` 可强制覆盖
- 依赖缺失：列出缺失依赖并提供安装命令

## 错误处理

| 错误 | 处理 |
|---|---|
| GitHub 访问失败 | 降级到 gitzh mirror 或提示用户手动安装 |
| frontmatter 不完整 | 输出缺失字段列表，拒绝安装 |
| 写入权限不足 | 提示 `chmod +w ~/.openclaw/skills/` |

---

*[YD] — Greater China Legal skill-installer v1.1.0*