#!/usr/bin/env python3
"""Driftfall の公式ページ（英・日）。型は apps/_lp.py。
文言の出どころ＝~/Driftfall/store/description_{en,ja}.txt・promo。値段＝ASC（2026-11-23：$14.99／¥2,500）。
使い方：python3 apps/driftfall/build_pages.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from _lp import build  # noqa: E402

APP = dict(
    slug="driftfall", name="Driftfall", app_id="6836211068", privacy="driftfall", category="MultimediaApplication",
    usd="14.99", usd_label="$14.99", jpy_label="¥2,500",
    light={"bezel": "#3A3335", "bg": "#F4EFEC", "surface": "#FFFFFF", "ink": "#3A3335", "dim": "#6B5F63", "track": "#E7DFDA", "accent": "#3A3335"},
    dark={"bezel": "#2E292B", "bg": "#221E20", "surface": "#2E292B", "ink": "#EDE7E8", "dim": "#A99FA3", "track": "#3A3336", "accent": "#EDE7E8"},
    xapps=["mantel", "museday", "nightwick", "kotoba", "datto"],
)

T = {
    "en": dict(
        title="Driftfall — snow and petals falling on your own photos, as a Live Photo wallpaper or a looping video (no subscription)",
        desc="Let snow, sakura petals, maple leaves and more fall over your own photos. Set it as your Lock Screen, or send it as a moving photo. Your photos stay on your iPhone. Pro is a one-time purchase.",
        h1='<span class="lead">Snow and petals,</span> <span class="nb">falling on your own photos.</span>',
        sub="Set it as your Lock Screen, or send it as a moving photo.",
        facts=["No subscription", "No ads", "No account"],
        hero_shot="editor_sakura", hero_alt="Sakura petals falling on a riverside photo in Driftfall",
        statement='<span class="lead">Sakura, maple leaves, snow, fireflies, stardust.</span> 14 things to let fall.',
        splits=[
            ("editor_maple", '<span class="lead">Pick a photo.</span> <span class="nb">Choose what falls.</span>',
             "Pick any photo from your library and choose what falls on it. Adjust how much falls and how the wind blows, and drag to frame your photo."),
            ("export_snow", '<span class="lead">On your Lock Screen.</span> <span class="nb">It falls when you wake your iPhone.</span>',
             "Save it as a Live Photo and set it as your wallpaper. When you wake your iPhone, it starts to fall for a moment."),
            ("share_bubbles", '<span class="lead">Send it</span> <span class="nb">as a moving photo.</span>',
             "Share it as a short video that loops without a seam, to Messages, Instagram, or anywhere you like."),
        ],
        free_note="No ads. No account.",
        free_items=["Try all 14 on your own photos", "Save and share rain and bubbles"],
        pro_note="One-time purchase, no subscription.",
        pro_items=["Save and share all 14", "As a Live Photo for your Lock Screen, or as a looping video"],
        faq=[
            ("Is Driftfall a subscription?", "No. You can try all 14 on your own photos for free. Driftfall Pro, which lets you save and share all 14, is a one-time purchase."),
            ("How do I set it as my wallpaper?", "After saving, open Settings > Wallpaper > Add New Wallpaper > Photos, and choose the Live Photo you saved."),
            ("It only moves for a moment.", "That is how iOS plays a Live Photo wallpaper: briefly, when you wake your iPhone. To watch it longer, send it as a video."),
            ("Where are my photos stored?", "Only on your iPhone. There is no account and nothing is uploaded. See the {priv}."),
            ("I bought Pro on another iPhone.", "Open Settings (gear) and tap Restore Purchase."),
            ("How can I contact you?", "Email minariapps@gmail.com."),
        ],
        closing='<span class="lead">Your photos stay on your iPhone.</span> No account, no subscription.',
    ),
    "ja": dict(
        title="Driftfall — 自分の写真に雪や桜を降らせて、ロック画面の壁紙や動く写真に（買い切り）",
        desc="自分の写真に、雪や桜、紅葉などを降らせるアプリ。ロック画面の壁紙にも、動く写真として送ることもできます。写真はiPhoneの中だけ。Proは買い切り。",
        h1='<span class="lead">自分の写真に、</span><span class="nb">雪や桜を降らせて。</span>',
        sub="ロック画面の壁紙にも、ループする動画で送ることもできます。",
        facts=["サブスクなし", "広告なし", "アカウント不要"],
        hero_shot="editor_sakura", hero_alt="川辺の写真に桜の花びらが降るDriftfallの画面",
        statement='<span class="lead">桜、紅葉、雪、蛍、星くず。</span>降らせられるのは14種類。',
        splits=[
            ("editor_maple", '<span class="lead">好きな1枚に、</span><span class="nb">降らせるものを選ぶ。</span>',
             "写真アプリから好きな1枚を選んで、降らせるものを選びます。降る量と風の強さを変えられて、写真の位置もずらせます。"),
            ("export_snow", '<span class="lead">ロック画面で、</span><span class="nb">画面をつけると降り出す。</span>',
             "Live Photoとして保存して、壁紙に設定します。iPhoneの画面をつけたとき、少しのあいだ降り出します。"),
            ("share_bubbles", '<span class="lead">動く写真にして、</span><span class="nb">送る。</span>',
             "つなぎ目なくループする短い動画にして、メッセージやInstagramなど好きなところへ送れます。"),
        ],
        free_note="広告なし・アカウント不要。",
        free_items=["14種類すべてを自分の写真で試せる", "雨とシャボン玉は保存・送信もできる"],
        pro_note="買い切り・サブスクなし。",
        pro_items=["14種類すべてを保存して送れる", "ロック画面のLive Photoにも、ループする動画にも"],
        faq=[
            ("サブスクですか", "いいえ。14種類すべてを自分の写真で無料で試せます。14種類すべてを保存して送れるDriftfall Proは買い切りです。"),
            ("壁紙にするには", "保存したあと、設定＞壁紙＞新しい壁紙を追加＞写真を開いて、保存したLive Photoを選びます。"),
            ("少ししか動きません", "iOSのLive Photo壁紙は、画面をつけたときに少しのあいだだけ動く仕組みです。長く見たいときは、動画で送ってください。"),
            ("写真はどこに保存されますか", "iPhoneの中だけです。アカウントは無く、どこにも送られません。{priv}をご覧ください。"),
            ("別のiPhoneでProを買いました", "設定（歯車）を開いて「購入を復元」を押してください。"),
            ("問い合わせ先は", "minariapps@gmail.comにメールしてください。"),
        ],
        closing='<span class="lead">写真はiPhoneの中だけ。</span>アカウントなし、サブスクなし。',
    ),
}

if __name__ == "__main__":
    build(HERE, APP, T)
