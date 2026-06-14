---
name: secret-identification-assessment
description: |
  分析secret-identification-assessment相关知识产权侵权问题。
  覆盖：侵权行为识别、证据收集、维权策略建议。
  适用情形：用户说"secret-identification-assessment"相关问题。
argument-hint: "[核心事实]"
legal_frame: cn-mainland
trigger_phrases:
  - 'secret-identification-assessment'
  - 'ip_infringement'
legal_sources:
  - name: '中华人民共和国知识产权相关法律'
    effective_date: 'varies'
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

## 数据源与判断框架引用

本 skill 引用以下 plugin 根级 references 与 CLAUDE.md：

- **判断框架**：`../../references/判断框架.md`（4 类型 IP 场景簇 + 商标/专利/著作权/商业秘密侵权判断 + 维权路径 + 赔偿计算 + 开源合规）
- **数据源清单**：`../../references/数据源清单.md`（[YD]/[WKL]/[GOV]/[BD]/[model] + CNIPA/版权局/海关 + 专利商标数据库 + 典型判例）
- **查询路径**：`../../references/查询路径.md`（主管机关 + 检索平台 + 案例库）
- **CLAUDE.md**：`../../CLAUDE.md`（公司基本信息 + IP 资产 + 数据源配置）
- **货币触发主题**：`../../../references/currency-watch.md`
- **数据源注册表**：`../../../references/data-source-registry.md`

来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）详见 `../../references/数据源清单.md` §八。
IP 类型判断与维权路径详见 `../../references/判断框架.md` §一/§七。

# /secret-identification-assessment

1. 读取用户提供的信息。
2. 识别侵权类型和行为。
3. 评估证据状况。
4. 给出维权策略建议。
5. 升级决策门。

---

# secret-identification-assessment

## 目的

[说明本技能目的]

## 法域假设

默认中国大陆法域 `[SME 核查]`。

## 加载信息

- [用户提供的相关信息]

## 工作流程

### 第一步：信息提取

| 信息项 | 内容 |
|--------|------|
| 权利内容 | [___] |
| 涉嫌侵权行为 | [___] |
| 当事人角色 | [权利人/侵权人] |
| 已有证据 | [___] |

### 第二步：侵权分析 `[SME 核查]`

- **侵权类型**：[___]
- **构成要件**：[___]
- **举证要求**：[___]

### 第三步：维权策略

| 维权路径 | 适用场景 | 效果 |
|---------|---------|------|
| 协商和解 | 侵权轻微、双方有意愿 | 快、成本低 |
| 发送律师函 | 侵权明确、需要施压 | 中等效果 |
| 行政投诉 | 商标/专利/著作权侵权 | 行政执法快 |
| 民事诉讼 | 损失较大、需要赔偿 | 效果强但周期长 |
| 刑事报案 | 严重侵权、达到立案标准 | 最强震慑 |

### 第四步：升级决策门

> "知识产权侵权案件建议委托知识产权律师代理。涉及技术问题的案件可能需要申请鉴定。行政投诉和刑事报案须达到相应条件。这不构成法律意见。"

## 输出格式

```
# secret-identification-assessment — [简要描述]

## 基本信息
| 要素 | 内容 |
|------|------|
| 权利内容 | [___] |
| 侵权行为 | [___] |
| 证据状况 | [___] |

## 侵权分析 `[SME 核查]`
- 侵权类型：[___]
- 构成要件满足度：[___]

## 维权策略建议
- 首选：[___]
- 备选：[___]

## 建议后续行动
- [ ] [___]
- [ ] 委托律师代理 `[SME 核查]`
```

## 本技能不涵盖

- **代理诉讼或行政程序**
- **确认侵权事实** — 须由法院认定 `[SME 核查]`
