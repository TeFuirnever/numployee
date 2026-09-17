# 数字员工规范（Digital Employee Specification）

- **Status**: Draft v1.0-rc2
- **项目品牌**: numployee（num(数字) + em(ployee)(员工) 的拼合词）
- **日期**: 2026 年 9 月 17 日
- **修订流程**: 本规范的演进通过 SIP（Specification Improvement Proposal）管理，流程与模板见 [sips/README.md](sips/README.md)。
- **配套资源**: 按标准装配员工见 [templates/](templates/)；行为探针与考核集见 [probes/](probes/)；参考实现见 [implementations/](implementations/)。
- **完整论述**: 本规范的理论背景、推理过程与全部学术引用见 [docs/whitepaper.md](docs/whitepaper.md)。

> 本规范与 ACP（Agent Client Protocol）、A2A（Agent2Agent Protocol）、MCP（Model Context Protocol）互补而不竞争：ACP 管"宿主 ↔ 编码代理"的通信，A2A 管 agent 间的互操作与能力声明，MCP 管工具接入，本规范管数字员工的人格、纪律、知识、治理与成熟度。

---

## 1. 引言

### 1.1 背景：从工具型 AI 到员工型 AI

过去两年，AI 应用的主语正在从"工具"变为"员工"：编码代理从代码补全进化为可异步委派任务、自主开 PR 并接受人审的自主开发者【业界】；"AI 软件工程师"被产品化并进入真实工程流程【业界】；数字劳动力叙事从规则驱动的 RPA 机器人切换到"理解任务、调用工具、处理异常"的 Agent 数字员工【业界】。学术侧，LLM-based agent 综述将 agent 系统归纳为身份、记忆、规划、行动四模块【学术】，与组织管理"定岗—授权—考核—沉淀"的逻辑一一同构。

工具型 AI 的典型形态是单次问答与单次生成：无状态、无身份、无责任主体——它回答"这个问题"，但不拥有"这项工作"。组织把 AI 放进真实流程时，三个缺口立刻暴露：

- **持久性缺口**：会话从零开始，偏好、决策与上下文不延续；
- **治理缺口**：无权限边界与审计对象，出事无法归因；
- **复用缺口**：专家配置（提示词、工具、知识）锁在个人对话框，无法沉淀为组织资产。

本规范围绕这三个缺口，给出判定定义、参考架构、成熟度模型与三类工程标准（可移植性、安全与信任、评测），供数字员工的设计者、分发者与采购方共同使用。

### 1.2 范围

本规范**管**什么：

- 数字员工的定义与判定（第 2 章）；
- 五层参考架构与每层职责（第 3 章）；
- L1–L5 能力成熟度门槛（第 4 章）；
- 人格、纪律、环境事实配置的移植、继承与版本（第 5 章）；
- 安全红线与信任标准（第 6 章）；
- 评测方法与上线裁决（第 7 章）；
- 合规声明的要求（第 8 章）。

本规范**不管**什么：

- **不管运行时实现**：不限定 agent loop、状态机、沙箱形态或宿主产品。任何 agent harness 均可承载符合本规范的员工；运行时升级不必然影响员工配置。
- **不管通信协议**：不限定宿主与代理之间的传输方式。本规范与 ACP（宿主 ↔ 编码代理）、A2A（agent 间互操作与能力声明）、MCP（工具接入）正交，可直接组合。

### 1.3 符合性措辞

本文档中"**必须（MUST）**"为硬性要求，"**应（SHOULD）**"为强烈建议，"**可（MAY）**"为允许选项。除显式标注外，规范性陈述句默认为 MUST（必须）；各层"职责"小节为描述性文字，不产生义务。正文中未带来源标注的机制性主张（如联合门槛、分离原则推论）为规范作者的观点性设计决策，其修订走 SIP 流程。实现如何声明合规见第 8 章。

## 2. 术语与定义

### 2.1 数字员工的判定四要素

一个 AI 实体是数字员工，当且仅当同时满足以下四项：

