import fs from 'node:fs';
import path from 'node:path';

const CJK_RE = /[一-鿿぀-ヿ가-힯]/g;
const CONTENT_DIR = path.join(process.cwd(), 'src/content/posts');

function stripFrontmatter(raw: string): string {
  const parts = raw.split('---\n');
  return parts.length > 2 ? parts.slice(2).join('---\n') : raw;
}

export function estimateReadingTime(postId: string): string {
  let raw: string;
  try {
    raw = fs.readFileSync(path.join(CONTENT_DIR, `${postId}.md`), 'utf-8');
  } catch {
    return '1 min read';
  }
  const body = stripFrontmatter(raw);
  const cjkCount = (body.match(CJK_RE) || []).length;
  const wordCount = (body.replace(CJK_RE, ' ').match(/\S+/g) || []).length;
  const minutes = Math.max(1, Math.round(wordCount / 235 + cjkCount / 400));
  return `${minutes} min read`;
}
