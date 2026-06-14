---
test_case_id: legal-builder-hub-registry-001
scene: legal-builder-hub
skill: skills/registry-browser/SKILL.md
contains:
  - skill注册
  - 注册表
  - 搜索
  - 发现
  - 安装
description: >
  验证 registry skill 能否帮助开发者搜索和浏览Greater China Legal生态中的可用Skill，
  包括按场景、法域、风险等级等维度筛选，以及查看Skill的详细元数据和版本信息。
  本测试对应 skills/registry-browser/SKILL.md。
last_reviewed: 2026-06
---

# Test Case: Skill注册表浏览与发现

## Query

我是一名legal skill开发者，正在为一家跨国公司的中国业务团队构建劳动法合规Skill。
我想在Greater China Legal生态的Skill注册表中搜索可复用的已有Skill。

具体需求：
1. 搜索所有与"劳动合同解除"相关的已有Skill
2. 过滤出法律场景为 employment-legal 或 labor-arbitration 的Skill
3. 查看每个Skill的版本号和最后审查日期
4. 查看每个Skill是否支持cn-mainland法域
5. 查看是否存在可直接安装使用的Skill

请帮我浏览注册表并推荐最相关的Skill。

## Expected Behavior

1. 应搜索注册表返回劳动合同解除相关的Skill列表
2. 支持按场景（employment-legal, labor-arbitration）过滤
3. 显示每个Skill的元数据：名称、描述、版本、法域、最后审查日期
4. 突出显示可直接安装的Skill
5. 推荐最匹配需求的2-3个Skill
6. 提供安装指引或命令
