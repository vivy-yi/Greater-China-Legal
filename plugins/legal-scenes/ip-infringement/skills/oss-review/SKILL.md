---
name: oss-review
description: '开源许可证合规审查——依赖列表/单库/ outbound代码的许可证检查。 适用情形：审查package.json/requirements.txt/go.mod等依赖清单的许可证合规。

  '
argument-hint: '[文件路径 | 包名 | 代码仓库路径]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
- 开源软件
- 许可证
legal_sources:
- name: 中华人民共和国民法典
  effective_date: '2021-01-01'
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /oss-review — China Mainland

## CN开源合规特殊说明

**中国企业的特殊考量：**
- 出口管制：部分开源软件受中国出口管制法规约束
- 数据安全：涉及数据处理的开源库须通过网络安全审查
- 国密算法：金融/政府相关项目须使用国密算法替代

---

## 许可证分类

| 类别 | 许可证示例 | 义务 |
|---|---|---|
| ** permissive** | MIT, BSD, Apache-2.0 | 保留版权声明即可 |
| **弱copyleft** | LGPL, MPL | 修改部分须开源，库本身可闭源 |
| **强copyleft** | GPL-3.0, AGPL-3.0 | 衍生作品整体须开源 |
| **非OSI认证** | SSPL, BUSL, Commons Clause | 非开源，需商业许可 |
| **未知** | 无LICENSE文件 | 须人工确认 |

---

## CN常见合规问题

### 强copyleft风险（GPL类）
- SaaS服务如果传输代码给用户，可能触发"传播"义务
- AGPL-3.0：通过网络对外提供服务也须开源

### 非OSI认证许可证
- SSPL (MongoDB) — 不是开源许可证，商业使用须申请商业许可
- Elastic License — 禁止提供云服务
- Commons Clause — 禁止商业销售

### 许可证冲突
- GPL代码不得与 proprietary代码直接结合
- Apache-2.0 + GPL-2.0 可能存在兼容性冲突

---

## 部署模式影响义务

| 模式 | 义务 |
|---|---|
| SaaS（对外提供服务）| AGPL/GPL可能要求开源 |
| 分发二进制 | 须保留许可证声明，提供源代码 |
| 内部使用 | 义务较轻，但仍须遵守许可证 |
| 嵌入式产品 | 须开源整产品（GPL传染性）|

---

## 审查输出

```
## 开源许可证合规报告

### 高风险（须替换或寻求商业许可）
🔴 [包名] — [许可证] — [问题] — [建议]

### 中风险（须法律意见）
🟠 [包名] — [许可证] — [问题] — [建议]

### 低风险（可直接使用）
🟡 [包名] — [许可证] — [合规条件]

### 许可证分布
- permissive: [N]个
- weak copyleft: [N]个
- strong copyleft: [N]个
- non-OSI: [N]个
- unknown: [N]个
```

---

*Greater China Legal — ip-legal oss-review CN adapter v1.0.0*
