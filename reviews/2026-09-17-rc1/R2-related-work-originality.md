材料包与外部证据均已就绪，证据链闭合。以下是完整评审报告。
> 档案说明（2026-09-17 去品牌决议）：本评审报告中的产品名称与私有仓库路径已匿名化，评审结论与证据不受影响。


---

# R2 评审报告 · numployee《数字员工规范》v1.0-rc1

## Review setup

**Input scope**
评审材料包含五个只读文件，即 SPEC.md（标准正文草案 v1.0-rc1）、docs/whitepaper.md（白皮书 v1.0，含 31 条参考来源）、probes/probes.md（12 题探针集）、templates/conformance-checklist.md（合规检查清单）、README.md（项目门面与生态位表）。我对 numployee 目录做了全文检索以确认材料包外的引用情况，未修改任何文件。

**Assessment boundary**
本人侧重 originality 与 importance，按五轴给出判断，同时把 technical soundness 中与原创性相关的缺陷纳入。全程独立工作，未与其他评审人交流。允许使用 WebSearch 核查在先工作是否存在，以下所有外部证据均注明 URL 与检索日期 2026-09-17。材料包内属于项目自身宇宙的事实（OpenClaw 生态、闭源产品 实现细节）按材料包口径采信，仅对可由公开渠道核验的论断做外部核查。

**Shared manuscript claim summary**
本项目的中心立论与贡献陈述可归纳为八条。其一，数字员工由持久身份、可装配能力、可治理红线、可沉淀知识四要素联合判定，缺一即降级（SPEC.md 2.1）。其二，五层参考架构（人格、能力、知识、运行时、治理）是职责划分层面的贡献（SPEC.md 第 3 章）。其三，L1–L5 成熟度是"能力 × 治理 × 评测"的联合门槛而非能力单维刻度（SPEC.md 第 4 章）。其四，可移植性三件套加语义化版本加继承协议加受管块，使员工配置可打包、可分发、可继承（SPEC.md 第 5 章）。其五，安全与信任标准含红线分层、最小权限、破坏性操作人审、停—引—问注入防护、审计留痕、错误枚举化（SPEC.md 第 6 章）。其六，评测标准含任务基准、行为探针、回归集、人工量表、防博弈设计（SPEC.md 第 7 章）。其七，生态位声明为与 ACP、MCP 互补而不竞争，不管运行时、不管通信协议、不做编排框架（SPEC.md 1.2，README 生态位表）。其八，原创性定位句为"别人定义 agent 怎么跑，我们定义数字员工凭什么算合格上岗"（README.md 12 行）。

**Visible evidence base**
材料包内证据为上述五文件的原文，claim pointer 精确到文件与行号。材料包外已核验的公开证据包括 A2A 官方规范与 Linux Foundation 治理沿革、MCP 捐赠至 Agentic AI Foundation 的公告、AGENTS.md 开放标准及其 Linux Foundation 托管事实、OWASP LLM Top 10 与 Agentic Top 10 2026、MITRE ATLAS、IEEE P3777 立项页、ISO/IEC 22989 与 42001 页面、InjecAgent（ACL 2024 Findings）、AgentHarm、FATH 与信息流控制两类注入防御、Sharma et al. 抗谄媚论文（ICLR 2024）、LoCoMo、LongMemEval、PersonaMem 记忆基准、Letta 更名史、bytefolk/digital-employee 与 OpenBMB/StaffDeck 仓库、多个业界五级 agentic 成熟度模型、三个前沿安全框架（RSP、Preparedness、FSF）的 crosswalk。材料包引用的 CausalArmor（arXiv 2602.07918）与 Anthropic Persona Selection Model 经核验真实存在，引用诚信整体良好。

**Missing materials affecting confidence**
implementations/case-study/MAPPING.md、probes/suites/ 各级子集、sips/、GOVERNANCE.md、CONTRIBUTING.md 未在指定材料包内，我仅通过目录检索看到 MAPPING.md 片段，无法验证合规声明的落地机制与 L5 探针子集的实际存在性。对 bytefolk 与 StaffDeck 的判断基于其公开仓库当前状态（检索日期 2026-09-17），未运行其代码。这些缺口不影响对原创性主线的判断，但影响对可移植性主张实证强度的评分。

## Overall assessment

