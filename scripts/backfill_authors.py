#!/usr/bin/env python3
"""Backfill the `author` frontmatter field for posts whose source domain is
known to be a single-author blog/newsletter, using scripts/domain_author_map.json.

Only touches posts that:
  - have a `source:` URL
  - do NOT already have an `author:` field
  - whose source hostname (www-stripped) is a key in the map

Usage:
  python3 scripts/backfill_authors.py --posts src/content/posts --map scripts/domain_author_map.json --dry-run
  python3 scripts/backfill_authors.py --posts src/content/posts --map scripts/domain_author_map.json
"""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse

SOURCE_RE = re.compile(r'^source:\s*"(.+)"\s*$', re.MULTILINE)
AUTHOR_RE = re.compile(r'^author:', re.MULTILINE)
CATEGORY_RE = re.compile(r'^(category:.*)$', re.MULTILINE)


def yaml_escape(s: str) -> str:
    return s.replace('\\', '\\\\').replace('"', '\\"')


def get_domain(url: str):
    try:
        host = urlparse(url).hostname or ''
        return host[4:] if host.startswith('www.') else host
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--posts', required=True)
    ap.add_argument('--map', required=True)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    domain_map = json.loads(Path(args.map).read_text(encoding='utf-8'))
    posts_dir = Path(args.posts)

    updated = 0
    per_domain = {}
    for path in sorted(posts_dir.glob('*.md')):
        text = path.read_text(encoding='utf-8')
        if AUTHOR_RE.search(text):
            continue
        m = SOURCE_RE.search(text)
        if not m:
            continue
        domain = get_domain(m.group(1))
        if not domain or domain not in domain_map:
            continue
        author = domain_map[domain]

        if args.dry_run:
            per_domain[domain] = per_domain.get(domain, 0) + 1
            updated += 1
            continue

        # Insert `author:` right after the `category:` line to match the
        # frontmatter field order used elsewhere in the repo.
        new_text, n = CATEGORY_RE.subn(
            lambda cm: cm.group(1) + f'\nauthor: "{yaml_escape(author)}"', text, count=1
        )
        if n == 0:
            # no category line (shouldn't happen) - skip safely
            continue
        path.write_text(new_text, encoding='utf-8')
        per_domain[domain] = per_domain.get(domain, 0) + 1
        updated += 1

    for d, c in sorted(per_domain.items(), key=lambda x: -x[1]):
        print(f'{c:4d}  {d}')
    print(f'\n{"[dry-run] " if args.dry_run else ""}updated {updated} posts across {len(per_domain)} domains')


if __name__ == '__main__':
    main()
