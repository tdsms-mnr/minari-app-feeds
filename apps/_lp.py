"""アプリ公式ページ（Savebar 型）の共通の型。2026-11-23。

各アプリの build_pages.py が APP（共通の設定）と T（言語ごとの文言）を渡して build() を呼ぶ。
ページの並び：ナビ → ヒーロー → ひとこと → 画面つきの節（交互） → 料金 → よくある質問 → ほかのアプリ → 締め → フッター。
英語は apps/<slug>/、日本語は apps/<slug>/ja/。本名は入れない（Made by minari）。
"""
import html
import json
import os

ROOT = "https://tdsms-mnr.github.io/minari-app-feeds/"

# ほかのアプリの一言（親ページ build_index.py と同じ文言）
XLINE = {
    "en": {"savebar": "Savings goals, as a widget", "datto": "Count down to big days", "kotoba": "Your words, as a widget",
           "mantel": "Your photos, as a widget", "bookspine": "Your reads, as a widget", "museday": "A painting a day, as a widget",
           "todayboard": "Calendars, kept separate", "rowmark": "Count rows on the Lock Screen",
           "nightwick": "Tonight's candle, from your shelf", "driftfall": "Snow and petals on your photos"},
    "ja": {"savebar": "貯金の目標をホーム画面に", "datto": "あと何日をホーム画面に", "kotoba": "好きな言葉をホーム画面に",
           "mantel": "好きな写真をホーム画面に", "bookspine": "読んだ本をホーム画面に", "museday": "毎日1枚の名画をホーム画面に",
           "todayboard": "カレンダーを分けて表示", "rowmark": "編み物の段数をロック画面で",
           "nightwick": "手元の棚から、今夜の1本を", "driftfall": "自分の写真に雪と花びらを"},
}
XNAME = {"savebar": "Savebar", "datto": "Datto", "kotoba": "Kotoba", "mantel": "Mantel", "bookspine": "Bookspine",
         "museday": "Museday", "todayboard": "Todayboard", "rowmark": "Rowmark", "nightwick": "Nightwick", "driftfall": "Driftfall"}

UI = {
    "en": dict(pricing="Pricing, plainly", free="Free", faq_h="Questions people ask", xapps_h="More apps", all_apps="All apps",
               badge_alt="Download on the App Store", priv_word="Privacy Policy", ios="iOS 17 or later",
               langs='<b>English</b> · <a href="ja/" hreflang="ja">日本語</a>'),
    "ja": dict(pricing="料金のこと", free="無料", faq_h="よくある質問", xapps_h="ほかのアプリ", all_apps="すべてのアプリ",
               badge_alt="App Storeからダウンロード", priv_word="プライバシーポリシー", ios="iOS 17以降",
               langs='<a href="../" hreflang="en">English</a> · <b>日本語</b>'),
}

