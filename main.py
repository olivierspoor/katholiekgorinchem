import os, re, yaml, markdown as md_lib
from datetime import datetime


def make_slug(title_str):
    slug = title_str.strip().lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    return slug.strip('-')


def load_posts(posts_dir, authors_data, url_prefix, excerpt_only=False):
    posts = []

    for filename in os.listdir(posts_dir):
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(posts_dir, filename)

        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        # Skip drafts
        if re.search(r'^draft:\s*true', content, re.MULTILINE):
            continue

        date = re.search(r'^date:\s*(.+)$', content, re.MULTILINE)
        title = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
        slug_match = re.search(r'^slug:\s*(.+)$', content, re.MULTILINE)

        if not title:
            title = re.search(r'^#\s+(.+)$', content, re.MULTILINE)

        # Get first author
        author_match = re.search(
            r'^authors:\s*\n\s+-\s*(.+)$',
            content,
            re.MULTILINE
        )

        author_key = author_match.group(1).strip() if author_match else None
        author = authors_data.get(author_key, {}) if author_key else {}

        # Strip front matter and title heading
        body = re.sub(r'^---.*?---', '', content, flags=re.DOTALL).strip()
        body = re.sub(r'^#\s+.+$', '', body, flags=re.MULTILINE).strip()

        if excerpt_only:
            if '<!-- more -->' in body:
                body = body.split('<!-- more -->')[0].strip()
            else:
                first_para = re.search(r'^(.+?)(?:\n\n|$)', body, re.DOTALL)
                body = first_para.group(1).strip() if first_para else body

            body = body.replace('\n', ' ')

        # Convert MkDocs image attributes to inline HTML
        def replace_img_attrs(text):
            pattern = r'(!\[([^\]]*)\]\(([^)]+)\))\{([^}]+)\}'

            def repl(m):
                alt = m.group(2)
                url = m.group(3)
                attrs_raw = m.group(4).strip()

                style_match = re.search(
                    r'style=["\']([^"\']+)["\']',
                    attrs_raw
                )

                style = (
                    ' style="' + style_match.group(1) + '"'
                    if style_match else ''
                )

                return (
                    '<img src="' + url +
                    '" alt="' + alt +
                    '"' + style + '>'
                )

            return re.sub(pattern, repl, text)

        body = replace_img_attrs(body)
        body_html = md_lib.markdown(
            body,
            extensions=['tables', 'fenced_code']
        )

        if title and date:
            date_str = date.group(1).strip()

            try:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")

                DUTCH_MONTHS = {
                    1: "januari",
                    2: "februari",
                    3: "maart",
                    4: "april",
                    5: "mei",
                    6: "juni",
                    7: "juli",
                    8: "augustus",
                    9: "september",
                    10: "oktober",
                    11: "november",
                    12: "december"
                }

                date_display = (
                    f"{date_obj.day} "
                    f"{DUTCH_MONTHS[date_obj.month]} "
                    f"{date_obj.year}"
                )

            except Exception:
                date_display = date_str

            # Use custom slug if present, otherwise generate one
            if slug_match:
                slug = slug_match.group(1).strip()
            else:
                slug = make_slug(title.group(1))

            url = url_prefix + slug + ".html"

            posts.append({
                "title": title.group(1).strip(),
                "date": date_str,
                "date_display": date_display,
                "body_html": body_html,
                "url": url,
                "author_name": author.get("name", ""),
                "author_avatar": author.get("avatar", ""),
            })

    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def render_article(p, extra_class="", prepend_html="", append_html=""):
    avatar_html = ""
    if p["author_avatar"]:
        avatar_html = (
            '<nav class="md-post__authors md-typeset">'
            '<span class="md-author">'
            '<img src="' + p["author_avatar"] + '" alt="' + p["author_name"] + '">'
            '</span>'
            '</nav>'
        )

    author_html = ""
    if p["author_name"]:
        author_html = '<li class="md-meta__item author-injected">' + p["author_name"] + '</li>'

    return (
        '<article class="md-post md-post--excerpt' + (' ' + extra_class if extra_class else '') + '">'
        + prepend_html +
        '<header class="md-post__header">'
        + avatar_html +
        '<div class="md-post__meta md-meta">'
        '<ul class="md-meta__list">'
        + author_html +
        '<li class="md-meta__item">'
        '<time datetime="' + p["date"] + '">' + p["date_display"] + '</time>'
        '</li>'
        '</ul>'
        '</div>'
        '</header>'
        '<div class="md-post__content md-typeset">'
        '<h2><a href="' + p["url"] + '">' + p["title"] + '</a></h2>'
        '<div>' + p["body_html"] + '</div>'
        + append_html +
        '</div>'
        '</article>'
    )


def define_env(env):
    @env.macro
    def latest_posts():
        authors_file = "docs/.authors.yml"
        with open(authors_file, encoding="utf-8") as f:
            authors_data = yaml.safe_load(f).get("authors", {})

        berichten = load_posts("docs/berichten/posts", authors_data, "/berichten/", excerpt_only=False)
        artikelen = load_posts("docs/artikelen/posts", authors_data, "/artikelen/", excerpt_only=True)

        parts = ['<div id="latest-posts">']

        # 1. First bericht
        if len(berichten) > 0:
            parts.append(render_article(berichten[0]))

        # 2. Featured artikel
        if len(artikelen) > 0:
            a = artikelen[0]
            prepend = '<h2>Nieuwste artikel</h2>'
            append = (
                '<nav class="md-post__action">'
                '<a href="' + a["url"] + '">Doorgaan met lezen</a>'
                '</nav>'
                '<a class="buttonAlle" href="/artikelen/index.html">Alle artikelen</a>'
            )
            parts.append(render_article(a, extra_class="featured-artikel", prepend_html=prepend, append_html=append))

        # 3. Remaining berichten
        for b in berichten[1:3]:
            parts.append(render_article(b))

        parts.append('</div>')
        return "\n".join(parts)