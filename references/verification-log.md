# 验证日志
*Greater China Legal — Verification Log*

---

## 目的

记录每个法规引用/事实的验证履历，避免重复验证，建立机构记忆。

同一引用在所有 matters 间通用（除非 matter workspace 隔离）。

---

## 格式

```
[YYYY-MM-DD] [引用/事实] verified by [姓名] against [来源] — [结果]
```

**结果选项：**
- `confirmed` — 确认，无修改
- `corrected to X` — 确认，但正确值是 X（原值有误）
- `disputed` — 有争议，建议律师复核
- `could not verify` — 无法验证（缺少来源/来源不可访问）

---

## 示例

```
[2026-06-01] 劳动合同法第47条 verified by 张律师 against [YD] — confirmed
[2026-06-01] 上海市2025年最低工资2690元/月 verified by 李律师 against [GOV] — confirmed
[2026-06-02] 经济补偿金基数计算方式 verified by 王律师 against [YD] + [WKL] — confirmed（两源一致）
[2026-06-03] 竞业限制最长期限 verified by 陈律师 against [YD] — corrected to 2年（原为3年，2024年修订）
```

---

## 有效期规则

| 引用类型 | 有效期 | 说明 |
|---|---|---|
| 法规条文 | 90天 | 法律修订可能发生 |
| 案例引用 | 180天 | 案例法可能变化 |
| 工资/基数标准 | 30天 | 年度更新频繁 |
| 地方裁判口径 | 60天 | 裁判口径可能随政策调整 |
| 中央政策/通知 | 60天 | 政策可能调整 |

**超过有效期的引用：**
Skill 输出时标注：`⚠️ 该引用上次验证于 [YYYY-MM-DD]，已超过有效期，建议重新验证`

---

## 最近验证记录

（按验证日期倒序，最新在上）

---

*最后更新：2026-06*
*Greater China Legal — Verification Log*