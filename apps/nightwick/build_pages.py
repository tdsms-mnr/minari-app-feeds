#!/usr/bin/env python3
"""Nightwick の公式ページ（英・日）。型は apps/_lp.py。
文言の出どころ＝~/Tomosu/store/description_{en,ja}.txt・subtitle。値段＝ASC（2026-11-23：$7.99／¥1,300）。
使い方：python3 apps/nightwick/build_pages.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from _lp import build  # noqa: E402

APP = dict(
    slug="nightwick", name="Nightwick", app_id="6835049487", privacy="tomosu", category="LifestyleApplication",
    usd="7.99", usd_label="$7.99", jpy_label="¥1,300",
    light={"bezel": "#2B2427", "bg": "#F7F4F1", "surface": "#FFFDFB", "ink": "#3B3538", "dim": "#8A8084", "track": "#EAE4DF", "accent": "#2B2427"},
    dark={"bezel": "#2B2427", "bg": "#221E20", "surface": "#2B2427", "ink": "#EDE7E8", "dim": "#A99FA3", "track": "#2E2729", "accent": "#D9B98C"},
    xapps=["mantel", "museday", "rowmark", "driftfall", "datto"],
)

T = {
    "en": dict(
        title="Nightwick — a candle journal for iPhone: your shelf and tonight's candle (no subscription)",
        desc="Keep the candles you have on one shelf, pick one for tonight and light it. Candles you burn to the end stay in your album. No account. Pro is a one-time purchase.",
        h1='<span class="lead">Your shelf,</span> <span class="nb">tonight\'s candle.</span>',
        sub="Keep every candle you have on one shelf. Tap one, and it becomes tonight's candle.",
        facts=["No subscription", "No ads", "No account"],
        hero_shot="home", hero_alt="Tonight's candle and your shelf in Nightwick",
        statement='<span class="lead">The candles you burn to the end</span> stay in your album, with every night you lit them.',
        splits=[
            ("lit", '<span class="lead">Light it.</span> <span class="nb">On its first night, a time to burn until.</span>',
             "A timer runs while it burns. On a candle's first night, Nightwick shows a time to let it burn until, based on its size, so the wax can melt across the top. When you put it out, choose “Light it again another time” or “It's used up.”"),
            ("add", '<span class="lead">Paste a shop link.</span> <span class="nb">Photo, name and scent fill in.</span>',
             "Paste the link to the shop page and Nightwick fills in the photo, the name, the scent notes and the weight. You can also take a photo and type it in yourself."),
            ("albumpage", '<span class="lead">Burned to the end.</span> <span class="nb">Kept in your album.</span>',
             "Candles you burn to the end move to the album, with every night you lit them and the hours they burned. The album is free and always stays with you."),
        ],
        free_note="No ads. No account.",
        free_items=["Up to 3 candles on your shelf", "Lighting and the first-night time", "The album", "Your scent families"],
        pro_note="One-time purchase, no subscription.",
        pro_items=["As many candles as you like", "The Lock Screen while a candle burns", "A Home Screen widget for tonight's candle",
                   "iCloud, so your candles stay when you change iPhones", "A scent family to try next"],
        faq=[
            ("Is Nightwick a subscription?", "No. You can use it for free with up to 3 candles. Nightwick Pro is a one-time purchase."),
            ("Where is my data stored?", "On your iPhone. With Pro, also in your own iCloud. There is no account. See the {priv}."),
            ("I bought Pro on another iPhone.", "Open Settings (gear) and tap Restore Purchase."),
            ("A shop link didn't fill everything in.", "Some shops don't show these details on the page. Type in what's missing yourself."),
            ("How can I contact you?", "Email minariapps@gmail.com, or open Settings (gear) › Contact in the app."),
        ],
        closing='<span class="lead">No account,</span> no ads, no subscription.',
    ),
    "ja": dict(
        title="Nightwick — 手元のキャンドルの棚と、今夜の1本（キャンドルの記録・買い切り）",
        desc="持っているキャンドルを1つの棚にまとめ、今夜の1本を選んで灯す。最後まで灯した1本はアルバムに残ります。アカウント不要・Proは買い切り。",
        h1='<span class="lead">手元の棚から、</span><span class="nb">今夜の1本を。</span>',
        sub="持っているキャンドルを、1つの棚に。押した1本が、今夜の1本になります。",
        facts=["サブスクなし", "広告なし", "アカウント不要"],
        hero_shot="home", hero_alt="Nightwickの今夜の1本と手元のキャンドル",
        statement='<span class="lead">最後まで灯した1本は、</span>灯した夜と一緒にアルバムに残ります。',
        splits=[
            ("lit", '<span class="lead">灯す。</span><span class="nb">初めての夜は、</span><span class="nb">「この時刻まで」の目安つき。</span>',
             "灯している間は時間が進みます。初めての夜は、大きさから「この時刻まで灯す」の目安が出ます。表面まで溶かすための目安です。火を消すときは「また今度灯す」か「使い切った」を選びます。"),
            ("add", '<span class="lead">お店のURLを貼るだけ。</span><span class="nb">写真・名前・香りが入ります。</span>',
             "お店のページのURLを貼ると、写真・名前・香り・容量が入ります。自分で撮って入れることもできます。"),
            ("albumpage", '<span class="lead">使い切った1本は、</span><span class="nb">アルバムへ。</span>',
             "使い切った1本は、灯した夜と時間と一緒にアルバムへ移ります。アルバムは無料で、いつでも見られます。"),
        ],
        free_note="広告なし・アカウント不要。",
        free_items=["手元のキャンドル3本まで", "灯す・初めての夜の目安", "アルバム", "香りの傾向"],
        pro_note="買い切り・サブスクなし。",
        pro_items=["キャンドルを何本でも", "灯している間のロック画面", "今夜の1本を出すホーム画面のウィジェット",
                   "機種を変えても残るiCloud", "次に試す香りの系統"],
        faq=[
            ("サブスクですか", "いいえ。キャンドル3本までなら無料で使えます。Nightwick Proは買い切りです。"),
            ("記録はどこに保存されますか", "iPhoneの中です。Proでは、ご自身のiCloudにも保存します。アカウントはありません。{priv}をご覧ください。"),
            ("別のiPhoneでProを買いました", "設定（歯車）を開いて「購入を復元」を押してください。"),
            ("お店のリンクから全部入りませんでした", "お店によっては、ページに載っていない項目があります。足りないところは自分で入れてください。"),
            ("問い合わせ先は", "minariapps@gmail.comにメールしてください。アプリの設定（歯車）＞「お問い合わせ」からも送れます。"),
        ],
        closing='<span class="lead">アカウントなし、</span>広告なし、サブスクなし。',
    ),
}

if __name__ == "__main__":
    build(HERE, APP, T)
