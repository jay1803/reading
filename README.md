# Reading

A minimal blog built with [Astro](https://astro.build) and GitHub Pages. Posts are Markdown
files with frontmatter; there's no database or CMS.

## Writing a post

Add a new file to `src/content/posts/`:

```md
---
title: Post title
date: 2026-08-15
category: notes
description: Optional one-line summary.
---

Body in Markdown.
```

Push to `main` and the GitHub Actions workflow builds and deploys automatically.

## Local development

```bash
npm install
npm run dev
```

## Deployment

Deployment runs via [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) on every
push to `main`. In the repo settings, set **Pages → Build and deployment → Source** to
**GitHub Actions**.

## Importing from org-roam

[`scripts/import_org_roam.py`](scripts/import_org_roam.py) converts org-roam nodes tagged
`:ref:` (saved articles with an AI-written summary) into posts here. It skips bare bookmarks
with no summary body, strips org-only syntax (drawers, citation markers, id-links, local
attachment references), and carries over the original tag as `category` when the node has one
beyond `:ref:` itself.

```bash
python3 scripts/import_org_roam.py --out src/content/posts --limit 10   # dry run on a few files
python3 scripts/import_org_roam.py --out src/content/posts              # full import
```

Known limitations: embedded screenshots/attachments aren't copied over (the reference is
dropped, not broken), and a handful of source files have typo'd `<citation>` tags that survive
as literal text.
