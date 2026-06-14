---
name: customize
description: >
  调整CN legal skill builder配置——修改skill输出路径、registry源、
  默认参数、工具链配置、通知偏好。
  适用情形：用户说"修改配置"、"变更registry源"、"设置默认参数"。
argument-hint: "[config-key] [config-value] 或 [--list] 或 [--reset]"
legal_frame: cn-mainland
last_reviewed: 2026-06-13
version: 1.1.0
risk_level: medium
trigger_phrases:
  - skill
  - 安装
  - 注册表
  - customize
---

# CN Legal Skill Builder — Configuration Manager

## 配置项

### registry源配置

```yaml
registry:
  primary: vivy-yi/Greater-China-Legal  # 主registry
  mirror: https://gitzh.com/vivy-yi/GL   # 镜像（访问github困难时）
  update_interval: 24h                    # 检查更新间隔
```

修改：`/customize registry.mirror https://mirror.example.com/GL`

### 工具链配置

```yaml
toolchain:
  clm: feishu       # 合同管理系统：feishu/dingtalk/eweaver/none
  storage: feishu    # 文档存储：feishu/aliyunoss/tencentdocs/none
  esign: esign      # 电子签：esign/tencent-esignfad/none
  notification: feishu  # 通知：feishu/dingtalk/wechatwork/none
```

### Skill输出路径

```yaml
paths:
  skills: ~/.openclaw/skills/     # skill安装目录
  backup: ~/.openclaw/skills/.backup/  # 备份目录
  temp: /tmp/gl-skills/          # 临时目录
  manifest: ~/.openclaw/skills/.manifest.yaml  # manifest路径
```

### 默认参数

```yaml
defaults:
  scene: labor-arbitration    # 默认场景
  legal_frame: cn-mainland    # 默认法律框架
  risk_threshold: medium      # 默认风险阈值
  language: zh                # 默认语言
  citation_style: chinese      # 引注格式：chinese/western/mixed
```

### 更新策略

```yaml
update_policy:
  auto_update: false          # 是否自动更新
  update_interval: 7d         # 检查间隔
  update_notify_only: true    # 只通知不自动下载
  backup_before_update: true  # 更新前备份
```

## 命令

### 列出当前配置

```
/customize --list
```

输出当前全部配置项（YAML格式）。

### 修改单项

```
/customize registry.primary vivy-yi/Greater-China-Legal
/customize toolchain.clm feishu
/customize paths.backup ~/.openclaw/backup/
```

### 重置为默认值

```
/customize --reset
```

删除用户配置，恢复默认配置（不可撤销，会提示备份）。

### 导出/导入配置

```
/customize --export ./my-config.yaml  # 导出到文件
/customize --import ./my-config.yaml  # 从文件导入
```

---

*[YD] — Greater China Legal customize v1.1.0*
