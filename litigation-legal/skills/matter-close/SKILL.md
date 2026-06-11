---
name: matter-close
description: >
  关闭案件——记录结果、最终风险敞口和教训，存档而不删除记录。
  适用情形：用户说"[案件]结束了"或"记录和解/判决结果"。
argument-hint: "[slug]"
legal_frame: cn-mainland
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

# /matter-close — China Mainland

## CN案件关闭工作流

### 记录结果

**结果类型：**
- 和解（settled）
- 撤诉（dismissed）
- 判决我方胜诉（judgment-for）
- 判决对方胜诉（judgment-against）
- 撤回（withdrawn）
- 合并（consolidated）

### 最终敞口/成本

- 律师费
- 赔偿金额（如有）
- 机会成本

### 经验教训

- [学到什么]
- [下次如何改进]

---

## CN案件关闭特殊说明

**劳动争议：**
- 仲裁裁决后15日内可向法院起诉
- 一裁终局案件（小额）不可起诉

**合同纠纷：**
- 调解书可申请强制执行
- 和解协议须明确履行期限

---

## 输出

更新 `_log.yaml`：
- `status: closed`
- `closed: YYYY-MM-DD`
- `outcome:` 字段

追加到最后一条 `history.md`。

---

*Greater China Legal — litigation-legal matter-close CN adapter v1.0.0*