# employment-legal — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:Employment Legal — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `annual-bonus-rules` — annual-bonus-rules / 年终奖 / 年终奖金 / 奖金发放 / 奖金争议 / employment_legal
- `expansion-kickoff` — 扩张启动 / 项目启动
- `expansion-update` — 业务扩张 / 人员扩充
- `handbook-updates` — 员工手册 / 制度更新
- `hiring-review` — 招聘合规 / 入职审查
- `internal-investigation` — 内部调查 / 合规调查
- `international-expansion` — 海外扩张 / 国际
- `investigation-add` — 补充调查 / 追加
- `investigation-memo` — 调查备忘录 / 法律意见
- `investigation-open` — 开启调查 / 立案
- `investigation-query` — 调查询问 / 访谈
- `investigation-summary` — 调查报告 / 总结
- `job-description-legality` — job-description-legality / 岗位职责 / 不胜任 / 调岗 / 末尾淘汰 / 绩效排名 / 不能胜任 / 不能胜任工作
- `labor-arbitration-filing` — labor-arbitration-filing / employment_legal / 劳动仲裁 / 仲裁申请 / 劳动仲裁材料
- `labor-contract-drafter` — 劳动合同 / labor-contract-drafter / employment_legal / 起草合同 / 合同审查 / 竞业限制 / 保密协议 / 服务期
- `leave-tracker` — 请假 / 休假管理
- `log-leave` — 请假记录 / 休假
- `non-compete-enforcement` — non-compete-enforcement / employment_legal / 竞业限制 / 竞业禁止 / 保密协议 / 跳槽
- `policy-drafting` — policy drafting
- `probation-period-advisor` — probation-period-advisor / employment_legal / 试用期 / 试用期解除 / 试用期工资 / 转正
- `resignation-negoitation` — resignation-negoitation / employment_legal
- `resignation-negotiation` — /employment-legal:resignation-negotiation / /employment-legal:resignation-negotiation --frame cn-mainland / 员工辞职协商 / 竞业限制处理 / 主动辞职违约金
- `salary-structure-design` — salary-structure-design / employment_legal / 工资结构 / 工资设计 / 加班费计算 / 工资构成 / 基本工资 / 绩效工资 / 最低工资 / 津贴
- `sexual-harassment-complaint` — sexual-harassment-complaint / employment_legal / 性骚扰 / 职场性骚扰 / 性骚扰投诉 / 性骚扰调查 / 性骚扰预防 / 合法权益
- `social-insurance-compliance` — social-insurance-compliance / employment_legal / 社保 / 社会保险 / 五险一金 / 社保缴纳 / 社保基数 / 社保补缴 / 试用期社保 / 社保合规
- `termination-legality-assessment` — termination-legality-assessment / employment_legal / 解除劳动合同 / 违法解除 / 经济补偿 / 裁员 / 协商解除 / 过失性解除 / 非过失性解除
- `work-injury-compensation` — 工伤 / 工伤认定 / 工伤赔偿 / 工伤保险 / 工伤待遇 / 工亡 / 劳动能力鉴定 / 伤残等级 / work-injury-compensation / employment_legal

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
