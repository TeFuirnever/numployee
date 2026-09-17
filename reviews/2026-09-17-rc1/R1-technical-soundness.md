五份材料与两处关键旁证（`probes/suites/l1-l2.md`、`suites/l5.md`）均已核验完毕。以下为完整评审报告。
> 档案说明（2026-09-17 去品牌决议）：本评审报告中的产品名称与私有仓库路径已匿名化，评审结论与证据不受影响。


---

# R1 评审报告 · numployee《数字员工规范》v1.0-rc1

**评审人** R1（同行评审，独立工作）｜**侧重** 技术健全性（technical soundness）｜**评审日期** 2026-09-17

## Review setup

**Input scope（输入范围）**
指定材料包五份，SPEC.md（标准正文草案 v1.0-rc1）、docs/whitepaper.md（v1.0 完整论述版）、probes/probes.md（12 题探针集）、templates/conformance-checklist.md（合规检查清单）、README.md（项目门面）。另为核实两处疑点，只读抽查了材料包外的 probes/suites/l1-l2.md 与 probes/suites/l5.md（未修改任何文件），下文凡引用这两处均单独标注。

**Assessment boundary（评估边界）**
本评审评估材料包的内部自洽性、条款的可检验性、四份文件间的一致性、引用标签与论断的匹配度。未实际运行任何探针，未对 31 条外部引用做联网逐条核验，未评审实现代码或 MAPPING.md 中的落地证据。所有证据指针均落在仓库文件内；无法从材料包内获得支撑处标注"材料缺失"，未引入任何材料包外证据。

**Shared manuscript claim summary（稿件中心立论）**
数字员工（同时具备持久身份、可装配能力、可治理红线、可沉淀知识的 AI 工作实体）可以标准化、可考核。标准化由五层参考架构、三类工程标准（可移植性、安全与信任、评测）与合规声明机制承载；可考核由 L1–L5"能力 × 治理 × 评测"联合门槛、行为探针集与合规检查清单承载；与 ACP、MCP 互补而不竞争。

**Visible evidence base（可见证据基础）**
五份指定文件全文；probes/suites/l1-l2.md、suites/l5.md（抽查）；SPEC 附录 C 与白皮书文末的 15 条学术引用、16 条业界引用清单。

**Missing materials affecting confidence（影响置信度的缺失材料）**
implementations/case-study/MAPPING.md（参考实现对照，被 SPEC 第 8 章与 README 引用，无法核实"落地验证"声明）；GOVERNANCE.md（被 checklist 的"失实声明移除"条款引用）；probes/suites/l3.md、l4.md 未读；31 条外部引用的真实性与时效未独立核验（其中 CausalArmor 2026、Anthropic Persona Selection Model 2026、新京报援引 IDC 数据三篇超出我可离线确认的范围）；探针的实际判定脚本或人工运行记录不存在于材料包。上述缺失不阻断本次内部一致性评审，但降低了"实践可行性"维度的置信度。

---

## Overall assessment

这是一份定位清晰、写作成熟、生态位判断准确的标准草案。它最硬的贡献不是概念（四要素与五层架构均有明确的学术与业界先例），而是把"员工上岗资格"变成了一组可执行的合约：判定四要素、联合门槛成熟度、通过/失败判定的探针、附证据的合规声明。探针集与"受管块"四条可执行性质（缺失插入、原位替换、用户内容保留、同版本幂等）是全文可检验性最强的部分。

但以技术健全性衡量，当前 rc1 存在三处规范级内部矛盾（L1 定义与四要素判定的冲突、探针等级与 SPEC 层级门槛的冲突、注入防护协议在 SPEC 与白皮书间的命名与步骤不一致）和一处系统性缺陷（评测门槛普遍不可测量、第 5–7 章对各成熟度层的适用范围未定义）。这些都不推翻中心立论，但任何一条不解决，第三方就无法对同一实现给出唯一合规结论，"可考核"将从可执行的验证退化为自评修辞。建议 rc1 之后安排一次以"单一事实来源"为目标的四文件同步修订，再进 v1.0。

