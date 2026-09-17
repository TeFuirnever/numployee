# 参考文献核验报告：numployee whitepaper.md 编号 17–31
> 档案说明（2026-09-17 去品牌决议）：本评审报告中的产品名称与私有仓库路径已匿名化，评审结论与证据不受影响。


核验日期：2026-09-17 ｜ 对象：`社区工程/numployee/docs/whitepaper.md:207-222`（SPEC.md 附录 C 逐字一致，已比对）｜ 只读，未修改任何文件。

## 统计

| 评级 | 数量 | 编号 |
|---|---|---|
| ✅ Verified | 9 | 18, 20, 22, 23, 24, 26, 28, 29, 30 |
| ⚠️ Check suggested | 5 | 17, 21, 25, 27, 31 |
| ❌ Needs fix | 1 | 19 |
| ❓ Unverifiable | 0 | — |

15/15 条 URL 完成 HTTP 检查：14 条 200；#19 返回 000（连接被拒/超时，整域不可达）。

## ❌ / ⚠️ 明细

| 编号 | 严重级 | 问题 | 当前值 | 应改为 | 证据来源 |
|---|---|---|---|---|---|
| 19 | **Critical（链接死）** | 整域 `openclaw-docs.website.cncfstack.com` 不可达（curl 000，系第三方镜像站）；官方文档存在同路径页面 | `https://openclaw-docs.website.cncfstack.com/reference/AGENTS.default` | `https://docs.openclaw.ai/reference/AGENTS.default`（实测 200，页面标题 "Default AGENTS.md · OpenClaw"，与所引标题语义一致） | <https://docs.openclaw.ai/reference/AGENTS.default> |
| 17 | Warning（标题不精确） | 页面实际名称（JSON-LD headline + 面包屑）为 "How Claude remembers your project"，无 "Memory" 标题；URL slug 为 memory | `Memory` | `How Claude remembers your project`（或 "Memory 文档"） | <https://code.claude.com/docs/en/memory> |
| 21 | Warning（日期错误，且正文同步出错） | 讨论创建于 2025-05-13（preview 期）；页面 og 标记显示 GA 文本更新于 **2025-09-25**；GitHub 官方 changelog 同日（`2025-09-25-copilot-coding-agent-is-now-generally-available`，实测 200）。引文"2025-08"两个日期都不沾；正文 §2.2"于 2025 年 8 月正式商用"同样错误，需一并改 | `2025-08` | `2025-09`（正文 §2.2 同改） | <https://github.com/orgs/community/discussions/159068>、<https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/> |
| 25 | Warning（标题为转述非实题） | 页面实际标题为 "LangChain vs. AutoGen in 2026: What the Maintenance Announcement Changed"（datePublished 2026-06-23，与所引 2026-06 吻合；归属 LangChain 正确） | `LangChain vs. AutoGen: LangGraph as a durable runtime` | `LangChain vs. AutoGen in 2026: What the Maintenance Announcement Changed` | <https://www.langchain.com/resources/langchain-vs-autogen> |
| 27 | Warning（日期漂移） | 文章最初发表于 **2024-06-14**，2026-08-11 修订；引文取的是修订日期，未注原始发布日期 | `2026-08` | `2024-06`（首发；或标注 2024-06 发布/2026-08 修订） | <https://www.ai-indeed.com/encyclopedia/9328.html> |
| 31 | Warning（两处日期/事实误差；归属与实现名单核实无误） | ① 仓库 created_at = **2025-06-23**（GitHub API），非 2025-08；② 官方 Updates 页记载 "ACP Registry is Released" 日期为 **2026-03-09**（registry 仓库创建于 2025-12-17），非"2026-01 上线"。其余论断核实通过：仓库存在（现 301 至 agentclientprotocol/agent-client-protocol 组织仓）、Zed 发起 ✅、JetBrains 共维护 ✅（官网导航并列 Zed Industries/JetBrains）、JSON-RPC over stdio ✅、OpenCode/Gemini CLI/Claude Agent 实现 ✅（agents 页与 ACP Registry 条目均含 Claude Agent） | `2025-08`；`ACP Registry 于 2026-01 上线` | `2025-06`；`ACP Registry 于 2026-03 发布` | <https://api.github.com/repos/zed-industries/agent-client-protocol>、<https://agentclientprotocol.com/updates>、<https://agentclientprotocol.com/overview/agents> |

