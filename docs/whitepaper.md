> 本文是《数字员工规范》的完整论述版（含学术引用与推理过程）。规范正文见 [../SPEC.md](../SPEC.md)；其中产品实现相关内容已剥离至 [../implementations/case-study/](../implementations/case-study/)（匿名案例研究，作者自述、未经独立验证）。

# 数字员工白皮书

> 从工具型 AI 到员工型 AI 的架构、标准与实践
>
> 版本：v1.0（与 SPEC Draft v1.0-rc4 同步）｜ 日期：2026 年 9 月 ｜ 编制：numployee 项目

**证据类型说明**：文中论断标注四类来源——【业界】业界事实（厂商文档、公开发布、官方博客）；【学术】学术结论（同行评议论文或高质量预印本）；【观点】本文观点（作者综合判断，非他方结论）；【实践】闭源产品实践（一个闭源桌面客户端产品的代码库与其领域术语表记录的设计决定，作者自述、未经独立验证，匿名案例见 [implementations/case-study/](../implementations/case-study/)）。每类论断均随文标注，完整 URL 见文末"参考来源"。

---

## 1. 摘要

过去两年，AI 应用的主语正在从"工具"变为"员工"。GitHub Copilot 从代码补全进化为可异步委派任务的 coding agent【业界】；Cognition 的 Devin 以"AI 软件工程师"定位进入真实工程流程【业界】；RPA 厂商将"数字员工"从规则机器人重塑为认知型 Agent【业界】。本文将这一趋势收束为一个可检验的定义：**数字员工是同时具备持久身份、可装配能力、可治理红线、可沉淀知识四要素的 AI 工作实体**【观点】。

围绕该定义，本白皮书给出四样东西：

1. **五层参考架构**——人格层、能力层、知识层、运行时层、治理层，分别回答"是谁、会什么、记得什么、如何跑、受什么约束"；
2. **L1–L5 能力成熟度模型**，每一级同时定义能力要求、治理要求、评测要求，成熟度是三者联动的门槛而非能力的单维刻度【观点】；
3. **三类工程标准**——可移植性标准、安全与信任标准、评测标准，供数字员工的设计者、分发者与采购方共同使用；
4. **产业实践映射表**，将 OpenClaw/Claude Code 人格文件生态、OpenAI GPTs、Devin、CrewAI、LangGraph 等业界方案，与一个闭源桌面客户端产品（作者自述案例）的 Role/Employee/Agent 领域模型逐层对齐【实践】。

**贡献限定**：四要素与五层为综合既有实践的定义工作；机制贡献为联合门槛、继承约束推导与探针一票否决【观点】。

## 2. 背景与问题：为什么"工具型 AI"走向"员工型 AI"

### 2.1 工具型 AI 的天花板

工具型 AI 的典型形态是单次问答与单次生成：无状态、无身份、无责任主体。它回答"这个问题"，但不拥有"这项工作"。当组织试图把 AI 放进真实流程时，三个缺口立刻暴露：

- **持久性缺口**：每次会话从零开始，偏好、决策与上下文不延续；
- **治理缺口**：没有权限边界与审计对象，出了问题无法归因；
- **复用缺口**：专家的配置（提示词、工具、知识）锁在个人对话框里，无法沉淀为组织资产。

### 2.2 业界的两条演进线

**第一条线是编码代理。** GitHub Copilot coding agent 于 2025 年 9 月（GA）正式商用，定位为"异步、自主的开发者代理"：用户委派任务，它创建分支、提交 PR，人类通过标准 code review 流程监督【业界】。Cognition 的 Devin 进一步把"AI 软件工程师"产品化，提供带浏览器、终端与编辑器的沙箱环境，自主完成多文件改动并迭代排错【业界】。普林斯顿大学的 SWE-agent 则证明：开源模型加上精心设计的 agent-computer interface，即可在真实 GitHub issue 上自动修复缺陷；SWE-agent 是 SWE-bench 上代表性的开源方案之一【业界】【学术】。

**第二条线是数字劳动力。** RPA 时代的"数字员工"指规则驱动的软件机器人；2024 年起，国内外厂商（UiPath、来也、实在智能、BetterYeah 等）相继把叙事切换到 Agent 数字员工——从"模拟人操作界面"转向"理解任务、调用工具、处理异常"【业界】。据 IDC 数据（经新京报转引），2026 年全球 AI 数字员工市场规模预计突破 469 亿元，中国占比约 31.56%【业界】。