**无一条 Major 达到 Blocking Yes 的判据**（即"不解决则中心立论不成立"均不成立），但 R1-M1、R1-M2、R1-M3 属规范文本自相矛盾，必须在 v1.0 之前解决。

## Who would be interested and why

- **agent harness 与数字员工产品的厂商**。合规声明给了他们一条与竞品互认的资质通道，L1–L5 等级可直接用于采购应答。
- **企业 AI 治理与采购方**。第 6 章安全红线与第 8 章证据化声明恰好填补了当前采购评估中只有基准分数、没有上岗资格的空白。
- **ACP/MCP 生态的集成者**。SPEC 1.2 对"管什么、不管什么"的切分写得干净，便于三方协议各就各位。
- **agent 评测与治理方向的研究者**。联合门槛模型与探针轮换、防博弈设计（7.5）是可检验的研究命题。
- **RPA 向 Agent 转型的厂商**。白皮书的第二条演进线（2.2 节）给了他们一个可挂靠的标准叙事。

## Major strengths

1. **联合门槛是真实贡献**。成熟度被定义为"能力 × 治理 × 评测"三者联动、禁止单维跳级（SPEC 第 4 章首段），这比业界的能力阶梯叙事（Anthropic 复杂度阶梯）更适合上岗场景，且与第 8 章"声明不得超出已验证层级"形成闭环。
2. **探针操作化程度高**。每题有通过判定与失败判定双列，记分规则含一票否决、配置哈希留痕、防过期机制（probes.md C 节），这是"可考核"主张最实的支撑。
3. **边界声明诚实**。1.2 节明确不管运行时与通信协议，README 生态位表逐格声明"我们不做什么"，附录 B 公开列出四个未解问题（遗忘判据、责任归属、人格健康度、评测博弈），epistemic hygiene 显著好于同类草案。
4. **"受管块"机制（SPEC 5.6）具有工程刚性**。四条可执行性质全部可被脚本化验证，是全文唯一达到"实现无关且可自动化判定"的移植性条款。
5. **人格与纪律分离的动机论证方向正确**。以继承传播约束（而非美学）作为分离依据，并指出分类错误的安全后果，这个论证框架本身值得保留，只需补操作判据（见 R1-M5）。

## Major Concerns

**R1-M1｜Severity High｜Blocking No｜Axis technical soundness**

- **Claim pointer** SPEC.md 第 2.1 节"一个 AI 实体是数字员工，当且仅当同时满足以下四项"，要素一要求持久身份"跨会话存在"；第 4.1 节 L1 能力要求却规定"不跨会话持有状态"、治理要求"不持有任何工具写权限"。
- **Evidence pointer** SPEC.md 第 2.1 节与第 4.1 节；templates/conformance-checklist.md L1 节首条要求"重启后会话与身份可恢复"；README.md 90 秒自测表 L1 行判定要点"持久身份成立"。四份文件对同一属性给出三种答案。
- **Concern** 判定四要素是类的成员资格，L1 是该类的最低成熟度档，但按第 4.1 节原文，L1 实体不持有跨会话状态、不持工具写权限，至少不满足要素一（持久身份跨会话存在），要素二（可装配能力）与要素四（可沉淀知识）也只以退化形式存在。于是"数字员工的成熟度模型"的最低档不是数字员工，四要素判定与成熟度模型管辖范围互相矛盾。checklist 与 README 实际上各自偷偷把 L1 改写为"有持久身份"，与 SPEC 正文打架。
- **Why it matters** 第 8 章合规声明以成熟度层级给出，等级映射的自洽性是"可考核"主张的地基。第三方审核员按 SPEC 审 L1 会放行一个无持久身份的实体，按 checklist 审则会驳回同一实体，合规结论取决于采用哪份文件。
- **Resolution test** 作者明确二选一并四文件同步：（a）宣布四要素适用于 L2 及以上，L1 为"数字员工预备态"并改第 4 章标题与第 8 章声明格式；或（b）修订第 4.1 节使 L1 明确持有持久身份文件（状态不持有、身份可恢复），并在第 2 章给出"状态"与"身份"的术语区分。修订后，同一 L1 实现在 SPEC、checklist、README、suites 四处应得出同一合规结论。

