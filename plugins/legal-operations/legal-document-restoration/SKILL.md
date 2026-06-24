---
name: legal-document-restoration
description: >
  法律文件脱敏稿还原——将外审后的脱敏稿 docx 按比对文件 .md 中的映射表 runs 级还原为原文，保留批注/修订/格式。
  适用情形：用户要求还原脱敏稿/还原审核稿/runs 级还原/收到脱敏稿后还原成原文/外审回来后还原入库。
  核心：解析比对文件 mapping 段 → runs 级精确替换（不跨 run 边界）→ 每替换一处重建 runInfo → round-trip 校验。
  与 legal-document-redaction 互为反向操作——一个写出去，一个读回来。
argument-hint: "[脱敏稿 docx + 比对文件 .md] → 输出还原稿 docx + 还原日志 + round-trip 校验"
legal_frame: cn-mainland
last_reviewed: 2026-06-24
version: 1.0.0
risk_level: high
trigger_phrases:
  - 还原脱敏稿
  - 还原审核稿
  - 还原
  - 比对还原
  - runs 级还原
  - restore redaction
  - restore
  - reverse redaction
  - unredact
---

# /legal-document-restoration — 法律文件脱敏稿还原

> 场景通用原子 skill。本 skill 与 `legal-document-redaction` 互为反向操作。
> 输入：脱敏稿（docx）+ 比对文件（.md）+ 比对文件 hash（可选）
> 输出：还原稿（docx）+ 还原日志 + round-trip 校验报告

## 一、加载上下文（必读）

调用本 skill 前必须确认：

```
1. 脱敏稿路径（必填）
2. 比对文件路径（必填）—— 必须包含 mapping 段
3. 输出格式（docx 默认 / md / txt）
4. 是否保留批注 / 修订痕迹（默认保留）
5. round-trip 校验是否启用（默认启用）
6. 适用法域（cn-mainland 默认 / hk / tw / sg / mo / eu）
```

未指定 → **暂停，要求补充**（按 GCL 原子 skill 规范）。

---

## 二、还原输入解析

### 2.1 解析脱敏稿结构

```
读取脱敏稿 docx → 解析为：
  ├─ 段落树（paragraphs）
  ├─ 每个段落含 N 个 run（runs）
  ├─ 每个 run 含文本（text）+ 格式属性（font, size, color）
  └─ 批注 / 修订 / 表格 / 图片 保留
```

### 2.2 解析比对文件

```
读取比对文件 .md → 提取：
  ├─ ## 批次元数据（批次 UUID / 法域 / 生成时间）
  ├─ ## 映射表（占位符 | 原文 | 实体类型 | 上下文角色）
  └─ 可选 ## 文件 hash（SHA256）—— 用于校验完整性
```

### 2.3 完整性校验

```
若有 hash：
  - 计算脱敏稿当前 hash → 与比对文件声明的 hash 对比
  - 不一致 → 拒绝还原（标 [ERROR] 比对文件与脱敏稿不匹配）
若无 hash：
  - 提示用户确认脱敏稿未被篡改
```

---

## 三、runs 级精确替换（核心）

### 3.1 替换原则

- **不跨 run 边界**：每个占位符必须完整位于一个 run 内，若跨 run 则失败（标 [WARN]）
- **按出现顺序处理**：从文档头到尾逐个 run 处理，避免重复匹配
- **每替换一处重建 runInfo**：替换后立即重建 run 的格式属性（font / size / color / bold 等），避免格式错位
- **大小写敏感**：占位符大小写必须与比对文件 mapping 完全一致

### 3.2 替换流程

```
步骤 1：扫描所有 run，构建占位符 → run 位置索引
步骤 2：按位置顺序遍历索引
步骤 3：每个占位符执行：
        a. 检查是否完整在单 run 内（否则 [WARN] 跳过）
        b. 用 mapping 中的原文替换占位符
        c. 重建该 run 的格式属性
        d. 记录替换日志（位置 / 占位符 / 原文 / 上下文）
步骤 4：保存还原稿 docx
```

### 3.3 失败处理

| 失败类型 | 处理 |
|---|---|
| 占位符跨 run | 标 [WARN] 跳过该占位符，记录位置 |
| 占位符在 mapping 中找不到 | 标 [WARN] 跳过，记录脱敏稿位置 |
| 原文在脱敏稿中已存在 | 标 [WARN] 可能重复占位符，跳过 |
| run 格式属性丢失 | 重建 runInfo，使用前一个 run 的格式兜底 |

---

## 四、格式保留

### 4.1 必须保留

- ✅ 字体 / 字号 / 颜色 / 加粗 / 斜体 / 下划线
- ✅ 段落结构 / 缩进 / 对齐
- ✅ 表格结构 / 单元格合并 / 边框
- ✅ 列表（有序 / 无序 / 多级）
- ✅ 修订痕迹（w:ins / w:del）
- ✅ 批注（w:commentReference）
- ✅ 页眉页脚 / 页码