两条线在学术侧汇合。LLM-based agent 综述（Xi et al., 2023）将 agent 系统归纳为 Profile（身份）、Memory（记忆）、Planning（规划）、Action（行动）四个模块【学术】，与组织管理中"定岗—授权—考核—沉淀"的逻辑一一同构。当 AI 的执行能力被工程验证之后，问题自然升级：谁在做（身份）、会什么（能力）、记得什么（知识）、受什么约束（治理）【观点】。

**范围说明**：本规范不覆盖托管对话式 SaaS 数字员工产品；此类产品可在本规范之上做实现映射【观点】。

### 2.3 本文立场

数字员工不是"更聪明的聊天机器人"，也不是"换个名字的自动化 workflow"【观点】。它与二者的边界在第 3 节给出；支撑它的架构在第 4 节展开。

## 3. 定义与边界

### 3.1 与相邻概念的区分

**聊天机器人（chatbot）**：以会话为单元，身份随会话结束而消散。系统提示词里"你是某某"只是 persona conditioning（人格条件化），不构成持久身份【学术】。Anthropic 的研究博客提出：预训练使模型习得模拟多样角色的能力，后训练筛选出稳定的 Assistant 人格【学术】。这意味着人格若不落盘、不治理，就只是上下文里的临时修辞——这与"员工"的稳定性要求根本冲突【观点】。

**自动化 workflow**：Anthropic《Building Effective Agents》作了关键区分——workflow 是"LLM 与工具沿预定义代码路径编排"的系统；agent 是"LLM 动态指挥自身过程与工具使用"的系统【业界】。数字员工以后者为底座；但在低风险的确定性任务上，应允许员工退化为 workflow 模式以换取可预测性， autonomy 是档位而非信仰【观点】。

**Agent harness（代理载体）**：承载 agent 的运行环境——上下文装配、工具调度、权限拦截、会话持久化。harness 是"雇主提供的办公场所"，数字员工是"在其中任职的个体"【观点】。把 harness 与员工混为一谈，等于把写字楼当作员工——这解释了为什么很多"agent 产品"换壳不换人：运行时升级了，岗位配置与人格资产仍无处安放【观点】。

**通信协议（ACP / A2A / MCP）**：本规范与三者互补而不竞争——ACP（Agent Client Protocol）管"宿主 ↔ 编码代理"的通信，A2A（Agent2Agent Protocol）管 agent 间的互操作与能力声明，MCP（Model Context Protocol）管工具接入，本规范管数字员工的人格、纪律、知识、治理与成熟度【观点】。同理，本规范的纪律文件可视为 AGENTS.md 开放标准（Linux Foundation 托管）的员工化扩展——增加完成判定与认知纪律条款，兼容而非分叉【观点】。

### 3.2 数字员工的判定四要素

一个 AI 实体是数字员工，当且仅当满足以下四项【观点】：

1. **持久身份**：有唯一标识、稳定人格与履历，跨会话存在。对应 OpenClaw 的 IDENTITY.md/SOUL.md 工作区文件实践【业界】；学术上对应 Generative Agents 的代理档案与记忆流【学术】。
2. **可装配能力**：能力以声明式清单存在，可按岗位装配、按运行时匹配、按版本审计。对应 OpenAI GPTs 的 instructions / knowledge / actions 三段式【业界】；学术上承接 ToolFormer 开启的工具学习传统【学术】。
3. **可治理红线**：存在独立于人格的操作纪律，越权可被拦截与追责。对应间接提示注入防护与 agent 治理研究【学术】，以及 OpenAI《Practices for Governing Agentic AI Systems》倡导的人本监督原则【业界】。
4. **可沉淀知识**：经验可写入组织记忆，可被继任者与副本继承。对应 MemGPT 分层记忆【学术】与 wiki 式组织档案实践【业界】。

四要素缺一即降级：无持久身份退化为聊天机器人；无可装配能力退化为一次性脚本；无可沉淀知识则永远停在个人助手阶段（无可治理红线者非降级而是取消上岗资格）【观点】。

### 3.3 一个产品化实现的领域映射（闭源案例，作者自述）

该闭源产品的领域模型与四要素逐一咬合【实践】：Role（角色模板：名称/描述/指令/推荐模型，不可对话）实例化为 Employee（数字员工：绑定 backing Agent，可对话、有持久状态），Employee 运行于 Agent（OpenClaw 隔离执行单元，独立 workspace 与 agentDir）。即"岗位说明书 → 在职员工 → 独立工位"的三段结构【观点】；其中 Agent 隔离执行单元、独立 workspace 与 agentDir 属 OpenClaw 原生机制，参考实现在 [implementations/openclaw/](../implementations/openclaw/) 的映射中独立验证。Code Mode 下员工改由 ACP 编码代理（codeagent/opencode）承载、与默认模型互斥——同一岗位可由不同工种的干法承接【实践】。