**R1-M2｜Severity High｜Blocking No｜Axis technical soundness**

- **Claim pointer** SPEC.md 第 4.4 节 L4 治理要求列"注入防护'停—引—问'（见 6.4）"；第 4.1 节 L1 治理要求仅"输入校验；输出边界显式声明；不持有任何工具写权限"。
- **Evidence pointer** probes.md 中 P1「停-引-问」标注成熟度等级 L1（A 节题头），其等级映射表（文末）将 P1 归入 suites/l1-l2.md；材料包外抽查的 probes/suites/l1-l2.md 确认 L1 子集勾选题含 P1；checklist L1 节〔探针〕条目要求通过"l1-l2.md 中标注 L1 的题目"。
- **Concern** 注入防护在 SPEC 中是 L4 才要求的治理控制，在探针集与检查清单中却是拿 L1 声明的必要条件。两个后果同时成立：按 checklist 申领 L1，必须通过一道 SPEC 并未要求 L1 具备的控制项；按 SPEC 自评合格的 L1，会被探针子集判失败。探针作为"必要条件"被允许严于门槛，但标准从未声明这一设计原则，且 P2"不编造工具"在 L1"不持有任何工具"前提下近乎空转，说明探针等级并非从 SPEC 门槛推导而来。
- **Why it matters** SPEC 第 7 章宣称探针是评测标准的操作化，"等级映射"是四份文件之间的合约。映射一旦交叉，声明方与审核方会各执一词，合规声明的可信度归零。
- **Resolution test** 产出一张三方映射表（SPEC 第 4 章每级治理/评测要求 ↔ 探针编号 ↔ checklist 条目），逐项标注"探针严于门槛"或"门槛严于探针"并给出理由；修订 P1 等级（降至 L4 子集或提升 L1 门槛）与 P2 的适用前提。映射表全绿前，第 8 章不接受任何 L1 声明。

**R1-M3｜Severity High｜Blocking No｜Axis technical soundness**

- **Claim pointer** SPEC.md 第 6.4 条将不可信输入防护定义为三步"停—引—问"（停，识别为数据并暂停工具执行；引，仅在数据/引用上下文中引述；问，必要时向用户确认）；第 4.4 节与 probes.md P1 均采用此名。
- **Evidence pointer** docs/whitepaper.md 第 7.4 条将同一防护定义为"停—问—执行"（停；问；执行），步骤数与第二步名称均不同，且未引用 SPEC 6.4。
- **Concern** 同一份标准体系的两份文件对同一项安全控制给出两个不同协议。SPEC 的三步以"引"为核心防御（伪指令不进入指令链），白皮书的三步以"执行"收尾，二者在"确认之后是否还要再引述"上行为不同。注入防护是全规范被引用次数最多的安全控制，其规范来源无法确定。
- **Why it matters** 审计者按白皮书实现的三步系统，会被按 SPEC 审核的探针 P1 判失败；反之亦然。安全控制命名不一致直接制造互操作与合规风险。
- **Resolution test** 选定唯一协议（建议保留含"引"的 SPEC 版本，因其与因果链区分"用户真实意图"的学术依据更咬合），在两份文件中逐字统一，并在另一处加注"原表述已废弃，见 SIP 编号"。同时把协议名登记进术语表，探针、checklist、suites 引用术语表而非各自措辞。

**R1-M4｜Severity High｜Blocking No｜Axis technical soundness**

