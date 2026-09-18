#!/usr/bin/env python3
"""把仓库公开内容镜像到 pages/content/，供 MkDocs 构建。

MkDocs 要求 docs_dir 是配置文件的子目录，而本仓内容散布在根目录，
因此构建前先把内容按原目录结构拷贝到 pages/content/（已 gitignore，
属生成物，不要手改）。
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DST = ROOT / "pages" / "content"

EXCLUDE_DIRS = {".git", "site", "pages", "node_modules", ".cache", "__pycache__"}
EXCLUDE_ROOT_FILES = {"mkdocs.yml", "requirements-pages.txt", "AGENTS.md", "CLAUDE.md"}


def main() -> None:
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)
    count = 0
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT)
        if path.is_dir():
            continue
        if any(part in EXCLUDE_DIRS or part.startswith(".") for part in rel.parts):
            continue
        if len(rel.parts) == 1 and rel.name in EXCLUDE_ROOT_FILES:
            continue
        target = DST / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        count += 1
    print(f"assembled {count} files -> pages/content/")


if __name__ == "__main__":
    main()
