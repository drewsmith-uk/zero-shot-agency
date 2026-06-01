#!/usr/bin/env python3
"""Validate Markdown YAML frontmatter shape for the ZSA MkDocs site.

This intentionally checks schema shape, not just YAML parseability. YAML accepts
unquoted list items containing ``: `` as mappings, which can silently turn a
frontmatter list of strings into a mixed list of strings and dictionaries.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

BLOG_REQUIRED_FIELDS = {
    "title": str,
    "date": (str,),
    "slug": str,
    "description": str,
}

STRING_LIST_FIELDS = (
    "categories",
    "tags",
    "geo_tactics",
)


def _type_name(expected: Any) -> str:
    if isinstance(expected, tuple):
        return " or ".join(t.__name__ for t in expected)
    return expected.__name__


def load_frontmatter(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    """Return parsed frontmatter and validation errors for extraction/parsing."""
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, ["missing YAML frontmatter block"]

    try:
        parsed = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return None, [f"invalid YAML frontmatter: {exc}"]

    if parsed is None:
        return {}, []
    if not isinstance(parsed, dict):
        return None, [f"frontmatter must be a mapping, got {type(parsed).__name__}"]
    return parsed, []


def validate_markdown_file(path: Path) -> list[str]:
    """Validate one Markdown file's frontmatter and return human-readable errors."""
    data, errors = load_frontmatter(path)
    if data is None:
        return errors

    is_blog_post = "docs/blog/posts" in path.as_posix() or path.parent.as_posix().endswith("blog/posts")

    if is_blog_post:
        for field, expected_type in BLOG_REQUIRED_FIELDS.items():
            if field not in data:
                errors.append(f"missing required field: {field}")
                continue
            if field == "date":
                # PyYAML may parse YYYY-MM-DD as datetime.date. MkDocs accepts it,
                # so only reject obviously structured values here.
                if isinstance(data[field], (list, dict)):
                    errors.append(f"{field} must be a scalar date, got {type(data[field]).__name__}")
            elif not isinstance(data[field], expected_type):
                errors.append(
                    f"{field} must be {_type_name(expected_type)}, got {type(data[field]).__name__}"
                )

    for field in STRING_LIST_FIELDS:
        if field not in data:
            continue
        value = data[field]
        if not isinstance(value, list):
            errors.append(f"{field} must be list[str], got {type(value).__name__}")
            continue
        for index, item in enumerate(value):
            if not isinstance(item, str):
                errors.append(
                    f"{field}[{index}] must be a string, got {type(item).__name__}; "
                    "quote list items containing ': '"
                )

    return errors


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(p for p in path.rglob("*.md") if ".git" not in p.parts))
        elif path.suffix == ".md":
            files.append(path)
    return files


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Markdown frontmatter schema shape.")
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path("docs/blog/posts")],
        help="Markdown files or directories to validate (default: docs/blog/posts)",
    )
    args = parser.parse_args(argv)

    failures: list[str] = []
    for path in iter_markdown_files(args.paths):
        for error in validate_markdown_file(path):
            failures.append(f"{path}: {error}")

    if failures:
        print("Frontmatter validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("Frontmatter validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
