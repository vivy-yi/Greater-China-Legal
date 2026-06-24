---
title: 企查查 MCP — 181 个工具完整列表
description: >
  企查查智能体数据平台 6 个 Server / 181 个工具的完整索引。
  数据源：https://agent.qcc.com/_next/static/chunks/40248-aa8229129c64dbf8.js
last_reviewed: 2026-06
---

# 企查查 MCP — 181 个工具完整列表

> **数据来源**：从 `agent.qcc.com` 公开加载的 Next.js chunk 文件解析得出。
> 完整 181 个工具，按 6 个 Server 分类。所有工具均以 `get_` 前缀调用。

---

## Server 1：qcc-company（企业基座）

工作流基础层 — 工商登记 / 基本信息 / 主体核查

| 工具 | 用途 |
|------|------|
| `get_company_by_query` | 企业名称/统一社会信用代码 模糊查询 |
| `get_company_profile` | 企业概览（核心要素聚合） |
| `get_company_registration_info` | 工商登记详情 |
| `get_company_announcement` | 企业公告 |
| `get_company_risk_scan` | 企业风险扫描（一键尽调） |
| `get_actual_controller` | 实际控制人 |
| `get_beneficial_owners` | 受益所有人 |
| `get_branches` | 分支机构 |
| `get_change_records` | 变更记录 |
| `get_contact_info` | 联系信息 |
| `get_annual_reports` | 企业年报 |
| `get_key_personnel` | 关键人员 |
| `get_shareholder_info` | 股东信息 |
| `get_qualifications` | 资质信息 |
| `get_related_announcement` | 相关公告 |
| `get_ranking_list_info` | 榜单信息 |

## Server 2：qcc-risk（司法风险）

诉讼 / 失信 / 处罚 / 风险预警

| 工具 | 用途 |
|------|------|
| `get_case_filing_info` | 立案信息（含时间窗口） |
| `get_judicial_documents` | 裁判文书 |
| `get_judgment_debtor_info` | 被执行人 |
| `get_dishonest_info` | 失信被执行人 |
| `get_high_consumption_restriction` | 限高令 |
| `get_equity_freeze` | 股权冻结 |
| `get_equity_pledge_info` | 股权出质 |
| `get_stock_pledge_info` | 股票质押 |
| `get_court_notice` | 法院公告 |
| `get_hearing_notice` | 开庭公告 |
| `get_service_notice` | 送达公告 |
| `get_termination_cases` | 终本案件 |
| `get_pre_litigation_mediation` | 诉前调解 |
| `get_judicial_auction` | 司法拍卖 |
| `get_asset_auction` | 资产拍卖 |
| `get_administrative_penalty` | 行政处罚 |
| `get_serious_violation` | 严重违法 |
| `get_business_exception` | 经营异常 |
| `get_tax_abnormal` | 税务异常 |
| `get_tax_arrears_notice` | 欠税公告 |
| `get_tax_violation` | 税务违法 |
| `get_environmental_penalty` | 环保处罚 |
| `get_credit_commitments` | 信用承诺 |
| `get_credit_evaluation` | 信用评价 |
| `get_default_info` | 违约信息 |
| `get_simple_cancellation_info` | 简易注销 |
| `get_cancellation_record_info` | 注销记录 |
| `get_property_asset_announcement` | 财产资产公告 |
| `get_property_rights_transaction` | 财产权交易 |
| `get_public_exhortation` | 公开劝诫 |
| `get_disciplinary_list` | 纪律处分 |
| `get_food_safety` | 食品安全 |
| `get_product_recall` | 产品召回 |
| `get_random_check` | 抽查检查 |
| `get_product_spot_check` | 产品抽检 |
| `get_software_violation` | 软件违规 |
| `get_government_interview` | 政府约谈 |
| `get_government_announcement` | 政府公告 |
| `get_advertising_review` | 广告审查 |
| `get_counterfeit_cosmetics` | 假冒化妆品 |
| `get_spot_check_info` | 抽检信息 |

