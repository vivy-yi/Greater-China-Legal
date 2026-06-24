---
title: 常用法律数据源网站清单
description: >
  中文法律研究最常用的免费+付费数据源网站，按功能分类。
  gcl CLI 默认查询路径的完整索引。
last_reviewed: 2026-06
---

# 常用法律数据源网站清单

## 一、法条查询（中央立法机关）

| 网站 | URL | 类型 | 说明 |
|------|-----|------|------|
| **国家法律法规数据库** | https://flk.npc.gov.cn | 官方 | 全国人大维护，最权威 |
| **国务院公报** | https://www.gov.cn/yaowen/ | 官方 | 行政法规 |
| **司法部** | https://www.moj.gov.cn/ | 官方 | 部门规章 |

## 二、案例检索（法院系统）

| 网站 | URL | 类型 | 说明 |
|------|-----|------|------|
| **中国裁判文书网** | https://wenshu.court.gov.cn | 官方 | 最高人民法院主办 |
| **中国法院网** | https://www.chinacourt.org/ | 官方 | 法院资讯、典型案例 |
| **12348 法律服务网** | https://www.12348.gov.cn | 官方 | 司法部公共法律服务 |

## 三、律师/律所

| 网站 | URL | 类型 | 说明 |
|------|-----|------|------|
| **中华全国律师协会** | https://www.acla.org.cn/ | 行业 | 律师执业规范 |
| **中国法律服务网** | https://www.lawyers.org.cn/ | 行业 | 律所/律师检索 |

## 四、检察/执法

| 网站 | URL | 类型 | 说明 |
|------|-----|------|------|
| **最高人民检察院** | https://www.spp.gov.cn/ | 官方 | 检察文书/指导案例 |
| **国家市场监督管理总局** | https://www.samr.gov.cn/ | 官方 | 工商/竞争执法 |
| **中国证监会** | https://www.csrc.gov.cn/ | 官方 | 资本市场监管 |

## 五、商业法律数据库（付费）

| 网站 | URL | 类型 | 数据规模 |
|------|-----|------|---------|
| **北大法宝** | https://www.pkulaw.com/ | 商业 | 500 万+法规 / 1.6 亿+案例 |
| **元典开放平台** | https://open.chineselaw.com/ | 商业+MCP | 36 个 API + MCP |
| **无讼** | https://www.itslaw.com/ | 商业 | 案例/法规检索 |
| **法信** | https://www.faxin.cn/ | 商业 | 人民法院出版社 |
| **律商网** | https://www.lawtime.cn/ | 商业 | 综合法律检索 |

## 六、学术/期刊

| 网站 | URL | 说明 |
|------|-----|------|
| **中国民商法律网** | https://www.civillaw.com.cn/ | 民商法学术 |
| **中国知识产权资讯网** | https://www.iplaw.com.cn/ | 知识产权 |

## 七、gcl CLI 默认优先级

按免费 → 权威 → 实用 → 付费顺序：

```
1. [GOV] 国家法律法规数据库 (flk.npc.gov.cn)
2. [GOV] 中国裁判文书网 (wenshu.court.gov.cn)
3. [GOV] 中国法院网 (chinacourt.org)
4. [YD]  元典开放平台（须 API key）
5. [WKL] 北大法宝（须 API key）
6. [web] 通用 web_search 备选
```

## 八、按需求选库

| 需求 | 首选 | 备选 |
|------|------|------|
| 查现行法条 | flk.npc.gov.cn | [YD][WKL] |
| 查案例/类案 | wenshu.court.gov.cn | [YD][WKL][itslaw] |
| 查法规修订 | flk.npc.gov.cn（看 effective_date）| [GOV] 国务院公报 |
| 查企业信息 | 国家企业信用信息公示系统 | [YD] |
| 查法律学术 | 中国知网/万方 | civillaw.com.cn |
| 查地方高院观点 | 各地高院官网 | 北大法宝/元典 |

## 九、可访问性（2026-06 验证）

- ✅ **可访问**：wenshu / flk / gov / 12348 / spp / csrc / acla / lawyers / civillaw / itslaw / faxin / lawtime
- ⚠️ **需登录**：pkulaw (567) / chinacourt (449) / samr (403)
- ❌ **不可达**：yuandian (0) / iplaw (0) / legalweekly (0)

## 十、配置建议

`~/.gcl/config.json` 推荐配置：

```json
{
  "data_sources": {
    "npc_api": {"enabled": true, "url": "https://flk.npc.gov.cn/api"},
    "wenshu": {"enabled": true, "url": "https://wenshu.court.gov.cn"},
    "web_search": {"enabled": true},
    "yuandian_mcp": {"enabled": false, "api_key": ""},
    "pkulaw_mcp": {"enabled": false, "api_key": ""}
  }
}
```

---

*Greater China Legal — gcl-data-service reference: 数据源清单*
*验证日期：2026-06-15*