这是一份组织良好、自我标注诚实（业界、学术、观点、实践四类来源随文标注）的工程标准草案，其价值在于把"员工型 AI"的判定、成熟度与合规声明做成可执行条款。就原创性而言，四要素与五层架构是已在正文中诚实标注为综合判断的重新组织，联合门槛与继承约束推导是全稿最有价值的部分，但相关工作覆盖对一份以定义权威自居的规范来说明显不全。A2A 完全缺席、MCP 被引用却无参考条目、AGENTS.md 开放标准未被引用、最近的同类可移植数字员工项目 bytefolk/digital-employee 被错误归类为"单个产品"、五级成熟度与能力阈值联动治理均有大量在先工作未区分。这些单项都不致命，合起来却使当前的贡献陈述超出证据。修订后该规范可以 credible 地占据其宣称的生态位。

## Who would be interested and why

agent 平台与 harness 的工程团队会关心三件套与继承协议的可移植性条款。企业 AI 治理与采购方会关心 L1–L5 持证语义与合规声明格式，这是材料中最具直接商用价值的部分。RPA 厂商的产品团队（材料已覆盖其叙事）可把它当作从规则机器人转向认知代理的资质框架。追踪 MCP、A2A、AGENTS.md、IEEE P3777 生态的标准化从业者会关心本规范与这些在途标准的对接。组织管理与 AI 责任归属的研究者会对附录 B 的开放问题（记忆遗忘判据、多智能体责任、人格健康度）感兴趣。

## Major strengths

其一，证据类型随文标注（whitepaper.md 9 行）并承诺完整 URL 见文末，这种契约在开源标准草案中少见，且经我抽查，两条最新的学术引用（CausalArmor、Persona Selection Model）均真实存在。其二，人格与纪律分离原则从继承约束推出两条硬性推论（SPEC.md 81 行），是从真实生态机制反推标准的论证范本，即使其普适性依赖单一生态，论证结构本身值得保留。其三，联合门槛思想把治理与评测升档绑定到自主性升档，并下沉为可执行的晋级与回归规则（SPEC.md 113 行、147 行），这是全稿最有标准价值的机制设计。其四，行为探针一票否决加任务探针允许一题抖动的记分规则（probes.md 102–108 行）简单、可运行、可审计。其五，附录 B 公开承认四个无共识问题，避免把开放问题包装成已解决贡献。其六，明确的不管清单（SPEC.md 40–43 行）体现了标准卫生意识。

## Major Concerns

**R2-M1 A2A 缺席使互补性定位不完整**
- Concern ID: R2-M1
- Severity: Major
- Blocking: No
- Axis: originality
- Claim pointer: SPEC.md 第 1.2 节"本规范与 ACP、MCP 互补而不竞争"（SPEC.md 10 行与 43 行），README 生态位表 48–59 行，SPEC.md 第 4.5 节 L5"多智能体协作、能力市场化分发、协作消息级安全检查"。
- Evidence pointer: A2A 官方规范 <https://a2aproject.github.io/A2A/v0.2.5/>；LF AI & Data 关于 ACP 并入 A2A 的公告 <https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/>；A2A v1.0 于 2026 年 3 月在 Linux Foundation 治理下发布 <https://rywalker.com/research/google-a2a>；均检索于 2026-09-17。
- Concern: 材料包全文无任何 A2A 或 Agent2Agent 字样，我已对 numployee 目录做全文检索确认。A2A 是已中立治理的 agent 互操作开放标准，其 Agent Card 正是"可装配能力"的声明式清单，其任务委派机制正是 L5 多智能体协作的通信层。规范一面声明不管通信协议，一面在 L5 要求能力市场化分发与协作消息级安全检查，却不与 A2A 的能力声明做任何区分。
- Why it matters: 生态位表是本项目原创性论证的核心载体，逐行划界是其可信度的来源。漏掉 A2A 使"互补而不竞争"的清单不完整，读者无法判断 numployee 的 L5 与 A2A 的 Agent Card 是互补、重叠还是竞争，直接削弱定位句的排他性。
- Resolution test: 在 SPEC 1.2 与 README 生态位表各加一行 A2A，说明 Agent Card 能力声明与本规范能力层的关系，并给出 L5 分发与 A2A 互操作的条款或显式排除理由。若不打算互操作，须在 L5 治理要求中写明替代机制。

