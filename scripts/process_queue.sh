#!/bin/bash
# Runs hourly via cron. Picks the first pending URL in queue.md, summarizes
# it into a new post, and publishes (commit + push). Fully unattended:
# scoped to a narrow tool allow-list rather than bypassing permissions
# entirely.
set -euo pipefail

REPO_DIR="/Volumes/Dev/Github/playground/reading"
cd "$REPO_DIR"

if ! grep -q '^- \[ \] ' queue.md; then
  echo "$(date -u +%FT%TZ) - queue empty, nothing to do"
  exit 0
fi

PROMPT="Read queue.md at the repo root. Take the FIRST line matching '- [ ] <url>'.

1. Fetch and read the article at that URL.
2. Write a new post file to src/content/posts/<slug>.md. Look at a couple of
   existing files in that directory first to match their exact frontmatter
   shape (title, date, category, description, source) and body style
   (structured with a few markdown headings, written in the same language as
   the source article, a genuine summary — not placeholder text). date should
   be the current UTC time in the same ISO 8601 format other posts use.
   category should be a single reasonable lowercase word inferred from the
   content (fall back to \"reading\" if nothing fits). source must be the
   exact URL processed. IMPORTANT: every frontmatter value is a
   double-quoted YAML string — if title or description need to quote a
   phrase, use curly quotes (“ ”) instead of straight \" characters,
   since a literal \" inside the value breaks YAML parsing and fails the
   build.
3. Remove that one line from queue.md. Leave every other line untouched.
4. Run \`npm run build\` to confirm the site still builds — this is not
   optional, it's the only check that catches broken frontmatter. If it
   fails, find and fix the actual problem (do not skip this step or commit
   with a failing build).
5. git add the new post and the updated queue.md, then:
   git commit --no-gpg-sign -m \"<a short commit message describing the new post>\"
   git push origin main

If queue.md has no '- [ ] ' lines, do nothing and exit."

claude -p "$PROMPT" \
  --permission-mode acceptEdits \
  --allowedTools "Read,Write,Edit,Glob,Grep,WebFetch,Bash(git add:*),Bash(git commit:*),Bash(git push:*),Bash(npm run build:*)" \
  --output-format text
