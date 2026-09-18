# numployee · 数字员工开放标准与工具包

> **numployee** = **num**(eral) + em**ployee** —— "数字员工"的拼合词，读作 /ˈnʌm.plɔɪ.iː/。

> **让数字员工有据可依、有器可用、有尺可量。**

**数字员工（Digital Employee）的开放标准与可移植工具包**：让任何 agent harness 都能按标准"造人"、按工具包"装配人"、按探针集"考核人"。

![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0%20%2B%20Apache--2.0-blue)
![Status](https://img.shields.io/badge/status-M0%20%E4%BB%93%E7%B3%BB%E5%BB%BA%E5%9F%BA-yellow)
[![文档站](https://img.shields.io/badge/%E6%96%87%E6%A1%A3%E7%AB%99-GitHub%20Pages-green)](https://tefuirnever.github.io/numployee/)

一句话定位：**别人定义 agent 怎么跑（harness、协议、编排框架），我们定义数字员工凭什么算"合格上岗"**——持久身份、可装配能力、可治理红线、可沉淀知识，以及衡量这一切的行为探针。

---

## 🧭 90 秒自测：你的"员工"在哪个成熟度等级？

L1–L5 是数字员工的成熟度模型（能力 × 治理 × 评测联合门槛）。对照下表找位置，再用对应探针子集验证。

| 等级 | 一句话特征 | 判定要点 | 对应探针子集 |
| --- | --- | --- | --- |
| **L1 应答工具** | 有名字、有岗位说明书的对话入口 | 岗位模板已实例化为持久身份（参考实现称 Employee）；持久身份成立 | [probes/suites/](probes/suites/) L1 子集 |
| **L2 岗位执行者** | 能按岗位纪律独立完成单任务 | 装了与运行时匹配的技能；守 Red Lines | [probes/suites/](probes/suites/) L2 子集 |
| **L3 流程协作者** | 技能串成流水线，多步任务不丢上下文 | 有 SOP 与交接纪律；任务探针稳定通过 | [probes/suites/](probes/suites/) L3 子集 |
| **L4 自主专家** | 规划—执行—反思闭环，跨会话学习 | 行为探针持续全绿；跨会话一致性通过；低风险任务可无人值守 | [probes/suites/](probes/suites/) L4 子集 |
| **L5 组织成员** | 可治理审计、可复用分发、多员工协作、持续进化 | 组织级权限模型在位；协作消息级安全检查；分发质量评级回流 | suites/l5.md（T8–T11，SIP-0002 起受理声明） |

> 自测不满足？没关系——下面的快速开始就是升级路线。

## 🚀 快速开始

1. **30 秒了解概念**：先记住一个比喻——**数字员工 = 你新招的一位真人同事**，harness 是公司提供的办公环境。详见 [docs/beginner/what-is-digital-employee.md](docs/beginner/what-is-digital-employee.md) 与 [一页速览](docs/beginner/quick-reference.md)。
2. **10 分钟装配第一个员工**：拿 [templates/](templates/README.md) 的人格三件套模板（三类职责：人格 / 纪律 / 环境事实，另附 IDENTITY / USER / BOOTSTRAP 三个辅助模板），填进你家 harness 的 workspace，实例化第一个员工。
3. **给自家员工跑探针**：敢不敢接这 13 道题？按 [probes/README.md](probes/README.md) 的清单跑一遍行为探针 + 任务探针，记分规则透明、可自动化判定。

## 🗺️ 仓库导览

| 路径 | 一句话 |
| --- | --- |
| [SPEC.md](SPEC.md) | 标准正文（v1.0）：定义、四要素、五层参考架构、L1–L5 成熟度模型、可移植性/安全/评测标准 |
| [docs/](docs/README.md) | 用户文档：白皮书、beginner（科普与速览）、runbooks（rb01–rb08 排障手册）、playbooks（L3–L5 进阶玩法与配方） |
| [templates/](templates/README.md) | 可移植资产：人格三件套空白模板 + 注释规范 + 装配检查清单 |
| [probes/](probes/README.md) | 行为探针集：13 题清单 + 记分规则 + 按成熟度等级划分的探针子集 |
| [implementations/](implementations/README.md) | 实现名录（研究案例登记）：OpenClaw 开源映射 + 匿名闭源案例研究（作者自述、未经独立验证） |
| [slides/](slides/index.html) | 16 页自包含 HTML 演示稿（深色终端风，断网可放映，←→ 翻页） |
| [sips/](sips/README.md) | SIP（Standard Improvement Proposal）：标准修订提案，一提案一文件 |
| [reviews/](reviews/2026-09-18-deep-audit/ANALYSIS.md) | 评审档案：rc1 三方互盲评审 + 2026-09-18 独立深审 |
| `mkdocs.yml` + [scripts/build-pages.py](scripts/build-pages.py) | GitHub Pages 文档站管线（推 main 自动部署，PR 上 strict 构建门控） |

## 🧩 生态位：我们不做什么

| 相邻项目 | 它们做的 | 本项目做的 |
| --- | --- | --- |
| agent harness（OpenClaw、Claude Code 等） | 身体与运行时：执行、工具调度、记忆机制 | 身体之上的人：人格、纪律、知识、治理标准 |
| ACP（Agent Client Protocol） | 宿主 ↔ 编码代理的通信协议 | 员工的内容与行为标准（与 ACP 互补，Code Mode 即建立在 ACP 之上） |
| MCP | 工具与资源的接入协议 | 员工的工具使用纪律与工具台账规范 |
| CrewAI / AutoGen | 多智能体编排框架 | 单个员工的资质标准与成熟度评级 |
| SWE-bench / AgentBench | 任务基准 | 员工上岗资格的行为探针与治理标准 |
| 数字员工产品（StaffDeck 等） | 单个产品/工作区：自家引擎、自家员工 | 跨产品的上岗标准：任何 harness 造的员工都能按 L1–L5 持证、考核与互认 |
| 可移植员工包（bytefolk/digital-employee） | 同生态位最近邻：员工包契约 + eval/validate 命令（产品化实现） | 标准侧互补：其包契约可映射本规范三件套与探针（对照表随 SIP 发布） |
| A2A（Agent2Agent Protocol） | agent 互操作与能力声明协议（Agent Card） | 通信层互补：L5 分发的可选承载，员工资质标准不变 |
| AGENTS.md 开放标准 | 编码代理纪律文件标准（LF 托管） | 纪律层兼容：本规范纪律文件为其员工化扩展 |

> 「数字员工产品」规模出处：GitHub 检索式 `digital employee`（不加引号）相关仓库逾 1600 个（2026-09 实测 1,615 个；精确短语 `"digital employee"` 为 462 个）。

三不原则：**不造运行时、不管通信协议、不做编排框架、不做封闭产品**——我们只定义"人"本身，以及"人凭什么算合格"。

## 🛣️ 路线图

| 里程碑 | 交付 | 状态 |
| --- | --- | --- |
| **M0 仓库奠基** | 仓库骨架、双 LICENSE、治理文件、README 门面、去产品化改造 | ✅ 已完成（v0.1.0） |
| **M1 SPEC v1.0** | SPEC v1.0 正式化（评审意见全部关闭：SIP-0001–0004）、L5 探针子集回填（SIP-0002）、探针双评审一致率先导研究（probes/irr-2026-09；正式研究随真实证据包积累） | ✅ 已完成（v1.0.0，2026-09-18） |
| **M2 研究与社区** | SIP 流程实跑（首批标准修订提案）、开放问题攻关（记忆遗忘判据、人格健康度）、英文版学术白皮书 | 待启动 |
| **M3 治理成熟** | 治理升级 maintainer 制、实现映射研究案例库（自愿登记，非认证）、同行评议机制常态化 | 待启动 |

> 定位声明：numployee 是**研究性项目**——追求概念框架的学术严谨与同行评议，不以产业采用率为验收标准。跨 harness 装配验证类工程环节已移出路线图。

修订流程与治理细节见 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [sips/](sips/)。

## 🤝 参与贡献

- **改标准**：走 SIP 流程（动机/方案/影响/实现参考），见 [sips/](sips/) 与 [CONTRIBUTING.md](CONTRIBUTING.md)。
- **交探针**：题目必须可被自动化判定；高危题不公开细节，遵守负责任披露。
- **报实现**：你的环境落地了本规范？欢迎作为**研究案例**登记进 [implementations/](implementations/case-study/MAPPING.md)——是研究素材，不是合规认证，更不是采用率考核。

## 📚 如何引用

学术或行业引用请使用仓库根目录的 [CITATION.cff](CITATION.cff)（GitHub 页面右侧会据此生成 APA / BibTeX 引用入口）。对外声明探针通过情况时，证据留存规范见 [probes/EVIDENCE.md](probes/EVIDENCE.md)（可复现、可审计、可抽查）。

## 📜 License

- **文档、标准、白皮书、探针题目**：[CC BY-SA 4.0](LICENSE)（署名-相同方式共享——衍生标准必须同源共享，防止改名洗稿）
- **模板、示例代码、检查清单**：[Apache-2.0](LICENSE)（允许商用集成，带专利授权条款）

## 🏗️ 参考实现声明

参考实现基于 **OpenClaw**（开源 agent harness，<https://github.com/openclaw/openclaw>）——本仓库的机制均可对照其公开代码验证。另有一个闭源桌面产品的匿名案例研究（作者自述、未经独立验证）在 [implementations/case-study/](implementations/case-study/MAPPING.md)，其中产品治理特性为待验证的设计主张。文中出现的界面文案与版本号，凡涉及具体落地处均已标注"参考实现"。

---

*「我们不是在调教模型，而是在培养同事。」*