## 4. 参考架构：五层模型

### 4.1 人格层（Persona）——"是谁"

**职责**：定义数字员工的身份、语气、边界与信任模型，使其行为可预期、可识别、可信赖。

- **业界对应**：OpenClaw 工作区以 SOUL.md（人格、语气、边界）、IDENTITY.md（身份）、USER.md（用户画像）分层定义代理人格；社区最佳实践明确"SOUL.md 放人格与边界，不放操作流程"【业界】。Claude Code 以 CLAUDE.md 加 auto memory 实现项目级人格与偏好的持久化，并支持 `@` 导入做模块化【业界】。CrewAI 用 role / goal / backstory 三元组定义角色化代理【业界】。OpenAI GPTs 的 instructions 是同一层的最简形态【业界】。
- **学术对应**：persona conditioning 研究证实系统提示能显著塑造行为，但人格一致性是架构属性而非纯提示词属性，需要显式机制维持【学术】；EMNLP 2025 的工作进一步考察了多轮辩论场景下 LLM 维持人格的极限【学术】。
- **闭源产品实现**（作者自述）：产品的提示词增强模板目录（v5.4.0）经产品主进程中的受管块同步器同步到 `~/.openclaw/workspace/`；SOUL.md 承载人格、语气、边界、信任模型，与承载操作纪律的 AGENTS.md 分离——分离依据见第 6 节【实践】。

### 4.2 能力层（Skills / Tools）——"会什么"

**职责**：以声明式清单管理数字员工可调用的工具与技能，支持按岗位装配、按运行时匹配、按版本审计。

- **业界对应**：GPTs 将 instructions / knowledge / actions 分层，actions 即函数调用接口【业界】；MCP 将工具接入标准化【业界】；Claude Code 的 skills 目录使能力以文件化方式分发【业界】。
- **学术对应**：ToolFormer 证明模型可自学何时、如何使用外部工具，是函数调用范式的学术源头【学术】；ReAct 将推理轨迹与工具调用交错，构成工具使用的基础循环【学术】。
- **闭源产品实现**（作者自述）：Usage 条目是角色/员工声明的可安装能力清单，分 openclaw / codeagent 两组，启用时只消费与运行时匹配的一组；产品仓库中的技能库（数十个）维护技能文件化分发【实践】。Code Mode 员工由 ACP 编码代理承载，能力消费切至 codeagent 组——能力装配与运行时解耦【实践】。

### 4.3 知识层（Memory / Knowledge）——"记得什么"

**职责**：管理工作记忆（会话内）、情景记忆（跨会话）与组织知识（档案与术语），让经验可沉淀、可检索、可继承。

- **学术对应**：MemGPT 以操作系统虚拟内存为喻，提出主上下文加外部存储的分层记忆与自定向记忆操作【学术】；Generative Agents（斯坦福小镇）确立"记忆流 + 重要性/新近性/相关性检索 + 周期性反思"的范式【学术】；Reflexion 把单次任务的教训语言化为可复用经验【学术】。
- **业界对应**：GPTs knowledge files 将私有知识挂载到助手【业界】；CLAUDE.md auto memory 让代理自动积累项目学习【业界】。
- **闭源产品实现**（作者自述）：产品的 AI 导航 wiki（AI 导航层）、工程文档档案、仓库根目录的领域术语表构成组织知识三件套；运行时工作区 MEMORY.md 承载长期记忆；市场模板实现岗位知识的组织级复用【实践】。

### 4.4 运行时层（Harness / Runtime）——"如何跑"

**职责**：提供隔离执行单元、会话管理、任务派发与规划—执行循环。

- **业界对应**：Devin 的浏览器+终端+编辑器沙箱【业界】；Copilot coding agent 的异步委派与 PR 回归【业界】；LangGraph 以显式状态图加检查点提供 durable execution，长任务可恢复、可审计【业界】；AutoGen 以多代理对话编排协作【业界】；CrewAI 以 crew 组织角色团队【业界】。ACP（Agent Client Protocol，Zed 发起、JetBrains 共维护的开放协议，JSON-RPC over stdio）正在成为"宿主—编码代理"对接的业界标准，OpenCode、Gemini CLI、Claude Agent 等均以其实现接入【业界】。
- **学术对应**：plan-and-execute 规划范式、ReAct 的交错推理—行动、CAMEL 的角色扮演双代理协作【学术】。
- **闭源产品实现**（作者自述）：Agent 是 OpenClaw 隔离执行单元（独立 workspace 与 agentDir，OpenClaw 原生机制，可对照公开代码验证）；Team 是多员工命名组合，支持 parallel / sequential 两种派发模式，Team 会话使用独立 session key（`team:{teamId}:{agentId}:main`），与 1:1 员工会话完全隔离；parallel 模式下 Agent 间互不可见（独立视角避免锚定效应），sequential 模式单向可见（上游输出拼入下游输入）【实践】。Code Mode 将员工对话经 ACP 对接至 opencode 编码代理（acp-bridge 插件），思考、工具调用、正文三段实时流出——过程可见性本身就是治理能力【实践】。