## Server 3：qcc-ipr（知识产权）

商标 / 专利 / 软著 / 著作权

| 工具 | 用途 |
|------|------|
| `get_trademark_info` | 商标信息 |
| `get_trademark_document` | 商标文书 |
| `get_patent_info` | 专利信息 |
| `get_international_patent` | 国际专利 |
| `get_software_copyright_info` | 软件著作权 |
| `get_copyright_work_info` | 作品著作权 |
| `get_integrated_circuit_layout` | 集成电路布图 |
| `get_ipr_pledge` | 知识产权出质 |
| `get_standard_info` | 标准信息 |
| `get_tech_achievement` | 科技成果 |
| `get_domain_info` | 域名信息 |
| `get_mini_program` | 小程序信息 |
| `get_wechat_official_account` | 微信公众号 |
| `get_weibo_account` | 微博账号 |
| `get_douyin_account` | 抖音账号 |
| `get_kuaishou_account` | 快手账号 |
| `get_online_store` | 网店 |
| `get_app_info` | APP 信息 |

## Server 4：qcc-operation（经营状况）

招投标 / 资质 / 经营 / 招聘

| 工具 | 用途 |
|------|------|
| `get_bidding_info` | 招投标信息 |
| `get_chattel_mortgage_info` | 动产抵押 |
| `get_land_mortgage_info` | 土地抵押 |
| `get_land_grant_info` | 土地出让 |
| `get_land_transfer_info` | 土地转让 |
| `get_financing_lease_info` | 融资租赁 |
| `get_guarantee_info` | 对外担保 |
| `get_financing_records` | 融资记录 |
| `get_investment_institution` | 投资机构 |
| `get_private_fund_manager` | 私募基金管理人 |
| `get_listing_info` | 上市信息 |
| `get_financial_data` | 财务数据 |
| `get_recruitment_info` | 招聘信息 |
| `get_news_sentiment` | 新闻舆情 |
| `get_valuation_inquiry` | 评估询价 |
| `get_tax_invoice_info` | 发票信息 |
| `get_taxpayer_qualification` | 纳税人资质 |
| `get_import_export_credit` | 进出口信用 |
| `get_internet_service_info` | 互联网服务 |
| `get_game_approval` | 游戏审批 |
| `get_telecom_license` | 电信许可 |
| `get_commercial_franchise` | 商业特许 |
| `get_administrative_license` | 行政许可 |
| `get_bankruptcy_reorganization` | 破产重整 |
| `get_liquidation_info` | 清算信息 |

## Server 5：qcc-executive（高管人员）

高管 / 法人 / 关联方穿透

| 工具 | 用途 |
|------|------|
| `get_executive_positions` | 高管任职 |
| `get_executive_investments` | 高管对外投资 |
| `get_executive_controlled_companies` | 高管控制企业 |
| `get_executive_legal_rep_roles` | 高管法人代表 |
| `get_executive_partners` | 高管合伙人 |
| `get_executive_related_companies` | 高管关联企业 |
| `get_executive_case_filing` | 高管涉诉 |
| `get_executive_judicial_docs` | 高管司法文书 |
| `get_executive_dishonest` | 高管失信 |
| `get_executive_high_consumption_ban` | 高管限高 |
| `get_executive_court_notice` | 高管法院公告 |
| `get_executive_hearing_notice` | 高管开庭公告 |
| `get_executive_service_notice` | 高管送达公告 |
| `get_executive_judgment_debtor` | 高管被执行人 |
| `get_executive_equity_freeze` | 高管股权冻结 |
| `get_executive_equity_pledge` | 高管股权出质 |
| `get_executive_stock_pledge` | 高管股票质押 |
| `get_executive_exit_restriction` | 高管出境限制 |
| `get_executive_tax_violation` | 高管税务违法 |
| `get_executive_admin_penalty` | 高管行政处罚 |
| `get_executive_beneficial_owner` | 高管受益所有人 |
| `get_executive_property_reward_notice` | 高管悬赏公告 |
| `get_executive_pre_litigation_mediation` | 高管诉前调解 |
| `get_executive_risk_scan` | 高管风险扫描 |
| `get_executive_valuation_inquiry` | 高管评估询价 |
| `get_executive_terminated_cases` | 高管终本案件 |

