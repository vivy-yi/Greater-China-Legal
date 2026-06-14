---
target: skills/cross-border-crypto-tax-advisor/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["加密资产", "税务", "DeFi", "CRS", "申报"]
  - no_placeholder: true
expected:
  - section: "输出格式"
    type: must
  - section: "升级决策门"
    type: must
trigger_phrases:
  - 虚拟货币
  - 加密资产
  - NFT
  - 数字藏品
  - DeFi
  - Web3
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---
