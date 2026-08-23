#!/usr/bin/env python3
"""Convert org-roam :ref: articles into blog Markdown posts.

Usage:
  python3 import_org_roam.py --limit 10 --out /path/to/outdir [--src /path/to/org-roam]

Only files whose #+filetags line contains :ref: are considered. Files that,
after stripping drawers/citations/headings, contain no real prose are skipped
(these are bare bookmark stubs with no AI summary).
"""
import argparse
import re
import sys
from pathlib import Path

FILENAME_RE = re.compile(r'^(\d{14})-(.+)\.org$')
TITLE_RE = re.compile(r'^#\+title:\s*(.+)$', re.IGNORECASE)
AUTHOR_RE = re.compile(r'^#\+author:\s*(.+)$', re.IGNORECASE)
FILETAGS_RE = re.compile(r'^#\+filetags:\s*(.+)$', re.IGNORECASE)
ROAM_REFS_RE = re.compile(r'^:ROAM_REFS:\s*(.+)$', re.IGNORECASE)
DRAWER_RE = re.compile(r'^[ \t]*:[A-Za-z_]+:\n(?:.*\n)*?[ \t]*:END:\n?', re.MULTILINE | re.IGNORECASE)
ATTACHMENT_LINK_RE = re.compile(r'\[\[attachment:[^\]]*\](?:\[[^\]]*\])?\]')
ORG_KEYWORD_LINE_RE = re.compile(r'^[ \t]*#\+[A-Za-z_`]*:.*\n?', re.MULTILINE)
LOCAL_PATH_LINE_RE = re.compile(r'^[ \t]*.*(?:/Users/[a-zA-Z0-9_.-]+|/Volumes/[A-Za-z0-9_. -]+).*\n?', re.MULTILINE)
HEADLINE_TODO_RE = re.compile(r'^(TODO|DONE|NEXT|WAITING|CANCELLED|SOMEDAY)\s+')
CITATION_RE = re.compile(r'\s*<citation[^>]*>[^<]*</citation>')
COMMENT_BLOCK_RE = re.compile(r'^[ \t]*#\+begin_comment\n(?:.*\n)*?[ \t]*#\+end_comment\n?', re.MULTILINE | re.IGNORECASE)
QUOTE_BLOCK_RE = re.compile(r'^[ \t]*#\+begin_quote\n((?:.*\n)*?)[ \t]*#\+end_quote\n?', re.MULTILINE | re.IGNORECASE)
SRC_BLOCK_RE = re.compile(r'^[ \t]*#\+begin_src\s*\w*\n((?:.*\n)*?)[ \t]*#\+end_src\n?', re.MULTILINE | re.IGNORECASE)
OTHER_BLOCK_RE = re.compile(r'^[ \t]*#\+begin_(\w+)[^\n]*\n((?:.*\n)*?)[ \t]*#\+end_\1\n?', re.MULTILINE | re.IGNORECASE)
# link description allows one level of nested [...] (e.g. "[[id:x][[course] Title]]")
_LINK_DESC = r'((?:[^\[\]]|\[[^\[\]]*\])*)'
ORG_ID_LINK_RE = re.compile(r'\[\[id:[A-Za-z0-9-]+\]\[' + _LINK_DESC + r'\]\]')
ORG_BARE_ID_LINK_RE = re.compile(r'\[\[id:[A-Za-z0-9-]+\]\]')
ORG_URL_LINK_RE = re.compile(r'\[\[(https?://[^\]]+)\]\[' + _LINK_DESC + r'\]\]')
ORG_BARE_URL_RE = re.compile(r'\[\[(https?://[^\]]+)\]\]')
HEADLINE_RE = re.compile(r'^(\*+)\s+(.*)$', re.MULTILINE)
HEADLINE_TAGS_RE = re.compile(r'\s+:[A-Za-z0-9_@:]+:\s*$')
URL_IN_REFS_RE = re.compile(r'https?://\S+')


def clean_org_links(s: str) -> str:
    s = ORG_ID_LINK_RE.sub(r'\1', s)
    s = ORG_BARE_ID_LINK_RE.sub('', s)
    s = ORG_URL_LINK_RE.sub(r'[\2](\1)', s)
    s = ORG_BARE_URL_RE.sub(r'<\1>', s)
    return s