### 4.5 治理层（Governance）——"受什么约束"

**职责**：权限最小化、红线拦截、破坏性操作人审、审计留痕、分发权限。

- **业界对应**：OpenAI《Practices for Governing Agentic AI Systems》强调人本监督、可审计与渐进授权【业界】；GitHub coding agent"代理开 PR、人做 review"是破坏性操作人审的成熟样板【业界】。
- **学术对应**：间接提示注入研究表明攻击者可通过被检索的文档、网页、邮件劫持代理行为【学术】；AgentDojo 提供了攻防一体的评测环境【学术】；CausalArmor 用因果归因做选择性拦截，在防护强度与可用性之间取得平衡【学术】。
- **闭源产品实现**（作者自述）：Bastion 安全层做消息级安全检查，Team fan-out 前统一过检；AGENTS.md 内置 Red Lines 安全红线；市场分发以 owner 为黄区编辑/上传唯一权限依据，市场条目版本为唯一版本来源，上传 id 与导出 zip 内 id 同源（`roleId || 员工id`）以堵住覆盖洞；产品仓库以统一交付门禁脚本（lint + typecheck + test + 打包）为交付门禁，ESLint 规则防止渲染层 Node 模块泄漏【实践】。

## 5. 能力成熟度模型

本章为数字员工制定 L1–L5 成熟度标准。层级越高，自主性越强，治理与评测要求同步升档——**成熟度不是能力的单维刻度，而是"能力 × 治理 × 评测"的联合门槛**【观点】。

| 层级 | 名称 | 形态 | 能力要求 | 治理要求 | 评测要求 |
|---|---|---|---|---|---|
| L1 | 应答工具 | 单次问答/生成 | 指令遵循、事实准确 | 持有持久身份文件（身份跨会话可恢复，工作状态不跨会话持有）；输入校验、输出边界声明 | 静态 QA 基准 + 人工抽检 |
| L2 | 岗位执行者 | 规则驱动完成任务 | prompt chaining、routing；固定子任务可靠完成 | 操作范围白名单；全量日志留痕 | 任务成功率达标（阈值由实现方显式声明，建议 ≥80%）；中间产物程序化 gate |
| L3 | 流程协作者 | 多步任务、工具组合、追问澄清 | ReAct 式交错推理—行动；主动澄清歧义；多工具编排 | 破坏性操作人审；权限最小化；会话隔离 | SWE-bench / WebArena 类任务基准；轨迹级评估 |
| L4 | 自主专家 | 规划—执行—反思闭环；跨会话学习 | plan-and-execute；Reflexion 自我反思；分层记忆读写；可在低风险任务（实现方须给出风险分级枚举，最低档至少含只读与可逆操作）上长期无人值守 | 行为探针持续监测；红线分层（不可变/可变）；注入防护；记忆写入留痕、可回滚 | 行为探针集 + 回归集；跨会话一致性测试 |
| L5 | 组织成员 | 可治理审计、可复用分发、多智能体协作、持续进化 | 多智能体协作（CAMEL/AutoGen 式）；能力市场化分发；组织记忆共享 | 语义化版本与来源审计；组织级权限模型；协作消息级安全检查 | 多智能体协作基准；人工评估量表；市场质量评级 |

**分层依据**：Anthropic 将 agentic 系统按"预定义路径 vs 动态自主"切分，并给出 prompt chaining → routing → parallelization → orchestrator-workers → 自主 agent 的渐进复杂度阶梯【业界】；学术上 ReAct、Reflexion、MemGPT 分别补足了 L3 的行动循环、L4 的反思与记忆机制【学术】。本文把"组织成员"单列为 L5，因为治理、分发与协作构成质变门槛，而非量变积累【观点】。

**分级传统与在先工作**：以五级刻画成熟度并非新发明——CMMI 以五级度量软件组织能力，SAE 以 L0–L5 分级自动驾驶自动化程度，本规范继承其"自主性升档则治理同步升档"的分级直觉【观点】。业界亦已有多个五级 agentic 成熟度模型，如 sema4.ai 的"五级 agentic 自动化"（见参考来源第 38 条）。前沿安全框架（Anthropic RSP、OpenAI Preparedness、Google FSF）则以能力阈值联动更强缓释义务【业界】。numployee 与这些框架的差异有三：其一，分级对象是部署级员工资质，而非模型风险级；其二，门槛判据是上岗资格，而非系统安全档；其三，治理终点是组织采纳，而非前沿模型的发布治理【观点】。

