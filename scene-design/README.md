# B 重构：场景优先的 Skill 设计规范

## 核心理念

A 阶段（翻译式适配）已覆盖所有域，但仍是"US 工作流的中文翻译"。B 重构从中国法律工作的真实场景出发，重新设计 skill 体系。

## 三层结构

```
第一层：场景簇（scene cluster）
  law-student  → 4 个独立场景
  legal-clinic → 4 个独立场景
  law-firm/... → 4 个核心场景（已设计）

第二层：判断树（judgment tree）
  每个场景有完整的判断逻辑链
  不是 workflow，是 decision tree（先识别 → 再分流 → 再决策）

第三层：工具（tool）
  法规检索 [YD] yuandian / [GOV] 官方
  案例检索 [WKL] 裁判文书网 / [GOV] 指导案例
  文档生成 [BD] 内部 / [model] 推理
```

## 数据源锚定规范

每个 skill 输出必须锚定到具体数据源：

| 标签 | 含义 | 用途 |
|---|---|---|
| [YD] | 法律精灵/yuandian MCP | 实时法规+案例检索 |
| [WKL] | 裁判文书网/无讼/聚法 | 案例检索 |
| [GOV] | CNIPA/SAMR/CAC/MOJ | 官方数据 |
| [BD] | 内部数据/历史档案 | 内部检索 |
| [model] | 法律推理 | 推断性结论 |

## 判断树模板（每个 skill 必须遵循）

```
## 一、场景识别（Scene Recognition）
  问 X1？→ 场景分支 A
  问 X2？→ 场景分支 B

## 二、判断节点（Decision Nodes）
  Node 1：[关键事实判断]
    ├─ 是 → 走路径 X
    └─ 否 → 走路径 Y

## 三、地区/院校差异（Regional/Institutional Variance）
  各省市/各院校差异表（如适用）

## 四、输出锚定（Output Anchoring）
  引用数据源：[YD] [WKL] [GOV] [BD] [model]
  输出文件路径：clients/[id]/xxx.md

## 五、升级决策门（Escalation Gate）
  触发条件：[情形 A] → 移交专业律师
```

## law-student 场景簇（4 个）

| 场景 | skill 映射 | 核心判断 |
|---|---|---|
| S1 法考备考 | bar-prep-questions / exam-forecast / flashcards / irac-practice / case-brief | 客观题/主观题/重难点 |
| S2 法学硕博 | study-plan / outline-builder / session / legal-writing | 院校选择/科目难度/导师沟通 |
| S3 JD 备考 | bar-prep-questions（复用）/ cold-call-prep / socratic-drill / legal-writing | 案例教学法/英文案例 |
| S4 课程学习 | cold-call-prep / socratic-drill / irac-practice / case-brief | 课堂参与/案例分析/期末考试 |

## legal-clinic 场景簇（4 个）

| 场景 | skill 映射 | 核心判断 |
|---|---|---|
| C1 劳动法援 | client-intake / research-start / memo / draft / supervisor-review-queue / status / deadlines | 仲裁前置/60日时效/经济困难认定 |
| C2 消费者维权 | client-intake / client-letter / client-comms-log / form-generation | 消保法/小额诉讼/调解 |
| C3 婚姻家事 | client-intake / memo / draft / plain-language-letters | 婚姻法/继承/家事调解/未成年人保护 |
| C4 行政诉讼援助 | client-intake / research-start / memo / deadlines / supervisor-review-queue | 复议前置/民告官/被告主体 |

## 通用 skill（跨场景复用）

| skill | 适用场景 |
|---|---|
| cold-start-interview | law-student + legal-clinic 通用 |
| customize | 同上 |
| semester-handoff | legal-clinic 学期交接 |
| ramp | legal-clinic 入项 |

## 版本升级说明

- v1.x → A 阶段（翻译适配）
- v2.x → B 重构（场景优先 + 判断树 + 数据源锚定）
- v2.0.0 目标：每个 skill 50-150 行，可独立运行