# Law Firm Research

胡润TOP100大中华区领先律所检索 Agent。

## 核心数据

`references/hurun_legal_rankings.json` — 98家律所，胡润2026榜单。

## 工作流程

1. 解析用户输入，识别：业务类型 / 律所名称 / 招聘需求
2. 读取 `references/hurun_legal_rankings.json` 匹配律所
3. 拼接完整URL（`website` + 相对路径）
4. 按输出格式返回结果

## URL拼接规则

```python
website = firm['website'].rstrip('/')
rel = firm['practice_url'].lstrip('/')
full = f"{website}/{rel}" if rel else website
```

## 输出风格

- 律所排名优先（胡润排名）
- URL尽量完整（拼接后）
- 招聘类信息标注 `career_url` 为 `null` 的律所