**闭源产品自评**（作者自述）【实践】：单个 Employee 具备 L3 能力（多步任务 + 工具组合 + Bastion 前置检查）；Team 协作骨架能力初现——parallel / sequential 派发与 5 种目标结果状态（dispatched / failed / blocked / unavailable / skipped）已可用，但按联合门槛规则，在治理与评测未升档前不作 L5 自评；selector 路由、Agent 间共享上下文、per-target 策略等仍在 V2 规划。

## 6. 可移植性标准

数字员工要成为组织资产而非个人玩具，其配置必须可打包、可分发、可继承【观点】。

1. **人格三件套分离**：SOUL.md（人格/语气/边界/信任模型）、AGENTS.md（操作纪律/MCP 纪律/完成规则/Red Lines）、TOOLS.md（本地环境事实）三者职责单一、互不渗透。分离的工程依据不是美学，而是**继承约束**——在多代理生态中，子代理通常只继承纪律文件与环境事实文件（如 OpenClaw 生态中子代理只继承 AGENTS.md + TOOLS.md），关键规则放进 AGENTS.md 才会随委派传播【业界】【实践】。**分类判定标准**：影响工具调用权限、拦截逻辑与完成判定的规则归纪律文件；影响表达风格、口吻与自我披露方式的规则归人格文件。正例：「未跑完回归集不得声明任务完成」影响完成判定，归纪律文件；反例：「向用户解释拒绝时使用温和口吻」虽涉及红线话题，但只影响表达方式，归人格文件。在子代理不继承人格文件的生态中，可推出两条推论：人格写入 AGENTS.md，子代理语气漂移；纪律写入 SOUL.md，规则被子代理绕过——换一个人格文件可被继承的 harness，这两条推论即失效【观点】。
2. **单一职责与分层协议**：一个文件只回答一类问题。AGENTS.md 采用目录树分层协议——深层优先、按需读取；根文件保持精简，避免膨胀吃光上下文窗口。Claude Code 官方文档同样警告：CLAUDE.md 过长会挤占任务空间、迫使频繁压缩【业界】。
3. **语义化版本**：人格包版本随内容演进——新增段落升 minor、修正升 patch。市场条目版本是员工的唯一版本来源，不信任安装包内自声明版本，以防元数据漂移；本地导入无市场上下文时才以包内声明兜底【实践】。
4. **继承协议**：多层规则冲突时深层优先，与 AGENTS.md 目录树协议一致；消费方一律按标识（如 roleId）解析身份，不按 id 等式匹配，容忍历史数据漂移而不重开安全洞【实践】。
5. **环境事实与策略分离**：TOOLS.md 只写"本机有什么、路径是什么"这类可验证事实；策略（该做什么、不该做什么）归 AGENTS.md。事实随机器变化，策略随组织变化，二者生命周期不同，必须分文件治理【观点】。
6. **受管块（managed block）思想**：员工配置由"用户内容"与"托管内容"分块组成。托管区块以显式标记圈定，标记格式为 `<!-- numployee:managed begin v<版本> -->` 与 `<!-- numployee:managed end -->`（实现方可自定义标记名，但必须在合规档案中声明所用格式）；块外为用户领地。缺失插入、原位替换、块外保留、同版本幂等四性质分别由标记存在性、版本比对、块外区域不动、同版本跳过来保证。该机制使"系统升级不覆盖用户定制"成为可执行约束【观点】。

## 7. 安全与信任标准