**R2-M2 MCP 被引用但无参考条目，AGENTS.md 开放标准未被引用**
- Concern ID: R2-M2
- Severity: Major
- Blocking: No
- Axis: originality
- Claim pointer: SPEC.md 87 行"【业界】MCP 将工具接入标准化"，SPEC.md 10 行与 43 行对 MCP 的定位，whitepaper.md 9 行的证据契约"每类论断均随文标注，完整 URL 见文末"，SPEC.md 第 5 章可移植性三件套与 whitepaper.md 133 行。
- Evidence pointer: MCP 进入 Linux Foundation Agentic AI Foundation 的官方公告 <https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/>；AGENTS.md 由 OpenAI Codex、Sourcegraph、Gemini、Factory 等共同维护并自 2025 年 12 月起由 Linux Foundation Agentic AI Foundation 托管 <https://factory.com/news/agents-md> 与 <https://codexinsider.com/agents-md/>；均检索于 2026-09-17。
- Concern: 规范两处把 MCP 作为带标注的业界论断引用，但 31 条参考来源中没有 MCP 的任何条目，违反白皮书自己设定的证据契约。更实质的问题是，AGENTS.md 已是跨工具开放标准（九个以上工具原生支持），本规范把 AGENTS.md 直接定为纪律层并纳入可移植性三件套，参考来源却只有 OpenClaw 一家的默认文件说明（第 19 条）。
- Why it matters: 一份以开放标准自居的规范，其三层文件中最通用的那一层已被中立机构标准化。不引用也不区分，"可移植性三件套"的贡献陈述会被读成对单一厂商文件约定的重新包装。
- Resolution test: 附录 C 增补 MCP 与 AGENTS.md 标准两条一手来源，SPEC 第 5 章增加与 AGENTS.md 标准的关系说明（兼容、扩展还是分叉），并给出三件套在非 OpenClaw harness 上的映射表。

**R2-M3 与 bytefolk/digital-employee 及 StaffDeck 的定位差异论述不成立**
- Concern ID: R2-M3
- Severity: Major
- Blocking: No
- Axis: originality
- Claim pointer: README.md 57 行"数字员工产品（StaffDeck、bytefolk/digital-employee 等 1630+ 实现）…单个产品/工作区：自家引擎、自家员工"，README.md 12 行原创性定位句，SPEC.md 第 5 章可移植性标准。
- Evidence pointer: bytefolk/digital-employee 仓库及其自述 <https://github.com/bytefolk/digital-employee>，公开定位为 portable versioned employee packages、package contracts、Agent Host adapters，并提供 validate 与 eval 命令，其定位句为 Agent frameworks answer how work gets done, Digital Employee answers who to ask and who is responsible；StaffDeck 仓库 <https://github.com/OpenBMB/StaffDeck>；均检索于 2026-09-17。
- Concern: README 把 bytefolk/digital-employee 归类为单个产品、自家引擎、自家员工，与该项目公开自述直接矛盾。bytefolk 做的正是可移植、可版本化、跨 Agent Host 的员工包加契约加评测命令，与 numployee 的可移植性三件套和探针考核处于同一生态位，其定位句与本项目 README 一句话定位几乎同构。SPEC 与白皮书对该项目零引用零区分，同一行的"1630+ 实现"数字在材料包内无任何出处。
- Why it matters: 这是原创性简报的核心检验点。若最近的同类在先项目已在做跨宿主可移植数字员工包而未被区分，可移植性贡献就有 rebranding 之嫌，生态位表的可信度连带受损，采购方按此表做决策会被误导。
- Resolution test: 作者提供 numployee 与 bytefolk 包契约的逐项对照（人格、纪律、事实文件对其 package contract，L1–L5 对其 eval 与 validate），写清 numployee 新增了什么、放弃了什么，并给"1630+"一个可核验的统计口径或删除该数字。

