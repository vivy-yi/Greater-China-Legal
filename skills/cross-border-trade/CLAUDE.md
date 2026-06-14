# CLAUDE.md — Cross-Border Trade Compliance Workspace

## Workspace Overview
This workspace provides AI-powered guidance for cross-border trade compliance operations, including export controls, import tariffs, sanctions screening, Incoterms, customs compliance, and trade dispute resolution.

## Available Skills

### Core Skills
| Skill | Purpose |
|-------|---------|
| `export-control-reviewer` | EAR/ITAR/Commerce Control List compliance review |
| `import-tariff-adviser` | HTS classification and duty rate advisory |
| `trade-sanctions-checker` | OFAC, UN, EU sanctions list screening |
| `incoterms-guide` | Incoterms 2020 rules interpretation and selection |
| `customs-compliance-assessor` | Customs bonds, bonded warehouses, FTA utilization |
| `trade-dispute-advisor` | WTO, anti-dumping, countervailing duty disputes |

## Directory Structure
```
/tmp/gl-work/cross-border-trade/
├── CLAUDE.md
├── export-control-reviewer/
│   └── skill.md
├── import-tariff-adviser/
│   └── skill.md
├── trade-sanctions-checker/
│   └── skill.md
├── incoterms-guide/
│   └── skill.md
├── customs-compliance-assessor/
│   └── skill.md
├── trade-dispute-advisor/
│   └── skill.md
└── references/
    ├── 判断框架.md
    ├── 查询路径.md
    └── 数据源清单.md
```

## Usage Guidelines
1. Always identify the specific trade compliance question before invoking a skill
2. When in doubt about jurisdiction, check multiple relevant skills (e.g., US + EU for transatlantic trade)
3. Escalate complex cases involving penalties >$100K or criminal exposure to human legal counsel
4. Document all compliance determinations with supporting regulatory citations

## Key Regulatory Frameworks
- **US**: EAR (15 CFR 730-774), ITAR (22 CFR 120-130), Customs Regulations (19 CFR)
- **EU**: Dual-Use Regulation (EC 428/2009), EU Sanctions Framework
- **International**: Incoterms® 2020, WTO Agreements, UN Sanctions Resolutions

## Quality Assurance
- All tariff/HTS classifications should be verified against official government databases
- Sanctions screening requires real-time database checks, not historical knowledge
- Legal determinations involving penalty exposure require human attorney review