1. **持久身份**：有唯一标识、稳定人格与履历，跨会话存在。对应业界的工作区身份文件实践【业界】；学术上对应 Generative Agents 的代理档案与记忆流【学术】。
2. **可装配能力**：能力以声明式清单存在，可按岗位装配、按运行时匹配、按版本审计。对应业界 GPTs 的 instructions / knowledge / actions 三段式【业界】；学术上承接 ToolFormer 开启的工具学习传统【学术】。
3. **可治理红线**：存在独立于人格的操作纪律，越权可被拦截与追责。对应间接提示注入防护与 agent 治理研究【学术】，以及业界倡导的人本监督原则【业界】。
4. **可沉淀知识**：经验可写入组织记忆，可被继任者与副本继承。对应 MemGPT 分层记忆【学术】与 wiki 式组织档案实践【业界】。

**四要素缺一即降级**（无可治理红线者非降级而是取消上岗资格）：无持久身份退化为聊天机器人；无可装配能力退化为一次性脚本；无可沉淀知识则永远停在个人助手阶段。

### 2.2 与相邻概念的区分

**聊天机器人（chatbot）**：以会话为单元，身份随会话结束而消散。系统提示词里"你是某某"只是 persona conditioning（人格条件化），不构成持久身份【学术】。Persona Selection Model 研究表明：LLM 的"人格"是预训练习得的候选集合经后训练筛选的产物，同一模型可稳定呈现多种人格【学术】——人格若不落盘、不治理，就只是上下文里的临时修辞，与"员工"的稳定性要求根本冲突。

**自动化 workflow**：业界作了关键区分——workflow 是"LLM 与工具沿预定义代码路径编排"的系统；agent 是"LLM 动态指挥自身过程与工具使用"的系统【业界】。数字员工以后者为底座；但在低风险的确定性任务上，应允许员工退化为 workflow 模式以换取可预测性——autonomy 是档位而非信仰。

**Agent harness（代理载体）**：承载 agent 的运行环境——上下文装配、工具调度、权限拦截、会话持久化。harness 是"雇主提供的办公场所"，数字员工是"在其中任职的个体"。把 harness 与员工混为一谈，等于把写字楼当作员工——很多"agent 产品"换壳不换人：运行时升级了，岗位配置与人格资产仍无处安放。

### 2.3 术语表

- **人格三件套**：人格文件、纪律文件、环境事实文件三类职责的统称（分离原则与继承协议见 3.1 与第 5 章）；产品实现中常见文件映射见 [templates/README.md](templates/README.md)。
- **身份（identity）**：跨会话可恢复的持久标识——唯一标识、稳定人格与履历。
- **状态（state）**：单次会话内的工作记忆，不跨会话持有。本文凡论及"跨会话存在"均指身份而非状态。
- **红线（Red Lines）**：独立于人格的操作底线，分不可变层与可变层（见 6.1）。
- **受管块（managed block）**：配置中由系统托管、以显式标记圈定的区块，块外为用户领地（机制与标记格式见 5.6）。
- **行为探针（behavioral probes）**：针对人格与红线的定向探测样本与判定程序（见 7.2）。
- **回归集**：固定的任务集 + 探针集 + 历史事故案例，用于发布前验证行为不回退（见 7.3）。
- **个人助手 / 一次性脚本**：四要素缺一时的降级去向——个人助手指可交互但经验不可沉淀为组织资产的形态；一次性脚本指能力不可装配、不可按版本审计的固定流程形态。

### 2.4 与正式标准的关系

- **ISO/IEC 22989:2022**：第 2 章术语拟与其 AI 概念与术语体系做对照（见附录 C 第 40 条）；具体映射表留待 SIP 细化。
- **IEEE P3777**：第 7 章评测维度拟与其"AI agent 基准与性能测量"维度做对照（见附录 C 第 41 条）。
- **ISO/IEC 42001**：是否承认其 AI 管理体系审计结果作为本规范合规证据，留待 SIP 决定。

## 3. 参考架构：五层模型