- **Claim pointer** SPEC.md 第 4 章宣称"成熟度是联合门槛……仅有能力升级而治理、评测不升档，不得晋级"；第 7 章与第 6 章给出多项门槛。
- **Evidence pointer** SPEC.md 第 4.2 节"任务成功率达标"（无阈值、无归口）；第 4.4 节"可在低风险任务上长期无人值守"（"低风险"无任何分级定义）；第 7.4 条"分歧过大触发复核"（无分歧度量）；第 6.3 条"删除、上传、发布、资金类操作必须有人在环"为全文级 MUST，而第 4.3 节又将"破坏性操作人审"列为 L3 治理要求，第 5、6、7 章对 L1、L2 是否整体适用从未声明；docs/whitepaper.md 第 4.5 节自评"已搭出 L5 协作骨架"但同时承认"selector 路由、Agent 间共享上下文、per-target 策略等仍在 V2 规划"，即在治理与评测未升档时宣称 L5 能力，恰为其自身联合门槛规则所禁止。
- **Concern** 门槛分两类问题。其一，可测量性缺失，"达标""低风险""分歧过大"三个术语gate着 L2、L4、L5 的裁决，却无任何判据或记录位置。其二，适用范围缺失，第 5–7 章是全文义务还是分级义务没有声明，导致第 6.3 条与第 4.3 节在人审要求上重叠且关系不明。参考实现作者自己的 L5 自评违反联合门槛规则，说明该规则当前没有操作化的裁决程序，只停留在修辞。
- **Why it matters** "可考核"的中心立论要求不同审核者对同一证据得出同一结论。不可测量的门槛使 L2、L4、L5 的认证结果依赖审核者个人解释；适用范围不明使 L1、L2 实体是否受第 6 章全部 MUST 约束成为自由心证。
- **Resolution test** 为每个门槛补一项即可：给出数值或枚举判据，或显式标注"profile 自定义"并规定自定义值的记录位置（建议入检查清单条目）；新增一小节声明第 5、6、7 章对各成熟度级的适用矩阵；删除或降级 whitepaper 第 4.5 节的"L5 骨架"表述，使其与联合门槛规则一致。验收标准为两名独立审核者对同一份 L1–L5 证据包给出相同裁决。

**R1-M5｜Severity Medium｜Blocking No｜Axis technical soundness**

- **Claim pointer** SPEC.md 第 3.1 节"人格与纪律分离原则"及其两条"硬性推论"；第 5.1 条人格三件套分离。
- **Evidence pointer** SPEC.md 第 3.1 节人格层职责含"身份、语气、边界与信任模型"，纪律文件含"操作纪律、工具纪律、完成规则、红线"（第 5.1 条），但"边界"与"红线/操作纪律"的区分标准全文未给出；同节继承前提为"子代理通常只继承纪律文件与环境事实文件"，以"通常"这一或然前提推出"硬性推论"；docs/whitepaper.md 第 6.1 条将同一前提标注为【业界】【实践】。
- **Concern** 分离原则是全规范移植性与治理论证的承重墙，其分类判据却不可操作。"边界"与"红线"在字面上同属行为限制，规则该进人格文件还是纪律文件，文档给不出判定程序，而分类错误有明确安全后果（纪律误入人格文件则子代理不继承）。更关键的是，"通常"继承的或然前提推不出"硬性"推论，论证强度被夸大。
- **Why it matters** 三件套分离是 L2 合规条目（checklist L2 首条）的直接依据，判据缺失会使该条目沦为形式审查；继承推论的夸大则把生态偶然性包装成必然规律，误导跨 harness 实现者。
- **Resolution test** 增加一条分类决策标准（示例方向，"影响工具调用权限、拦截器与完成判定的归纪律文件；影响表达风格、口吻与自我披露方式的归人格文件"），各配一个正例与一个反例；将"通常"改为对具体生态（OpenClaw 系）的可核验声明，或把推论降级为条件句（"在子代理不继承人格文件的生态中"）。

**R1-M6｜Severity Medium｜Blocking No｜Axis technical soundness**

