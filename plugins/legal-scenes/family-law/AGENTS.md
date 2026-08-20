# family-law — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Family Law — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `child-custody` — 抚养权 / 抚养费 / 探视权 / 子女
- `domestic-violence` — 家暴 / 人身安全保护令 / 跟踪 / 虐待
- `inheritance-dispute` — 遗嘱 / 继承 / 遗产 / 继承权纠纷
- `marriage-and-divorce` — 离婚 / 协议离婚 / 诉讼离婚 / 婚姻效力
- `prenuptial-agreement` — 婚前协议 / 婚内协议 / 离婚协议 / 财产约定
- `property-division` — 财产分割 / 共同财产 / 个人财产 / 夫妻财产

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
