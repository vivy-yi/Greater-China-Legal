# ip-infringement — Agent 入口(跨平台)

> 本文件是 OpenCode / Codex / Gemini CLI 等 agentic tool 进入本场景的跨平台入口;Claude Code 直接读 `CLAUDE.md`(本文件经 `@import` 引用,内容一致)。

**场景**:IP Infringement — Practice Profile (curator v2.0)

**用法**:用户问题命中下方任一触发词 → 读取对应 `skills/<skill>/SKILL.md` 按流程执行。

**本场景 Skills 与触发词**:
- `brand-license-contract` — 商标许可使用合同审查 / 商标许可协议审查 / 品牌授权合同审核 / trademark license agreement review / 商标许可合同风险评估
- `cease-desist` — 停止侵权 / 警告函
- `clearance` — IP清除 / 侵权检索
- `content-copyright-dispute` — content-copyright-dispute / ip_infringement
- `damage-calculator` — 侵权赔偿 / 损害计算
- `employee-trade-secret-risk` — 员工带走商业秘密风险 / 商业秘密保护方案 / 员工泄密风险评估 / 竞业限制有效性审查 / 保密协议执行 / 离职员工商业秘密 / 商业秘密防泄漏
- `evidence-guide` — 证据指导 / 举证
- `fto-triage` — FTO分析 / 自由实施
- `infringement-detector` — 侵权检测 / 盗版
- `infringement-evidence-collection` — infringement-evidence-collection / ip_infringement
- `infringement-triage` — 侵权分类 / 初步判断
- `invention-intake` — 发明披露 / 专利申请
- `ip-clause-review` — IP条款 / 知识产权条款
- `music-film-copyright` — 音乐侵权 / 影视侵权 / 版权侵权 / 盗版 / 切条视频 / 短视频配乐 / 翻唱 / 盗录 / 盗版传播 / music infringement / film piracy / copyright infringement
- `oss-review` — 开源软件 / 许可证
- `patent-claim-analysis` — 专利权利要求解读 / 专利侵权分析 / 专利保护范围 / 等同侵权判断 / patent-infringement / ip-infringement / patent-claim-analysis
- `patent-invalidity-defense` — patent-invalidity-defense / ip_infringement / 专利无效 / 现有技术 / 新颖性 / 创造性 / 专利侵权
- `patent-validity-checker` — 专利有效性 / 无效
- `portfolio` — 知识产权组合 / 商标专利
- `rights-protection-path` — 维权路径 / 知识产权保护
- `secret-identification-assessment` — secret-identification-assessment / ip_infringement
- `software-copyright-analysis` — 软件著作权侵权 / 软件抄袭 / 代码相似 / 软件侵权分析 / software copyright / code similarity / 开源合规 / software-copyright-analysis
- `takedown` — 下架 / 删除通知
- `trade-secret-litigation` — trade-secret-litigation / ip_infringement / 商业秘密 / 侵犯商业秘密罪 / 竞业限制 / 保密协议
- `trademark-infringement-assessment` — 商标侵权认定评估 / 商标侵权判断 / trademark infringement assessment / 商标混淆可能性 / 商标正当使用抗辩 / 商标平行进口
- `trademark-search` — 商标检索 / 近似查询
- `trademark-search-report` — 商标注册前检索报告 / 商标近似查询 / 商标驳回风险 / 商标布局 / trademark-search-report / ip-infringement

**详细工作规范**(角色分级、数据源标注、升级决策门、Part A/B 双层)见 `CLAUDE.md`,经 `@import` 自动加载。

@import CLAUDE.md