CSS = """
  :root { %(light)s }
  @media (prefers-color-scheme: dark) {
    :root { %(dark)s }
  }
  * { box-sizing: border-box; }
  body { margin:0; background:var(--bg); color:var(--ink);
         font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans", sans-serif;
         -webkit-font-smoothing: antialiased; line-height:1.6; }
  a { color:var(--accent); }
  .wrap { max-width:1120px; margin:0 auto; padding:0 24px; }
  .nav { position:sticky; top:12px; z-index:2; display:flex; justify-content:center; padding:0 16px; }
  .nav-inner { display:flex; align-items:center; gap:10px; padding:8px 18px 8px 10px; border-radius:999px;
               background:color-mix(in srgb, var(--surface) 80%%, transparent); backdrop-filter:blur(12px);
               box-shadow:0 1px 8px rgba(0,0,0,.06); font-weight:600; font-size:15px; }
  .nav img { width:28px; height:28px; border-radius:7px; }
  .nav .lang { font-weight:400; font-size:14px; color:var(--dim); text-decoration:none; margin-left:8px; }
  .hero { display:grid; grid-template-columns:1.1fr .9fr; gap:56px; align-items:center; padding-top:56px; padding-bottom:80px; }
  h1 { font-size:52px; line-height:1.15; font-weight:700; letter-spacing:-0.03em; margin:0 0 24px; }
  .lead { color:var(--accent); }
  .sub { font-size:18px; color:var(--dim); margin:0 0 32px; max-width:30em; }
  .badge { display:inline-block; }
  .badge img { height:54px; display:block; }
  .facts { display:flex; flex-wrap:wrap; gap:8px; margin:28px 0 0; padding:0; list-style:none; }
  .facts li { font-size:14px; padding:6px 12px; border-radius:999px; background:var(--track); }
  .device { width:100%%; max-width:300px; aspect-ratio:1320/2868; border:10px solid var(--bezel); border-radius:52px;
            overflow:hidden; box-shadow:0 30px 60px -20px rgba(43,36,39,.35); background:#000; justify-self:center; }
  .device img { width:100%%; height:100%%; object-fit:cover; display:block; }
  .statement { text-align:center; padding:96px 24px; }
  .statement p { font-size:40px; line-height:1.2; font-weight:600; letter-spacing:-0.035em; margin:0 auto; max-width:22em; }
  .split { display:grid; grid-template-columns:1fr 1fr; gap:56px; align-items:center; padding-bottom:96px; }
  .split.rev .text { order:2; }
  h2 { font-size:40px; line-height:1.2; font-weight:600; letter-spacing:-0.035em; margin:0 0 20px; }
  .split .text p { font-size:18px; color:var(--dim); margin:0; max-width:28em; }
  .pricing { display:grid; grid-template-columns:1fr 1fr; gap:20px; padding-bottom:96px; }
  .pricing h2 { grid-column:1/-1; text-align:center; margin-bottom:12px; }
  .plan { background:var(--surface); border-radius:32px; padding:32px; }
  .plan h3 { font-size:22px; letter-spacing:-0.02em; margin:0 0 4px; }
  .plan h3 .price { font-weight:400; color:var(--dim); margin-left:8px; }
  .plan .note { color:var(--dim); margin:0 0 16px; font-size:15px; }
  .plan ul { margin:0; padding-left:1.1em; }
  .plan li { margin:.35em 0; }
  .faq { max-width:760px; padding-bottom:96px; }
  .faq h2 { text-align:center; margin-bottom:32px; }
  .faq .q { border-top:1px solid var(--track); padding:20px 0; }
  .faq .q:last-child { border-bottom:1px solid var(--track); }
  .faq .q b { display:block; font-weight:600; margin-bottom:4px; }
  .faq .q span { color:var(--dim); }
  .xapps { padding-bottom:72px; }
  .xapps h2 { text-align:center; margin:0 0 24px; }
  .xapps ul { list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(auto-fill, minmax(290px, 1fr)); gap:12px; }
  .xapps li a { display:flex; gap:16px; align-items:center; background:var(--surface); border-radius:24px;
                padding:16px 20px 16px 16px; text-decoration:none; color:var(--ink); }
  .xapps img { width:56px; height:56px; border-radius:13px; flex:none; box-shadow:0 0 0 0.5px rgba(0,0,0,.08); }
  .xapps li a > span { color:var(--dim); font-size:15px; line-height:1.4; }
  .xapps b { display:block; font-weight:600; font-size:17px; color:var(--ink); }
  .xapps .all { text-align:center; margin:24px 0 0; font-size:15px; }
  .closing { text-align:center; padding:32px 24px 96px; }
  .closing p { font-size:40px; line-height:1.2; font-weight:600; letter-spacing:-0.035em; margin:0 auto 32px; max-width:18em; }
  footer { text-align:center; color:var(--dim); font-size:14px; padding:0 24px 16px; }
  .langs-row { text-align:center; font-size:13px; line-height:2; color:var(--dim); margin:0 16px 32px; }
  .nb { display:inline-block; }
  @media (max-width: 820px) {
    .wrap { padding:0 16px; }
    .hero, .split, .pricing { grid-template-columns:1fr; gap:40px; }
    .hero { padding-top:48px; padding-bottom:64px; }
    .split.rev .text { order:0; }
    h1 { font-size:40px; }
    h2, .statement p, .closing p { font-size:30px; }
    .statement { padding:64px 16px; }
    .split, .pricing, .faq { padding-bottom:64px; }
    .device { max-width:260px; }
  }
  :lang(ja) h1, :lang(ja) h2, :lang(ja) .statement p, :lang(ja) .closing p { letter-spacing:0.01em; line-height:1.35; }
  :lang(ja) h1 { font-size:46px; }
  @media (max-width: 820px) { :lang(ja) h1 { font-size:34px; } :lang(ja) h2, :lang(ja) .statement p, :lang(ja) .closing p { font-size:26px; } }
  :lang(ja) body { word-break:auto-phrase; }
"""


def _vars(d):
    return " ".join("--%s:%s;" % (k, v) for k, v in d.items())