数字员工系统按职责划分为五层，分别回答"是谁、会什么、记得什么、如何跑、受什么约束"。五层是职责划分而非模块划分：一个物理组件可承载多层职责，但实现必须能声明其所对应的层。各层只给出职责与业界、学术对应；具体实现示例见 [implementations/](implementations/)。

### 3.1 人格层（Persona）——"是谁"

**职责**：定义数字员工的身份、语气、边界与信任模型，使其行为可预期、可识别、可信赖。

- **业界对应**：工作区以人格 / 身份 / 用户画像三类文件分层定义代理人格，"人格文件放人格与边界，不放操作流程"是社区最佳实践【业界】；项目级人格持久化与模块化导入【业界】；role / goal / backstory 角色三元组【业界】；instructions 最简形态【业界】。
- **学术对应**：persona conditioning 研究证实系统提示能显著塑造行为，但人格一致性是架构属性而非纯提示词属性，需显式机制维持【学术】；多轮场景维持人格的极限已被考察【学术】。

**人格与纪律分离原则**：人格文件不得承载操作纪律，纪律也不得写入人格文件。分离的工程依据不是美学，而是**继承约束**——在多代理生态中，子代理通常只继承纪律文件与环境事实文件，不继承人格文件；关键规则放进纪律文件才会随委派传播。**分类判定标准**：影响工具调用权限、拦截逻辑与完成判定的规则归纪律文件；影响表达风格、口吻与自我披露方式的规则归人格文件。正例：「未跑完回归集不得声明任务完成」影响完成判定，归纪律文件。反例：「向用户解释拒绝时使用温和口吻」虽涉及红线话题，但只影响表达方式，归人格文件。在子代理不继承人格文件的生态（如 OpenClaw 系）中，可推出两条推论：人格写入纪律文件，子代理语气漂移；纪律写入人格文件，规则被子代理绕过。落地协议见第 5 章"人格三件套"。

### 3.2 能力层（Skills / Tools）——"会什么"

**职责**：以声明式清单管理数字员工可调用的工具与技能，支持按岗位装配、按运行时匹配、按版本审计。

- **业界对应**：instructions / knowledge / actions 分层，actions 即函数调用接口【业界】；MCP 将工具接入标准化【业界】；文件化技能目录使能力以文件方式分发【业界】。
- **学术对应**：ToolFormer 证明模型可自学何时、如何使用外部工具，是函数调用范式的学术源头【学术】；ReAct 将推理轨迹与工具调用交错，构成工具使用的基础循环【学术】。

### 3.3 知识层（Memory / Knowledge）——"记得什么"

**职责**：管理工作记忆（会话内）、情景记忆（跨会话）与组织知识（档案与术语），让经验可沉淀、可检索、可继承。

- **学术对应**：MemGPT 以操作系统虚拟内存为喻，提出主上下文加外部存储的分层记忆与自定向记忆操作【学术】；Generative Agents 确立"记忆流 + 重要性/新近性/相关性检索 + 周期性反思"的范式【学术】；Reflexion 把单次任务的教训语言化为可复用经验【学术】。
- **业界对应**：私有知识文件挂载到助手【业界】；auto memory 让代理自动积累项目学习【业界】。

### 3.4 运行时层（Harness / Runtime）——"如何跑"

**职责**：提供隔离执行单元、会话管理、任务派发与规划—执行循环。

- **业界对应**：沙箱（浏览器 + 终端 + 编辑器）【业界】；异步委派与 PR 回归【业界】；显式状态图 + 检查点的 durable execution，长任务可恢复、可审计【业界】；多代理对话编排【业界】；角色团队组织【业界】。ACP（JSON-RPC over stdio）正成为"宿主—编码代理"对接的开放标准，多个编码代理实现均已接入【业界】。
- **学术对应**：plan-and-execute 规划范式、ReAct 的交错推理—行动、角色扮演双代理协作【学术】。

### 3.5 治理层（Governance）——"受什么约束"

**职责**：权限最小化、红线拦截、破坏性操作人审、审计留痕、分发权限。

