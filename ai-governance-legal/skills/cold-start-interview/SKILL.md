---
name: cold-start-interview
description: >
  AI治理实践冷启动向导——了解AI系统组合、监管范围和合规状态。
  适用情形：首次使用、配置缺失 [--redo]、或 [--check-integrations]。
argument-hint: "[--redo | --check-integrations]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# /cold-start-interview — China Mainland

## CN AI治理初始化询问

### 1. AI系统组合

**须识别以下类型的AI系统：**
- 算法推荐系统（内容推荐/商品推荐）
- 深度合成系统（AI换脸/语音合成）
- 生成式AI服务（LLM/图像生成）
- 自动驾驶系统（L2+/L3/L4）
- 人脸识别/生物识别系统

### 2. 监管范围

**CN主要监管机关：**
- 国家网信办（CAC）— 算法推荐/深度合成/生成式AI
- 工业和信息化部（MIIT）— 电信合规
- 公安部 — 个人信息采集
- 交通运输部 — 自动驾驶

### 3. 合规状态

**当前合规状态检查：**
- 算法备案（是否已完成）
- 安全评估（是否在有效期内）
- 个人信息保护评估（是否已做）

---

## 输出

创建 `AI_SYSTEMS.yaml` 清单文件。

---

*Greater China Legal — ai-governance-legal cold-start-interview CN adapter v1.0.0*