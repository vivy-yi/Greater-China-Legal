# maritime — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Maritime — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `general-average-salvage` — 共同海损 / 海难救助 / 救助报酬
- `maritime-arbitration` — 海事仲裁 / CMAC / LMAA
- `maritime-cargo-contract` — 货损 / 提单 / 海运 / 承运人
- `maritime-lien-arrest` — 船舶扣押 / 海事保全 / 船扣
- `ship-collision` — 船舶碰撞 / 碰撞责任 / 过失
- `ship-financing` — 船舶抵押 / 船舶融资 / 优先权

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
