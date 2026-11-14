import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// 域名已定：https://freeapi.anemy.org（2026-11-14 用户确认）
// anemy.org 已在 Cloudflare，freeapi 子域此前无解析，空闲可用。
// ai.anemy.org / api.anemy.org 已占用，勿动。
export default defineConfig({
  site: 'https://freeapi.anemy.org',
  integrations: [sitemap()],
});
