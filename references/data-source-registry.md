# 法律数据源注册表
*Greater China Legal — Data Source Governance*

---

## 核心理念

**数据源治理原则：**
- Skill 输出用 `[legal_db]` 标注来源，而非绑定单一 MCP
- 实际数据源通过注册表动态路由，而非硬编码
- 关键结论须多源交叉验证
- 数据源质量持续评分，不合格则降级
- **来源标注描述实际做了什么，不是你希望 claim 什么**

---

## 来源标注体系（5级）

| 标注 | 含义 | 触发条件 |
|---|---|---|
| `[YD]` | 元典检索结果 | yuandian-mcp 实际返回了该结果 |
| `[WKL]` | 无合力检索结果 | weiken-mcp 实际返回了该结果 |
| `[BD]` | 北达检索结果 | beidalu 实际返回了该结果 |
| `[GOV]` | 政府平台数据 | 官方网址直接访问的结果 |
| `[web]` | 网络搜索结果 | 通过 web search 工具获取 |
| `[model]` | 模型知识（须核实） | 默认 fallback |
| `[user]` | 用户提供的文件 | 用户直接粘贴/上传 |
| `[settled — last confirmed YYYY-MM-DD]` | 已验证的稳定引用 | 曾在 primary source 确认过，且在有效期内 |

**标注原则：**
- 禁止 promotion：不能因为"这个引用看起来是对的"就把 `[model]` 标为 `[YD]`
- tag 描述的是：这次会话里这个引用真正从哪里来的
- `[model]` 是默认 fallback，不是羞耻标注——它只是诚实地说"我不知道它从哪来"

---

## Pre-flight Citation Check（引用前测试）

**每次 Skill 引用法规/案例前，必须执行：**

```
1. 测试 legal research connector 是否真的在响应
   → 发送一个测试查询（如"劳动合同法第47条"）
   → 验证是否返回有效结果

2. 如 connector 未连接 / 无返回：
   → 将以下内容记录到输出的 Sources 行：
     "connector not connected — cites from training knowledge, 
      verify before relying"
   → 不输出独立的 banner，但 per-citation 的 `[model]` tag 保留

3. 如 connector 正常响应：
   → 正常引用，标注对应 tag（如 [YD]）
```

**为什么这是关键设计：**
- 配置了 connector ≠ connector 在工作（网络问题/API key过期/服务下线）
- 如果不测试就引用，可能在用户不知情的情况下输出了 model 知识
- 验证动作应该在 Skill 生命周期早期执行，不是在输出时才被发现

---

## Currency Trigger（货币触发）

**以下情形必须 web search，不能直接用模型知识：**

| 情形 | 示例 | 原因 |
|---|---|---|
| 近期案例/生效日期 | "这个法规什么时候生效的" | 模型知识总是过期的 |
| 执法姿态/监管动向 | "最近劳动仲裁口径有什么变化" | 季度级更新，模型赶不上 |
| 年度更新的阈值 | "2025年上海最低工资是多少" | 每年更新，模型无法确认是哪年 |
| 征求意见稿/新法 | "刚刚通过的个人信息保护法" | 尚未生效，状态不稳定 |
| currency-watch.md 内的主题 | （按监控清单执行） | 主动追踪的变更点 |

**判断标准：**
> 如果一个firm alert在这个话题上有"近期动态"部分，这个话题就触发currency trigger。

**执行流程：**
```
问题涉及 currency trigger 主题？
    ↓ 是
执行 web search（或调用 [GOV] connector）
    ↓
结果标注 [web] 或 [GOV]
    ↓
如无有效结果，标注 [model — verify] 并输出：
  "Note: 这个问题依赖最新法规动态，我无法确认当前状态。
   建议通过 [GOV] 或 [YD] 查询确认后再做决策。"
```

---

## 三值系统（禁止静默补充）

**Skill 需要信息但没有时，有三种有效响应，不是两种：**

### 情况A：补充 + flag（继续执行）
```
可用 web search / 模型知识补充
→ 标注来源（如 [web]、[model]）
→ 继续执行，结论处加 [review] 供律师复核

示例：
"关于竞业限制的判决惯例，我通过 [web] 找到以下参考，
 但地方裁判口径可能有差异，建议 [review]。"
```

### 情况B：停下 + 请求补充（停止等待）
```
关键信息缺失，无法继续
→ 不继续分析，直接请求用户提供
→ 格式："我需要以下信息才能继续：[具体缺失内容]"

示例：
"要计算经济补偿金，我需要知道员工离职前12个月的平均工资。
 请提供或确认：[数据]。"
```

### 情况C：flag 但不替代分析（已知疑问但不改变结论）
```
知道某个信息可能影响结论，但无法用它改变分析
→ 输出时标注该已知疑问（tag: [model knowledge — verify]）
→ 分析基于"假设该法规仍在有效状态"继续
→ 不因已知疑问而改变结论方向

示例：
"Note: 我注意到这项规定可能自上次确认以来有过修订 
（[model knowledge — verify]）。我的分析基于其现行有效状态，
 建议在决策前验证其最新状态。"
```

**静默补充的禁止：**
- 沉默地用一个不确定的信息改变了结论方向 = 误导
- 这种情况比"直接说不知道"更危险，因为它更难被察觉

---

## 验证日志（Verification Log）

