# 参考实现映射：Claude Code（纸面 desk-check）

> **映射性质**：这是**纸面映射（desk-check）**，非运行时验证。所有事实取自 Claude Code 官方文档站（code.claude.com/docs/en/）2026-09-18 访问的一手页面，每条附来源 URL；未在真实 Claude Code 运行时中逐条复跑。若官方文档与实际行为不符，以实际行为为准并请通过 SIP 提出修正。
>
> **目的**：SPEC 第 5 章（可移植性标准）此前仅有 OpenClaw 单源支撑。本映射逐条检验六条机制在第二个 harness 上的对应物，使该章的论断可被第三方证伪或证实。

本文件是《数字员工规范》（见 [../../SPEC.md](../../SPEC.md)）的第二参考实现映射；不是规范的一部分，示例不构成规范要求。

## 1. 配置面总览（对应规范第 2、3 章）

Claude Code 的员工配置面由五类原生机制组成：

| 机制 | 位置 | 对应规范层 | 来源 |
| --- | --- | --- | --- |
| CLAUDE.md 记忆文件 | managed / `~/.claude/` / 项目 / local 四层，拼接加载 | 人格层 + 纪律 + 知识层（混合） | <https://code.claude.com/docs/en/memory> |
| Output styles | 用户 / 项目 / managed 三级 | 人格层（语气与输出风格） | <https://code.claude.com/docs/en/output-styles> |
| Skills | 企业 / 个人 / 项目 / 插件四级 | 能力层 | <https://code.claude.com/docs/en/skills> |
| settings.json 权限 | managed > 命令行 > project local > project > user | 治理层 | <https://code.claude.com/docs/en/settings> |
| Hooks（PreToolUse 等） | settings 内配置 | 治理层（拦截） | <https://code.claude.com/docs/en/hooks> |

四要素落点：持久身份 ≈ 项目 CLAUDE.md + auto memory；可装配能力 = Skills/插件；可治理红线 = 权限规则 + PreToolUse hook；可沉淀知识 = CLAUDE.md + memory 目录。

## 2. 可移植性六条逐条 desk-check（规范第 5 章）

| 规范条目 | Claude Code 对应物 | 判定 | 来源 |
| --- | --- | --- | --- |
| 5.1 三件套分离 | 无原生三文件划分；纪律与环境事实同混于单一 CLAUDE.md，人格侧另有 output styles | **部分对应**（人格/纪律可分，纪律/事实不分文件） | memory / output-styles 页 |
| 5.2 单一职责与分层协议 | `@path` import（递归限 4 跳，相对引入文件解析）+ 子目录 CLAUDE.md 懒加载；官方建议 ≤200 行 | **对应** | memory 页 |
| 5.3 语义化版本 | 配置文件无官方版本字段；插件 manifest 有可选 `version`，市场分发存在 | **部分对应**（插件层有，配置层无） | <https://code.claude.com/docs/en/plugins> |
| 5.4 继承协议 | 子代理默认加载全部四层 CLAUDE.md；`omitClaudeMd: true` 可退出（managed 层除外）；深层覆盖浅层的目录树语义无对应 | **部分对应**（继承存在，为默认开启 + 逐项退出模型） | <https://code.claude.com/docs/en/sub-agents> |
| 5.5 环境事实与策略分离 | 无对应——两者同混于 CLAUDE.md；settings.json 只承载行为开关而非环境事实清单 | **无原生对应** | memory / settings 页 |
| 5.6 受管块 | 无块级标记机制；最近似物为 managed settings 层（「Nothing you set overrides them」）的**文件外**托管 | **无原生对应**（仅层级的整体托管，无块级粒度） | settings 页 |

**结论**：六条中两条对应、三条部分对应、一条无对应。第 5 章的机制不是任一单一生态的既有事实——分离粒度（三文件）、受管块（块级标记）是本规范相对两个 harness 的**增量要求**，可证伪性成立：任何 harness 均可按此表逐项自查。

## 3. 继承约束推论的独立检验（规范 3.1）

规范 3.1 推论的适用条件是「子代理不继承人格文件的生态」。Claude Code 的官方记载行为独立证实了该条件与推论方向：

- **人格不传播 ✓**：output styles 只作用于主对话与 fork，「其他子代理运行自己的 system prompt，不受影响」；主对话 auto memory 不进入子代理——与 OpenClaw「SOUL.md 不继承」结论一致（来源：output-styles / sub-agents 页）。
- **纪律传播 ✓**：子代理默认加载全部层级 CLAUDE.md——与 OpenClaw「AGENTS.md 继承」方向一致，但 OpenClaw 是按文件类型白名单继承，Claude Code 是单一文件默认全继承 + `omitClaudeMd` 退出（来源：sub-agents 页）。
- **推论外延**：在 Claude Code 上，「纪律写入人格文件会被子代理绕过」表现为「纪律只写进 output style 或主对话记忆，子代理收不到」——推论的机制形式不同，失效后果相同。规范推论的适用范围由此覆盖两个继承模型不同的生态。

## 4. 评测可执行性（规范第 7 章）

`claude -p` headless 模式提供非交互运行、退出码、`--output-format json` / `--json-schema` 结构化输出；`--bare` 模式跳过 hooks/skills/subagents/CLAUDE.md 自动发现以保证跨机器确定性；`--permission-mode dontAsk` 适合锁死的 CI 环境。规范第 7 章「回归集自动跑测」在该 harness 上有可执行路径（来源：<https://code.claude.com/docs/en/headless>）。

## 5. 边界说明

- 本映射只覆盖官方文档记载行为；未实测。文档未回答的问题（如钩子超时 fail-open 的实际触发率）不在本文件下结论。
- PreToolUse 的 `permissionDecision: "ask"` 可实现规范 6.3「破坏性操作人审」的拦截语义，但 command 类 hook 超时不阻断（fail-open）——治理强度有明确上限，引用时须注意（来源：hooks 页）。
- Claude Code 原生不读 AGENTS.md（需 `@AGENTS.md` 桥接）——规范 5.1「纪律文件为 AGENTS.md 开放标准的员工化扩展」在该 harness 上需经 import 间接落地（来源：memory 页）。
