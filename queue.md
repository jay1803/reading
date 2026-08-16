# Reading queue

Add one URL per line as `- [ ] <url>`. The hourly job (`scripts/process_queue.sh`)
picks the first pending line, reads and summarizes it, publishes a post, and
removes the line here. This file is only ever meant to hold *pending* items —
once something's published it lives in `src/content/posts/` instead.