def parse_file(path: Path):
    m = FILENAME_RE.match(path.name)
    if not m:
        return None
    ts, slug_raw = m.group(1), m.group(2)
    text = path.read_text(encoding='utf-8', errors='replace')
    lines = text.split('\n')

    title = None
    author = None
    filetags = None
    roam_refs_line = None
    body_start = 0

    for i, line in enumerate(lines):
        if title is None:
            tm = TITLE_RE.match(line)
            if tm:
                title = tm.group(1).strip()
                continue
        if author is None:
            am = AUTHOR_RE.match(line)
            if am:
                author = am.group(1).strip()
                continue
        if filetags is None:
            fm = FILETAGS_RE.match(line)
            if fm:
                filetags = fm.group(1).strip()
                body_start = i + 1
                continue
        rm = ROAM_REFS_RE.match(line)
        if rm:
            roam_refs_line = rm.group(1).strip()

    if filetags is None:
        return None
    tags = [t for t in filetags.split(':') if t]
    if 'ref' not in tags:
        return None
    extra_tags = [t for t in tags if t != 'ref']

    if title:
        title = clean_org_links(title)

    if author:
        author = clean_org_links(author).strip()
        author = author or None

    source_url = None
    if roam_refs_line:
        urls = URL_IN_REFS_RE.findall(roam_refs_line)
        if urls:
            # org-roam sometimes quotes refs and leaves a trailing \" artifact
            source_url = re.sub(r'[\\"]+$', '', urls[0])

    body_raw = '\n'.join(lines[body_start:])

    # Strip PROPERTIES drawers (per-headline metadata, not content)
    body = DRAWER_RE.sub('', body_raw)
    # Strip private annotation blocks (not meant for publication)
    body = COMMENT_BLOCK_RE.sub('', body)
    # #+begin_quote/#+end_quote -> markdown blockquote
    def quote_sub(m):
        inner = m.group(1).rstrip('\n')
        return '\n'.join('> ' + l if l else '>' for l in inner.split('\n')) + '\n'
    body = QUOTE_BLOCK_RE.sub(quote_sub, body)
    # #+begin_src/#+end_src -> fenced code block
    def src_sub(m):
        inner = m.group(1).rstrip('\n')
        return '```\n' + inner + '\n```\n'
    body = SRC_BLOCK_RE.sub(src_sub, body)
    # any other #+begin_X/#+end_X block (verse, example, center, ...) -> unwrap, keep inner text
    def other_block_sub(m):
        return m.group(2)
    body = OTHER_BLOCK_RE.sub(other_block_sub, body)
    # local screenshot/file attachments have no target in the blog
    body = ATTACHMENT_LINK_RE.sub('', body)
    # stray org buffer keywords (#+ATTR_ORG:, #+DOWNLOADED:, ...) - not content
    body = ORG_KEYWORD_LINE_RE.sub('', body)
    # safety net: drop any remaining line referencing a local filesystem path
    body = LOCAL_PATH_LINE_RE.sub('', body)
    # Strip citation markers e.g. <citation>9</citation> or <citation type="image">...</citation>
    body = CITATION_RE.sub('', body)
    # org links -> markdown / plain text
    body = clean_org_links(body)

    # org headlines "* TODO Heading :tags:" -> markdown heading, shifted one
    # level down (post title already serves as the h1), TODO state and tags
    # stripped.
    def heading_sub(m):
        stars, rest = m.group(1), m.group(2)
        rest = HEADLINE_TAGS_RE.sub('', rest)
        rest = HEADLINE_TODO_RE.sub('', rest)
        level = min(len(stars) + 1, 6)
        return ('#' * level) + ' ' + rest.strip()

    body = HEADLINE_RE.sub(heading_sub, body)

    # tabs -> 2 spaces (keeps nested org bullets from being read as code blocks)
    body = body.replace('\t', '  ')
    # collapse 3+ blank lines
    body = re.sub(r'\n{3,}', '\n\n', body).strip('\n')

    # drop a leading heading that just repeats the post title (the layout
    # already renders the title as h1)
    if title:
        norm_title = re.sub(r'[^a-z0-9一-鿿]+', '', title.lower())
        body_lines = body.split('\n')
        if body_lines and body_lines[0].startswith('#'):
            heading_text = body_lines[0].lstrip('#').strip()
            norm_heading = re.sub(r'[^a-z0-9一-鿿]+', '', heading_text.lower())
            if norm_heading == norm_title:
                body = '\n'.join(body_lines[1:]).lstrip('\n')

    # content check: strip headings/blank lines, see if any prose remains
    prose = '\n'.join(
        l for l in body.split('\n')
        if l.strip() and not l.strip().startswith('#')
    )
    if len(prose) < 40:
        return None

    description = None
    for l in body.split('\n'):
        s = l.strip().lstrip('-').strip()
        if not s or s.startswith('#') or s.startswith('```') or s == '>':
            continue
        s = s.lstrip('>').strip()
        if s:
            description = s
            break
    if description:
        description = re.sub(r'\*\*|\*|`', '', description).strip()
        if len(description) > 160:
            description = description[:157].rstrip() + '...'
        if not description:
            description = None

    year, mon, day, hh, mm, ss = ts[0:4], ts[4:6], ts[6:8], ts[8:10], ts[10:12], ts[12:14]
    iso_date = f'{year}-{mon}-{day}T{hh}:{mm}:{ss}Z'

    return {
        'ts': ts,
        'iso_date': iso_date,
        'title': title or slug_raw,
        'author': author,
        'category': extra_tags[0] if extra_tags else 'reading',
        'description': description,
        'source_url': source_url,
        'body': body,
        'slug_raw': slug_raw,
        'orig_path': str(path),
    }