### 4.2 不应变更

- ❌ 不修改脱敏稿之外的元数据（作者 / 创建时间）
- ❌ 不删除批注 / 修订（即使与脱敏内容无关）
- ❌ 不重新计算页码 / 目录

---

## 五、round-trip 校验

> **核心安全机制**：还原后的文件再次脱敏，应得到与原脱敏稿一致的输出。

### 5.1 校验流程

```
还原稿 → 调用 legal-document-redaction（相同参数）→ 输出新脱敏稿
对比：新脱敏稿 与 原脱敏稿
  ├─ 一致 → round-trip 通过 ✅
  └─ 不一致 → round-trip 失败 [ERROR]
```

### 5.2 失败场景

| 失败原因 | 排查方向 |
|---|---|
| 占位符未完全还原 | 检查 runs 跨边界情况 |
| 还原时引入新占位符 | 检查原文是否含触发脱敏的字符 |
| 格式破坏导致识别失败 | 检查 runInfo 重建逻辑 |
| 比对文件与脱敏稿不匹配 | 检查 hash 校验 |

### 5.3 强制约束

- ❌ round-trip 校验失败时禁止输出还原稿——输出"[ERROR] 还原失败，请人工核对"
- ❌ 不可跳过 round-trip 直接交付还原稿

---

## 六、输出格式

```markdown
## [A] 还原元数据
- 原脱敏稿：<文件名>
- 比对文件：<文件名>
- 还原计数：N 处
- round-trip 校验：<通过/失败>
- hash 校验：<通过/失败/未提供>

## [B] 还原后文本
[完整原文，保留原格式]

## [C] 还原日志
- [WARN] 占位符未匹配（位置 / 占位符）
- [WARN] 跨 run 边界（位置 / 占位符）
- [ERROR] hash 不一致 / round-trip 失败
- [SKIP] 批注 / 修订未处理（附说明）
```

---

## 七、与场景的协作

本 skill 是 `legal-document-redaction` 的反向操作，调用方相同但顺序相反：

| 上游场景 | 触发时机 | 用途 |
|---|---|---|
| contract-review | 外审合同稿收回后 | 还原入库 + 内部留底 |
| litigation-support | 外审案例分享稿收回后 | 还原入内部案例库 |
| data-compliance | PIPL 审查外发样本收回后 | 还原留底 |
| cocounsel-legal | 外部律师协办稿收回后 | 还原到内部系统 |
| employment-legal | 监管外发文书收回后 | 还原留底 |
| government-investigation | 外审调查材料收回后 | 还原归档 |
| law-student / legal-clinic | 外部批改收回后 | 还原到教学档案 |

**配套 references / 相邻 skill：**
- `legal-document-redaction/` — 反向操作（脱敏）
- `legal-document-redaction/references/config.md` — 白/黑/自定义类型（脱敏时的配置）
- `shared/matter-workspace/` — 案件工作区（实际路径 `plugins/legal-scenes/<本场景>/matters/<slug>/`）

---

## 八、禁用与边界

- ❌ **不可逆模式不可还原**——映射表已销毁，物理上无法还原
- ❌ **比对文件被篡改 → 拒绝还原**——hash 校验失败的脱敏稿不予还原
- ❌ **跨案映射表不可复用**——每个案号独立比对文件
- ❌ **禁止还原刑事证据原件**——破坏证据完整性，需走原件流程
- ❌ **禁止跳过 round-trip 校验**——失败即拒绝输出
- ❌ **禁止跨 run 边界强行替换**——可能导致 run 错位，宁可标 [WARN] 跳过

---

## 九、版本与变更

| 版本 | 日期 | 变更 |
|---|---|---|
| 1.0.0 | 2026-06-24 | 初版：runs 级精确替换 + 格式保留 + round-trip 校验 |

`★ Insight ─────────────────────────────────────`
- **runs 级替换是 docx 还原的核心难点**：docx 不是纯文本，每个字符在 run 里。直接正则全文替换会破坏 run 边界与格式属性。必须按 run 粒度逐个处理，每替换一处重建 runInfo——这是参考通用开源工具还原逻辑的核心工程要求。
- **round-trip 是安全网**：还原后再次脱敏应得到原脱敏稿。看似多余但实际是检测"还原完整性 + 还原过程不引入新触发字符"的关键校验。失败即拒绝输出，宁可人工核对也不冒险。
- **本 skill 与脱敏 skill 互为镜像**：trigger_phrases、§ 七协作链路、§ 八禁用边界都成对设计。修改任一边时记得同步另一边，避免一致性漂移。
`─────────────────────────────────────────────────`