# CONTRIBUTING.md — 贡献指南

感谢你对 numployee（数字员工开放标准与工具包）的兴趣。本文件说明欢迎的贡献类型与流程。

## 欢迎的贡献类型

| 贡献类型 | 说明 | 入口 |
| --- | --- | --- |
| 标准修订 SIP | 修改 SPEC、调整成熟度要求 | `sips/README.md` |
| 新实现映射 | 将标准映射到新的运行时/平台 | Issue 先行讨论，再提 PR |
| 探针贡献 | 新增/修订回归探针 | `probes/README.md` + 本文件「探针贡献规范」 |
| 模板改进 | 改进 `templates/` 空白模板 | 直接 PR（需说明可移植性影响） |
| 翻译 | 翻译标准、文档、模板 | 直接 PR（术语表以 SPEC 为准） |

## 探针贡献规范

1. **可判定性**：每道题必须有明确的标准输入、可观察的通过判定与失败判定；不接受「看感觉打分」的题目。
2. **不教攻击**：探针集用于员工上岗考核。贡献中**不得**包含可复用的越狱技巧、提示注入 payload 或绕过细节；题目描述到「足以判定」为止，高危细节由维护者在评审中把关。
3. **双评审**：新探针须两名评审人评审通过后方可合入——评审人可为维护者邀请的外部评审（单人维护阶段由维护者加一名外部评审执行）；涉及判定标准变更的，须同步走 SIP 流程（见 `sips/README.md`）。

## 行为准则

所有参与者须遵守本仓库的 `CODE_OF_CONDUCT.md`。参与本项目即表示同意其中的条款。

## Commit 规范

采用 Conventional Commits：

- `feat:` 新功能/新探针/新模板章节
- `fix:` 修正错误（含探针判定修正）
- `docs:` 仅文档变动
- `refactor:` 不改变行为的重构
- `test:` 探针或测试相关
- `chore:` 构建、杂项

示例：`feat(probes): 新增 L5 多员工协作探针草案`

## PR 流程

1. Fork 本仓库，从 `main` 切出分支：`git checkout -b feat/your-topic`。
2. 提交 commit（遵循上述规范），推送到你的 Fork。
3. 向 `main` 发起 Pull Request，描述改动动机与影响面（涉及 SPEC 的改动须先有关联 SIP）。
4. 至少一名维护者评审通过后合并；标准类变更需按 `GOVERNANCE.md` 的决策分级执行。

## English Summary

This repository welcomes contributions in five areas: standard revisions via SIPs, new implementation mappings, probe contributions, template improvements, and translations. Probes must be objectively judgeable and must not include reusable jailbreak or prompt-injection details; they require two maintainer reviews. All contributors must follow `CODE_OF_CONDUCT.md`. We use Conventional Commits and a fork-and-branch PR workflow reviewed by maintainers.
