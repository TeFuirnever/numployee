# Changelog

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 与[语义化版本](https://semver.org/lang/zh-CN/)。版本号锚定 SPEC：major = 不兼容标准变更，minor = 新等级/新章节，patch = 措辞勘误。

## [Unreleased]

### 定位（2026-09-17，所有者拍板）

- 明确为**研究性项目**：追求概念框架的学术严谨与同行评议，不以产业采用率为验收
- 路线图移除"第二个 harness 装配验证"等工程采用类环节，转向学术验证（探针一致率研究、开放问题攻关、英文版学术白皮书）
- 实现映射登记改为研究案例性质（自愿、非认证、非采用率考核）
- 去品牌：原参考实现产品名字样全仓移除；参考实现锚定开源 OpenClaw（implementations/openclaw/），闭源产品降级为匿名案例研究（implementations/case-study/，作者自述未经独立验证）

### 修订（rc2，2026-09-17，同行评审后）

- 三位互盲评审人（技术健全性 / 相关工作 / 可操作性）+ 两组参考文献核验，完整报告见 reviews/2026-09-17-rc1/
- 注入防护协议全文统一为"停—引—问"（SPEC 6.4 为准，白皮书对齐）
- 修复 L1 定义与四要素的矛盾（L1 持有持久身份文件，身份与状态术语区分）
- 第 8 章增设过渡条款：L5 声明在 suites/l5.md 回填前不予受理
- 门槛可测量化（达标阈值 / 低风险枚举 / 分歧分差）与第 5–7 章适用性声明
- 受管块获得标记格式（`numployee:managed` 伪语法）；语义化版本补 major 规则
- 参考来源修正 7 条（含 #19 死链替换）并新增 10 条（32–41：MCP/AGENTS.md/A2A/InjecAgent/抗谄媚/OWASP/五级在先工作/LongMemEval/ISO 22989/IEEE P3777）
- 探针判定操作手册化（P1/P2/P4/P5/T2/T5/T6）、基线与抖动定义、双评审一致率要求
- 补齐 IDENTITY/USER/BOOTSTRAP 三个辅助模板；人格三件套明确为三类职责
- 生态位表修正 bytefolk 归类、新增 A2A 与 AGENTS.md 行、"1630+"改为可核验表述
- 合规声明绑定 EVIDENCE.md 证据包（配置哈希 + 逐题留证 + 可复跑入口）

## [0.1.0] - 2026-09-17

M0 仓库奠基。

### 新增

- **SPEC.md v1.0-rc1**（草案）：判定四要素、五层参考架构、L1–L5 成熟度模型（能力×治理×评测联合门槛）、可移植性/安全信任/评测标准、合规声明；附录含产业实践映射表、开放问题与 31 条参考来源
- **templates/**：人格三件套空白模板（SOUL/AGENTS/TOOLS）+ 装配说明 + L1–L5 合规检查清单
- **probes/**：12 题行为探针集（5 行为 + 7 任务）+ 记分规则 + 按成熟度等级划分的四个跑测子集
- **docs/**：白皮书（完整论述版）、小白科普与速览、rb01–rb08 用户 runbook、L3–L5 进阶玩法手册与配方
- **implementations/case-study/**（由原参考实现目录 git 迁移而来，保留历史）：首个参考实现映射（标准条目 ↔ 产品落地事实对照）
- **治理**：双 LICENSE（文档 CC BY-SA 4.0 / 模板与代码 Apache-2.0）、CONTRIBUTING、CODE_OF_CONDUCT、GOVERNANCE、SECURITY、SIP 流程（sips/）
- **社区设施**：4 类 issue 模板 + Discussions；topics 六项；release v0.1.0
