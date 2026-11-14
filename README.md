# 免费 API 目录 — MVP 骨架

只做 5 张中文对比表（Tier 1 长尾词），不做 2,388 条大列表。

| 页面 | 关键词 |
|---|---|
| `/llm/` | 免费大模型 API 国内能用 免 Key 不用绑卡 |
| `/weather/` | 免费天气 API 国内能用 免 Key |
| `/stock/` | 免费股票 API / A股行情 API |
| `/maps/` | 免费地图 API 高德 百度 免费额度 |
| `/ip-express/` | 免费 IP 归属地 / 快递查询 API |

数据在 `src/data/apis.json`，每条带额度 / Key / 绑卡 / 国内直连 / 商用 / 来源 / 核实日期。

## 本地跑

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # 输出 dist/
python3 scripts/health_check.py   # 生成 public/health.json
```

## 部署到 Cloudflare Pages（推荐 MVP）

1. 推到 GitHub 新仓库。
2. Cloudflare Dashboard → Workers & Pages → Create → Pages → Connect to Git → 选这个仓库。
3. Build command: `npm run build`，Output directory: `dist`，Node 20+。
4. **绑自定义域名**（别用 `xxx.pages.dev`，国内 DNS 污染不稳）。
   域名先在阿里云 / 腾讯云买 `.com`，以后要备案注册商必须在工信部白名单。
5. 上线后在 Google Search Console + 百度站长平台提交 sitemap：`https://freeapi.anemy.org/sitemap-index.xml`。

## 中国访问慢怎么办（按顺序，别跳步）

1. 先测 17ce / chinaz，国内延迟普遍 >250ms 再动。
2. 过渡：腾讯 EdgeOne 前置（源站海外时实名即可，不用 ICP 备案），有人实测 300ms+ → 30-40ms。
3. 做起来后（月自然点击 >1,000）：阿里云 / 腾讯云轻量服务器 1核2G 3M，¥50-80/月 + ICP 备案 7-20 工作日，备案号放页脚，30 天内做公安备案。

## 千万别放家里

200.3 / 200.5 不适合放公网站：动态 IP、停电就断、mihomo fake-ip 会把活 API 误判成死（2026-11-14 实测 Open-Meteo / CoinGecko）。家里只做“国内直连延迟”抽测，方法：DoH（223.5.5.5）取真实 IP 再 `curl --resolve`。

## 每日健康检查

`.github/workflows/health-check.yml` 每天 09:00 北京时间跑 `scripts/health_check.py`，只查官方文档页是否 200，写回 `public/health.json`。真实 API 调用 / 延迟另外跑，不在这里烧额度。

## 止损线

5 页上线 90 天，自然搜索点击 <1,000/月 或 Pro 等待列表 <10 人，就停 / 只做最小维护。
