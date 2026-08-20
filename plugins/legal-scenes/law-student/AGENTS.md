# law-student — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:法学院学习辅助 — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `bar-prep-questions` — 法考 / 学习 / 案例 / bar prep questions
- `case-brief` — 法考 / 学习 / 案例 / case brief
- `cold-call-prep` — 法考 / 学习 / 案例 / cold call prep
- `cold-start-interview` — 法考 / 学习 / 案例 / cold start interview
- `customize` — 法考 / 学习 / 案例 / customize
- `exam-forecast` — 法考 / 学习 / 案例 / exam forecast
- `flashcards` — 法考 / 学习 / 案例 / flashcards
- `irac-practice` — 法考 / 学习 / 案例 / irac practice
- `legal-writing` — 法考 / 学习 / 案例 / legal writing
- `outline-builder` — 法考 / 学习 / 案例 / outline
- `session` — 法考 / 学习 / 案例 / session
- `socratic-drill` — 法考 / 学习 / 案例 / socratic drill
- `study-plan` — 法考 / 学习 / 案例 / study plan

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
