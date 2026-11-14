#!/usr/bin/env python3
"""每日健康检查：只查官方文档页是否 200，不做真实 API 调用。
真实调用额度 / 延迟另外跑 scripts/probe.py（家里 200.5 用 DoH 取真实 IP，绕开 mihomo fake-ip）。
输出：public/health.json，页面可直接读。
"""
import json, urllib.request, ssl
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "src/data/apis.json").read_text(encoding="utf-8"))
out = {"date": str(date.today()), "checks": []}
ctx = ssl.create_default_context()
for cat in data["categories"]:
    for item in cat["items"]:
        url = item["docs"]
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "free-api-directory-health/0.1"})
            with urllib.request.urlopen(req, timeout=15, context=ctx) as r:
                status = r.status
        except Exception as e:
            status = f"ERR {type(e).__name__}: {e}"
        out["checks"].append({"category": cat["slug"], "name": item["name"], "docs": url, "status": status})
        print(cat["slug"], item["name"], status)
(ROOT / "public/health.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("wrote public/health.json")