**每次验证一个引用后，写入：**
```
~/.claude/plugins/config/greater-china-legal/verification-log.md
```

**格式：**
```
[YYYY-MM-DD] [引用/事实] verified by [姓名] against [来源] — [结果]
[YYYY-MM-DD] 劳动合同法第47条 verified by 张律师 against [YD] — confirmed
[YYYY-MM-DD] 上海市2024年最低工资 verified by 李律师 against [GOV] — confirmed 2690元/月
```

**规则：**
1. 验证日志按 plugin 维度，不是按 matter——同一个引用在 matters 间通用
2. 验证结果有有效期（按引用类型）：
   - 法规条文：90天（法律修订可能发生）
   - 案例引用：180天（案例法可能变化）
   - 工资/基数标准：30天（年度更新频繁）
3. 验证结果过期后，Skill 输出中提示："该引用上次验证于 [日期]，已超过有效期，建议重新验证"
4. 验证日志可通过 `log-verification` skill 追加

**Verification Log 存储位置：**
```
references/verification-log.md
```
（与 data-source-registry.md 同级，供所有 Skill 共用）

---

## 数据源路由规则

### 按查询类型路由

| 查询类型 | 首选 | 备选 | 说明 |
|---|---|---|---|
| 劳动法法规条款 | YD | BD | YD有地方配套规定 |
| 劳动仲裁案例 | YD | WKL | YD劳动案例覆盖更全 |
| 地方裁判口径 | YD | - | YD独家收录 |
| 中央法规原文 | BD | WKL | BD原文最准确 |
| 最低工资标准 | GOV | YD | GOV最权威，YD有时效 |
| 社保缴纳基数 | GOV | YD | GOV官方公告 |
| 综合法律检索 | WKL | YD | WKL覆盖面广 |
| 近期动态/执法口径 | [web] | YD | currency trigger 场景 |

### 按法域路由

| 法域 | 首选 | 备选 |
|---|---|---|
| 中国大陆 | YD | WKL / GOV |
| 香港 | WKL | BD |
| 澳门 | WKL | BD |
| 台湾 | WKL | BD |
| 新加坡 | WKL | - |

---

## 数据源连接性检测

**每次启动 Skill 时执行连接性测试：**

```python
# 伪代码：连接性检测
def test_connector(connector_id):
    test_query = "劳动合同法第一条"  # 已知稳定查询
    result = connector.search(test_query)
    if result and len(result) > 0:
        return "connected"
    else:
        return "not_connected"

# Skill 输出 Sources 行示例：
# Sources: [YD] connected, [WKL] not connected — [model knowledge] for case citations
```

**自动降级触发：**
- 连续3次检索无结果 → 该数据源标记为 degraded
- Skill 输出时提示："[YD] degraded — results may be stale"
- 评分低于3星 → 从注册表移除，路由自动切换到备选

---

## 多源交叉验证规则

### 必须交叉验证的情形

1. **关键结论**：补偿金计算/违法解除认定/竞业限制有效性
2. **新型问题**：平台经济用工/灵活用工等新兴领域
3. **地方差异**：涉及非北上广深地区

### 交叉验证方法

```
关键结论 = 2个以上数据源一致确认
         ↓
         如不一致，输出：
         "⚠️ 来源冲突：[YD]说是A，[WKL]说是B。请律师复核。"
         ↓
         律师复核结果写入 verification-log.md
```

---

## 来源标注格式

Skill 输出中统一使用：

| 标注 | 含义 | 调用方式 |
|---|---|---|
| `[legal_db]` | 法律数据库通用标注（路由后实际为YD/WKL/BD） | 自动路由 |
| `[YD]` | 元典检索结果 | yuandian-mcp |
| `[WKL]` | 无合力检索结果 | weiken-mcp |
| `[BD]` | 北达检索结果 | beidalu-mcp |
| `[GOV]` | 政府平台数据 | 人社部/税务局官网 |
| `[web]` | 网络搜索结果 | web search |
| `[model]` | 模型知识（请核实） | - |
| `[user]` | 用户提供的文件 | - |

**输出格式示例：**

```
【Greater China Legal — 劳动法实务工作成果】
⚠️ 复核提示：
- 本文件依据中国劳动法出具，法规引用已标注来源
- 关键结论已进行多源验证，不一致处已标注
- 连接性检测：[YD] connected, [WKL] not connected
- 来源标注：[YD]=元典 / [WKL]=无合力 / [BD]=北达 / [GOV]=政府平台 / [web]=联网检索 / [model]=模型知识(请核实)
- 数据源路由规则详见：references/data-source-registry.md

---

## 经济补偿金计算

依据：[YD] 劳动合同法第47条 + [GOV] 上海市2025年社保基数

...
```

---

## 数据源注册表维护

- **更新频率**：每季度审查一次质量评分
- **新增数据源**：通过 PR 提交，附测试报告和质量评估
- **移除数据源**：质量评分低于3星或有3次严重错误记录
- **连接性检测**：每次 Skill 启动时自动执行

---

## References 目录结构

```
references/
├── data-source-registry.md    # 本文件
├── verification-log.md         # 验证履历（所有 Skill 共用）
└── currency-watch.md           # 货币监控清单（定期更新的主题列表）
```

---

*最后更新：2026-06*
*Greater China Legal — Data Source Governance*
*参考：anthropic/claude-for-legal pre-flight citation check + verification log 设计*