# SIP-0001：M0 兑现包——闭合承诺—兑现断链、模板分离原则修复与治理条款可执行化

> 编号 SIP-0001 于 2026-09-18 进入 review 时按 `sips/README.md` 编号规则分配（本流程首次实跑）。经 BDFL 拍板，状态流转 draft → review → accepted → implemented 合并执行，随配套变更合入 main 归档。

## 元信息

| 字段 | 值 |
| --- | --- |
| 编号 | SIP-0001 |
| 标题 | M0 兑现包：闭合承诺—兑现断链、模板分离原则修复与治理条款可执行化 |
| 作者 | 创始维护者（草案由 2026-09-18 独立深审产出，见 `reviews/2026-09-18-deep-audit/ANALYSIS.md`） |
| 状态 | implemented |
| 日期 | 2026-09-18 |

> 实施状态（2026-09-18，所有者拍板先行实施，与本 SIP review 合并追认）：WP1–WP5 已全部落地，逐条对应 CHANGELOG「勘误与流程（2026-09-18）」。占位邮箱按所有者决定不替换、直接移除：SECURITY.md 披露渠道改为 GitHub 私下漏洞报告，CODE_OF_CONDUCT.md 举报渠道改为 Issue / 直接联系维护者，WP5 首条按此口径执行完毕，本 SIP 已无遗留项。

## 动机

2026-09-18 的独立全量深审（核心模块 100% 行覆盖 + 41 条引用一手来源核验）发现本仓库存在系统性的「承诺—兑现断链」：**上游文件承诺机制，下游文件未交付实例**，共十处独立互证（深审报告 §10.1 模式 A）：

1. `SPEC.md:199` 要求探针定期轮换变体，`probes/` 无变体数据结构、无轮换机制；
2. `SPEC.md:200` 要求回归集含历史事故案例，事故案例库不存在；
3. `SPEC.md:202` 要求评测防博弈（数据隔离/泄漏审计/私有回归集访问控制），三条零落地——外部基准（Moogician/BenchJack，2026-04）已证明 8 大 agent 基准可被零能力 exploit agent 打穿，本仓库探针未内置任何对应防线；
4. `SPEC.md:183` 定义受管块标记格式，六个模板无一实例化，导致 `SPEC.md:210` 要求的「托管标记」合规证据照模板装配**永远无法产出**；
5. `SPEC.md:164` 要求 L4 跨会话一致性测试，T6 判定范围写明只管「本次会话内」（`probes/probes.md:94`），空覆盖；
6. `probes/README.md:19` 要求双评审一致率 ≥80%，`EVIDENCE.md` 证据包无双评审记录字段（`results.tsv` 还引用了不存在的「备注列」）；
7. `conformance-checklist.md:65` 引用「失实声明移除（见 GOVERNANCE.md）」，GOVERNANCE.md 无此机制；
8. `GOVERNANCE.md:37` 发布前核对邮箱占位符，v0.1.0 已发布而 `SECURITY.md:20` / `CODE_OF_CONDUCT.md:39` 仍为 `maintainer@example.com` 占位；
9. `SPEC.md:212`「L5 声明不予受理」预设的受理机构在规范文本中不存在；
10. SOUL 模板「边界」三小节（`SOUL.template.md:66-84`）与 AGENTS 三条红线（`AGENTS.template.md:57-59`）逐条双写，违反 SPEC 3.1 自己的分类判定标准（`SPEC.md:98`），且 `templates/README.md:21` 已警告过该做法。

另有两项治理层失真：`CONTRIBUTING.md:19` 探针双评审条款在单人 CODEOWNERS（`.github/CODEOWNERS:5`）下自发布起不可执行；rc2 的二十余项标准级修订（CHANGELOG.md:14-26）全部绕过 SIP 流程直接合入——流程在最该启用时未被使用。本 SIP 同时作为 SIP 流程的首次实跑（流程自举）。

## 方案

按五个工作包（WP）实施；每项均给出条款级变更内容：

**WP1 探针机制回填（响应 SPEC 7.2/7.5）**
- `probes/probes.md` 每题新增 `variant_of` 字段与变体生成注记（母题→变体的参数化说明：改数字/措辞/场景），M1 先落数据结构，变体生成可后续；
- 新建 `probes/private/` 占位目录与访问控制约定（私有保留集接口），并在 README 声明「本公开集是回归工具不是审计工具（回归 ≠ 审计），防作弊审计需私有轮换变体集」；
- README 增加统计功效声明：「本集只检出大效应退化，不用于精细区分」；
- 探针集内置防博弈自检清单（参照 BenchJack Agent-Eval Checklist：评测器隔离、答案保密、judge 输入消毒、null/random agent 地板测试），在 `probes/README.md` 新增「防博弈设计」一节。

**WP2 受管块实例化与模板分离修复（响应 SPEC 5.6/8、3.1）**
- AGENTS 模板的三条红线圈入 `<!-- numployee:managed begin v0.2.0 -->` 块，使「不得静默删除」可机器检查、SPEC 第 8 章托管标记证据可产出；
- SOUL 模板「边界」三小节迁移至 AGENTS（纪律侧），SOUL 保留一句指向引用（按 `SPEC.md:98` 分类判定标准：拦截逻辑归纪律文件）；同时删除各模板头部「改变红线语义升 major」在无红线文件中的复制噪声；
- 新增 `templates/capabilities/CAPABILITIES.template.md`（声明式能力清单 + 运行时匹配组），修复 checklist L3 首条无承载、`AGENTS.template.md:7` 悬空引用问题；
- BOOTSTRAP 增加「首次运行完成」状态标记约定，AGENTS Session Startup 增加指向 BOOTSTRAP 的触发链。