def slugify(text: str, fallback: str) -> str:
    s = text.lower()
    s = re.sub(r"[’'\"]", '', s)
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = re.sub(r'-{2,}', '-', s).strip('-')
    return s or fallback


def yaml_escape(s: str) -> str:
    return s.replace('\\', '\\\\').replace('"', '\\"')


def write_post(entry, out_dir: Path, used_slugs: set):
    base_slug = slugify(entry['title'], fallback=f'post-{entry["ts"]}')
    slug = base_slug
    n = 2
    while slug in used_slugs:
        slug = f'{base_slug}-{n}'
        n += 1
    used_slugs.add(slug)

    fm = ['---']
    fm.append(f'title: "{yaml_escape(entry["title"])}"')
    fm.append(f'date: {entry["iso_date"]}')
    fm.append(f'category: {entry["category"]}')
    if entry['author']:
        fm.append(f'author: "{yaml_escape(entry["author"])}"')
    if entry['description']:
        fm.append(f'description: "{yaml_escape(entry["description"])}"')
    if entry['source_url']:
        fm.append(f'source: "{entry["source_url"]}"')
    fm.append('---')
    content = '\n'.join(fm) + '\n\n' + entry['body'] + '\n'

    out_path = out_dir / f'{slug}.md'
    out_path.write_text(content, encoding='utf-8')
    return out_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', default='/Volumes/Dev/SynologyDrive/OrgMode/org-roam')
    ap.add_argument('--out', required=True)
    ap.add_argument('--limit', type=int, default=None)
    ap.add_argument('--list-file', default=None,
                     help='optional file with explicit list of org filenames to convert (one per line)')
    args = ap.parse_args()

    src = Path(args.src)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.list_file:
        names = [l.strip() for l in Path(args.list_file).read_text().splitlines() if l.strip()]
        paths = [src / n for n in names]
    else:
        paths = sorted(src.glob('*.org'))

    entries = []
    skipped_no_ref = 0
    skipped_no_content = 0
    skipped_bad_name = 0

    for p in paths:
        parsed_name = FILENAME_RE.match(p.name)
        if not parsed_name:
            skipped_bad_name += 1
            continue
        entry = parse_file(p)
        if entry is None:
            has_ref = False
            for line in p.read_text(encoding='utf-8', errors='replace').split('\n'):
                fm = FILETAGS_RE.match(line)
                if fm and 'ref' in [t for t in fm.group(1).strip().split(':') if t]:
                    has_ref = True
                    break
            if has_ref:
                skipped_no_content += 1
            else:
                skipped_no_ref += 1
            continue
        entries.append(entry)

    entries.sort(key=lambda e: e['ts'])
    if args.limit:
        entries = entries[:args.limit]

    used_slugs = set()
    for e in entries:
        out_path = write_post(e, out_dir, used_slugs)
        print(f'{e["ts"]}  ->  {out_path.name}   [{e["category"]}]  {e["title"]}')

    print(f'\nwrote {len(entries)} posts to {out_dir}')
    print(f'skipped (no ref tag): {skipped_no_ref}, skipped (no real content): {skipped_no_content}, skipped (bad filename): {skipped_bad_name}')


if __name__ == '__main__':
    main()
