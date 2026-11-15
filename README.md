# 免费 API 目录

免费 API 的额度、Key、绑卡、国内直连、商用，一张表讲清。

- 线上：https://freeapi.anemy.org/
- 8 类，79 个 API，90 页：8 张分类表 + 79 个详情页（`/api/<slug>/`）+ 2 篇横评（`/guides/weather/`、`/guides/llm/`）

| 分类 | 页面 | 条数 |
|---|---|---|
| 免费大模型 API 国内能用 | `/llm/` | 16 |
| 免费天气 API 国内能用 | `/weather/` | 8 |
| 免费股票 / 金融 API | `/stock/` | 13 |
| 免费地图 API 高德 百度 免费额度 | `/maps/` | 9 |
| 免费 IP 归属地 / 快递查询 API | `/ip-express/` | 3 |
| 免费开发 / 测试 API | `/dev/` | 8 |
| 免费图片 / 媒体 / 新闻 API | `/media/` | 15 |
| 国内 API 聚合市场 | `/china/` | 7 |

数据在 `src/data/apis.json`，每条带额度 / Key / 绑卡 / 国内直连 / 商用 / 来源。查不到的写“未查到，以官方文档为准”，不编数字。

## 本地跑

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # 输出 dist/
python3 scripts/health_check.py   # 生成 public/health.json
```

## 部署

已上线：Cloudflare Pages 项目 `free-api-directory`，连这个仓库自动部署，生产域名 `freeapi.anemy.org`（生产环境，2026-11-14 绑好）。Build command: `npm run build`，Output directory: `dist`。

## 收录

- Google Search Console：2026-11-14 域名已验证，sitemap `https://freeapi.anemy.org/sitemap-index.xml` 提交成功。每周四查一次点击/曝光汇总。
- 百度搜索资源平台：暂不做。

## 每日健康检查

`.github/workflows/health-check.yml` 每天 09:00 北京时间跑 `scripts/health_check.py`，只查官方文档页是否 200，写回 `public/health.json`。2026-11-15 首次手动触发已跑通（1 分 20 秒）。真实 API 调用 / 延迟另外跑，不在这里烧额度。

## 中国访问慢怎么办（按顺序，别跳步）

1. 先测 17ce / chinaz，国内延迟普遍 >250ms 再动。
2. 过渡：腾讯 EdgeOne 前置（源站海外时实名即可，不用 ICP 备案），有人实测 300ms+ → 30-40ms。
3. 做起来后（月自然点击 >1,000）：阿里云 / 腾讯云轻量服务器 1核2G 3M，¥50-80/月 + ICP 备案 7-20 工作日，备案号放页脚，30 天内做公安备案。

## 千万别放家里

200.3 / 200.5 不适合放公网站：动态 IP、停电就断、mihomo fake-ip 会把活 API 误判成死（2026-11-14 实测 Open-Meteo / CoinGecko）。家里只做“国内直连延迟”抽测，方法：DoH（223.5.5.5）取真实 IP 再 `curl --resolve`。

## 止损线

上线 90 天，自然搜索点击 <1,000/月，就停 / 只做最小维护。
