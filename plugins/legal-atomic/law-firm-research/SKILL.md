---
name: law-firm-research
description: >
  胡润TOP100大中华区领先律所检索——根据业务类型匹配合适律所，
  输出律所排名、官网、专业领域页/律师团队页/招聘页/新闻页直链。
  适用情形：用户说"找律所"、"推荐劳动法律师"、"哪家律所擅长IP"、
  "这个案子找哪个律所"、"查找金杜官网"、"律所团队页面"。
  数据来源：胡润智榜·大中华区卓越推荐律所TOP100（2026），98家律所。
argument-hint: "[业务类型/律所名称/招聘需求/其他需求]"
legal_frame: cn-mainland, hk, mo, tw, sg
last_reviewed: 2026-06
version: 1.0.0
risk_level: low
data_source: hurun_legal_rankings.json
data_scope: 98 firms
---

# 律所检索

根据用户描述的业务类型，从胡润TOP100大中华区卓越推荐律所中匹配合适律所。

## 数据文件

`references/hurun_legal_rankings.json` — 98家律所完整数据。

字段说明：

| 字段 | 说明 |
|---|---|
| rank | 胡润排名（1-98） |
| name | 律所名称 |
| website | 官网 |
| practice_url | 专业领域页相对路径 |
| team_url | 律师团队页相对路径 |
| career_url | 招聘页相对路径 |
| news_url | 新闻动态页相对路径 |
| status | explored / homepage_only / partial |
| capabilities_summary | 四项能力是否覆盖 |

**完整URL拼接规则：** `website` + `practice_url`（去掉开头的 `/`）

---

## 使用方式

### 方式一：按业务类型匹配

用户描述业务类型时，读取 JSON 数据，匹配相关律所：

```
输入："推荐几家擅长劳动仲裁的律所"
输出：按胡润排名列出提供劳动仲裁相关服务的律所，附官网+各页面URL
```

### 方式二：直接查询律所信息

用户指定律所名称时，返回该律所的全部链接：

```
输入："金杜律师事务所官网是什么"
输出：官网 + practice_url + team_url + career_url + news_url
```

### 方式三：查询招聘相关信息

```
输入："哪些律所在招聘律师/合伙人"
输出：胡润排名 + 律所名称 + 官网 + career_url（拼接完整URL）
```

---

## 输出格式

### 按业务类型推荐

**推荐律所（胡润TOP100）— [业务类型]**

| 排名 | 律所名称 | 官网 | 专业领域 | 律师团队 | 招聘 | 新闻 |
|---|---|---|---|---|---|---|
| 1 | 北京市金杜律师事务所 | [官网](url) | [专业领域](url) | [团队页](url) | [招聘页](url) | [新闻页](url) |
| ... | ... | ... | ... | ... | ... | ... |

### 直接查询律所

**[律所名称]**

- **胡润排名：** [rank]
- **官网：** [url]
- **专业领域：** [url]
- **律师团队：** [url]
- **招聘：** [url]
- **新闻动态：** [url]
- **数据状态：** [status]

---

## URL拼接示例

```python
# 拼接完整URL
website = firm['website'].rstrip('/')
practice_url = firm['practice_url'].lstrip('/')
practice_full_url = f"{website}/{practice_url}" if practice_url else website
```

示例：

- 金杜 practice：`https://www.kingandwood.com` + `expertise` → `https://www.kingandwood.com/expertise`
- 中伦 team：`https://www.zhonglun.com` + `team` → `https://www.zhonglun.com/team`

---

## 已知覆盖情况

| 能力 | 覆盖律所数 |
|---|---|
| 专业领域 | 71/98 |
| 专业人员（团队页） | 80/98 |
| 招聘页 | 60/98 |
| 新闻动态 | 79/98 |

无某项数据的律所，URL 位置填 `null`，不在表格中显示该列。

---

## 无法访问的2家（胡润原榜删除）

1. **江苏世纪同仁律师事务所** — 网站维护/无公网
2. **上海市联合律师事务所** — 原网站不可考

---

## 参考链接

- 胡润榜单原始页：https://hurun.net/zh-cn/info/detail?num=EYKWKBLUFTIX
- 数据来源：openclaw-site-agent / hurun_legal_rankings.json