# Readar

An installable reading web app built with [Astro](https://astro.build) and GitHub Pages. Posts
are Markdown files with frontmatter; there's no database or CMS.

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

## Offline reading

The site saves the newest 50 posts and the archive pages containing them in your browser
when you first open it online. After that, these pages load from local storage even without
an internet connection. When you scroll to older entries online, their archive page and
individual post pages are saved too. The **Refresh** button downloads the current newest 50
posts and archive pages, then reloads the page.

Offline reading requires a browser with service worker support and an initial online visit.
Browser storage can be cleared or evicted by the device, and links to external source sites
still require a connection. To change the number of recent posts, update
`OFFLINE_POST_COUNT` in `src/pages/offline-manifest.json.ts`.

## Install as a web app

Open Readar over HTTPS, then use your browser's **Install app** or **Add to Home Screen**
action. It opens in a standalone window and keeps the same offline reading cache.

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