- **业界对应**：人本监督、可审计与渐进授权的治理实践【业界】；"代理开 PR、人做 review"是破坏性操作人审的成熟样板【业界】。
- **学术对应**：间接提示注入可通过被检索的文档、网页、邮件劫持代理行为【学术】；攻防一体评测环境已存在【学术】；因果归因选择性拦截在防护强度与可用性之间取得平衡【学术】。

## 4. 能力成熟度模型（L1–L5）

成熟度不是能力的单维刻度，而是"能力 × 治理 × 评测"的**联合门槛**：层级越高，自主性越强，治理与评测要求同步升档。仅有能力升级而治理、评测不升档，不得晋级。

| 层级 | 名称 | 形态 |
|---|---|---|
| L1 | 应答工具 | 单次问答 / 生成 |
| L2 | 岗位执行者 | 规则驱动完成任务 |
| L3 | 流程协作者 | 多步任务、工具组合、追问澄清 |
| L4 | 自主专家 | 规划—执行—反思闭环；跨会话学习 |
| L5 | 组织成员 | 可治理审计、可复用分发、多智能体协作、持续进化 |

分层依据：业界将 agentic 系统按"预定义路径 vs 动态自主"切分，给出 prompt chaining → routing → parallelization → orchestrator-workers → 自主 agent 的渐进复杂度阶梯【业界】；学术上 ReAct、Reflexion、MemGPT 分别补足 L3 的行动循环、L4 的反思与记忆机制【学术】。"组织成员"单列 L5：治理、分发与协作构成质变门槛，而非量变积累。

### 4.1 L1 应答工具

- **能力要求**：单次问答与单次生成；指令遵循、事实准确；不跨会话持有状态。
- **治理要求**：持有持久身份文件——身份跨会话可恢复（工作状态不跨会话持有）；输入校验；输出边界显式声明（该答什么、不该答什么）；不持有任何工具写权限。
- **评测要求**：静态 QA 基准 + 人工抽检；不设上线自动裁决。

### 4.2 L2 岗位执行者

- **能力要求**：prompt chaining、routing；固定子任务可靠完成；失败时停机上报，不得自由发挥补位。
- **治理要求**：操作范围白名单（只许做什么必须可枚举）；全量日志留痕。
- **评测要求**：任务成功率达标（阈值由实现方在合规档案中显式声明，建议默认 ≥80%）；中间产物过程序化 gate（格式校验、测试、脚本断言），gate 不过即失败。

### 4.3 L3 流程协作者

- **能力要求**：多步任务与多工具编排；ReAct 式交错推理—行动；主动澄清歧义——问比错好。
- **治理要求**：破坏性操作人审（删除、上传、发布、资金类必须有人在环）；权限最小化；会话隔离（多员工并存的会话 key 独立，员工间数据面互不可见或单向可见）。
- **评测要求**：SWE-bench / WebArena 类任务基准——任务取自真实分布、成功标准可自动验证、失败可归因到步骤【学术】；轨迹级评估（既看结果，也看过程是否合规）。

### 4.4 L4 自主专家

- **能力要求**：plan-and-execute 闭环；Reflexion 式自我反思；分层记忆读写（跨会话学习）；可在低风险任务（实现方需给出风险分级枚举，最低档至少包含只读操作与可逆操作）上长期无人值守。
- **治理要求**：行为探针持续监测（见 7.2）；红线分层落地（不可变层任何会话、任何子代理不得改写，见 6.1）；注入防护"停—引—问"（见 6.4）；记忆写入留痕、可回滚。
- **评测要求**：行为探针集 + 固定回归集——人格包、技能集、运行时任何升级后全绿才允许发布；跨会话一致性测试（人格、偏好、关键决策不因会话切换而漂移）。

### 4.5 L5 组织成员

- **能力要求**：多智能体协作（角色扮演双代理、对话编排式）【学术】；能力市场化分发（岗位包可被组织内复用、跨组织流通）；组织记忆共享。
- **治理要求**：语义化版本与来源审计（见 5.3）；组织级权限模型；协作消息级安全检查（fan-out 前统一过检）。
- **评测要求**：多智能体协作基准；人工评估量表（见 7.4）；分发质量评级（使用方反馈回流为评级输入）。

