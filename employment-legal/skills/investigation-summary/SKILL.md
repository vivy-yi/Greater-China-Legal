---
name: investigation-summary
description: '从保密调查报告起草面向特定受众的摘要 — HR版、管理层版、外部律师版。 适用情形：调查报告需要传达给不应看到完整保密工作成果的受众。

  '
argument-hint: '[事项名称] [受众: hr / leadership / outside-counsel]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
user_invocable: true
legal_sources:
- type: statute
  name: Labor Contract Law of the PRC
  article: Article 39 (Employer's right to dissolve)
  effective_date: 2012-07-01
  jurisdiction: cn-mainland
risk_level: low
escalation_triggers:
- 向外部律师披露前须确认律师-委托人特权状态（中国大陆无强制特权，但须评估）
trigger_phrases:
- 调查报告
- 总结
---

## 数据源与判断框架引用

本 skill 引用以下 plugin 根级 references 与 CLAUDE.md：

- **判断框架**：`../../references/判断框架.md`（跨 skill 决策路由 + 5 节点判断 + 解除子流程）
- **数据源清单**：`../../references/数据源清单.md`（[YD]/[WKL]/[GOV]/[BD]/[model] 标注规则 + 路由优先级）
- **查询路径**：`../../references/查询路径.md`（法规/案例/地方数据实际检索入口）
- **CLAUDE.md**：`../../CLAUDE.md`（核心法规 + 高风险情形 + 各省市差异 + 计算框架）
- **货币触发主题**：`../../../references/currency-watch.md`（高频更新主题清单）
- **数据源注册表**：`../../../references/data-source-registry.md`（GCL 全局数据源治理）

来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）详见 `../../references/数据源清单.md` §六。

# /investigation-summary

从保密调查报告起草面向特定受众的摘要。

## 工作流程

1. 加载 `internal-investigation` 参考 Skill，执行 Mode 5（受众摘要）
2. 如调查报告尚不存在，先起草报告
3. HR摘要不得包含律师心理印象、可信度评估方法或法律风险分析

---

## 使用说明

**管辖法域默认为中国大陆。** 如涉及香港/澳门/台湾/新加坡：
`/employment-legal:investigation-summary --frame hk`

---

## 受众类型

### HR版
- 可采取的行动建议
- 须注意的合规问题
- 后续跟踪事项
- 不含调查细节（保密需要）
- 不得包含律师心理印象、可信度评估方法、法律风险分析

### 管理层版（董事会/高管）
- 结论先行
- 关键证据摘要（3-5条）
- 建议行动（简洁）
- 不含敏感细节（保护被调查对象隐私、保留内部调查完整性）

### 外部律师版
- 完整背景信息
- 调查范围和已完成的来源
- 关键证据和问题
- 法律分析待律师完成

---

## 示例

```
/employment-legal:investigation-summary [事项名称] hr
```

```
/employment-legal:investigation-summary [事项名称] leadership
```

```
/employment-legal:investigation-summary [事项名称] outside-counsel
```

---

## 本 Skill 依赖

`internal-investigation` 参考 Skill 中的受众裁剪规则和摘要模板。

---

## 本 Skill 不涵盖

- 代理劳动仲裁或诉讼代理
- 代理与公安机关的沟通