**R2-M4 五级成熟度阶梯与能力阈值联动的在先工作未引用未区分**
- Concern ID: R2-M4
- Severity: Major
- Blocking: No
- Axis: originality
- Claim pointer: SPEC.md 113–123 行（联合门槛表述与 L1–L5 表及分层依据），whitepaper.md 115–125 行。
- Evidence pointer: sema4 的五级 agentic 自动化 <https://sema4.ai/blog/the-five-levels-of-agentic-automation/>；Strata 的五级 agentic 身份成熟度 <https://www.strata.io/blog/agentic-identity/5-levels-agentic-identity-maturity/>；agno 的五级 agentic 软件 <https://www.agno.com/blog/the-5-levels-of-agentic-software-a-progressive-framework-for-building-reliable-ai-agents>；Anthropic RSP（2023 年 9 月）、OpenAI Preparedness Framework（2023 年 12 月）、Google DeepMind FSF（2024 年 5 月）三框架的 crosswalk <https://standardsbody.ai/library/research-note/frontier-framework-crosswalk/>；均检索于 2026-09-17。
- Concern: 五级 agentic 成熟度模型在业界已大量存在，其分级原型可追溯到 CMMI 五级与自动驾驶 SAE 分级。能力升级必须伴随治理升档的思想，与前沿安全框架的能力阈值触发更强缓释是同一模式，差别在于 numployee 面向部署层级与员工资质而非模型风险层级。这些在先工作均未引用也未区分。白皮书把联合门槛标注为观点，但 SPEC 直接将其规范化为晋级规则，读者无法判断这是新机制还是既有模式的移植。
- Why it matters: L1–L5 是规范最常用的对外接口，README 自测表、合规声明、探针子集全部建立其上。不锚定在先工作，联合门槛的贡献陈述会被认为夸大。引用并明确区分（部署级对模型级、员工资质对系统风险、组织采纳对前沿安全）反而能强化其正当性。
- Resolution test: 在白皮书第 5 章或 SPEC 第 4 章补相关工作小节，至少覆盖 CMMI 与 SAE 的分级传统、两个以上业界五级模型、三个前沿安全框架，并逐条写明 numployee 的差异点。

**R2-M5 注入防护与行为探针的安全类在先工作覆盖不足**
- Concern ID: R2-M5
- Severity: Major
- Blocking: No
- Axis: originality
- Claim pointer: SPEC.md 171 行"停—引—问"三步，whitepaper.md 144 行"停—问—执行"，probes.md 12–45 行 P1 至 P5，SPEC.md 第 6 章安全与信任标准。
- Evidence pointer: InjecAgent（ACL 2024 Findings，工具集成代理间接注入基准）<https://aclanthology.org/2024.findings-acl.624/>；AgentHarm <https://arxiv.org/abs/2410.09024>；FATH 认证式测试时防御 <https://arxiv.org/pdf/2410.21492>；信息流控制视角的间接注入系统级防御 <https://arxiv.org/pdf/2409.19091>；OWASP LLM Top 10（LLM01 Prompt Injection、LLM06 Excessive Agency）与 Agentic Top 10 2026（ASI01 Agent Goal Hijack 等）及 MITRE ATLAS 的对照 <https://agentstateattack.com/blog/owasp-agentic-mitre-atlas-crosswalk>；抗谄媚研究 Sharma et al.（ICLR 2024）<https://openreview.net/forum?id=tvhaxkMKAn>；均检索于 2026-09-17。
- Concern: 停—引—问对应已发表的认证式防御与数据指令分离思想，P1 探针对应 InjecAgent 类基准则，P4 抗谄媚对应 Sharma et al. 已系统量化的谄媚现象，但 31 条参考中只有 AgentDojo、CausalArmor、OpenAI 治理文件三条安全类来源，工业侧事实标准 OWASP 与 MITRE ATLAS 完全缺席。安全章是规范的信任基础，其行文读起来像首次提出这些机制。
- Why it matters: 可治理红线是四要素之一，安全章的完整引用是红线可信度的前提。安全团队的评审人与采购方会首先检查这一章对攻防研究谱系的掌握，漏引会连带损害规范其余部分的可信度。
- Resolution test: 附录 C 增补 InjecAgent、AgentHarm、Greshake et al. 的间接注入奠基工作、OWASP LLM Top 10、OWASP Agentic Top 10、MITRE ATLAS 各一条，并在 SPEC 6.4 与白皮书对应节说明停—引—问与认证式防御、数据与指令分离原则的关系。