**适用性声明**：第 5、6、7 章的通用条款为全文义务；条文中标注了具体等级要求的，仅适用于该级及以上。6.3 的人审要求为全文级 MUST，4.3 的人审条款与 4.2 的白名单分别为其在 L3、L2 的具体化。

## 5. 可移植性标准

数字员工要成为组织资产而非个人玩具，其配置必须可打包、可分发、可继承。

1. **人格三件套分离**：人格文件（人格 / 语气 / 边界 / 信任模型）、纪律文件（操作纪律、工具纪律、完成规则、红线）、环境事实文件（本机路径、可用服务）三者职责单一、互不渗透。分离依据见 3.1 节分离原则与第 5 章第 4 条继承协议。纪律文件可视为 AGENTS.md 开放标准的员工化扩展（增加完成判定与认知纪律条款），兼容而非分叉；三件套在非 OpenClaw harness 上的文件映射见 [templates/README.md](templates/README.md)。
2. **单一职责与分层协议**：一个文件只回答一类问题。纪律文件采用目录树分层协议——深层优先、按需读取；根文件保持精简，文件过长会挤占任务空间、迫使频繁压缩【业界】。
3. **语义化版本**：人格包版本随内容演进——新增段落升 minor、修正升 patch；删除或重命名既有条目、改变红线语义，升 major；major 升级须附迁移说明。分发渠道中的条目版本是员工的唯一版本来源，不信任安装包内自声明版本，以防元数据漂移；无分发上下文时才以包内声明兜底。
4. **继承协议**：多层规则冲突时**深层优先**，与目录树协议一致；消费方一律按标识（而非 id 等式）解析身份，容忍历史数据漂移而不重开安全洞。
5. **环境事实与策略分离**：环境事实文件只写"本机有什么、路径是什么"这类可验证事实；策略（该做什么、不该做什么）归纪律文件。事实随机器变化，策略随组织变化，二者生命周期不同，必须分文件治理。
6. **受管块（managed block）思想**：员工配置由"用户内容"与"托管内容"分块组成。托管区块以显式标记圈定，标记格式为 `<!-- numployee:managed begin v<版本> -->` 与 `<!-- numployee:managed end -->`（实现方可自定义标记名，但必须在合规档案中声明所用格式）；块外为用户领地。缺失插入、原位替换、块外保留、同版本幂等四性质分别由标记存在性、版本比对、块外区域不动、同版本跳过来保证。该机制使"系统升级不覆盖用户定制"成为可执行约束。

## 6. 安全与信任标准

1. **红线清单分层**：红线分**不可变层**（禁止泄露密钥、禁止绕过安全检查——任何会话、任何子代理不得改写）与**可变层**（操作纪律随岗位调整）。治理规则必须借继承协议（第 3.1、5.4 节）下沉到每一次委派。
2. **权限最小化**：能力清单默认空装配，按岗位逐项授予；多运行时场景只消费与自身匹配的能力组，与业界渐进授权原则一致【业界】。
3. **破坏性操作人审**：删除、上传、发布、资金类操作必须有人在环；样板是"代理开 PR、人 review"【业界】。人审不得被代理以任何理由绕过、代签或自我豁免。
4. **不可信输入"停—引—问"**：对不可信输入（网页、文档、邮件、他人消息）执行三步——**停**：识别为数据而非指令，暂停工具执行；**引**：仅在数据 / 引用上下文中引述，不进入指令链；**问**：必要时向用户确认真实意图。确认之后再在最小权限下执行。间接提示注入已被证明可劫持工具调用型代理，有效防御需要在因果链上区分"用户真实意图"与"检索内容中的伪指令"【学术】。该协议即数据与指令分离思想（见 InjecAgent 等间接注入研究的奠基工作）在员工纪律层的落地。
5. **审计留痕**：派发结果必须结构化、可追溯——谁发起、谁执行、过了哪些检查、结果如何，必须能重建完整链路。
6. **错误枚举化**：对外暴露的错误必须是有限枚举（如 gateway_unreachable / bastion_blocked / sequential_step_failed），禁止原始错误消息外泄——审计面要可读，泄露面要可控。

