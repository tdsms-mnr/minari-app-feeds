#!/usr/bin/env python3
"""Jewelday の公式ページ（英・日）。型は apps/_lp.py。
文言の出どころ＝~/Hako/store/description_{en,ja}.txt。値段＝ASC（2026-11-23：$12.99／¥2,000）。
2026-11-23 時点で審査待ち＝App Store のボタンは公開されるまで開けない。
使い方：python3 apps/jewelday/build_pages.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from _lp import build  # noqa: E402

APP = dict(
    slug="jewelday", name="Jewelday", app_id="6828661691", privacy="hako", category="LifestyleApplication",
    usd="12.99", usd_label="$12.99", jpy_label="¥2,000",
    light={"bezel": "#3B3436", "bg": "#F7F3F0", "surface": "#FFFDFB", "ink": "#3B3436", "dim": "#8E8183", "track": "#EEE7E4", "accent": "#2E3A4F"},
    dark={"bezel": "#282324", "bg": "#1E1A1B", "surface": "#282324", "ink": "#F1EAE7", "dim": "#A99C9E", "track": "#2C2627", "accent": "#AFC2DA"},
    xapps=["mantel", "nightwick", "museday", "savebar", "datto"],
)

T = {
    "en": dict(
        title="Jewelday — your jewelry box on iPhone: ear map, stacks and trip checks (no subscription)",
        desc="Plan which earring goes in which piercing, try a stack on your own hand, and bring every piece home from a trip. No account. Pro is a one-time purchase.",
        h1='<span class="lead">Your jewelry box,</span> <span class="nb">on your iPhone.</span>',
        sub="Plan which earring goes in which piercing, try a stack on your own hand, and bring every piece home from a trip.",
        facts=["No subscription", "No ads", "No account"],
        hero_shot="today", hero_alt="Today's pieces for ears, neck, wrist and fingers in Jewelday",
        statement='<span class="lead">Photograph a piece,</span> and the background is removed on your iPhone.',
        splits=[
            ("ear", '<span class="lead">Nine piercings.</span> <span class="nb">An earring for each.</span>',
             "Both ears, nine piercing positions: first, second and third lobe, helix, forward helix, rook, daith, tragus and conch. Keep only the piercings you have, then choose an earring for each one. Save the ears you put together."),
            ("stack", '<span class="lead">Try a stack</span> <span class="nb">on your own hand.</span>',
             "Place your cut-out pieces on a photo of your own hand, neck or ear. Move them with a finger, resize and turn them with two. A stack you like goes into today's record with one tap."),
            ("trip", '<span class="lead">Bring every piece</span> <span class="nb">home from a trip.</span>',
             "Choose what you're taking, then check each piece three times: before you go, before checkout and back home. Anything that isn't back yet is listed. Mark an earring when one of the pair is missing."),
            ("bulk", '<span class="lead">Lay them out.</span> <span class="nb">One photo adds them all.</span>',
             "Lay several pieces out and one photo adds them all. Keep the days you wore each piece this year, the metal and stones, the next care date and where the certificate is kept."),
        ],
        free_note="No ads. No account.",
        free_items=["Up to 5 pieces", "1 set, 1 trip, 1 stack and 1 saved ear"],
        pro_note="One-time purchase, no subscription.",
        pro_items=["As many of everything as you like", "Certificate photos and PDFs", "Filters by metal and stone", "Home Screen widget"],
        faq=[
            ("Is Jewelday a subscription?", "No. You can keep up to 5 pieces for free. Jewelday Pro is a one-time purchase."),
            ("Where is my data stored?", "Only on your iPhone. There is no account, and your photos and records are never uploaded. See the {priv}."),
            ("I bought Pro on another iPhone.", "Open Settings (gear) and tap Restore Purchases."),
            ("Some pieces weren't separated from the photo.", "Small pieces placed close together can be missed. Tap “Trace to add” and draw around them. Use the eraser to clean up the inside of rings."),
            ("How can I contact you?", "Email minariapps@gmail.com."),
        ],
        closing='<span class="lead">No account,</span> no ads, no subscription.',
    ),
    "ja": dict(
        title="Jewelday — iPhoneのジュエリーボックス。耳の地図・重ね付け・旅行の確認（買い切り）",
        desc="ピアスの穴ごとの組み合わせを決め、自分の手に重ねて試し、旅先から全部持ち帰るためのジュエリーのアプリ。アカウント不要・Proは買い切り。",
        h1='<span class="lead">iPhoneの中の、</span><span class="nb">ジュエリーボックス。</span>',
        sub="ピアスの穴ごとの組み合わせを決めて、自分の手に重ねて試して、旅先から全部持ち帰る。",
        facts=["サブスクなし", "広告なし", "アカウント不要"],
        hero_shot="today", hero_alt="Jeweldayの今日つけるもの（耳・首・手首・指）",
        statement='<span class="lead">撮るだけで、</span>iPhoneの中で背景が抜けます。',
        splits=[
            ("ear", '<span class="lead">9か所の穴に、</span><span class="nb">1つずつ選ぶ。</span>',
             "左右の耳に、ファースト・セカンド・サード・ヘリックス・フォワードヘリックス・ルーク・ダイス・トラガス・コンクの9か所。自分があけている穴だけを残し、穴ごとにつけるピアスを選びます。組んだ耳は名前をつけて残せます。"),
            ("stack", '<span class="lead">自分の手に、</span><span class="nb">重ねて試す。</span>',
             "自分の手・首元・耳の写真に、切り抜いたジュエリーを置いて重ねてみます。指で動かし、2本の指で大きさと向きを変えます。決まった重ね付けは、押すだけで今日の記録に入ります。"),
            ("trip", '<span class="lead">旅先から、</span><span class="nb">全部持ち帰る。</span>',
             "持っていくものを選び、出発前・チェックアウト前・帰宅後の3回、1点ずつ確かめます。帰ってから戻っていないものは一覧に出ます。片方だけなくしたピアスにも印をつけられます。"),
            ("bulk", '<span class="lead">並べて1枚撮れば、</span><span class="nb">まとめて登録。</span>',
             "何点か並べて1枚撮れば、まとめて登録できます。この1年でつけた日、地金・石・お手入れの日・鑑別書のしまい場所も残せます。"),
        ],
        free_note="広告なし・アカウント不要。",
        free_items=["ジュエリー5点まで", "セット・旅行・重ね付け・耳の組み合わせは1つずつ"],
        pro_note="買い切り・サブスクなし。",
        pro_items=["すべていくつでも", "鑑別書・保証書の写真とPDF", "金属と石での絞り込み", "ホーム画面のウィジェット"],
        faq=[
            ("サブスクですか", "いいえ。ジュエリー5点までなら無料で使えます。Jewelday Proは買い切りです。"),
            ("記録はどこに保存されますか", "iPhoneの中だけです。アカウントはなく、写真や記録が外へ送られることはありません。{priv}もご覧ください。"),
            ("別のiPhoneでProを買いました", "設定（歯車）の「購入を復元」を押してください。"),
            ("並べて撮ったのに、分かれないものがあります", "小さいものや近くに置いたものは見落とすことがあります。「なぞって足す」で囲んでください。リングの内側に残った背景は消しゴムで消せます。"),
            ("問い合わせ先は", "minariapps@gmail.comにメールしてください。"),
        ],
        closing='<span class="lead">アカウントなし、</span>広告なし、サブスクなし。',
    ),
}

if __name__ == "__main__":
    build(HERE, APP, T)
