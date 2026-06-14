---
name: legal-writing
description: >
  法律文书/学术写作（S2+S4）。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: law-student
last_reviewed: 2026-06
version: 2.0.0
risk_level: low
---

# /legal-writing — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 法律文书/学术写作

**所属场景：** S2+S4

## 二、判断树

**Node 1：** 写作类型？
  - 案例分析/课程论文/学年论文/学位论文

**Node 2：** 字数？
  - 2000/5000/10000/30000+

**Node 3：** 引用规范？
  - GB/T 7714（学术）/ 法学引注手册
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 学位论文 | 知网/万方查重，引注严格 |
| 课程论文 | 教师指定格式优先 |

## 四、数据源锚定

- **主要数据源：** [WKL] 学术案例 / [GOV] 法规
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/legal-writing/[session-id]/output.md
```

---

*Greater China Legal — law-student legal-writing B-phase v2.0.0（场景优先重构）*
