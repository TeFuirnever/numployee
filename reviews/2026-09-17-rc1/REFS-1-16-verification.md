核验完成，以下为完整报告。
> 档案说明（2026-09-17 去品牌决议）：本评审报告中的产品名称与私有仓库路径已匿名化，评审结论与证据不受影响。


---

# 参考文献核验报告：numployee whitepaper.md 参考来源（编号 1–16）

核验日期：2026-09-17。方法：全部 16 条 URL 经 `curl -sL -o /dev/null -w "%{http_code}"` 可达性检查；arXiv 条目（1–12、15）经 `export.arxiv.org/api/query` 核对标题/首作者/发表日期；ACL 条目（14）核对 anthology 页面元数据（含 citation_author / citation_publication_date / citation_doi meta 标签）；Anthropic 条目（13、16）核对页面标题与正文署名/日期。

## 统计行

| 等级 | 数量 | 编号 |
|---|---|---|
| ✅ Verified | 15 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16 |
| ⚠️ Check suggested | 1 | 14 |
| ❌ Needs fix | 0 | — |
| ❓ Unverifiable | 0 | — |

Critical 差异：0；Warning 差异：1。

## ❌/⚠️ 明细表

| 编号 | 级别 | 问题 | 当前值 | 应改为 | 证据来源 |
|---|---|---|---|---|---|
| 14 | Warning（完整性，不影响真实性） | 条目标题/出处/年份/URL 全部正确，但缺失作者列表（其余学术条目均含首作者 et al.） | `Can LLM Agents Maintain a Persona in Discourse? EMNLP 2025.` | `Pranav Bhandari et al. Can LLM Agents Maintain a Persona in Discourse? EMNLP 2025, pp. 29213–29229. DOI: 10.18653/v1/2025.emnlp-main.1487.` | https://aclanthology.org/2025.emnlp-main.1487/ 页面 meta：`citation_author` ×7（Bhandari, Fay, Wise, Datta, Meek, Naseem, Nasim），`citation_conference_title` = Proceedings of the 2025 Conference on EMNLP，`citation_publication_date` = 2025/11 |

补充观察（不构成问题）：13 引用页全题为 "The Persona Selection Model: **Why AI Assistants might Behave like Humans**"（Sam Marks, Jack Lindsey, Christopher Olah，2026-02-23），现条目用了主标题简写、未列作者——机构博客引用惯例下可接受。16 页面正文明示 "Dec 19, 2024"，与所标 "2024-12" 一致。

## 各条核验证据（简记）

- **1** arXiv:2309.07864 → 标题、首作者 Zhiheng Xi、2023-09-14 完全一致 ✅
- **2** 2210.03629 → ReAct，Shunyu Yao，ICLR 2023 属实 ✅
- **3** 2303.11366 → Reflexion，Noah Shinn，NeurIPS 2023 属实 ✅
- **4** 2302.04761 → ToolFormer，Timo Schick，2023 ✅
- **5** 2310.08560 → MemGPT，Charles Packer，2023 ✅
- **6** 2304.03442 → Generative Agents，Joon Sung Park，UIST 2023 属实 ✅
- **7** 2303.17760 → CAMEL，Guohao Li，NeurIPS 2023 属实 ✅
- **8** 2308.03688 → AgentBench，Xiao Liu，ICLR 2024 属实 ✅
- **9** 2307.13854 → WebArena，Shuyan Zhou，ICLR 2024 属实 ✅
- **10** 2310.06770 → SWE-bench，Carlos E. Jimenez，ICLR 2024 属实 ✅
- **11** 2406.13352 → AgentDojo，Edoardo Debenedetti，2024-06 ✅
- **12** 2602.07918 → CausalArmor（Minbeom Kim et al.），2026-02，标题一致；`/html/2602.07918v1` 返回 200 ✅
- **13** alignment.anthropic.com/2026/psm/ → 200，标题、归属 Anthropic、2026 年一致 ✅
- **15** 2308.08155 → AutoGen，Qingyun Wu，2023 ✅
- **16** anthropic.com/engineering/building-effective-agents → 200，H1 "Building effective agents"，页面日期 Dec 19, 2024 = 所标 2024-12 ✅