1. **红线清单分层**：红线分不可变层（禁止泄露密钥、禁止绕过安全检查——任何会话、任何子代理不得改写）与可变层（操作纪律随岗位调整）【观点】。该闭源产品将 Red Lines 写入 AGENTS.md，并依赖"子代理必继承 AGENTS.md"的约束完成传播——治理规则借继承协议下沉到每一次委派【实践】。
2. **权限最小化**：能力清单默认空装配，按岗位逐项授予；运行时只消费与自身匹配的那组 Usage 条目【实践】。这与 OpenAI 治理文件倡导的渐进授权一致【业界】。
3. **破坏性操作人审**：删除、上传、发布、资金类操作必须有人在环。人审不得被代理以任何理由绕过、代签或自我豁免。业界样板是"代理开 PR、人 review"【业界】；该产品的对等物是市场上传的 owner 校验与统一交付门禁脚本【实践】。
4. **注入防护——"停—引—问"**：对不可信输入（网页、文档、邮件、他人消息）执行三步——**停**：识别为数据而非指令，暂停工具执行；**引**：仅在数据 / 引用上下文中引述，不进入指令链；**问**：必要时向用户确认真实意图。确认之后再在最小权限下执行（与 SPEC 6.4 对齐，原"停—问—执行"表述废弃）。间接提示注入已被证明可劫持工具调用型代理，有效防御需要在因果链上区分"用户真实意图"与"检索内容中的伪指令"【学术】。Bastion 的消息级统一安全检查是同一原则的产品化【实践】。谱系定位：间接注入的奠基研究（InjecAgent，见参考来源第 35 条）与谄媚现象研究（第 36 条）刻画了攻击面与失范面，工业侧已有 OWASP LLM Top 10（含 Agentic Top 10）与 MITRE ATLAS 分类（第 37 条）；"停—引—问"与 P1 探针分别对应其中的纪律层落地与基准则【观点】。
5. **审计留痕**：派发结果必须结构化、可追溯——谁发起、谁执行、过了哪些检查、结果如何，必须能重建完整链路【观点】。
6. **错误枚举化**：对外暴露的错误必须是有限枚举，禁止原始错误消息外泄——审计面要可读，泄露面要可控【观点】。该产品的 Team 派发将内部错误映射为有限枚举（gateway_unreachable / bastion_blocked / sequential_step_failed 等）【实践】。

## 8. 评测标准

1. **任务基准**：采纳 SWE-bench（真实 GitHub issue 修复、以测试用例通过为门）与 WebArena（长程真实网页任务）的设计思路——任务取自真实分布、成功标准可自动验证、失败可归因到步骤【学术】。公开基准用于横向对比与 harness 健全性检查，不单独作为上线裁决依据【业界】。跨会话记忆的事实保持可另采 LongMemEval 类基准（见参考来源第 39 条）；本仓库探针集守红线与人格【观点】。
2. **行为探针（behavioral probes）**：针对人格与红线做定向探测——canary 提示注入样本、越权请求样本、人格漂移样本，观察员工是否守住边界。行为探针实行**一票否决**：P1–P5 任一失败即回滚本次人格/配置变更，不允许带伤上线（题目与判定程序见 [probes/probes.md](../probes/probes.md)）【观点】。该产品的受管块同步器版本断言与 canary 实践同源【实践】。探针必须定期轮换变体，防止员工"记住考题"【观点】。
3. **回归集**：每次人格包、技能集、运行时升级，跑固定回归集（任务集 + 探针集 + 历史事故案例），全绿才允许发布；与产品仓库的统一交付门禁同构，把"升级不破坏行为"变成可执行约束【实践】。
4. **人工评估量表**：L5 的协作表现与组织适配度无法全自动评估。建议量表维度：任务完成质量、指令遵循、边界遵守、协作可读性、知识沉淀质量，按 5 分制双评审取均值，双评审分差 ≥2 分即分歧过大，触发复核【观点】。
5. **评测防博弈**：公开基准存在 gold answer 泄漏与奖励黑客化风险——2026 年的独立审计发现 WebArena 存在 gold answer 经 `file://` 泄漏、可被扫描代理在不解题的情况下拿到满分；另有研究报告显示部分前沿模型在评测中出现奖励黑客化行为【业界】。评测管线必须内建防博弈设计：评测数据与训练 / 检索语料隔离、泄漏通道审计、探针轮换、私有回归集受访问控制；开放性与防作弊的取舍须显式声明【观点】。

## 9. 产业实践映射表

| 业界方案 | 对应白皮书分层/标准 | 闭源产品案例实现（作者自述，未经独立验证） |
|---|---|---|
| OpenClaw SOUL.md / IDENTITY.md / USER.md 工作区文件 | 人格层 | 产品的提示词增强模板目录 → SOUL.md（v5.4.0） |
| Claude Code CLAUDE.md + auto memory | 人格层 + 知识层 | 根 AGENTS.md + 产品 AI 导航 wiki + 工程档案 + 领域术语表 |
| OpenAI GPTs（instructions / knowledge / actions） | 人格 / 知识 / 能力层 | Role 指令 + 市场知识 + Usage 条目 |
| CrewAI（role / goal / backstory） | 人格层 | Role 模板（名称 / 描述 / 指令） |
| LangGraph durable execution | 运行时层 | OpenClaw Agent 隔离执行 + Team session 隔离 |
| AutoGen / CAMEL 多代理协作 | 运行时层 | Team parallel / sequential 派发 + 5 种目标结果状态（dispatched / failed / blocked / unavailable / skipped） |
| Devin / Copilot coding agent（沙箱 + 人审 PR） | 运行时层 + 治理层 | Code Mode（ACP codeagent）+ Bastion + 市场 owner 校验 |
| Zed / JetBrains Agent Client Protocol（开放协议，JSON-RPC over stdio） | 运行时层 | Code Mode：acp-bridge 对接 opencode，思考/工具/正文三段流式承载 |
| SWE-agent + SWE-bench 评测回路 | 评测标准 | 产品交付门禁脚本 + 受管块同步器版本断言 |
| RPA → Agent 数字劳动力叙事 | 背景与定义 | Role → Employee → Agent 领域链路 |
| Agent2Agent 协议（A2A）/ AGENTS.md 开放标准 | 通信层与纪律层的标准化 | 互补协议与标准（见 §3.1），案例产品无对应物 |

