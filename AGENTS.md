# AGENTS.md — numployee 仓库协作规则

## 仓库性质

标准/文档仓 + 一个 GitHub Pages 站点管线。唯一可执行脚本：`scripts/build-pages.py`（stdlib only）。

## 站点管线（改动任何 .md 前必读）

- `mkdocs.yml` 在根目录，但 `docs_dir` 是 `pages/content/`——由 `scripts/build-pages.py` 装配的生成物，勿手改（MkDocs 要求 docs_dir 为配置文件的子目录，故内容先镜像）。
- 本地验证（等价 CI）：`python3 scripts/build-pages.py && uv run --no-project --with mkdocs-material --with jieba mkdocs build --strict`。
- **新增、删除、重命名任何 .md 文件，必须同步更新 `mkdocs.yml` 的 nav**——verify.yml 在 PR 上跑 `mkdocs build --strict`，nav 缺页即红。
- MkDocs 默认把顶层 `templates/` 当作主题目录整体排除；本仓的 `templates/` 是内容目录，已在 `mkdocs.yml` 用 `exclude_docs: "!/templates/"` 显式收回——不要删除该行。
- `site/`、`pages/content/` 是生成物，已 gitignore；部署为 artifact 方式，构建产物不入库。
- 发布：push 到 main 触发 pages.yml 自动部署到 <https://tefuirnever.github.io/numployee/>。

## 文档纪律

- 承诺—兑现一致：文档声明的机制必须有对应实例（2026-09-18 深审的十条断链教训，见 `reviews/2026-09-18-deep-audit/ANALYSIS.md`）。
- 标准级改动（SPEC 条款、探针判定标准、治理模型）先走 SIP（`sips/README.md`）；措辞勘误直接 PR。
- Conventional Commits；变更记入 `CHANGELOG.md` 的 Unreleased。
- 探针、模板、合规清单的格式基准以 `SPEC.md` 为准，其他文件引用而不复述。
