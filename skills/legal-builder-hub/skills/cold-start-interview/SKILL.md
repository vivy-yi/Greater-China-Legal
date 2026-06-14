---
name: cold-start-interview
description: >
  CN legal skill builder初始化向导——通过交互式问答了解用户的使用场景、
  法律框架、常用工具链，生成个性化 skill registry 和配置文件。
  适用情形：首次使用（无manifest）、用户要求重新配置（--redo）。
argument-hint: "[--redo] [--skip-questions]"
legal_frame: cn-mainland
last_reviewed: 2026-06-13
version: 1.1.0
risk_level: low
---

# CN Legal Skill Builder — Cold Start Interview

## 目标

为新用户（或要求重置的用户）完成初始配置：

1. 确定使用场景
2. 选择法律框架（大陆/香港/澳门/台湾/新加坡）
3. 配置工具链（MCP servers）
4. 生成个性化 manifest
5. 推荐首批 skills

## 交互流程

### Step 1: 场景确认

```
欢迎使用 Greater China Legal Skill Builder。

请选择您的法律业务场景（可多选）：
  [1] 劳动法律（劳动仲裁、员工纠纷）
  [2] 商业合同（合同审查、谈判支持）
  [3] 知识产权（专利商标、侵权分析）
  [4] 数据合规（GDPR合规、数据泄露）
  [5] 公司治理（董监事会议事合规）
  [6] 监管合规（法规监控、政策跟踪）
  [7] 全部场景
```

### Step 2: 法律框架

```
您的主要法律管辖区：
  [A] 中国大陆（cn-mainland）
  [B] 香港（hk）
  [C] 澳门（mo）
  [D] 台湾（tw）
  [E] 新加坡（sg）
  [F] 多个地区
```

### Step 3: 工具链配置

```
您当前使用的企业工具（跳过使用默认）：
  合同管理系统（CLM）：泛微 / 钉钉 / 飞书 / 其他 / 暂无
  文档存储：飞书云文档 / 腾讯文档 / 阿里云OSS / 其他
  电子签：e签宝 / 腾讯电子签 / 法大大 / 其他 / 暂无
  消息通知：飞书 / 钉钉 / 企业微信 / 其他
```

### Step 4: 安装首批 Skills

基于前两步选择，推荐首批 skills：

```
推荐为您安装以下 skills：
  dispute-classifier      （劳动仲裁必备）
  nda-review             （合同审查入口）
  cease-desist            （IP侵权初步分析）
  breach-notification     （数据泄露响应）
  entity-compliance       （公司治理基础）

是否全部安装？ [Y/n]
```

### Step 5: 生成配置

输出：
- `~/.openclaw/skills/.manifest.yaml` — skill manifest
- `~/.openclaw/skills/.config.yaml` — 用户配置（场景/法律框架/工具链）
- `~/.openclaw/skills/.welcome.md` — 欢迎文档和快速开始

## --redo flag

重新运行全部问答，生成新配置（会提示备份旧配置）。

## --skip-questions flag

使用默认值快速初始化，不交互（适合自动化安装）。

---

*[YD] — Greater China Legal cold-start-interview v1.1.0*