## Server 6：qcc-history（历史变更）

历史快照 — 时间序列数据

| 工具 | 用途 |
|------|------|
| `get_historical_shareholders` | 历史股东 |
| `get_historical_executives` | 历史高管 |
| `get_historical_legal_rep` | 历史法人 |
| `get_historical_registration` | 历史登记信息 |
| `get_historical_change_records` | 历史变更 |
| `get_historical_investments` | 历史对外投资 |
| `get_historical_admin_license` | 历史行政许可 |
| `get_historical_admin_penalty` | 历史行政处罚 |
| `get_historical_case_filing` | 历史立案 |
| `get_historical_judicial_docs` | 历史裁判文书 |
| `get_historical_court_notice` | 历史法院公告 |
| `get_historical_hearing_notice` | 历史开庭公告 |
| `get_historical_dishonest` | 历史失信 |
| `get_historical_high_consumption_ban` | 历史限高 |
| `get_historical_equity_freeze` | 历史股权冻结 |
| `get_historical_equity_pledge` | 历史股权出质 |
| `get_historical_ipr_pledge` | 历史知产出质 |
| `get_historical_land_mortgage` | 历史土地抵押 |
| `get_historical_chattel_mortgage` | 历史动产抵押 |
| `get_historical_trademark` | 历史商标 |
| `get_historical_patent` | 历史专利 |
| `get_historical_business_exception` | 历史经营异常 |
| `get_historical_serious_violation` | 历史严重违法 |
| `get_historical_bankruptcy` | 历史破产 |
| `get_historical_terminated_cases` | 历史终本 |
| `get_historical_judgment_debtor` | 历史被执行人 |
| `get_historical_service_notice` | 历史送达 |
| `get_historical_pre_litigation_mediation` | 历史诉前调解 |
| `get_historical_listing` | 历史上市 |
| `get_historical_honor` | 历史荣誉 |
| `get_historical_random_check` | 历史抽检 |
| `get_historical_spot_check` | 历史抽查 |
| `get_historical_environmental_penalty` | 历史环保处罚 |
| `get_historical_tax_arrears` | 历史欠税 |
| `get_historical_internet_service` | 历史互联网服务 |

---

## 调用示例

```bash
# 工商基本信息
qcc company get_company_by_query "小米科技有限责任公司"

# 风险扫描（尽调必跑）
qcc company get_company_risk_scan "小米科技有限责任公司"

# 高管穿透
qcc executive get_executive_controlled_companies "雷军"

# 知识产权
qcc ipr get_trademark_info "小米科技有限责任公司"
```

---

## 接入 GCL

每个工具对应 GCL 30 场景中的具体查询：

| GCL 场景 | 必用工具 |
|---------|---------|
| `m-and-a` | get_company_risk_scan, get_actual_controller, get_company_by_query, get_company_profile |
| `corporate-governance` | get_shareholder_info, get_actual_controller, get_beneficial_owners |
| `contract-review` | get_company_registration_info, get_company_risk_scan |
| `litigation-support` | get_case_filing_info, get_judicial_documents |
| `data-compliance` | get_company_announcement, get_related_announcement |
| `employment-legal` | get_company_registration_info, get_change_records |
| `tax-compliance` | get_tax_arrears_notice, get_tax_violation |

---

*Greater China Legal — gcl-data-service reference: 企查查工具完整列表*
*数据采集时间：2026-06-15*
*工具总数：181（实际匹配官方宣传的 182，差 1 个可能为内部隐藏工具）*