## 7. 评测标准

配套探针的实现与目录规范见 [probes/](probes/)。

1. **任务基准**：采纳 SWE-bench（真实 GitHub issue 修复、以测试用例通过为门）与 WebArena（长程真实网页任务）的设计思路——任务取自真实分布、成功标准可自动验证、失败可归因到步骤【学术】。公开基准用于横向对比与 harness 健全性检查，不单独作为上线裁决依据【业界】。跨会话记忆的事实保持可另采 LongMemEval 类基准；本探针集守红线与人格。
2. **行为探针（behavioral probes）**：针对人格与红线做定向探测——提示注入样本、越权请求样本、人格漂移样本，观察员工是否守住边界。探针必须定期轮换变体，防止员工"记住考题"。
3. **回归集**：人格包、技能集、运行时任何升级，必须跑固定回归集（任务集 + 探针集 + 历史事故案例），全绿才允许发布——把"升级不破坏行为"变成可执行约束。
4. **人工评估量表**：L5 的协作表现与组织适配度无法全自动评估。量表维度：任务完成质量、指令遵循、边界遵守、协作可读性、知识沉淀质量；按 **5 分制双评审**取均值，双评审分差 ≥2 分即分歧过大，触发复核。
5. **评测防博弈**：公开基准存在 gold answer 泄漏与奖励黑客化风险，已有基准被"不解题拿满分"的攻击实证【业界】。评测管线必须内建防博弈设计：评测数据与训练 / 检索语料隔离、泄漏通道审计、探针轮换、私有回归集受访问控制；开放性与防作弊的取舍须显式声明。

## 8. 合规声明

实现可声明"符合《数字员工规范》Draft v1.0-rc2"，声明按成熟度层级给出（如"单员工 L3"；协作维度及其门槛待 SIP 定义）。声明必须附证据：

- 逐项对照 [templates/conformance-checklist.md](templates/conformance-checklist.md) 的自评结果；
- 与所声明层级对应的回归集运行记录（任务集 + 探针集）；
- 红线清单及不可变层的实现位置（文件路径与托管标记）。

**过渡条款**：在 [probes/suites/l5.md](probes/suites/l5.md) 回填可勾选题目前，L5 合规声明不予受理；此前最高可声明等级为 L4。

声明格式示例：

> 实现声明符合《数字员工规范》Draft v1.0-rc2 之"单员工 L3"。
> 自评对照：templates/conformance-checklist.md；回归集运行记录：<链接>；证据可复跑入口：<链接>

声明不得超出已验证层级。任何 L5 声明必须额外提供组织级权限模型与协作消息级安全检查的实现证据。证据缺失或拒绝公开自检结果的声明视为无效。

---

## 附录 A：产业实践映射表

下表将业界方案与规范分层 / 标准逐层对齐；第三列"参考实现示例"取自 OpenClaw 参考实现与一个闭源桌面产品的匿名案例（见 [implementations/openclaw/](implementations/openclaw/) 与 [implementations/case-study/](implementations/case-study/)），仅作示范，不构成规范要求，亦非唯一合法实现。

