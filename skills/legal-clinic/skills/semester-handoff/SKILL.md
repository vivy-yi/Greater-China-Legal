---
name: semester-handoff
description: >
  学期末案件交接——确保连续性（通用（学期交接））。
argument-hint: "[输入]"
legal_frame: cn-mainland
scene_cluster: legal-clinic
last_reviewed: 2026-06
version: 2.0.0
risk_level: medium
---

## 数据源与判断框架引用

本 skill 引用场景级配置 `../../CLAUDE.md`。
来源标注规范（[YD]/[WKL]/[BD]/[GOV]/[model]）参见场景级 references/ 目录。

# /semester-handoff — China Mainland（B 重构 v2.0.0）

## 一、场景识别

**核心定位：** 学期末案件交接——确保连续性

**所属场景：** 通用（学期交接）

## 二、判断树

**Node 1：** 交接类型？
  - 完整交接/临时交接/紧急交接

**Node 2：** 案件阶段？
  - 受理/审理中/结案前

**Node 3：** 交接对象？
  - 下届学生/其他诊所/督导
**最终输出：** 基于判断树结果，给出针对性输出。

## 三、场景差异

| 场景 | 说明 |
|---|---|
| 学期中 | 工作日志+文件夹 |
| 学期末 | 全套档案+案件评估 |
| 紧急 | 电子移交+电话确认 |

## 四、数据源锚定

- **主要数据源：** [BD] 学期交接档案
- **辅助源：** [model] 法律推理
- **更新策略：** 法条/案例数据实时校对（[YD]）

## 五、升级决策门

触发以下任一情形，必须升级至督导/专业律师：
- 涉及具体案件的法律意见
- 案件复杂程度超过学生能力（须督导介入）
- 时效紧迫或金额重大
- 刑事案件会见/阅卷/辩护意见
- 行政诉讼复议前置/被告主体认定
- 跨学科/跨法域问题

## 六、输出路径

```
legal-clinic/semester-handoff/[client-id]/output.md
```

---

*Greater China Legal — legal-clinic semester-handoff B-phase v2.0.0（场景优先重构）*
