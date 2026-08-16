import { defineConfig } from 'astro/config';
import rehypePangu from './src/lib/rehype-pangu.mjs';

export default defineConfig({
  site: 'https://read.maxoxo.me',
  markdown: {
    rehypePlugins: [rehypePangu],
  },
  build: {
    inlineStylesheets: 'always',
  },
});
