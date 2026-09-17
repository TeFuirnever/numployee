# SIP — Standard Improvement Proposal（标准改进提案）

SIP 是修改本仓库**标准类资产**的正式流程。探针措辞修订、模板示例调整、文档勘误等不改变标准含义的改动不需要 SIP，直接 PR 即可。

## 什么是 SIP

SIP 是一份书面提案，记录一项标准变更的动机、方案与影响面，供维护者评审与投票。它保证标准演进可追溯、可讨论、可回放。

## 何时需要 SIP

- 修改 `SPEC.md` 的任何条款；
- 新增或调整成熟度等级（L1-L5）要求；
- 改变 `probes/probes.md` 中既有探针的判定标准；
- 修改治理模型（`GOVERNANCE.md`）。

新增探针而不改变既有判定标准，走探针贡献双评审即可（见 `CONTRIBUTING.md`）；若想固化判定标准，仍需 SIP。

## 状态机

```
draft → review → accepted ──→ implemented
              └────→ rejected
```

- **draft**：作者起草中，可自由修改。
- **review**：提交 PR 进入评审，维护者按 `GOVERNANCE.md` 决策分级评审。
- **accepted / rejected**：评审结论；rejected 的 SIP 保留存档，说明理由后可重新提交。
- **implemented**：配套变更已合入 `main`，SIP 状态更新并归档。

## 编号规则

- 编号格式：`SIP-NNNN`（四位数字，不足补零），从 `SIP-0001` 起顺序分配。
- 编号在 review 状态确认时分配，一经分配不复用（即使该 SIP 被拒绝）。

## 与 SPEC 版本号的关系

SPEC 采用语义化版本，映射规则：

| 变更类型 | 版本段 | 示例 |
| --- | --- | --- |
| 不兼容的标准变更 | major | 2.0.0 |
| 新增成熟度等级或新增章节 | minor | 1.1.0 |
| 措辞勘误（不改变含义） | patch | 1.0.1 |

每次 SPEC 发版须在发布说明中列出对应 SIP 编号。

## 如何提交

1. 复制 `sips/sip-template.md` 为 `sips/SIP-XXXX-<slug>.md`（编号先留 `XXXX`，进入 review 后分配）。
2. 填写全部章节；「影响面」一节必须逐条列出受影响的 SPEC 章节、探针与模板。
3. 发起 PR，关联本文件与 `GOVERNANCE.md` 中对应的决策分级。