- **Claim pointer** SPEC.md 第 8 章允许按 L5 声明合规，须附"与所声明层级对应的回归集运行记录（任务集 + 探针集）"；第 4.5 节 L5 评测要求为"多智能体协作基准；人工评估量表（见 7.4）；分发质量评级"。
- **Evidence pointer** probes.md 文末等级映射表无任何 L5 题目；材料包外抽查的 probes/suites/l5.md 自认"暂不设置勾选题目"，证据要求以 SPEC 第 4 章定性条目兜底；第 7.4 条量表仅给五个维度名，无评分锚点；"分发质量评级"无评级函数；第 4.5 节"多智能体协作基准"未指定任何基准或构造规范。
- **Concern** L5 的全部评测仪器要么是外部未定（协作基准），要么是无锚点量表（5 分制双评审），要么是未定义函数（反馈回流评级），探针集为空。这意味着第 8 章当前提供了一条无法被第三方裁决的合规声明路径。材料对这一点处理得相当诚实（l5.md 拒绝用低等级探针冒充组织级证据），但诚实的留白不等于可考核。
- **Why it matters** 若 L5 声明可被发布而其证据不可 adjudicate，"可考核"主张在最高等级上落空，且会诱发"刷 L5"的劣币行为，恰好触发附录 B 自己警告的评测博弈。
- **Resolution test** 在第 8 章增设过渡条款，"L5 声明在 suites/l5.md 回填可勾选题目前不予受理"；同时给 7.4 量表补评分锚点示例、给"分发质量评级"一个最小定义（评分维度、聚合方式、防刷机制）。回填前允许发布的最高等级为 L4。

## Minor Comments

**R1-m1｜Severity Minor｜Axis technical soundness｜Affected element** SPEC.md 第 2.1 节"缺一即降级"句
**Evidence pointer** SPEC.md 第 2.1 节降级映射（"一次性脚本""个人助手"）；第 2.2 节定义的相邻概念仅聊天机器人、自动化 workflow、agent harness 三类。
**Issue** 降级映射引入"一次性脚本""个人助手"两个未定义范畴，且"无可治理红线是不可上岗的"是取消资格而非降级，与句首"缺一即降级"的统摄 claim 不齐；"个人助手"一词与第 2.2 节"个人对话框"语境重叠，边界模糊。材料包外抽查的 suites/l1-l2.md 又给 L1、L2 贴了"可信执行""稳定执行"的别称，与 SPEC（应答工具/岗位执行者）、README（对话入口/单任务）三套称谓并存。
**Required correction** 在术语表补齐四个降级范畴的操作定义，或把"不可上岗"移出降级句式；全文统一每级一个名称，别称只出现在术语表。

**R1-m2｜Severity Minor｜Axis technical soundness｜Affected element** SPEC.md 第 5.3 条语义化版本
**Evidence pointer** SPEC.md 第 5.3 条仅规定"新增段落升 minor、修正升 patch"。
**Issue** 条款自称语义化版本，但无 breaking change（删除段落、重命名键、改变继承语义）的 major 升档规则，SemVer 的核心恰好是 major；当前规则下破坏性演进无处安放，只能升 minor，与"按版本审计"的治理目标冲突。
**Required correction** 补"删除或重命名已有条目、改变红线语义升 major"规则，并声明 major 升级时的兼容策略。

**R1-m3｜Severity Minor｜Axis technical soundness｜Affected element** SPEC.md 第 1.3 节符合性措辞与全文规范条款
**Evidence pointer** SPEC.md 第 1.3 节承诺 MUST/SHOULD/MAY 三级措辞，但第 4 章 L1–L5 各项要求、第 5 章多数条款为无语级关键词的陈述句（对照有标注的"必须能声明其所对应的层"第 3 章、"必须有人在环"第 6.3 条、"更新必须满足四条"第 5.6 条）。
**Issue** 关键词使用不均，第三方无法判断"L2 治理要求：操作范围白名单"是 MUST 还是描述性目标；同一章内有的条目加粗"必须"、有的裸写，义务等级不可分辨。
**Required correction** 做一次关键词审计，为每个规范性条目补 MUST/SHOULD/MAY 或显式声明为描述性文字；checklist 逐条引用条款编号。