## 论断支撑对齐抽查

| 编号 | 正文转述位置（章节） | 判定 | 一句话理由 |
|---|---|---|---|
| 16 | §3.1 与相邻概念的区分（workflow=预定义代码路径 / agent=动态自指挥）；§5 分层依据（chaining→routing→parallelization→orchestrator-workers→自主 agent 阶梯） | faithful | 与 Anthropic 原文的定义和五种 workflow 模式一一对应 |
| 17 | §4.1 人格层（CLAUDE.md + auto memory 持久化、`@` 导入模块化）；§4.3 知识层；§6.2（CLAUDE.md 过长挤占上下文） | faithful | 与文档页自述（persistent instructions + auto memory）及最佳实践警告一致 |
| 18 | §4.1 人格层（SOUL.md=人格/语气/边界、IDENTITY.md、USER.md；"SOUL.md 放人格与边界"） | faithful | 原文逐文件讲解 SOUL.md "personality, values, tone, behavioral boundaries"，文件清单吻合 |
| 19 | §6.1 继承约束（"子代理只继承 AGENTS.md + TOOLS.md"） | ❓ Unverifiable | 链接已死无法核对原文；改用官方 `docs.openclaw.ai/reference/AGENTS.default` 后需复核该继承论断 |
| 30 | §3.2 四要素（人本监督）；§4.5 治理层（人本监督、可审计、渐进授权）；§7.2（渐进授权） | faithful | 白皮书标题页与摘要确认主题（人本监督/责任/渐进自主），属合理转述非逐字引用 |
| 31 | §4.4 运行时层（"Zed 发起、JetBrains 共维护的开放协议，JSON-RPC over stdio…OpenCode、Gemini CLI、Claude Agent 等均已实现接入"）；§9 映射表 | faithful（日期除外） | 协议定位、发起方、实现名单均与官方站点一致；"正在成为业界标准"为可接受的业界判断；但引文自带的两处日期（2025-08、Registry 2026-01）错误，见明细表 |

## ✅ 一行带过

- **18**：标题逐字一致（OpenAgent.Mom，第三方博客非官方文档，引文未标机构故无归属错误），datePublished 2026-03-07 ✅
- **20**：标题一致；原文 2023-11-07 首发、2026-08-01 大改版（现标题含 "August 2026"），引文 2026-08 取当前版本日期，可接受 ✅
- **22**：SWE-agent 仓库 200，Princeton NLP 归属正确 ✅
- **23**：标题（headline "SWE-2 Is Free on Devin's $20 Plan: The Best AI Coding Deal in September 2026"）与日期 2026-09-10 吻合；注意 SaaSCity 为小站，文内已链 cognition.com 一手来源 ✅
- **24**："Agents - CrewAI" 页面 200，v1.15.20 版本钉取有效 ✅
- **26**：H1 逐字一致，datePublished 2025-06-03 ✅
- **28**：标题（"2026年AI数字员工行业趋势：从'概念展示'到'规模化商用'的四大信号"）与 2026-07-09 日期吻合；正文 469 亿元/31.56%/IDC 数据均在原文命中 ✅
- **29**：标题、作者（Hao Wang/Moogician）、日期 2026-04-08 全部吻合 ✅
- **30**：PDF 378KB 下载成功，标题页 "Practices for Governing Agentic AI Systems"（Shavit 等，OpenAI），2023-12 吻合 ✅

**给主代理的要点**：#19 是唯一 Critical（死链→官方同路径替换）；#21 的日期错误同时污染正文 §2.2，需两处同改；#31 核心归属论断全部成立，仅引文自带两处日期需修正；#19 支撑的 §6.1 继承论断因原链死亡标记为待复核。