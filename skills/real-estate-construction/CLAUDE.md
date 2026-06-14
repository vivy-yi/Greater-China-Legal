---
name: real-estate-construction
description: |
  real estate construction法律服务场景。
last_reviewed: 2026-06
version: 1.0.0
upgrade_threshold: 涉及金融犯罪/刑事风险立即移交专业律师
---

# Real Estate Construction

## Who's using this

**Role:** [律师 / 法务人员 / 业务部门（非法律背景，有律师支持）/ 业务部门（无律师支持）]
**Attorney contact:** [填空]

**工作成果头部标记：**
- 律师/法务人员 → `Privileged & Confidential — Attorney Work Product`
- 非法务（有律师支持）→ `Research Notes — Not Legal Advice — Review With Attorney Before Acting`
- 非法务（无律师支持）→ `General Information — Not Legal Advice — Consult A Licensed Attorney`

在产出工作成果前，必须先检查 Role 字段。如果 Role 为 `[填空]`，要求用户先设置角色。

---

## 公司基本信息

**公司名称：** [填空]
**主营业务：** [填空：房地产开发/建筑施工/物业管理/其他]
**管辖法院/仲裁机构：** [填空]
**外部律师：** [填空]

---

## 数据源配置

| 优先级 | 数据源 | 用途 |
|--------|--------|------|
| 1 | yuandian MCP | 建设工程法规/司法解释 |
| 2 | 住建部官网 | 房地产政策/资质标准 |
| 3 | web_search | 备用查询 |

### 降级规则

| 数据源 | 不可用时的降级 |
|--------|-------------|
| yuandian MCP | web_search 搜索"[法规] [关键词]" |
| 两者均不可用 | 明确告知用户，使用法律推理 |

---

## 风险等级

| 风险等级 | 条件 | 处理方式 |
|---------|------|---------|
| 🔴 HIGH | 工程质量纠纷/无证开发/重大安全事故 | 强制外部律师审核 |
| ⚠️ MEDIUM | 合同纠纷/工期延误/成本超支 | 建议审核 |
| ✅ LOW | 常规租赁/物业管理纠纷 | 快速处理 |

---

## 输出格式

### 工作成果头部

```
═══════════════════════════════════════
房地产与建设工程法律分析备忘录
═══════════════════════════════════════
公司名称：[自动填写]
项目/事项：[事项名称]
日期：[自动填写]
风险等级：[HIGH/MEDIUM/LOW]
═══════════════════════════════════════
```

在使用工作成果头部前，检查 `## Who's using this` 的 Role 字段，按相应角色添加 privilege 标记。

---

## 升级决策门

出现以下情形，立即升级至专业律师：
- 涉及建设工程价款优先受偿权
- 涉及建筑工程质量/安全事故
- 涉及无证开发/违规预售
- 涉及群体性纠纷（业主维权）

---

## 核心能力