## 10. 路线图与开放问题

**近期（该产品 V2 方向）**【实践】：Team 引入 selector（LLM 路由）派发、Agent 间共享上下文开关、per-target Bastion 策略、Team 模板经市场分发。

**中期**：数字员工跨设备、跨组织的身份与记忆同步；组织级审计面板；行为探针平台化。

**开放问题**【观点】：

1. **记忆的遗忘判据**：跨会话学习需要决定"什么该沉淀、什么该丢弃"。MemGPT 给了读写机制，没给写入判据；当前工程实践依赖启发式，缺乏理论保证。
2. **多智能体责任归属**：Team sequential 链中一步出错，责任在人、在员工、还是在编排？组织需要新的责任认定规则，这与 AI 工伤认定同构。
3. **人格健康度量化**：persona 研究提示一致性受上下文与记忆机制侵蚀（EMNLP 2025 在对话语境中实测了一致性漂移）；目前尚无可量化的"人格健康度"指标。
4. **评测博弈的军备竞赛**：基准泄漏与奖励黑客化使公开基准的半衰期持续缩短；私有回归集将成为组织的核心资产，也可能成为新的封闭墙——评测的开放性与防作弊之间存在结构性张力。

---

## 参考来源

**学术**

（注：第 13 条为机构研究博客，按研究质量引用，严格归类属业界。）

1. Zhiheng Xi et al. The Rise and Potential of Large Language Model Based Agents: A Survey. arXiv:2309.07864, 2023. <https://arxiv.org/abs/2309.07864>
2. Shunyu Yao et al. ReAct: Synergizing Reasoning and Acting in Language Models. ICLR 2023. <https://arxiv.org/abs/2210.03629>
3. Noah Shinn et al. Reflexion: Language Agents with Verbal Reinforcement Learning. NeurIPS 2023. <https://arxiv.org/abs/2303.11366>
4. Timo Schick et al. ToolFormer: Language Models Can Teach Themselves to Use Tools. 2023. <https://arxiv.org/abs/2302.04761>
5. Charles Packer et al. MemGPT: Towards LLMs as Operating Systems. 2023. <https://arxiv.org/abs/2310.08560>
6. Joon Sung Park et al. Generative Agents: Interactive Simulacra of Human Behavior. UIST 2023. <https://arxiv.org/abs/2304.03442>
7. Guohao Li et al. CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society. NeurIPS 2023. <https://arxiv.org/abs/2303.17760>
8. Xiao Liu et al. AgentBench: Evaluating LLMs as Agents. ICLR 2024. <https://arxiv.org/abs/2308.03688>
9. Shuyan Zhou et al. WebArena: A Realistic Web Environment for Building Autonomous Agents. ICLR 2024. <https://arxiv.org/abs/2307.13854>
10. Carlos E. Jimenez et al. SWE-bench: Can Language Models Resolve Real-World GitHub Issues? ICLR 2024. <https://arxiv.org/abs/2310.06770>
11. Edoardo Debenedetti et al. AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents. 2024. <https://arxiv.org/abs/2406.13352>
12. CausalArmor: Efficient Indirect Prompt Injection Guardrails via Causal Attribution. 2026. <https://arxiv.org/html/2602.07918v1>
13. Anthropic. The Persona Selection Model: Why AI Assistants might Behave like Humans（机构研究博客）. 2026-02. <https://alignment.anthropic.com/2026/psm/>
14. Pranav Bhandari et al. Can LLM Agents Maintain a Persona in Discourse? EMNLP 2025, pp. 29213–29229. DOI: 10.18653/v1/2025.emnlp-main.1487. <https://aclanthology.org/2025.emnlp-main.1487.pdf>
15. Qingyun Wu et al. AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation. 2023. <https://arxiv.org/abs/2308.08155>

