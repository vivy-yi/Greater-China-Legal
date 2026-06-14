---
name: cold-start-interview
description: >
  通用冷启动初始化向导——自动扫描场景 CLAUDE.md 中的 [填空] 和 [PLACEHOLDER]
  标记，逐个生成访谈问题，收集答案后填充到文件中。
  适用情形：首次安装、CLAUDE.md 仍有 [填空] 标记、--redo 重新运行。
argument-hint: "[场景名] [--redo]"
trigger_phrases:
  - 冷启动
  - 初始化
  - 配置向导
  - 场景配置
  - 首次设置
last_reviewed: 2026-06
legal_frame: cn-mainland
version: 1.0.0
risk_level: low
---

# /cold-start-interview — 通用冷启动向导

## 原理

每个场景的 CLAUDE.md 包含 `[填空]` 和 `[PLACEHOLDER]` 标记。本向导自动扫描这些标记，将配置信息的采集转化为一问一答的访谈流程。

## 工作流程

### Step 0：识别目标场景

确定需要配置的场景：

- 如用户在 `plugins/scenes/<scene>/` 目录下调用的，直接读取该场景的 CLAUDE.md
- 如用户直接运行 `/cold-start-interview`，询问：
  > "要为哪个场景做初始化配置？可选：contract-review / data-compliance / litigation-support / ..."

### Step 1：读取场景 CLAUDE.md

读取 `plugins/scenes/<scene>/CLAUDE.md`，扫描所有 `[填空]` 和 `[PLACEHOLDER]` 标记。

标记示例：
```
**公司名称：** [填空]
**业务描述：** [填空：公司主营业务]
**外部律师：** [填空：常年法律顾问/专项律师联系方式]
Role: [PLACEHOLDER — Lawyer / legal professional | Non-lawyer ...]
```

### Step 2：分类访谈问题

将扫描到的标记按类型分组，逐组提问：

#### 2a：角色确认

```
系统：请选择您的角色：
A) 律师/法务人员
B) 业务部门（有律师支持）
C) 业务部门（无律师支持）
```

用户选择后写入 Role 字段。

#### 2b：公司基本信息

提取 `## 公司基本信息` 节下的所有 `[填空]`，逐一提问：

```
系统：公司名称是什么？
用户：XX科技有限公司

系统：公司主营业务是什么？
用户：软件开发

系统：外部律师的联系方式是？
用户：XX律所，张律师，138xxxx
```

#### 2c：场景特定配置

提取业务规则相关的 `[填空]`：

```
系统：合同金额超过多少需要送法务审核？
用户：50万
   → 写入 合同金额阈值 > 500万 列（如果有对应字段）

系统：常用的争议解决方式是仲裁还是诉讼？
用户：仲裁
   → 写入 争议解决路径
```

### Step 3：写入 CLAUDE.md

将所有收集到的答案填入对应的 `[填空]` 位置。

输出格式示例：
```
[场景名] 冷启动完成 ✅

已配置字段：
- 公司名称：XX科技有限公司
- 角色：律师/法务人员
- 外部律师：XX律所
- 合同审批阈值：50万

⚠️ 仍有未配置字段（可选）：
- [字段名] — 如不填写将使用默认值

运行 /cold-start-interview --redo 可重新配置。
```

### Step 4：验证

确认 CLAUDE.md 中不再有 `[填空]` 标记。如有遗漏，提示用户：

```
以下字段仍为 [填空] 状态，建议补充：
- [字段列表]
```

## 标记采集规则

| CLAUDE.md 中的标记 | 生成的访谈问题 |
|-------------------|--------------|
| `[填空]` | 读取上下文。如前面是 "公司名称："，问"公司名称是什么？" |
| `[填空：提示语]` | 用提示语作为问题。如"[填空：公司主营业务]" → 问"公司主营业务是什么？" |
| `[PLACEHOLDER — 描述]` | 用描述内容作为问题。如"Role: [PLACEHOLDER — Lawyer / legal professional | Non-lawyer]" → 提供选项让用户选择 |
| `[自动填写]` | 不问，从上下文推导 |

## 本技能不做什么

- 不提供法律建议。只构建配置模板。
- 不验证用户输入的真实性。
- 不改变已有配置——只填充 [填空] 标记，不会覆盖已填写的字段。

---

*Greater China Legal — shared cold-start-interview v1.0.0*
