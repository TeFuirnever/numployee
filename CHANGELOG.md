# Changelog

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 与[语义化版本](https://semver.org/lang/zh-CN/)。版本号锚定 SPEC：major = 不兼容标准变更，minor = 新等级/新章节，patch = 措辞勘误。

## [Unreleased]

### 术语归一与白皮书回填（2026-09-18，SIP-0001 附带执行）

- 新增第二 harness 纸面映射 [implementations/claude-code/MAPPING.md](implementations/claude-code/MAPPING.md)（desk-check，官方文档一手来源）：SPEC 第 5 章六条逐条检验——2 条对应、3 条部分对应、受管块无原生对应（增量要求成立）；3.1 继承约束推论在第二生态独立证实（人格不传播、纪律传播），SPEC 第 5 章可证伪性落地
- SPEC 升 Draft v1.0-rc3：新增附录 D「术语与符号注册表」（登记性条款，不改规范性含义）——L1–L5 专指员工成熟度、用户段位改 U1–U5、多员工协作归位 L5、P5 归一「人格表达生效」、SOUL 七维、员工市场/SKILL 市场两渠道、Bastion 唯一名、ACP 消歧指针
- 各文档按注册表对齐：README 自测表 L4/L5 归位 SPEC 4.4/4.5；playbooks 用户段位全文改 U1–U5 并声明两套刻度勿混用；beginner 补 SOUL 第七维「边界感」、「人才市场」归一为「员工市场」；rb08 修正「安全中心」→Bastion 与「上面 5 步」→6 步事实错误
- 白皮书以 SPEC rc3 反向回填 8 处漂移 + 版头加同步锚点：L1 持久身份文件、L2 成功率阈值显式声明、L4 低风险无人值守与记忆留痕回滚、人格/纪律分类判定标准与正反例（含生态适用条件限定）、人审三不得、错误枚举化独立条款、评测防博弈升格为评测章第 5 条（含 LongMemEval）、A2A/AGENTS.md 互补定位段与映射表行；§8.2 补探针一票否决定义
- slides 门面纪律：封面与 slide 9 的「47 Skills」标注为案例产品自述数字；slide 12 消除 Team 编排错位（L3 去 Team 化、L5 对齐 SPEC）并补联合门槛声明；slide 13 补列 P5 并注明 canary 同源

## [0.2.0] - 2026-09-18

### 勘误与流程（2026-09-18，深审后）

- 附录 C 引用卫生修正（依据 reviews/2026-09-18-deep-audit 附录 A 的一手来源核验，SPEC 与白皮书同步）：InjecAgent 署名更正为 Qiusi Zhan et al.；消歧两个同名 ACP（并入 A2A 的是 IBM/BeeAI Agent Communication Protocol，Zed 的 Agent Client Protocol 独立存续）；Zed ACP 发布日期更正为 2025-08（ACP Registry 2026-01 上线）；IEEE P3777 改用官方题名；LongMemEval 标题与链接对齐 v1（ICLR 2025）并补 V2 链接；AGENTS.md 托管出处补 AAIF 官方公告
- README 数字员工仓库规模注明检索口径与日期
- 新增 SIP-0001（[sips/SIP-0001-m0-gap-closure.md](sips/SIP-0001-m0-gap-closure.md)，M0 兑现包：闭合承诺—兑现断链、模板分离原则修复、治理条款可执行化），流程首次实跑，编号于 review 时分配、经 BDFL 拍板状态合并流转至 implemented
- SIP-0001 WP1–WP3 落地：12 题探针补 variant_of 变体注记与变体机制说明，probes/README 新增「回归 ≠ 审计」边界声明、统计功效声明与「防博弈设计」一节，新增 probes/private/ 私有保留集占位约定；AGENTS 三条红线圈入受管块（首个 numployee:managed 实例，SPEC 5.6 落地），SOUL 边界三小节迁往 AGENTS（SOUL 只留表达层边界，修复人格/纪律双写），新增 capabilities/CAPABILITIES.template.md（修复 L3 声明式能力清单断档与 AGENTS 头部悬空引用），BOOTSTRAP 补完成标记、AGENTS Session Startup 补触发链；EVIDENCE 证据包补 evidence-sha256 防篡改清单与双评审留痕字段（含 kappa 口径说明），checklist 明示「必要条件子集」属性、声明格式以 SPEC 第 8 章为唯一基准（本清单字段为推荐扩展）
- SIP-0001 WP4–WP5 落地（所有者拍板，与该 SIP review 合并追认）：T6 拆分为 T6a（会话内）+ T6b（跨会话一致性，L4，承接 SPEC 4.4），P4/P5 判定操作化补强（反对意见须含具体理由；立场/语气三档参照量表），记分规则补基线跨版本语义；GOVERNANCE 新增现阶段投票为咨询性质声明、创始维护者任命程序、BDFL 失联兜底、M3 可判定启动条件、实现名录与失实声明移除机制；CONTRIBUTING 双评审条款改为外部评审可担任（单人阶段可执行）。SECURITY/COC 的占位邮箱处理当时待定
- 联系渠道改为无邮箱方案（所有者拍板）：SECURITY.md 披露改走 GitHub 私下漏洞报告（Security Advisories），CODE_OF_CONDUCT.md 举报改走 Issue / 直接联系维护者 @TeFuirnever，GOVERNANCE 发布前核对项由「邮箱占位符」改写为「联系渠道可用性」，SIP-0001 遗留项清零
- 独立深度审视报告归档 reviews/2026-09-18-deep-audit/
- GitHub Pages 文档站（已上线：<https://tefuirnever.github.io/numployee/>）：mkdocs.yml（Material 主题、深浅色切换、中文搜索 jieba 分词、Mermaid 渲染、显式收回 MkDocs 对顶层 templates/ 的默认排除），scripts/build-pages.py 内容装配（MkDocs 要求 docs_dir 为配置子目录），docs/、probes/suites/、implementations/ 等 5 个目录补 README 导览页（目录链接在站点与 GitHub 双侧可达）；CI 双工作流：pages.yml 推 main 即构建部署，verify.yml 在 PR/main 上以 mkdocs build --strict 门控
- 收尾对齐：新建 AGENTS.md（站点管线规则与文档纪律）；README 仓库导览补 reviews/ 与站点管线两行，docs/、implementations/、sips/ 行改指各自导览页；CITATION.cff 探针数 12→13；CONTRIBUTING 补站点 strict 门控说明

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
