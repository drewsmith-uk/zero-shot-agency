from pathlib import Path

from tools.validate_frontmatter import validate_markdown_file


def write_post(tmp_path: Path, frontmatter: str) -> Path:
    post_dir = tmp_path / "docs" / "blog" / "posts"
    post_dir.mkdir(parents=True)
    post = post_dir / "post.md"
    post.write_text(f"---\n{frontmatter}---\n\n# Day 99: Test Post\n", encoding="utf-8")
    return post


def test_rejects_mapping_inside_string_list_field(tmp_path):
    post = write_post(
        tmp_path,
        """
title: "Day 99: Test Post"
date: 2026-06-02
slug: "day-99-test-post"
description: "Test description"
categories:
  - Build in Public
tags:
  - GEO
geo_tactics:
  - Keep the Google caveat clear: llms.txt is not magic
""".lstrip(),
    )

    errors = validate_markdown_file(post)

    assert any(
        "geo_tactics[0] must be a string" in error and "quote list items containing ': '" in error
        for error in errors
    )


def test_accepts_quoted_colon_inside_string_list_field(tmp_path):
    post = write_post(
        tmp_path,
        """
title: "Day 99: Test Post"
date: 2026-06-02
slug: "day-99-test-post"
description: "Test description"
categories:
  - Build in Public
tags:
  - GEO
geo_tactics:
  - "Keep the Google caveat clear: llms.txt is not magic"
""".lstrip(),
    )

    assert validate_markdown_file(post) == []


def test_rejects_missing_required_blog_string_fields(tmp_path):
    post = write_post(
        tmp_path,
        """
title: "Day 99: Test Post"
categories:
  - Build in Public
""".lstrip(),
    )

    errors = validate_markdown_file(post)

    assert "missing required field: date" in errors
    assert "missing required field: slug" in errors
    assert "missing required field: description" in errors