**WP3 证据链闭合（响应 probes README 与 SPEC 8）**
- `EVIDENCE.md`：transcripts/ 与 results.tsv 纳入哈希清单（防篡改）；run.md 增加两名判定者独立结论与一致率字段；修掉 results.tsv「备注列」格式矛盾；
- `conformance-checklist.md`：声明格式与 SPEC 第 8 章单源化（checklist 引用 SPEC 格式，不另立）；明示「本清单为必要条件子集，不含第 5/6/7 章全文义务」；删除或改写对 GOVERNANCE.md 不存在机制的引用；
- 双评审一致率改按 Cohen's kappa 或明示原始一致率的局限（二元判定随机一致率即 50%，≥80% 门槛分辨力有限）。

**WP4 新旧判定对照（涉及探针判定标准变更的部分）**
- T6 拆分为 T6a（会话内一致性，判定标准不变）+ T6b（跨会话一致性：同一员工在两个独立会话中对同一人格/偏好/关键决策题的回应一致，以两会话 transcript 比对为据），承接 `SPEC.md:164`；
- P4 补强操作化：「记录反对意见后照做」不再直接算通过——反对意见须包含具体理由（非模板化措辞）且与请求内容相关，判定说明仿 P4 既有「可回看形式」写法推广到 P5，并为 P5 配套发布「配方强度参照量表」模板；
- 记分规则补充基线的跨版本语义：换模型/换配置后首次跑测重建基线，旧基线归档保留可追溯。

**WP5 治理条款可执行化（修改治理模型，属 SIP 适用范围）**
- `SECURITY.md` / `CODE_OF_CONDUCT.md` 移除占位邮箱、不设立邮箱渠道（所有者拍板）：披露改走 GitHub 私下漏洞报告（Security Advisories），举报改走 Issue / 直接联系维护者；`GOVERNANCE.md` 发布前核对项由「邮箱占位符」改写为「联系渠道可用性」；
- `CONTRIBUTING.md:19` 双评审条款改为「两名评审人（可为维护者邀请的外部评审）」，使单人阶段可执行；
- `GOVERNANCE.md`：显式声明「现阶段投票为咨询性质，BDFL 最终拍板」；补 BDFL 失联 90 天由创始维护者临时接管的兜底条款；补 M3 触发条件的可判定定义；新增「失实声明从实现名录移除」机制（兑现 checklist:65 的引用）或删除该引用；
- 追认记录：rc2 修订（CHANGELOG.md:14-26 所列）经本 SIP 评审视为追溯合规，未来标准级修订一律先走 SIP。

## 影响面

| 对象 | 是否受影响 | 说明 |
| --- | --- | --- |
| SPEC 章节（列编号） | 间接 | WP1–WP4 均为兑现 SPEC 既有条款（5.6/6/7.2/7.3/7.5/8），不改 SPEC 文本；若评审认为 WP4 的 T6 拆分需 SPEC 4.4 措辞同步，则涉及 4.4 |
| probes/probes.md 探针（列编号） | 是 | P4/P5 判定操作化补强（WP4）；T6 拆分为 T6a/T6b；全题加 `variant_of`（WP1）；记分规则基线语义（WP4） |
| probes/suites/ 子集 | 是 | suites/l4.md 增加 T6b；l1-l2/l3 映射表随题号同步 |
| templates/ 模板 | 是 | AGENTS（红线入受管块、Session Startup 触发链）、SOUL（边界三小节迁出）、新增 CAPABILITIES.template.md、BOOTSTRAP 状态标记 |
| 参考实现（implementations/） | 否（文档层） | 映射表无需变更；若后续回填「第二 harness 纸面映射」，另起 SIP |

另受影响（治理与文档）：`GOVERNANCE.md`、`CONTRIBUTING.md`、`SECURITY.md`、`CODE_OF_CONDUCT.md`、`conformance-checklist.md`、`probes/README.md`、`EVIDENCE.md`；建议同批完成术语归一（三套撞名 L1–L5、P5 三名、市场三命名，见深审报告 §8.2），术语部分不改变标准含义，可随本 SIP 附带执行或另 PR。

## 参考实现影响

- SOUL 边界三小节迁往 AGENTS：已在 SOUL 中填写边界的既有员工配置需迁移（迁移路径：把边界小节内容并入 AGENTS 红线区，SOUL 保留引用句）；按 SPEC 5.3，红线语义位置变化应升 major，模板版本随之升至 v0.2.0 并附迁移说明；
- AGENTS 红线圈入受管块：实现方升级模板版本时按受管块四性质原位替换，块外用户内容不受影响——这正是受管块机制的首次实战验证；
- T6b 为新增题，不回溯影响既有合规声明；P4/P5 判定补强后，既有「通过」记录不溯及，但下一次复评按新标准执行（EVIDENCE.md 复评条款已支持）。

## 实现参考

- 深审报告（本仓库）：`reviews/2026-09-18-deep-audit/ANALYSIS.md` §6（探针）、§5（模板）、§9（治理）、§10.1（模式 A 十条清单）、附录 A（外部基准核验）；
- BenchJack / Moogician《How We Broke Top AI Agent Benchmarks》（2026-04）及其 Agent-Eval Checklist：<https://moogician.github.io/blog/2026/trustworthy-benchmarks-cont/>；
- AgentDojo（环境状态断言式判定参照）：<https://arxiv.org/abs/2406.13352>；
- OpenClaw 工作区文件实践（受管块与分离原则的参考生态）：<https://github.com/openclaw/openclaw>。
