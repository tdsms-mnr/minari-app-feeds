#!/usr/bin/env python3
"""すべてのアプリを並べる親ページ（/ と /ja/）を書き出す。2026-11-23。

載せるのは App Store で公開中のアプリだけ（2026-11-23 に iTunes の lookup で US・JP とも確認した17本）。
並びは累計DLの多い順（監査_推移.md §0）。新しいアプリが公開されたら APPS に1行足して流し直す。
使い方：python3 build_index.py
"""
import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://tdsms-mnr.github.io/minari-app-feeds/"

# (フォルダ, 店頭の名前, 英語の一言, 日本語の一言)
APPS = [
    ("savebar", "Savebar", "Savings goals, as a widget", "貯金の目標をホーム画面に"),
    ("datto", "Datto", "Count down to big days", "あと何日をホーム画面に"),
    ("kotoba", "Kotoba", "Your words, as a widget", "好きな言葉をホーム画面に"),
    ("mantel", "Mantel", "Your photos, as a widget", "好きな写真をホーム画面に"),
    ("bookspine", "Bookspine", "Your reads, as a widget", "読んだ本をホーム画面に"),
    ("museday", "Museday", "A painting a day, as a widget", "毎日1枚の名画をホーム画面に"),
    ("todayboard", "Todayboard", "Calendars, kept separate", "カレンダーを分けて表示"),
    ("threeline", "Threeline", "Three things today", "今日の3つをホーム画面に"),
    ("leafday", "Leafday", "Which plants need water today", "今日水をやる鉢をホーム画面に"),
    ("feelboard", "Feelboard", "A year of moods in one picture", "1年の気分を1枚の絵に"),
    ("weeklybump", "Petalweek", "Your pregnancy week, as a widget", "妊娠週数をホーム画面に"),
    ("rowmark", "Rowmark", "Count rows on the Lock Screen", "編み物の段数をロック画面で"),
    ("nightwick", "Nightwick", "Tonight's candle, from your shelf", "手元の棚から、今夜の1本を"),
    ("driftfall", "Driftfall", "Snow and petals on your photos", "自分の写真に雪と花びらを"),
    ("classicallog", "ClassicalLog", "A journal for classical concerts", "クラシック演奏会の記録"),
    ("slowdial", "Slowdial", "A timer you can watch shrink", "減っていく円盤のタイマー"),
    ("farwalk", "Farwalk", "Walk the real distance to someone", "誰かのところまで、実際の距離を歩く"),
]

T = {
    "en": dict(lang="en", up="", other=("ja/", "日本語"),
               title="minari — small apps for iPhone",
               desc="Small apps for iPhone by minari. No ads in any of them.",
               h1="Small apps for iPhone.",
               sub="No ads in any of them.",
               contact="Contact: "),
    "ja": dict(lang="ja", up="../", other=("../", "English"),
               title="minari — iPhoneの小さなアプリ",
               desc="minariが作るiPhoneの小さなアプリ。どれも広告なし。",
               h1='<span class="nb">iPhoneの、</span><span class="nb">小さなアプリ。</span>',
               sub="どれも広告なし。",
               contact="お問い合わせ："),
}

CSS = """
  :root { --bg:#F4F0EB; --surface:#FFFDFB; --ink:#2B2A28; --dim:#7D7A75; --track:#E4DED6; }
  @media (prefers-color-scheme: dark) { :root { --bg:#1F1E1D; --surface:#2B2A28; --ink:#EDE9E4; --dim:#A6A29C; --track:#34322F; } }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--bg); color:var(--ink);
         font-family:-apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans", sans-serif;
         -webkit-font-smoothing:antialiased; line-height:1.6; }
  a { color:inherit; }
  .wrap { max-width:1120px; margin:0 auto; padding:0 24px; }
  header { display:flex; justify-content:space-between; align-items:center; padding-top:32px; }
  .nb { display:inline-block; }
  .mark { font-weight:600; font-size:17px; text-decoration:none; }
  .lang { font-size:14px; color:var(--dim); text-decoration:none; }
  .hero { padding:96px 0 64px; }
  h1 { font-size:52px; line-height:1.15; font-weight:700; letter-spacing:-0.03em; margin:0 0 16px; }
  .sub { font-size:18px; color:var(--dim); margin:0; }
  .apps { list-style:none; margin:0; padding:0 0 96px; display:grid; grid-template-columns:repeat(3, 1fr); gap:16px; }
  .apps a { display:flex; gap:16px; align-items:center; background:var(--surface); border-radius:24px;
            padding:20px 24px 20px 20px; text-decoration:none; height:100%; transition:transform .2s ease; }
  .apps a:hover { transform:translateY(-2px); }
  .apps img { width:64px; height:64px; border-radius:15px; flex:none; box-shadow:0 0 0 0.5px rgba(0,0,0,.08); }
  .apps b { display:block; font-weight:600; font-size:17px; }
  .apps span span { display:block; color:var(--dim); font-size:15px; line-height:1.4; }
  footer { border-top:1px solid var(--track); padding:32px 0 48px; color:var(--dim); font-size:14px;
           display:flex; flex-wrap:wrap; gap:8px 24px; justify-content:space-between; }
  @media (max-width: 900px) { .apps { grid-template-columns:repeat(2, 1fr); } }
  @media (max-width: 600px) {
    .wrap { padding:0 16px; }
    .hero { padding:64px 0 48px; }
    h1 { font-size:36px; }
    .apps { grid-template-columns:1fr; gap:12px; padding-bottom:64px; }
  }
  :lang(ja) h1 { letter-spacing:0.01em; line-height:1.35; font-size:46px; }
  @media (max-width: 600px) { :lang(ja) h1 { font-size:32px; } }
  :lang(ja) body { word-break:auto-phrase; }
"""


def page(t):
    e = html.escape
    rows = []
    for folder, name, en, ja in APPS:
        has_ja = os.path.exists(os.path.join(HERE, "apps", folder, "ja", "index.html"))
        href = f"{t['up']}apps/{folder}/" + ("ja/" if t["lang"] == "ja" and has_ja else "")
        line = en if t["lang"] == "en" else ja
        rows.append(f'  <li><a href="{href}"><img src="{t["up"]}icons/{folder}.png" alt="" loading="lazy">'
                    f'<span><b>{name}</b><span>{e(line)}</span></span></a></li>')
    url = BASE + ("" if t["lang"] == "en" else "ja/")
    return f"""<!doctype html>
<html lang="{t['lang']}">
<meta charset="utf-8">
<script src="/minari-app-feeds/legacy-notice.js" defer></script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{BASE}">
<link rel="alternate" hreflang="ja" href="{BASE}ja/">
<link rel="alternate" hreflang="x-default" href="{BASE}">
<style>{CSS}</style>

<div class="wrap">
<header><a class="mark" href="{t['up'] or './'}">minari</a><a class="lang" href="{t['other'][0]}">{t['other'][1]}</a></header>
<section class="hero">
  <h1>{t['h1']}</h1>
  <p class="sub">{e(t['sub'])}</p>
</section>
<ul class="apps">
{chr(10).join(rows)}
</ul>
<footer><span>{t['contact']}minariapps@gmail.com</span><span>© 2026 minari</span></footer>
</div>
"""


for lang, t in T.items():
    d = HERE if lang == "en" else os.path.join(HERE, "ja")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(page(t))
    print("wrote", os.path.relpath(os.path.join(d, "index.html"), HERE))
