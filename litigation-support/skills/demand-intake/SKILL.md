---
name: demand-intake
description: '律师函发送前的预起草信息收集——写入intake.md供demand-draft读取。 适用情形：用户要求"准备律师函"、"运行intake后再起草"。

  '
argument-hint: '[标题] [--full]'
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
trigger_phrases:
- 律师函
- 催告
- 权利要求
legal_sources:
- name: 中华人民共和国民法典
  effective_date: '2021-01-01'
---

# /demand-intake — China Mainland

## CN律师函接收工作流

### 收集信息

1. **当事人信息**
   - 我方名称
   - 对方名称
   - 关系背景

2. **事实基础**
   - 发生了什么
   - 时间线
   - 关键证据

3. **法律依据**
   - 合同条款（如有）
   - 相关法律条文（《民法典》）

4. **我方诉求**
   - 具体要求
   - 金额（如有）
   - 时间节点

5. **谈判筹码**
   - 我方优势
   - 对方弱点
   - 最佳替代方案（BATNA）

---

### CN律师函特别注意事项

- 时效：劳动争议60日、合同纠纷3年
- 语气：不过于激进，不捏造事实
- 证据：每个事实陈述都须有依据

---

## 输出

写入 `demand-letters/[slug]/intake.md`，然后提示：
"Intake已保存。准备好后运行 `/litigation-legal:demand-draft [slug]`"

---

*Greater China Legal — litigation-legal demand-intake CN adapter v1.0.0*