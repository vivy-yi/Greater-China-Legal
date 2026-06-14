---
name: demand-draft
description: '根据完成接收的案件起草律师函——须通过特权/保密检查。 适用情形：用户说"起草律师函"、"写催告函"。

  '
argument-hint: '[slug] [--skip-gate] [--version=N]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
- 律师函起草
- 催款函
legal_sources:
- name: 中华人民共和国民法典
  effective_date: '2021-01-01'
---

## 数据源与判断框架引用

本 skill 引用以下 plugin 根级 references：

- **判断框架**：`../../references/判断框架.md`（诉讼全流程 35 skill + 14 类时效 + 案由分析 + 管辖判断 + 证据规则 + 保全 + 强制措施 + 执行 + 行政复议/诉讼 + 案件管理 + 上诉 + 刑事案件 + 政府合同）
- **数据源清单**：`../../references/数据源清单.md`（[YD]/[WKL]/[GOV]/[BD]/[model] + 最高法司法解释 + 法院体系 + 仲裁机构 + 知产法院 + 涉外）
- **查询路径**：`../../references/查询路径.md`（法规 + 案例 + 司法解释）
- **货币触发主题**：`../../../references/currency-watch.md`
- **数据源注册表**：`../../../references/data-source-registry.md`

来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）详见 `../../references/数据源清单.md` §十一。
诉讼时效详见 `../../references/判断框架.md` §三（**时效管理是高风险点**）。

# /demand-draft — China Mainland

## CN律师函起草工作流

### Step 1：读取案件接收文件

读取 `demand-letters/[slug]/intake.md` 中的案件信息。

---

### Step 2：预起草Gate检查

**每个Gate必须明确回应后才能起草：**

#### 特权检查
> 是否存在特权问题？
- 特权放弃的风险
- 律师-当事人特权

#### 保密性检查
> 律师函内容是否涉及保密信息？

#### 事实准确性检查
> 律师函中的事实陈述是否有证据支持？
- 引用合同条款必须有原文依据
- 引用邮件/通信必须为原文

#### 语气检查
> 语气是否适当？（不过于激进也不过于软弱）

---

### Step 3：CN律师函格式

**CN律师函须包含：**
1. 发函律所/律师信息
2. 收函方信息
3. 函件编号
4. 日期
5. 事实陈述（清晰、简洁、有证据支持）
6. 法律依据（《民法典》相关条款）
7. 要求（明确、具体、可执行）
8. 后果警告（如不履行的法律后果）
9. 律师签字/盖章

---

### Step 4：CN律师函特殊要求

**CN律师函法律效力：**
- 律师函不等于法院裁定
- 恶意发函可能构成不正当竞争
- 不得捏造虚假事实

**CN律师函中的时效提示：**
- 劳动争议：60日仲裁时效
- 合同纠纷：3年诉讼时效
- 应当在时效期间内发送

---

## 输出格式

```
## 律师函草稿 — [对方当事人]

[完整律师函内容]

---
审查状态：[待审/已批准]
发送前确认：
□ 特权问题已检查
□ 事实陈述有证据支持
□ 法律依据准确
□ 时效已考虑
□ 律师已审核
```

---

*Greater China Legal — litigation-legal demand-draft CN adapter v1.0.0*