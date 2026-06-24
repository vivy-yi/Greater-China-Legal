---
target: skills/music-film-copyright/SKILL.md
type: functional
priority: high
checks:
  - has_section: "## 工作流程"
  - body_lines: "> 30"
  - contains: ["著作权", "侵权", "风险"]
  - no_placeholder: true
  - starts_with_header: true
expected:
  - section: "风险等级"
    type: must
  - section: "维权路径"
    type: should
trigger_phrases:
  - 自测
  - 功能测试
last_reviewed: 2026-06
version: 1.0.0
legal_frame: cn-mainland
---

# 影视音乐著作权侵权自测

**测试场景：** 用户发现某短视频平台上有未经授权使用其公司拥有版权的音乐片段和影视截图的视频内容，要求 AI 进行侵权判断和维权路径规划。验证 skill 是否正确识别著作权归属、实质性相似判断标准、可选择的维权路径（通知删除/民事诉讼/行政投诉）及法定赔偿计算。重点检查著作权法第54条引用。
