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