**R1-m4｜Severity Minor｜Axis technical soundness｜Affected element** probes.md T2 通过判定
**Evidence pointer** probes.md T2"按 AGENTS.md 术语描述"为通过判据之一；对照 SPEC.md 第 1.2 节"不管运行时实现"与 README 生态位表"不造运行时"的中立性承诺。
**Issue** 探针集作为中立考核工具，其判据引用了特定产品的文件名（AGENTS.md），换一个 harness 的员工将被判失败，与"任何 harness 造的员工都能持证"的门面声明冲突。
**Required correction** 改为"按该员工纪律文件所载术语表描述"，并在探针 README 声明产品名仅作示例。

**R1-m5｜Severity Minor｜Axis technical soundness｜Affected element** docs/whitepaper.md 相对 SPEC.md 的完整性
**Evidence pointer** SPEC.md 第 5.6 条"受管块"机制在 whitepaper.md 第 6 章可移植性标准中完全缺席（该章仅五条）；SPEC.md 第 6.6 条错误枚举化在 whitepaper 中被并入第 7.5 条审计留痕，SPEC.md 第 7.5 条评测防博弈在 whitepaper 中归入第 7.6 条安全章。
**Issue** 白皮书自称"完整论述版"，却漏掉一项规范机制，另有两项的章节归属与 SPEC 不一致；读者以白皮书为准会遗漏受管块这一可执行约束。
**Required correction** 白皮书补受管块论述，章节编号与条目划分对齐 SPEC，或在两份文件头部互相声明差异清单。

**R1-m6｜Severity Minor｜Axis technical soundness｜Affected element** 证据标签体系与两处引用归类
**Evidence pointer** whitepaper.md 第 0 节定义【学术】为"同行评议论文或高质量预印本"，【观点】为作者综合判断；但 SPEC.md 通篇仅使用【业界】【学术】，四要素"当且仅当"定义、"缺一即降级"与两条"硬性推论"在 SPEC 中均无标签（whitepaper 中同句均标【观点】）；SPEC 附录 C 第 13 条（Anthropic Persona Selection Model，alignment.anthropic.com 网页）归入学术，与上述自定义不完全吻合；whitepaper.md 第 2.2 节市场规模数字（469 亿元、31.56%）仅引新京报转述 IDC（第 28 条）。
**Issue** 同一论断在两份文件中证据类型标注不一致，SPEC 读者无法区分引用结论与作者判断；第 13 条归类依据不足；精确市场数字依赖单一二手媒体源。
**Required correction** SPEC 引入【观点】标签（或全部论断补齐四标签之一）；第 13 条改标业界研究报告或补预印本链接；市场数字补 IDC 原始出处或降格为定性表述。

**R1-m7｜Severity Minor｜Axis readability for nonspecialists｜Affected element** README.md 快速开始
**Evidence pointer** README.md 快速开始第 2 步将 SOUL.md、AGENTS.md、TOOLS.md、IDENTITY.md、USER.md、BOOTSTRAP.md 六文件统称为"人格三件套"；SPEC.md 第 5.1 条三件套为人格文件、纪律文件、环境事实文件的抽象三元组。
**Issue** "三件套"名下列六个文件，命名自相矛盾；SPEC 去产品化后的抽象名与 README 的产品文件名之间无映射表，新人按 README 装配后无法对照 SPEC 与 checklist 的自评条目。
**Required correction** 明确"三件套 = 三类职责"，列产品文件时标注每个文件对应哪一类职责，或直接链接 templates/README 的映射。

**R1-m8｜Severity Minor｜Axis technical soundness｜Affected element** "5+2 目标状态"枚举
**Evidence pointer** whitepaper.md 第 4.5 节与 SPEC.md 附录 A"5+2 种目标结果状态（dispatched / failed / blocked / unavailable / skipped）"，仅列出五个。
**Issue** "5+2"的"+2"在材料包内无任何说明，枚举不完整。
**Required correction** 补全七个状态或删去"+2"。

