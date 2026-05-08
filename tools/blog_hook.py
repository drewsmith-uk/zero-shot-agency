import re
from datetime import datetime
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*", re.DOTALL)
FIELD_RE = r"^{field}:\s*[\"']?(.*?)[\"']?\s*$"


def _frontmatter_value(content, field):
    frontmatter_match = FRONTMATTER_RE.match(content)
    if not frontmatter_match:
        return None

    match = re.search(
        FIELD_RE.format(field=re.escape(field)),
        frontmatter_match.group(1),
        flags=re.MULTILINE,
    )
    return match.group(1).strip() if match else None


def _slug_from_title(title):
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s\-]", "", slug)
    slug = re.sub(r"[\s\-]+", "-", slug).strip("-")
    return slug


def _parse_post(file):
    content = file.read_text(encoding="utf-8")
    title = _frontmatter_value(content, "title")
    date_raw = _frontmatter_value(content, "date")

    if not title or not date_raw:
        return None

    slug = _frontmatter_value(content, "slug") or _slug_from_title(title)
    date_part = date_raw.split()[0]
    sort_date = datetime.fromisoformat(date_raw)

    return {
        "title": title,
        "date": date_raw,
        "sort_date": sort_date,
        "url": f"/blog/{date_part.replace('-', '/')}/{slug}/",
    }


def _get_posts():
    blog_dir = Path("docs/blog/posts")
    if not blog_dir.exists():
        return []

    posts = []
    for file in blog_dir.glob("*.md"):
        post = _parse_post(file)
        if post:
            posts.append(post)

    return sorted(posts, key=lambda post: post["sort_date"], reverse=True)


def on_config(config, **kwargs):
    posts = _get_posts()

    config.setdefault("extra", {})
    config["extra"]["recent_posts"] = [
        {"title": post["title"], "date": post["date"], "url": post["url"]}
        for post in posts[:5]
    ]

    for item in config.get("nav", []):
        if "Blog" in item:
            item["Blog"] = [{"View All Posts": "blog/index.md"}]
            item["Blog"].extend(
                {post["title"]: post["url"]}
                for post in posts[:3]
            )
            break

    return config