## 论断支撑对齐表

正文采用【学术】/【业界】分类标签而非数字角标，以下按内容对应关系定位转述。

| 编号 | 正文转述位置（章节） | 判定 | 一句话理由 |
|---|---|---|---|
| 1 (Xi 综述) | §"两条线在学术侧汇合"（约 L40）：综述将 agent 归纳为 Profile/Memory/Planning/Action 四模块 | faithful | 综述 §2 即按 profiling、memory、planning、action 组织 agent 构造（其上层框架表述为 brain/perception/action，四模块是其展开，转述成立） |
| 2 (ReAct) | §4.2 能力层（L86）："将推理轨迹与工具调用交错，构成工具使用的基础循环" | faithful | 正是 ReAct 的核心贡献（reasoning traces 与 actions 交错生成） |
| 3 (Reflexion) | §4.3 记忆层（L93）："把单次任务的教训语言化为可复用经验" | faithful | verbal reinforcement + episodic memory 的文本反思即其机制 |
| 4 (ToolFormer) | §4.2 能力层（L86）："证明模型可自学何时、如何使用外部工具" | faithful | 与论文 self-supervised 学习 API 调用（which tool/when/what input）吻合 |
| 5 (MemGPT) | §4.3 记忆层（L93）及§6 未解问题（L178）：OS 虚拟内存之喻、分层记忆与自定向读写；"给了读写机制，没给写入判据" | faithful | 与 MemGPT 的 main context + external storage、self-directed paging 一致；"无写入判据"是对论文空白处的准确观察 |
| 6 (Generative Agents) | §4.3 记忆层（L93）："记忆流 + 重要性/新近性/相关性检索 + 周期性反思" | faithful | 与论文 memory stream、retrieval 三因子（recency/relevance/importance）、reflection 机制一一对应 |
| 7 (CAMEL) | §4.4 规划层（L102）："角色扮演双代理协作" | faithful | CAMEL 即 role-playing + inception prompting 的双 agent 交流框架 |
| 10 (SWE-bench) | §5.1 任务基准（L150）："真实 GitHub issue 修复、以测试用例通过为门" | faithful | 与论文任务构造（真实仓库 issue、以 FAIL→PASS 测试为解决判据）一致 |
| 13 (PSM) | §3 形态光谱（L50）："人格是预训练习得的候选集合经后训练筛选的产物，同一模型可稳定呈现多种人格" | oversimplified（轻度） | 博客确称预训练习得模拟多样角色、后训练筛选出 Assistant persona；但"稳定呈现多种人格"是博客调研的延伸含义而非原文断言，且该页是观点性博文而非同行评议"研究"，正文称其"研究表明"略微拔高了证据等级 |
| 14 (EMNLP persona) | §6 未解问题 1（L180）："persona 研究证实一致性是架构属性，但上下文压缩、记忆污染、模型升级都会侵蚀它" | oversimplified | 论文实测的是 LLM 在 dyadic discourse 中因 context-shifting 而 persona 一致性下降，支持"会被侵蚀"的一半；"证实一致性是架构属性"是超出该文结论的强表述（论文未建立"架构属性"这一定性） |

## 遗留说明（供主代理参考）

- 编号 1–16 之外（17–31）未在本轮范围内，但其 URL 多属博客/文档类，如需扩展核验可用同一套 curl + 页面元数据流程。
- 两处文件（whitepaper.md 与 SPEC.md 附录 C）声明为同一份清单，本次仅核验了 whitepaper.md；若 SPEC.md 版本有出入，建议做一次 diff 即可，无需重复核验。
- 未修改任何文件。