def page(app, lang, t):
    e = html.escape
    ui = UI[lang]
    slug = app["slug"]
    base = ROOT + "apps/%s/" % slug
    url = base + ("" if lang == "en" else "ja/")
    up = "" if lang == "en" else "../"          # アプリのフォルダまで
    root = "../../" + up                         # サイトの一番上まで
    img = up + "img/"
    priv = root + "privacy/%s/%s" % (app["privacy"], "" if lang == "en" else "ja/")
    store = "https://apps.apple.com/app/id%s?pt=129250766&ct=lp-%s-%s&mt=8" % (app["app_id"], slug, lang)
    priv_link = '<a href="%s">%s</a>' % (priv, ui["priv_word"])
    plain = lambda s: s.replace("{priv}", ui["priv_word"])
    li = lambda xs: "".join("<li>%s</li>" % e(x) for x in xs)

    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "SoftwareApplication", "name": app["name"], "operatingSystem": "iOS 17 or later",
         "applicationCategory": app["category"], "description": t["desc"], "installUrl": store, "url": url,
         "offers": [{"@type": "Offer", "price": "0", "priceCurrency": "USD"},
                    {"@type": "Offer", "name": app["name"] + " Pro", "price": app["usd"], "priceCurrency": "USD",
                     "description": "One-time in-app purchase, not a subscription."}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in t["faq"]]},
    ]}

    splits = []
    for i, (shot, h, p) in enumerate(t["splits"]):
        splits.append('<section class="wrap split%s">\n  <div class="text">\n    <h2>%s</h2>\n    <p>%s</p>\n  </div>\n'
                      '  <div class="device"><img src="%s%s_%s.jpg" alt="" loading="lazy"></div>\n</section>'
                      % (" rev" if i % 2 else "", h, e(p), img, shot, lang))
    faq = "\n".join('  <div class="q"><b>%s</b><span>%s</span></div>' % (e(q), e(a).replace("{priv}", priv_link))
                    for q, a in t["faq"])
    xapps = "\n".join(
        '    <li><a href="%sapps/%s/%s"><img src="%sicons/%s.png" alt="" loading="lazy"><span><b>%s</b>%s</span></a></li>'
        % (root, a, "" if lang == "en" else "ja/", root, a, XNAME[a], e(XLINE[lang][a])) for a in app["xapps"])
    other = ("ja/", "日本語") if lang == "en" else ("../", "English")
    price = app["usd_label"] if lang == "en" else app["jpy_label"]

    return f"""<!doctype html>
<html lang="{lang}">
<meta charset="utf-8">
<script src="/minari-app-feeds/legacy-notice.js" defer></script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="apple-itunes-app" content="app-id={app['app_id']}">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{base}">
<link rel="alternate" hreflang="ja" href="{base}ja/">
<link rel="alternate" hreflang="x-default" href="{base}">
<style>{CSS % {"light": _vars(app["light"]), "dark": _vars(app["dark"])}}</style>
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>

<nav class="nav"><div class="nav-inner"><img src="{img}icon.png" alt="">{app['name']}<a class="lang" href="{other[0]}">{other[1]}</a></div></nav>

<section class="wrap hero">
  <div>
    <h1>{t['h1']}</h1>
    <p class="sub">{e(t['sub'])}</p>
    <a class="badge" href="{store}"><img src="{img}badge_{lang}.svg" alt="{ui['badge_alt']}"></a>
    <ul class="facts">{li(t['facts'])}</ul>
  </div>
  <div class="device"><img src="{img}{t['hero_shot']}_{lang}.jpg" alt="{e(t['hero_alt'])}"></div>
</section>

<section class="statement">
  <p>{t['statement']}</p>
</section>

{chr(10).join(splits)}

<section class="wrap pricing">
  <h2>{ui['pricing']}</h2>
  <div class="plan"><h3>{ui['free']}</h3><p class="note">{t['free_note']}</p><ul>{li(t['free_items'])}</ul></div>
  <div class="plan"><h3>{app['name']} Pro<span class="price">{price}</span></h3><p class="note">{t['pro_note']}</p><ul>{li(t['pro_items'])}</ul></div>
</section>

<section class="wrap faq">
  <h2>{ui['faq_h']}</h2>
{faq}
</section>

<section class="wrap xapps">
  <h2>{ui['xapps_h']}</h2>
  <ul>
{xapps}
  </ul>
  <p class="all"><a href="{root}{'' if lang == 'en' else 'ja/'}">{ui['all_apps']}</a></p>
</section>

<section class="closing">
  <p>{t['closing']}</p>
  <a class="badge" href="{store}"><img src="{img}badge_{lang}.svg" alt="{ui['badge_alt']}"></a>
</section>

<footer>{ui['ios']}{' · ' if lang == 'en' else '・'}Made by minari{' · ' if lang == 'en' else '・'}{priv_link}</footer>
<p class="langs-row">{ui['langs']}</p>
"""


def build(app_dir, app, T):
    for lang, t in T.items():
        d = app_dir if lang == "en" else os.path.join(app_dir, "ja")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(app, lang, t))
        print("wrote", os.path.relpath(os.path.join(d, "index.html"), os.path.dirname(app_dir)))