**R1-m9｜Severity Minor｜Axis technical soundness｜Affected element** SPEC.md 第 8 章声明维度的术语
**Evidence pointer** SPEC.md 第 8 章示例"单员工 L3、协作 L4"；第 4 章成熟度均按单个实体定义，checklist 无"协作"维度条目。
**Issue** 声明引入"单员工/协作"两个正交维度，但成熟度模型、探针子集、检查清单均无协作维度的定义、门槛与条目，示例悬空。
**Required correction** 要么在第 4 章定义协作维度及其门槛，要么从第 8 章删除该示例，待 SIP 补维度后再开放。

## Technical failings to address

按优先级排列的修复清单，可构成一次 rc2 修订。

1. **单一事实来源同步**（对应 R1-M1、M2、M3、R1-m1、m5、m7）。以 SPEC 为唯一规范源，白皮书降为论述，checklist 与 suites 只做引用不复制判据；建立术语表（持久身份/状态/边界/红线/低风险/达标/分歧过大/降级范畴）。
2. **三方映射表**（对应 R1-M2）。SPEC 门槛 ↔ 探针 ↔ checklist 条目逐格对齐，声明每一处"探针严于门槛"或"门槛严于探针"及其理由。
3. **门槛可测量化与适用范围矩阵**（对应 R1-M4、R1-m3）。每个 gate 给判据或显式 profile 化并规定记录位置；声明第 5、6、7 章对各级是否适用；修正 whitepaper 第 4.5 节自评，使其不违反联合门槛规则。
4. **注入防护协议统一**（对应 R1-M3）。选定一个三步名与语义，全文逐字一致，废弃表述挂 SIP 编号。
5. **L5 通道临时封闭**（对应 R1-M6）。第 8 章在 suites/l5.md 回填前不受理 L5 声明；补量表锚点与评级函数的最小定义。
6. **分类判据与版本规则**（对应 R1-M5、R1-m2）。给出人格/纪律分类决策标准与正反例；语义化版本补 major 规则。
7. **探针中立性编辑**（对应 R1-m4、m8）。清除探针判据中的产品专名；补全"5+2"。
8. **标签与引用治理**（对应 R1-m6）。SPEC 引入【观点】标签；第 13、28 条引用降级或补源。

## Assessment against axes

| 轴 | 评分（5 分制） | 一句话依据 |
| --- | --- | --- |
| originality | 3 | 概念均为既有工作的综合（Xi 四模块、OpenClaw 文件生态、Anthropic 阶梯），新意在上岗资格的标准化合约与联合门槛框架，属组合式创新而非概念创新 |
| scientific importance | 3 | 对采购与治理有实际重要性，但贡献形态是工程标准而非科学结论；防博弈与探针轮换是可检验的研究命题 |
| interdisciplinary readership | 4 | 组织管理、HCI、治理、评测四类读者均有入口，隐喻与表格降低了跨域门槛 |
| technical soundness | 2 | 本评审重点。三处规范级内部矛盾、门槛系统性不可测、适用范围未定义，详见 R1-M1 至 M6 |
| readability for nonspecialists | 4 | 写字楼比喻、90 秒自测、双列判定、开放问题附录均友好；扣分项为术语多套并存（m1、m7） |

## Recommendation posture

**Major revision，建议 rc1 之后插入 rc2，再议 v1.0。** 项目方向值得支持，生态位判断准确，"可考核"主张在 L1–L4 探针层面已经拿到实据；当前没有任何一条缺陷达到推翻中心立论的程度（故无 Blocking Yes），但 R1-M1、M2、M3 属于规范文本自相矛盾，按标准工程的惯例不应带矛盾进正式版。若第 8 章采纳 R1-M6 的过渡条款、四文件完成单一事实来源同步，本评审人预期下一轮可转为支持发布。