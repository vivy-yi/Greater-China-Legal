---
name: bar-prep-questions
description: >
  法考/JD 备考客观题与主观题训练（S1+S3）。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: law-student
last_reviewed: 2026-06
version: 2.0.0
risk_level: low
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /bar-prep-questions — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 法考/JD 备考客观题与主观题训练

**所属场景：** S1+S3

## 二、判断树

**Node 1：** 客观题还是主观题？
  - 客观题：单选/多选/不定项；主观题：案例分析/论述

**Node 2：** 考试类型？
  - 法考/学硕/JD 三类，分数权重不同

**Node 3：** 学科？
  - 民法/刑法/民诉/刑诉/行政/商法/经济法/三国法
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 法考 | 9月客观题（180道选择）+10月主观题（5道大题） |
| 学硕 | 全国联考：政治+英语+法学综合+业务课 |
| JD | 中国 JD 试点 14 所院校，各校自主命题 |

## 四、数据源锚定

- **主要数据源：** [YD] 历年真题 / [WKL] 主观题参考答案
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，建议咨询专业指导或转人工：
- 涉及具体案件的法律意见
- 跨学科综合问题
- 学术规范争议（需导师复核）

## 六、输出路径

```
law-student/bar-prep-questions/[session-id]/output.md
```

---

*Greater China Legal — law-student bar-prep-questions B-phase v2.0.0（场景优先重构）*