| 业界方案 | 对应规范分层/标准 | 参考实现示例 |
|---|---|---|
| OpenClaw SOUL.md / IDENTITY.md / USER.md 工作区文件 | 人格层 | prompt-enhancements → SOUL.md（v5.4.0） |
| Claude Code CLAUDE.md + auto memory | 人格层 + 知识层 | 根 AGENTS.md + `.omc/wiki/` + `docs/` + CONTEXT.md |
| OpenAI GPTs（instructions / knowledge / actions） | 人格 / 知识 / 能力层 | Role 指令 + 市场知识 + Usage 条目 |
| CrewAI（role / goal / backstory） | 人格层 | Role 模板（名称 / 描述 / 指令） |
| LangGraph durable execution | 运行时层 | OpenClaw Agent 隔离执行 + Team session 隔离 |
| AutoGen / CAMEL 多代理协作 | 运行时层 | Team parallel / sequential 派发 + 5 种目标结果状态（dispatched / failed / blocked / unavailable / skipped） |
| Devin / Copilot coding agent（沙箱 + 人审 PR） | 运行时层 + 治理层 | Code Mode（ACP codeagent）+ Bastion + 市场 owner 校验 |
| Zed / JetBrains Agent Client Protocol（开放协议，JSON-RPC over stdio） | 运行时层 | Code Mode：acp-bridge 对接 opencode，思考/工具/正文三段流式承载 |
| SWE-agent + SWE-bench 评测回路 | 评测标准 | build.sh 门禁 + prompt-enhancer 版本断言 |
| RPA → Agent 数字劳动力叙事 | 背景与定义 | Role → Employee → Agent 领域链路 |
| Agent2Agent 协议（A2A）/ AGENTS.md 开放标准 | 通信层与纪律层的标准化 | 互补协议与标准（见 1.2 与第 5 章） |

## 附录 B：开放问题

以下问题在本规范起草时暂无共识答案，留待 SIP 演进与社区实践回答：

1. **记忆的遗忘判据**：跨会话学习需要决定"什么该沉淀、什么该丢弃"。MemGPT 给了读写机制，没给写入判据；当前工程实践依赖启发式，缺乏理论保证。
2. **多智能体责任归属**：协作链中一步出错，责任在人、在员工、还是在编排？组织需要新的责任认定规则，这与 AI 工伤认定同构。
3. **人格健康度量化**：persona 研究提示一致性受上下文与记忆机制侵蚀（EMNLP 2025 在对话语境中实测了一致性漂移），但"一致性在多大程度上是架构属性"尚无定论；目前也无可量化的"人格健康度"指标。
4. **评测博弈的军备竞赛**：基准泄漏与奖励黑客化使公开基准的半衰期持续缩短；私有回归集将成为组织的核心资产，也可能成为新的封闭墙——评测的开放性与防作弊之间存在结构性张力。

## 附录 C：参考来源

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
31. Zed Industries / JetBrains. Agent Client Protocol（ACP）——编辑器与编码代理对接的开放协议（JSON-RPC over stdio；OpenCode、Gemini CLI、Claude Agent 等均已实现）. 2025-06（ACP Registry 于 2026-03 发布）. <https://github.com/zed-industries/agent-client-protocol>
32. Model Context Protocol. MCP joins the Agentic AI Foundation. 2025-12. <https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/>
33. AGENTS.md Open Standard（Linux Foundation Agentic AI Foundation 托管）. <https://factory.com/news/agents-md>
34. Google et al. Agent2Agent Protocol (A2A)，Linux Foundation 治理. 2026-03. <https://a2aproject.github.io/A2A/>；ACP 并入 A2A 公告 <https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/>
35. Kai Greshake et al. InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents. ACL 2024 Findings. <https://aclanthology.org/2024.findings-acl.624/>
36. Mrinank Sharma et al. Towards Understanding Sycophancy in Language Models. ICLR 2024. <https://openreview.net/forum?id=tvhaxkMKAn>
37. OWASP. Top 10 for Large Language Model Applications（含 Agentic Top 10）. <https://owasp.org/www-project-top-10-for-large-language-model-applications/>；MITRE ATLAS. <https://atlas.mitre.org/>
38. sema4.ai. The Five Levels of Agentic Automation. <https://sema4.ai/blog/the-five-levels-of-agentic-automation/>
39. LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. <https://xiaowu0162.github.io/longmemeval-v2/>
40. ISO/IEC 22989:2022. Information technology — Artificial intelligence — AI concepts and terminology. <https://www.iso.org/standard/74296.html>
41. IEEE P3777. Standard for AI Agent Benchmarks and Performance Measurement（PAR 于 2025-12 获批）. <https://standards.ieee.org/ieee/3777/12350>