**R2-M6 治理与评测章节未对接正式标准化机构**
- Concern ID: R2-M6
- Severity: Major
- Blocking: No
- Axis: scientific importance
- Claim pointer: SPEC.md 第 2 章术语与定义，第 7 章评测标准，第 8 章合规声明，conformance-checklist.md 全文。
- Evidence pointer: ISO/IEC 22989 人工智能概念与术语 <https://www.iso.org/standard/74296.html>；ISO/IEC 42001 说明 <https://www.snowflake.com/en/artificial-intelligence/ai-governance/iso-42001/>；IEEE P3777《AI 代理基准与性能度量标准》立项页（PAR 2025 年 12 月 10 日获批）<https://standards.ieee.org/ieee/3777/12350>；IEEE-USA 就 Agentic AI 致 NIST 的立场文件 <https://ieeeusa.org/assets/public-policy/policy-log/2026/IEEE-USA-NIST-RFI-Agentic-AI-030926.pdf>；均检索于 2026-09-17。
- Concern: 规范自定术语体系并设合规声明机制，但不与 ISO/IEC 22989 的术语、ISO/IEC 42001 的管理体系要求做任何映射。评测标准一章与正在制定的 IEEE P3777 完全无对接。IEEE 与 ISO 均已有智能体相关标准化动向，材料包内零提及。
- Why it matters: 持证、考核与互认是 README 的对外承诺，不与正式标准对接，互认只能停留在社区自评层面。对重要性而言，这也意味着评测一章的贡献边界不清，易被在途标准反超或重复。
- Resolution test: 增加"与正式标准的关系"小节，给出术语对照表（至少覆盖 22989）与评测维度对照（至少覆盖 P3777），并声明合规声明是否承认 ISO/IEC 42001 审计结果作为证据。

## Minor Comments

**R2-m1 三文档对同一防护机制命名不一致**
- Concern ID: R2-m1
- Severity: Minor
- Axis: technical soundness
- Affected element: SPEC.md 171 行"停—引—问"，whitepaper.md 144 行"停—问—执行"，probes.md 12 行 P1"停-引-问"
- Evidence pointer: 上述三处原文
- Issue: 同一三步防御在规范正文、白皮书、探针集中使用两套命名，第二步与第三步的语序也不同
- Required correction: 统一为一套三步名称并同步三个文档，探针 P1 的通过判定措辞随之对齐

**R2-m2 SPEC 与白皮书条款漂移**
- Concern ID: R2-m2
- Severity: Minor
- Axis: technical soundness
- Affected element: SPEC.md 155–164 行（六条，含受管块），whitepaper.md 129–137 行（五条，无受管块）
- Evidence pointer: 上述两处原文
- Issue: 受管块作为可移植性第六条只出现在 SPEC，白皮书缺位，两份文件对同一标准的条款数不一致
- Required correction: 同步两份文件，或显式声明白皮书不覆盖受管块及其理由

**R2-m3 "1630+ 实现"无出处**
- Concern ID: R2-m3
- Severity: Minor
- Axis: technical soundness
- Affected element: README.md 57 行
- Evidence pointer: 该数字在材料包内仅出现一次，无任何来源标注
- Issue: 生态位表使用不可核验的数量级表述
- Required correction: 给出统计口径与来源（如某平台实现计数），或改为定性表述

**R2-m4 部分参考来源为二手且与正文论断不匹配**
- Concern ID: R2-m4
- Severity: Minor
- Axis: technical soundness
- Affected element: whitepaper.md 211 行（ref 20，Spinach 博客支撑 GPTs 三段式），214 行（ref 23，SaaSCity 博客作为 Devin 产品化的唯一引用，其标题谈 SWE-2 定价计划，正文未使用该信息），212 行（ref 22，以仓库链接支撑 whitepaper.md 36 行"SWE-agent 在 SWE-bench 上长期保持开源最优"这一时效敏感强论断）
- Evidence pointer: whitepaper.md 36 行与参考来源 20、22、23 条
- Issue: 关键产品论断依赖营销类二手博客或无法支撑强论断的链接
- Required correction: 换成一手来源（OpenAI 官方文档、Cognition 官方发布、SWE-bench 排行榜快照日期），或弱化措辞

**R2-m5 记忆与人格一致性的评测在先基准未引**
- Concern ID: R2-m5
- Severity: Minor
- Axis: originality
- Affected element: SPEC.md 147 行 L4"跨会话一致性测试"，SPEC.md 92–95 行知识层
- Evidence pointer: LongMemEval（副标题即 Toward Experienced Colleagues）<https://xiaowu0162.github.io/longmemeval-v2/>；LoCoMo 与 PersonaMem 作为长期记忆基准被广泛使用 <https://arxiv.org/html/2512.06688v1>；Letta 更名史 <https://docs.letta.com/guides/legacy/naming_history>；均检索于 2026-09-17
- Issue: 跨会话一致性与长期记忆已有公开基准与工程实现，规范未引用也未说明行为探针与记忆基准的分工
- Required correction: 在评测标准处补引并写明分工（探针守红线与人格，记忆基准守事实保持），知识层补 Letta 等工程现状一句定位