**业界**

16. Anthropic. Building Effective Agents. 2024-12. <https://www.anthropic.com/engineering/building-effective-agents>
17. Anthropic / Claude Code Docs. How Claude remembers your project（Claude Code Memory 文档）. <https://code.claude.com/docs/en/memory>
18. OpenClaw Workspace Files Explained: SOUL.md, AGENTS.md, HEARTBEAT.md and More. 2026-03. <https://openagents.mom/blog/openclaw-workspace-files-explained>
19. OpenClaw. Default AGENTS.md Reference. <https://docs.openclaw.ai/reference/AGENTS.default>
20. Spinach. Everything You Need to Know About the OpenAI Assistants API and GPTs. 2026-08. <https://www.spinach.ai/blog/openai-assistants-api-gpts>
21. GitHub. Copilot coding agent is now generally available! 2025-09. <https://github.com/orgs/community/discussions/159068>
22. Princeton NLP. SWE-agent. <https://github.com/SWE-agent/SWE-agent>
23. SaaSCity. SWE-2 Is Free on Devin's $20 Plan. 2026-09. <https://saascity.io/blog/devin-swe-2-20-dollar-plan-september-2026>
24. CrewAI. Agents — official documentation. <https://docs.crewai.com/v1.15.20/en/concepts/agents>
25. LangChain. LangChain vs. AutoGen in 2026: What the Maintenance Announcement Changed. 2026-06. <https://www.langchain.com/resources/langchain-vs-autogen>
26. BetterYeah. 从 RPA 到 Agent 数字员工：企业 AI 转型的必经之路. 2025-06. <https://www.betteryeah.com/blog/rpa-to-agent-digital-employees-ai-transformation-path>
27. 实在智能. RPA 数字员工到 Agent 数字员工，有什么质的发展？ 2024-06（2026-08 修订）. <https://www.ai-indeed.com/encyclopedia/9328.html>
28. 新京报. 2026 年 AI 数字员工行业趋势（援引 IDC 数据）. 2026-07. <https://m.bjnews.com.cn/detail/1783562552129855.html>
29. Moogician. How We Broke Top AI Agent Benchmarks. 2026-04. <https://moogician.github.io/blog/2026/trustworthy-benchmarks-cont/>
30. OpenAI. Practices for Governing Agentic AI Systems. 2023-12. <https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf>
31. Zed Industries / JetBrains. Agent Client Protocol（ACP）——编辑器与编码代理对接的开放协议（JSON-RPC over stdio；OpenCode、Gemini CLI、Claude Agent 等均已实现）. 2025-08-27 发布（ACP Registry 于 2026-01 上线）. <https://github.com/zed-industries/agent-client-protocol>
32. Model Context Protocol. MCP joins the Agentic AI Foundation. 2025-12. <https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/>
33. AGENTS.md Open Standard（2025-12 起由 Linux Foundation Agentic AI Foundation 托管）. <https://factory.com/news/agents-md>；AAIF 成立与托管公告 <https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation>
34. Google et al. Agent2Agent Protocol (A2A)，v1.0 于 2026-03 发布，2026-08 转入 Linux Foundation Agentic AI Foundation. <https://a2aproject.github.io/A2A/>；并入 A2A 的 "ACP" 为 IBM/BeeAI 的 Agent Communication Protocol（与第 31 条 Zed 的 Agent Client Protocol 同名不同物），公告 <https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/>
35. Qiusi Zhan et al. InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents. ACL 2024 Findings. <https://aclanthology.org/2024.findings-acl.624/>
36. Mrinank Sharma et al. Towards Understanding Sycophancy in Language Models. ICLR 2024. <https://openreview.net/forum?id=tvhaxkMKAn>
37. OWASP. Top 10 for Large Language Model Applications（含 Agentic Top 10）. <https://owasp.org/www-project-top-10-for-large-language-model-applications/>；MITRE ATLAS. <https://atlas.mitre.org/>
38. sema4.ai. The Five Levels of Agentic Automation. <https://sema4.ai/blog/the-five-levels-of-agentic-automation/>
39. LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. ICLR 2025. <https://arxiv.org/abs/2410.10813>；面向 web agent 的 LongMemEval-V2（2026-05）见 <https://xiaowu0162.github.io/longmemeval-v2/>
40. ISO/IEC 22989:2022. Information technology — Artificial intelligence — AI concepts and terminology. <https://www.iso.org/standard/74296.html>
41. IEEE P3777. Standard for Benchmarking and Performance Metrics of Artificial Intelligence (AI) Agents（PAR 于 2025-12-10 获批）. <https://standards.ieee.org/ieee/3777/12350>