**R2-m6 背景章节的产品线覆盖不完整**
- Concern ID: R2-m6
- Severity: Minor
- Axis: interdisciplinary readership
- Affected element: whitepaper.md 34–40 行 2.2 节两条演进线
- Evidence pointer: 材料包内 2.2 节只覆盖编码代理与 RPA 两条线；以 digital employee 自居的对话式 SaaS 产品类别（AI workforce 类）未出现也未声明排除
- Issue: 员工型 AI 叙事的产品化主战场未被覆盖，组织读者可能质疑背景的代表性
- Required correction: 补一段定位或显式声明本规范范围不含托管对话式产品员工

**R2-m7 摘要贡献表述与正文标注存在张力**
- Concern ID: R2-m7
- Severity: Minor
- Axis: originality
- Affected element: whitepaper.md 15–22 行摘要"给出四样东西"与 58、115 行的【观点】标注
- Evidence pointer: 摘要未区分综合定义与机制创新
- Issue: 摘要的呈现方式暗示四要素与五层是白皮书产出，正文却标注为作者综合判断，两处口径不一致
- Required correction: 摘要加一句限定，说明哪些是综合既有实践的定义工作，哪些是本文的机制贡献（联合门槛、继承约束推导、探针一票否决）

## Technical failings to address

一是三文档对注入防护的命名漂移（停—引—问与停—问—执行并存），规范类文档的术语单一性必须保证。二是 SPEC 与白皮书条款数不一致（受管块缺位）。三是 MCP 论断无参考条目，违反白皮书自设的证据契约，这属于可机械核验的硬伤。四是"1630+ 实现"与"SWE-agent 长期保持开源最优"两处不可核验或时效敏感的强论断。五是 README 90 秒自测表（README.md 18–26 行）承诺每个等级有对应探针子集（含 L5），但 probes.md 只定义到 L4 的 12 题，L5 子集仅在 checklist 中以基础集加证据要求的形式存在（conformance-checklist.md 50 行），对外承诺与探针集现状不符。六是 README 声称记分规则透明、可自动化判定（README.md 34 行），但 probes.md 的通过判定均为自然语言描述（如 P4 必须先明确记录反对意见），未给出机器可执行的判定接口或示例实现，自动化判定主张目前无条款支撑。

## Assessment against axes

**originality**：中等偏弱。四要素与五层是诚实标注的合成，联合门槛与继承约束推导有真实增量，但可移植性三件套与 AGENTS.md 标准、A2A Agent Card、bytefolk 包契约的重叠未区分，当前贡献陈述超出证据。完成 R2-M1 至 R2-M5 后可提升至中等偏强。

**scientific importance**：中等。对企业采购与跨 harness 互认有实际价值，联合门槛模式有推广潜力；但单参考实现阶段限制了其作为标准的实证基础，且与 IEEE P3777、ISO/IEC 42001 无对接（R2-M6）压低了重要性上限。

**interdisciplinary readership**：中等。员工比喻与分层讲解对非工程读者友好，治理与采购读者可直接使用 L1–L5 与合规声明；但人格三件套中 OpenClaw 专有名词密度高，治理章未与 NIST、ISO 话语体系连接，跨学科可达性受限。

**technical soundness**：中等。条款结构清晰、判定逻辑可执行，但存在命名漂移、条款漂移、不可核验数字与二手来源等可机械核验的缺陷（见 Technical failings）。

**readability for nonspecialists**：较强。90 秒自测表、写字楼比喻、开放问题附录对非专业读者友好，是材料包的突出优点。

## Recommendation posture

要求重大修订（major revision），在 R2-M1 至 R2-M6 解决前不建议将 rc1 升为正式 v1.0。本项目值得继续投入，定位句所指向的生态位真实存在且无人完整占据，联合门槛、继承约束推导与探针一票否决是可辩护的贡献。修订优先级建议为先做 R2-M3 与 R2-M2（直接影响贡献陈述的真实性），再做 R2-M1 与 R2-M4（定位与成熟度锚点），R2-M5 与 R2-M6 可并入附录 C 扩充一并完成。同时建议把 README 路线图中 M1 的第二个 harness 验证与本次修订同步进行，用实证对照支撑可移植性主张，这比文字修订更能回应 rebranding 质疑。若作者完成上述修订，本评审人倾向于支持 v1.0 发布，并在后续 SIP 流程中关注与 A2A、AGENTS.md 标准的互操作条款。